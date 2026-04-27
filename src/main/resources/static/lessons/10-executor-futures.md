# Executors, `Future`, and `CompletableFuture`

## ExecutorService

```java
try (var pool = Executors.newVirtualThreadPerTaskExecutor()) {
    pool.submit(() -> work());
}
```

(Use platform thread pools when you need strict limits; virtual threads simplify blocking workloads on modern JDKs.)

## Futures

`future.get()` blocks; specify timeouts in production.

## CompletableFuture

Composable async pipelines: `supplyAsync`, `thenApply`, `thenCombine`, `exceptionally`.

## Key ideas

Understand **backpressure**: unlimited task submission can exhaust memory.

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

