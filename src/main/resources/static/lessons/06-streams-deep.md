# Streams: intermediate and terminal operations

## Pipeline

Source → intermediate ops (lazy) → terminal op (eager).

## Common operations

`map`, `flatMap`, `filter`, `distinct`, `sorted`, `peek` (debug), `takeWhile`, `dropWhile`.

Terminals: `collect`, `reduce`, `forEach`, `min`, `max`, `count`, `anyMatch`.

## Collectors

`toList()`, `toSet()`, `groupingBy`, `partitioningBy`, `joining`.

## Pitfalls

- Do not mutate shared state from parallel streams without synchronization.
- Do not use side-effect-heavy `forEach` when `collect` expresses intent better.

## Key ideas

Streams are about **declarative** data processing; measure readability vs loops.
