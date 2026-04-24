package com.learnjava.service;

import com.learnjava.dto.RunResponse;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertTrue;

class JavaCompileRunServiceTest {

    private final JavaCompileRunService service = new JavaCompileRunService();

    @Test
    void runsHelloWorld() {
        String code = """
                public class Main {
                    public static void main(String[] args) {
                        System.out.print("ok");
                    }
                }
                """;
        RunResponse r = service.compileAndRun(code, "Main", 10);
        assertTrue(r.success(), r.stderr() + r.compileOutput());
        assertTrue(r.stdout().contains("ok"));
    }
}
