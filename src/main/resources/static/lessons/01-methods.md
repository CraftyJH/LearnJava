# Methods, parameters, return values, and overloading

## Declaration

```java
public static int add(int a, int b) {
    return a + b;
}
```

`static` belongs to the class, not an instance.

## Overloading

Same method name, different parameter lists. Return type alone is **not** enough to overload.

## Varargs

```java
static int sum(int first, int... rest) { ... }
```

Varargs must be last parameter.

## Key ideas

Methods should be **short**, do one thing, and use names that read like intent: `computeTotalPrice`, not `doStuff`.

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

