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

## How to read Java like a practitioner

When you open a file, skim in this order: **package and imports** (dependencies), **public types** (what the module exports), then **constructors and public methods** (how it is used). Only then dive into private helpers. This mirrors how teams navigate large repositories.

## Common pitfalls (across lessons)

- Using `=` when you meant `==`, especially in `if` conditions.
- Integer division surprises (`5 / 2` is `2`, not `2.5`).
- Treating `null` as “empty”: always decide explicitly whether `null` is allowed.
- Catching `Exception` too broadly and hiding the real failure.

## Before you click Run

Say aloud **one predicted line of output**. If the real output differs, you have found a concrete misunderstanding—reread the theory section that matches the mismatch.

## After it works

Spend sixty seconds on **one** improvement: clearer variable names, a helper method, or a comment explaining *why* (not *what*). Small refactors build taste faster than only writing throwaway answers.

