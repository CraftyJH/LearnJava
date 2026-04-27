# `static`, `final`, and initialization order

## `static` members

Belong to the class. `static` methods cannot access instance fields directly.

## `static` blocks

Run once when the class is initialized:

```java
static {
    // class-level setup
}
```

## `final` fields

- Instance `final` must be definitely assigned by the end of every constructor.
- `static final` constants are common for configuration keys.

## Initialization order (simplified)

1. Superclass static initializers
2. Subclass static initializers
3. Superclass instance fields and instance initializers
4. Superclass constructor
5. Subclass instance fields and instance initializers
6. Subclass constructor

## Key ideas

Avoid complex initialization cycles across subclasses; keep constructors simple.

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

