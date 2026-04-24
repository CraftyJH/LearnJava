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
