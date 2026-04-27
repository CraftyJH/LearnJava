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

## How to read Java like a practitioner

When you open a file, skim in this order: **package and imports** (dependencies), **public types** (what the module exports), then **constructors and public methods** (how it is used). Only then dive into private helpers. This mirrors how teams navigate large repositories.

## Common pitfalls (across lessons)

- Using `=` when you meant `==`, especially in `if` conditions.
- Integer division surprises (`5 / 2` is `2`, not `2.5`).
- Treating `null` as “empty”: always decide explicitly whether `null` is allowed.
- Catching `Exception` too broadly and hiding the real failure.

## Before you click Run

Say aloud **one predicted line of output**. If the real output differs, you have found a concrete misunderstanding—reread the theory section that matches the mismatch.

## After it works

Spend sixty seconds on **one** improvement: clearer variable names, a helper method, or a comment explaining *why* (not *what*). Small refactors build taste faster than only writing throwaway answers.

