# `ConcurrentHashMap`, queues, and copy-on-write

## Concurrent maps

`ConcurrentHashMap` supports safe concurrent updates with fine-grained locking.

## Queues

`ArrayBlockingQueue`, `LinkedBlockingQueue`, `PriorityBlockingQueue`.

## Copy-on-write

`CopyOnWriteArrayList` for read-heavy, write-rare scenarios.

## Key ideas

Iterator behavior differs from ordinary collections; many concurrent iterators are **weakly consistent**.
