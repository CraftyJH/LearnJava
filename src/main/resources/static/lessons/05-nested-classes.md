# Nested and inner classes

## Kinds

- **static nested class**: like a top-level class scoped inside another type
- **inner class**: holds implicit reference to outer instance
- **local class**: inside a method
- **anonymous class**: quick one-off implementation (often replaced by lambdas)

## Key ideas

Inner classes can leak outer references; prefer `static` nested unless you truly need the outer instance.
