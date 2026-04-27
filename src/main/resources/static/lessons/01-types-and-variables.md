# Primitive types, variables, and literals

## Primitive types

Java has eight primitives:

| Type | Bits (typical) | Notes |
|------|----------------|-------|
| `byte` | 8 | small integers |
| `short` | 16 | uncommon |
| `int` | 32 | default integer math |
| `long` | 64 | suffix `L` on literals |
| `float` | 32 | suffix `f` |
| `double` | 64 | default floating math |
| `char` | 16-bit UTF-16 unit | not always one Unicode character |
| `boolean` | JVM-specific | `true` / `false` |

## Variables

```java
int count = 3;
final double PI = 3.14159;
```

`final` means the variable cannot be reassigned (constants by convention are `UPPER_SNAKE_CASE`).

## Casting and promotion

Smaller types may be **promoted** to `int` in expressions. Narrowing casts can lose data:

```java
int x = (int) 3.9; // 3
```

## Underscores in numeric literals

```java
long credit = 1_000_000_000L;
```

## Pitfalls

- **Integer division**: `5 / 2` is `2`, not `2.5`.
- **Floating comparisons**: prefer tolerance checks or `BigDecimal` for money.

## Key ideas

Choose the smallest reasonable type for clarity, but default to `int` and `double` until you have a concrete constraint.

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

