# Layering, boundaries, and dependency direction

## Hexagonal / ports and adapters

Core domain isolated from IO frameworks.

## Package-by-feature vs layer

Both can work; consistency matters.

## Key ideas

Push **framework code** to the edges; keep domain logic testable without servers.
