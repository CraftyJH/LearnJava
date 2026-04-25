# Installing the JDK and your first commands

## Install a JDK

Use **JDK 17 or newer** (this course targets modern Java). Popular distributions:

- **Eclipse Temurin** (Adoptium)
- **Amazon Corretto**
- **Oracle JDK** (license terms differ)

Verify in a terminal:

```text
java -version
javac -version
```

Both commands should report the same major version family.

## Compile and run locally (optional but recommended)

```text
javac Hello.java
java Hello
```

Your public class name must match the file name (`Hello.java` → `class Hello`).

## Editors

- **IntelliJ IDEA Community** is excellent for Java.
- **VS Code** with Java extensions works well.
- This website gives you a sandbox; your local IDE is where you will work on the **major projects**.

## Key ideas

- The **classpath** tells the JVM where to find classes.
- **Packages** map to directories and avoid name collisions.
