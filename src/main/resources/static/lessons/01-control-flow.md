# Conditionals and loops

## `if / else if / else`

Conditions must be `boolean`. There is no truthiness for `int` or pointers.

## `switch`

Modern `switch` can be an **expression** and supports multi-label cases:

```java
int day = 3;
String name = switch (day) {
    case 1, 7 -> "weekend edge";
    default -> "other";
};
```

## Loops

- `while` / `do-while`
- `for` traditional
- **enhanced for** over arrays and `Iterable`

```java
for (int v : arr) {
    System.out.println(v);
}
```

## `break` and `continue`

`break` exits the nearest loop or `switch`. Labeled `break` can exit outer loops (rare).

## Key ideas

Keep loop bodies small. Extract methods when nesting exceeds two levels for readability.

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

