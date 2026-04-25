# Assertions and defensive programming

## `assert`

```java
assert x >= 0 : "x must be non-negative";
```

Assertions are disabled unless you run with `-ea`. Use them for **internal invariants**, not user input validation.

## Preconditions

For public APIs, validate arguments and throw `IllegalArgumentException` or `Objects.requireNonNull`.

## Key ideas

Separate **public contract checks** (always on) from **internal sanity checks** (assertions in dev/test).
