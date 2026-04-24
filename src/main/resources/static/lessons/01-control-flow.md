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
