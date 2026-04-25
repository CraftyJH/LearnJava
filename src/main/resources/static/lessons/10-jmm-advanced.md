# Java Memory Model: `volatile`, atomics, and pitfalls

## `volatile`

Guarantees visibility and restricts reordering for the specific variable—not a mutex for compound actions.

## `java.util.concurrent.atomic`

Lock-free primitives for counters and references when contention patterns fit.

## Common bugs

Check-then-act races, lost updates, publishing partially constructed objects.

## Key ideas

Prefer **java.util.concurrent** utilities over low-level `wait/notify` for new code.
