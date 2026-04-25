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
