# Strings, text blocks, and `StringBuilder`

## `String` immutability

`String` objects are immutable: methods return new strings.

## Concatenation

`+` creates a new string. In tight loops, use `StringBuilder`.

## `StringBuilder`

Mutable buffer:

```java
StringBuilder sb = new StringBuilder();
sb.append("a").append(123);
String s = sb.toString();
```

## Text blocks (Java 15+)

Java text blocks use a triple-double-quote delimiter; they are ideal for SQL, JSON, and HTML snippets.

```java
String sql = """
    SELECT id, name
    FROM users
    WHERE active = true
    """;
```

## Common APIs

`isEmpty`, `isBlank`, `strip`, `lines`, `formatted`, `repeat`.

## Key ideas

Never use `==` for string **content** equality; use `Objects.equals(a, b)` or `a.equals(b)` with null-safe patterns.

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

