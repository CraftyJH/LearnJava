# Exceptions: checked vs unchecked, try-with-resources

## Exception types

- **Checked**: must be declared or handled (`IOException`).
- **Unchecked**: extend `RuntimeException` (often programming errors).

## `try / catch / finally`

```java
try {
    risky();
} catch (IOException e) {
    // handle or wrap
} finally {
    // always runs (almost)
}
```

## try-with-resources

Auto-closes `AutoCloseable`:

```java
try (var in = Files.newInputStream(path)) {
    // use in
}
```

## Best practices

- Catch **specific** types first.
- Do not swallow exceptions silently.
- Prefer **meaningful** messages and preserve causes: `throw new ServiceException("...", e)`.

## Key ideas

Use exceptions for **exceptional** conditions, not normal control flow.

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

