# Inheritance, overriding, and polymorphism

## `extends`

Subclass inherits superclass members (subject to visibility).

## Method overriding

Same signature, runtime dispatch on actual object type (`virtual` methods by default).

Use `@Override` to catch signature mistakes.

## `super`

Calls superclass implementation: `super.method()` or `super(...)`.

## `final` methods/classes

`final` class cannot be extended; `final` method cannot be overridden.

## Key ideas

Favor **composition over inheritance** when behavior varies widely; inheritance is a strong coupling.
