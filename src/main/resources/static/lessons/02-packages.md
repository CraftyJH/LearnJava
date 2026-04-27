# Packages, modules (overview), and JAR basics

## Packages

```java
package com.example.app;

public class User { }
```

Directory structure must mirror package names. Packages avoid collisions and organize large codebases.

## Imports

`import java.util.List;` or wildcard `import java.util.*;` (use sparingly for readability).

## Module system (Java 9+)

The **Java Platform Module System** adds `module-info.java` to declare exported packages and required modules. Enterprise apps may still be classpath-based; learn modules when you ship libraries.

## JAR files

A **JAR** is a zip of `.class` files plus metadata. Executable JARs specify a `Main-Class` in the manifest.

## Key ideas

Naming packages by **reverse DNS** (`com.yourname.project`) is standard.

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

