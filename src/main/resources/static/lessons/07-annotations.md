# Annotations and metadata

## Declaring

```java
public @interface Versioned {
    int value();
}
```

## Built-in

`@Override`, `@Deprecated`, `@SuppressWarnings`, `@FunctionalInterface`.

## Processing

Annotation processors run at compile time (e.g., code generation).

## Key ideas

Annotations document **framework contracts** (JPA, Spring, tests). Understand retention: `SOURCE`, `CLASS`, `RUNTIME`.
