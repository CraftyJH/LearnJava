# Profiling and microbenchmarking cautions

## JVM warmup

JIT optimizes hot code; naive timing loops lie.

## JMH

Java Microbenchmark Harness is the standard for microbenchmarks.

## Profilers

CPU vs allocation profiling; async profilers (e.g., async-profiler) for production-like insight.

## Key ideas

Optimize measured bottlenecks, not guesses.
