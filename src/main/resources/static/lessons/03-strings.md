# Strings, text blocks, and `StringBuilder`

## `String` immutability

`String` objects are immutable: methods return new strings.

## Concatenation

`+` creates a new string. In tight loops, use `StringBuilder`.

## `StringBuilder`

Mutable buffer:

```java
StringBuilder sb = new StringBuilder();
sb.append("a").append(123);
String s = sb.toString();
```

## Text blocks (Java 15+)

Java text blocks use a triple-double-quote delimiter; they are ideal for SQL, JSON, and HTML snippets.

```java
String sql = """
    SELECT id, name
    FROM users
    WHERE active = true
    """;
```

## Common APIs

`isEmpty`, `isBlank`, `strip`, `lines`, `formatted`, `repeat`.

## Key ideas

Never use `==` for string **content** equality; use `Objects.equals(a, b)` or `a.equals(b)` with null-safe patterns.
