# Collections framework: `List`, `Set`, `Map`, `Queue`

## Core interfaces

- `Collection`, `List`, `Set`, `Queue`, `Deque`
- `Map` is not a `Collection`

## Implementations

- `ArrayList`: dynamic array, fast random access
- `LinkedList`: deque operations, less cache-friendly for middle access
- `HashSet`: average O(1) membership
- `TreeSet`: sorted, `NavigableSet`
- `HashMap`, `TreeMap`, `LinkedHashMap` (insertion-ordered)

## Iteration

Enhanced `for`, `Iterator.remove()` cautiously, `forEach` with lambdas.

## Key ideas

Choose the simplest structure that meets complexity needs; measure if unsure.
