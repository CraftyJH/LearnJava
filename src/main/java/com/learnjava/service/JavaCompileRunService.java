package com.learnjava.service;

import com.learnjava.dto.RunResponse;
import org.springframework.stereotype.Service;

import javax.tools.Diagnostic;
import javax.tools.DiagnosticCollector;
import javax.tools.JavaCompiler;
import javax.tools.JavaFileObject;
import javax.tools.StandardJavaFileManager;
import javax.tools.ToolProvider;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.PrintStream;
import java.io.Writer;
import java.lang.reflect.Method;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.regex.Pattern;

@Service
public class JavaCompileRunService {

    private static final Pattern SAFE_CLASS = Pattern.compile("^[A-Za-z_][A-Za-z0-9_]*$");
    private static final int MAX_CODE_CHARS = 200_000;

    public RunResponse compileAndRun(String rawCode, String requestedClassName, int timeoutSeconds) {
        String className = sanitizeClassName(requestedClassName);
        String code = rawCode == null ? "" : rawCode;
        if (code.length() > MAX_CODE_CHARS) {
            return new RunResponse(false, "", "Code exceeds maximum length (" + MAX_CODE_CHARS + " characters).", "");
        }

        String detected = extractPublicClassName(code);
        if (detected != null && !detected.equals(className)) {
            className = detected;
        }

        if (!code.contains("class " + className)) {
            return new RunResponse(
                    false,
                    "",
                    "Public class name must match the editor. Use `public class " + className + "` or change the class name in the toolbar.",
                    ""
            );
        }

        JavaCompiler compiler = ToolProvider.getSystemJavaCompiler();
        if (compiler == null) {
            return new RunResponse(
                    false,
                    "",
                    "No Java compiler in this runtime (JDK required on the server).",
                    ""
            );
        }

        try {
            Path workDir = Files.createTempDirectory("learnjava-run-");
            try {
                Path src = workDir.resolve(className + ".java");
                Files.writeString(src, code, StandardCharsets.UTF_8);

                DiagnosticCollector<JavaFileObject> diagnostics = new DiagnosticCollector<>();
                try (StandardJavaFileManager fileManager = compiler.getStandardFileManager(diagnostics, Locale.US, StandardCharsets.UTF_8)) {
                    Iterable<? extends JavaFileObject> units = fileManager.getJavaFileObjectsFromPaths(List.of(src));

                    List<String> options = new ArrayList<>();
                    options.add("-classpath");
                    options.add(workDir.toString());
                    options.add("-d");
                    options.add(workDir.toString());

                    ByteArrayOutputStream compilerErr = new ByteArrayOutputStream();
                    Writer compilerWriter = new OutputStreamWriter(compilerErr, StandardCharsets.UTF_8);
                    JavaCompiler.CompilationTask task = compiler.getTask(
                            compilerWriter,
                            fileManager,
                            diagnostics,
                            options,
                            null,
                            units
                    );
                    boolean ok = Boolean.TRUE.equals(task.call());
                    compilerWriter.flush();

                    StringBuilder diagText = new StringBuilder();
                    for (Diagnostic<? extends JavaFileObject> d : diagnostics.getDiagnostics()) {
                        diagText.append(d.getKind()).append(": ");
                        if (d.getSource() != null) {
                            diagText.append(d.getSource().getName());
                        }
                        diagText.append(" line ").append(d.getLineNumber()).append(": ");
                        diagText.append(d.getMessage(Locale.US)).append(System.lineSeparator());
                    }
                    String compileOut = diagText + compilerErr.toString(StandardCharsets.UTF_8);

                    if (!ok) {
                        return new RunResponse(false, "", "Compilation failed.", compileOut);
                    }

                    return executeMain(workDir, className, timeoutSeconds, compileOut);
                }
            } finally {
                deleteRecursively(workDir);
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            return new RunResponse(false, "", "Interrupted.", "");
        } catch (Exception e) {
            return new RunResponse(false, "", "Execution error: " + e.getMessage(), "");
        }
    }

    private static RunResponse executeMain(Path classpathRoot, String className, int timeoutSeconds, String compileOut)
            throws ReflectiveOperationException, IOException, InterruptedException {
        try (SandboxClassLoader loader = new SandboxClassLoader(classpathRoot)) {
            Class<?> clazz = Class.forName(className, true, loader);
            Method main = clazz.getMethod("main", String[].class);

            ByteArrayOutputStream outBuf = new ByteArrayOutputStream();
            ByteArrayOutputStream errBuf = new ByteArrayOutputStream();
            PrintStream oldOut = System.out;
            PrintStream oldErr = System.err;
            Thread runner = new Thread(() -> {
                try {
                    System.setOut(new PrintStream(outBuf, true, StandardCharsets.UTF_8));
                    System.setErr(new PrintStream(errBuf, true, StandardCharsets.UTF_8));
                    main.invoke(null, (Object) new String[0]);
                } catch (Throwable t) {
                    t.printStackTrace(new PrintStream(errBuf, true, StandardCharsets.UTF_8));
                } finally {
                    System.setOut(oldOut);
                    System.setErr(oldErr);
                }
            }, "user-main-" + className);
            runner.start();
            runner.join(timeoutSeconds * 1000L);
            if (runner.isAlive()) {
                runner.interrupt();
                return new RunResponse(
                        false,
                        outBuf.toString(StandardCharsets.UTF_8),
                        errBuf.toString(StandardCharsets.UTF_8) + System.lineSeparator()
                                + "Timed out after " + timeoutSeconds + " seconds.",
                        compileOut
                );
            }
            String out = outBuf.toString(StandardCharsets.UTF_8);
            String err = errBuf.toString(StandardCharsets.UTF_8);
            return new RunResponse(true, out, err, compileOut);
        }
    }

    private static String sanitizeClassName(String name) {
        if (name == null || name.isBlank()) {
            return "Main";
        }
        String n = name.trim();
        if (!SAFE_CLASS.matcher(n).matches()) {
            return "Main";
        }
        return n;
    }

    private static String extractPublicClassName(String code) {
        Pattern p = Pattern.compile("public\\s+class\\s+([A-Za-z_][A-Za-z0-9_]*)");
        var m = p.matcher(code);
        if (m.find()) {
            return m.group(1);
        }
        return null;
    }

    private static void deleteRecursively(Path root) throws IOException {
        if (!Files.exists(root)) {
            return;
        }
        try (var walk = Files.walk(root)) {
            walk.sorted((a, b) -> b.getNameCount() - a.getNameCount()).forEach(p -> {
                try {
                    Files.deleteIfExists(p);
                } catch (IOException ignored) {
                }
            });
        }
    }

    private static final class SandboxClassLoader extends ClassLoader implements AutoCloseable {

        private final Path root;

        SandboxClassLoader(Path root) {
            super(ClassLoader.getPlatformClassLoader());
            this.root = root;
        }

        @Override
        protected Class<?> findClass(String name) throws ClassNotFoundException {
            Path file = root.resolve(name.replace('.', '/') + ".class");
            if (!Files.isRegularFile(file)) {
                throw new ClassNotFoundException(name);
            }
            try {
                byte[] bytes = Files.readAllBytes(file);
                return defineClass(name, bytes, 0, bytes.length);
            } catch (IOException e) {
                throw new ClassNotFoundException(name, e);
            }
        }

        @Override
        protected Class<?> loadClass(String name, boolean resolve) throws ClassNotFoundException {
            synchronized (getClassLoadingLock(name)) {
                Class<?> c = findLoadedClass(name);
                if (c == null) {
                    if (name.startsWith("java.") || name.startsWith("javax.") || name.startsWith("jdk.")) {
                        c = getParent().loadClass(name);
                    } else {
                        c = findClass(name);
                    }
                }
                if (resolve) {
                    resolveClass(c);
                }
                return c;
            }
        }

        @Override
        public void close() {
            // temp directory removed by caller
        }
    }
}
