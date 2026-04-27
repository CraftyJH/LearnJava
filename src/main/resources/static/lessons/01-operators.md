# Operators, expressions, and precedence

## Arithmetic

`+ - * / %` with usual precedence. `%` is remainder, sign follows dividend in Java.

## Relational and logical

`== != < > <= >=` compare values. For objects, `==` compares **references** unless overloaded (strings are special due to interning—still avoid `==` for content).

Logical: `&& || !` with **short-circuiting**:

```java
if (s != null && s.length() > 0) { ... }
```

## Bitwise (useful later)

`& | ^ ~ << >> >>>` operate on integer bits. `>>>` is unsigned right shift.

## Assignment operators

`+= -= *= /= %= &= ...` evaluate once and assign.

## Ternary

```java
String label = n == 1 ? "one" : "many";
```

## Key ideas

Prefer clarity over clever one-liners. If precedence is unclear to a reader, add parentheses.

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

