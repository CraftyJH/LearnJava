# Sealed classes and exhaustive pattern matching (overview)

## Sealed hierarchies

Restrict subclasses to a known set:

```java
public sealed interface Shape permits Circle, Rectangle { }
```

## Exhaustive `switch`

With sealed types, the compiler can verify you handled all permitted subtypes (when patterns are enabled and complete).

## Key ideas

Sealed types model **closed domains** (AST nodes, payment types) safely.

Learn `instanceof` patterns:

```java
if (shape instanceof Circle c) {
    System.out.println(c.radius());
}
```
