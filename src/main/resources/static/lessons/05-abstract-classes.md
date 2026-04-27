# Abstract classes and interfaces

## Abstract class

Cannot be instantiated; may contain abstract methods.

## Interface

Before Java 8: only abstract methods and constants.

Java 8+: **default** and **static** methods in interfaces.

Java 9+: **private** methods in interfaces.

## Multiple inheritance of type

A class can implement multiple interfaces; diamond problems are resolved with explicit rules for defaults.

## Key ideas

Use interfaces for **capabilities** (`Serializable`, `Comparable`). Use abstract classes for **shared partial implementation**.

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

