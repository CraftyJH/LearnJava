# Enums: type-safe constants with behavior

## Basic enum

```java
public enum Season { SPRING, SUMMER, FALL, WINTER }
```

## Constructors and fields

Enums are full classes: fields, methods, even per-constant class bodies.

## `EnumSet` and `EnumMap`

Compact, fast specialized collections for enum keys.

## Key ideas

Prefer enums over magic strings for fixed sets of alternatives.
