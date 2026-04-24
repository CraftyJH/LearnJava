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
