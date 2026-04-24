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
