# Concurrency: threads and synchronization basics

## Creating threads

- `new Thread(() -> { ... }).start()`
- `ExecutorService` for pooling (preferred)

## Shared mutable state

Synchronize access with `synchronized`, locks, or concurrent data structures.

## Visibility

The Java Memory Model defines **happens-before** rules; unsynchronized reads can see stale values.

## Key ideas

Concurrency bugs are **non-deterministic**; design immutability and clear ownership.
