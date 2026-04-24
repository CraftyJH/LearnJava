# Lambdas, functional interfaces, and method references

## Functional interfaces

Single abstract method (SAM) interfaces such as `Runnable`, `Supplier<T>`, `Function<T,R>`, `Predicate<T>`, `Consumer<T>`.

## Lambda syntax

```java
Predicate<String> p = s -> s.isBlank();
```

## Method references

`String::isEmpty`, `this::save`, `MyClass::parse`.

## Key ideas

Lambdas capture variables that are **effectively final**.

Keep lambdas short; extract methods when logic grows.
