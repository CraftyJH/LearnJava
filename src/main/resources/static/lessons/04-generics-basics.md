# Generics: type parameters, wildcards, erasure

## Type parameters

```java
class Box<T> {
    private T value;
    public void set(T v) { value = v; }
    public T get() { return value; }
}
```

## Wildcards

- `List<?>` unknown element type (read mostly as `Object`)
- `List<? extends Number>` upper bounded
- `List<? super Integer>` lower bounded (PECS: producer `extends`, consumer `super`)

## Type erasure

Generic type parameters are erased at runtime (with bounds). This affects reflection and overload resolution edge cases.

## Key ideas

Generics catch errors at **compile time** and document intent: `List<String>` is clearer than `List`.

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

