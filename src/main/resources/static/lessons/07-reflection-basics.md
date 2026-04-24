# Reflection basics (carefully)

## Core classes

`Class`, `Method`, `Field`, `Constructor`.

## Example

```java
Method m = String.class.getMethod("length");
int len = (Integer) m.invoke("abc");
```

## Trade-offs

Reflection breaks compile-time checks, can break across versions, and may violate module access rules.

## Key ideas

Use reflection where frameworks require it; prefer normal types elsewhere.
