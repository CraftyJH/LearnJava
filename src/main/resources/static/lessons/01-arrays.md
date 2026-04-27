# Arrays: creation, indexing, and multi-dimensional arrays

## Creation

```java
int[] a = new int[3];
int[] b = {1, 2, 3};
```

Length is `a.length` (field, not method).

## Bounds

Out-of-range access throws `ArrayIndexOutOfBoundsException`.

## Multi-dimensional

```java
int[][] grid = new int[3][4];
```

Ragged arrays are possible: each row can have different lengths.

## Copying

`System.arraycopy` or `Arrays.copyOf`.

## Key ideas

Prefer **lists** (`ArrayList`) for growable collections; arrays are fixed size and lower-level.

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

