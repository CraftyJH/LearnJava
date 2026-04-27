# How to approach the capstone projects

## Project-driven mastery

Each capstone should produce:

1. A **README** with goals, build instructions, and design notes.
2. **Automated tests** for core logic.
3. A short **retrospective**: what you would refactor next.

## Scope control

Ship a small vertical slice first, then widen.

## Code review mindset

Explain decisions as if reviewing a teammate's PR.

## Key ideas

Mastery is demonstrated by **iterative improvement**, not a single perfect commit.

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

