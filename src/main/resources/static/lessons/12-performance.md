# Performance engineering without folklore

## Algorithm first

Big-O beats micro-optimizations.

## Collections costs

Resizing arrays, hashing collisions, boxing.

## IO costs

Batch reads, avoid tiny writes, use buffered streams appropriately.

## Key ideas

Use **profilers** to validate hypotheses; cache only with eviction and measured benefit.
