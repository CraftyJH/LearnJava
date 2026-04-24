# Records (Java 16+): data carriers

## Motivation

Boilerplate for data classes (constructors, getters, `equals`, `hashCode`, `toString`) is tedious and error-prone.

## Record declaration

```java
public record Point(int x, int y) {}
```

The compiler generates accessors `x()` and `y()`, constructor, `equals`, `hashCode`, `toString`.

## Canonical constructor customization

```java
public record Email(String value) {
    public Email {
        if (value == null || value.isBlank()) {
            throw new IllegalArgumentException("email required");
        }
    }
}
```

## Key ideas

Use records for **transparent data** with clear invariants. Use classes when you need extensive mutable state or inheritance hierarchies.
