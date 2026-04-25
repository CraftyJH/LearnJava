# Memory model of the JVM: heap, stack, GC ergonomics

## Stack vs heap

Local primitives and references live on thread stacks; objects live in the heap (with exceptions like scalarization optimizations).

## GC collectors

Modern JDKs use region-based collectors (G1, ZGC, Shenandoah depending on version/vendor).

## Tuning mindset

Measure pause times and throughput requirements; defaults are good for many apps.

## Key ideas

Avoid unnecessary object churn in hot loops; prefer clear algorithms first.
