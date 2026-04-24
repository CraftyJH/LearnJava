# Operators, expressions, and precedence

## Arithmetic

`+ - * / %` with usual precedence. `%` is remainder, sign follows dividend in Java.

## Relational and logical

`== != < > <= >=` compare values. For objects, `==` compares **references** unless overloaded (strings are special due to interning—still avoid `==` for content).

Logical: `&& || !` with **short-circuiting**:

```java
if (s != null && s.length() > 0) { ... }
```

## Bitwise (useful later)

`& | ^ ~ << >> >>>` operate on integer bits. `>>>` is unsigned right shift.

## Assignment operators

`+= -= *= /= %= &= ...` evaluate once and assign.

## Ternary

```java
String label = n == 1 ? "one" : "many";
```

## Key ideas

Prefer clarity over clever one-liners. If precedence is unclear to a reader, add parentheses.
