# `static`, `final`, and initialization order

## `static` members

Belong to the class. `static` methods cannot access instance fields directly.

## `static` blocks

Run once when the class is initialized:

```java
static {
    // class-level setup
}
```

## `final` fields

- Instance `final` must be definitely assigned by the end of every constructor.
- `static final` constants are common for configuration keys.

## Initialization order (simplified)

1. Superclass static initializers
2. Subclass static initializers
3. Superclass instance fields and instance initializers
4. Superclass constructor
5. Subclass instance fields and instance initializers
6. Subclass constructor

## Key ideas

Avoid complex initialization cycles across subclasses; keep constructors simple.
