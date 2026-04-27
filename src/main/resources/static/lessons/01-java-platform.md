# The Java platform: JVM, bytecode, and write-once philosophy

## Why Java succeeded

Java aimed for **portable**, **memory-safe**, **networked** programs. The JVM abstracts the operating system so the same bytecode can run on servers, desktops, and (historically) browsers.

## Bytecode vs machine code

- **Ahead-of-time** languages often compile directly to CPU instructions.
- Java compiles to **bytecode**, a compact instruction set for an abstract machine.
- The JVM may **interpret**, **JIT-compile** hot code to native instructions, and apply **optimizations** at runtime.

## Garbage collection (preview)

Java manages heap memory automatically. You allocate objects; the **GC** reclaims unreachable objects. This reduces entire classes of bugs but introduces **latency** and **tuning** topics you will meet later.

## Class loading (preview)

Classes can be loaded dynamically. Frameworks use this for plugins, dependency injection, and proxies.

## Check your understanding

1. What is the difference between `javac` and `java`?
2. Why is bytecode helpful for portability?
3. Name one trade-off of automatic garbage collection.

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

