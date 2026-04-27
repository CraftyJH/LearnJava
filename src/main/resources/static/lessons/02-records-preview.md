# Records (Java 16+): data carriers

## Motivation

Boilerplate for data classes (constructors, getters, `equals`, `hashCode`, `toString`) is tedious and error-prone.

## Record declaration

```java
public record Point(int x, int y) {}
```

The compiler generates accessors `x()` and `y()`, constructor, `equals`, `hashCode`, `toString`.

## Canonical constructor customization

```java
public record Email(String value) {
    public Email {
        if (value == null || value.isBlank()) {
            throw new IllegalArgumentException("email required");
        }
    }
}
```

## Key ideas

Use records for **transparent data** with clear invariants. Use classes when you need extensive mutable state or inheritance hierarchies.

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

