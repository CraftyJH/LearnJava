# Methods, parameters, return values, and overloading

## Declaration

```java
public static int add(int a, int b) {
    return a + b;
}
```

`static` belongs to the class, not an instance.

## Overloading

Same method name, different parameter lists. Return type alone is **not** enough to overload.

## Varargs

```java
static int sum(int first, int... rest) { ... }
```

Varargs must be last parameter.

## Key ideas

Methods should be **short**, do one thing, and use names that read like intent: `computeTotalPrice`, not `doStuff`.
