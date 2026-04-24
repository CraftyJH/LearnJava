# Classes, objects, constructors, and `this`

## Class as blueprint

A **class** defines fields (state) and methods (behavior). An **object** is an instance in memory.

## Constructors

Constructors initialize new objects. If you define none, Java provides a default no-arg constructor unless you define any constructor.

## `this`

Refers to the current instance. Common uses: disambiguate fields from parameters; call other constructors with `this(...)`.

## Encapsulation

Hide fields behind accessors (`getX`, `setX`) when invariants must be enforced.

## Key ideas

Start with **immutable** objects when possible: fewer bugs in concurrent and large systems.
