# Sealed classes and exhaustive pattern matching (overview)

## Sealed hierarchies

Restrict subclasses to a known set:

```java
public sealed interface Shape permits Circle, Rectangle { }
```

## Exhaustive `switch`

With sealed types, the compiler can verify you handled all permitted subtypes (when patterns are enabled and complete).

## Key ideas

Sealed types model **closed domains** (AST nodes, payment types) safely.

Learn `instanceof` patterns:

```java
if (shape instanceof Circle c) {
    System.out.println(c.radius());
}
```

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

