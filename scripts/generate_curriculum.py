#!/usr/bin/env python3
"""Generate curriculum.json and lesson markdown files under src/main/resources/static/."""
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSONS_DIR = ROOT / "src/main/resources/static/lessons"
DATA_DIR = ROOT / "src/main/resources/static/data"

LESSONS_DIR.mkdir(parents=True, exist_ok=True)
DATA_DIR.mkdir(parents=True, exist_ok=True)


def md(title: str, body: str) -> str:
    return f"# {title}\n\n{body.strip()}\n"


# Each entry: (filename, title, markdown_body)
LESSON_SPECS = []

# --- Unit 0: Orientation ---
LESSON_SPECS += [
    (
        "00-welcome.md",
        "Welcome and how to use this course",
        """
## What you will build

You will progress from writing your first program to designing **multi-module style** applications: CLI tools, data processing, APIs (conceptually), concurrency, and larger **capstone-style** projects. Every lesson ends with runnable code in the **mini-IDE** on the right.

## How to study effectively

1. **Read the theory** first, but do not memorize every keyword on day one.
2. **Type** the starter code yourself; muscle memory matters.
3. **Predict** the output before you click **Run**.
4. When stuck, use **Hints**, then re-read the *Key ideas* section.
5. Keep a personal **cheat sheet** (one page per topic) in your own notes.

## The Java platform in one picture

- **Language**: syntax + semantics (what you write).
- **Compiler (`javac`)**: turns `.java` into **bytecode** (`.class`).
- **JVM**: executes bytecode with safety checks and optimizations.
- **JDK**: compiler + tools + libraries you need to develop.
- **JRE** (older term): runtime only; modern releases bundle runtime with JDK.

## Mini-IDE features

- **Monaco editor** with Java-like highlighting.
- **Run** sends your code to the server, compiles it with the JDK, and captures output.
- **Reset** restores the lesson starter template.

## Mindset: beginner to mastery

**Beginner** knows syntax and can read simple programs. **Intermediate** chooses correct collections, models errors, and tests edge cases. **Advanced** reasons about performance, concurrency contracts, and library design. **Mastery** means you can teach it: you can explain trade-offs and refactor safely under time pressure.

This course is intentionally large: treat it as a **multi-month** syllabus, not a weekend sprint.
""",
    ),
    (
        "00-setup-jdk.md",
        "Installing the JDK and your first commands",
        """
## Install a JDK

Use **JDK 17 or newer** (this course targets modern Java). Popular distributions:

- **Eclipse Temurin** (Adoptium)
- **Amazon Corretto**
- **Oracle JDK** (license terms differ)

Verify in a terminal:

```text
java -version
javac -version
```

Both commands should report the same major version family.

## Compile and run locally (optional but recommended)

```text
javac Hello.java
java Hello
```

Your public class name must match the file name (`Hello.java` → `class Hello`).

## Editors

- **IntelliJ IDEA Community** is excellent for Java.
- **VS Code** with Java extensions works well.
- This website gives you a sandbox; your local IDE is where you will work on the **major projects**.

## Key ideas

- The **classpath** tells the JVM where to find classes.
- **Packages** map to directories and avoid name collisions.
""",
    ),
]

# --- Unit 1: Fundamentals (many small lessons combined in rich files) ---
LESSON_SPECS += [
    (
        "01-java-platform.md",
        "The Java platform: JVM, bytecode, and write-once philosophy",
        """
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
""",
    ),
    (
        "01-types-and-variables.md",
        "Primitive types, variables, and literals",
        """
## Primitive types

Java has eight primitives:

| Type | Bits (typical) | Notes |
|------|----------------|-------|
| `byte` | 8 | small integers |
| `short` | 16 | uncommon |
| `int` | 32 | default integer math |
| `long` | 64 | suffix `L` on literals |
| `float` | 32 | suffix `f` |
| `double` | 64 | default floating math |
| `char` | 16-bit UTF-16 unit | not always one Unicode character |
| `boolean` | JVM-specific | `true` / `false` |

## Variables

```java
int count = 3;
final double PI = 3.14159;
```

`final` means the variable cannot be reassigned (constants by convention are `UPPER_SNAKE_CASE`).

## Casting and promotion

Smaller types may be **promoted** to `int` in expressions. Narrowing casts can lose data:

```java
int x = (int) 3.9; // 3
```

## Underscores in numeric literals

```java
long credit = 1_000_000_000L;
```

## Pitfalls

- **Integer division**: `5 / 2` is `2`, not `2.5`.
- **Floating comparisons**: prefer tolerance checks or `BigDecimal` for money.

## Key ideas

Choose the smallest reasonable type for clarity, but default to `int` and `double` until you have a concrete constraint.
""",
    ),
    (
        "01-operators.md",
        "Operators, expressions, and precedence",
        """
## Arithmetic

`+ - * / %` with usual precedence. `%` is remainder, sign follows dividend in Java.

## Relational and logical

`== != < > <= >=` compare values. For objects, `==` compares **references** unless overloaded (strings are special due to interning—still avoid `==` for content).

Logical: `&& || !` with **short-circuiting**:

```java
if (s != null && s.length() > 0) { ... }
```

## Bitwise (useful later)

`& | ^ ~ << >> >>>` operate on integer bits. `>>>` is unsigned right shift.

## Assignment operators

`+= -= *= /= %= &= ...` evaluate once and assign.

## Ternary

```java
String label = n == 1 ? "one" : "many";
```

## Key ideas

Prefer clarity over clever one-liners. If precedence is unclear to a reader, add parentheses.
""",
    ),
    (
        "01-control-flow.md",
        "Conditionals and loops",
        """
## `if / else if / else`

Conditions must be `boolean`. There is no truthiness for `int` or pointers.

## `switch`

Modern `switch` can be an **expression** and supports multi-label cases:

```java
int day = 3;
String name = switch (day) {
    case 1, 7 -> "weekend edge";
    default -> "other";
};
```

## Loops

- `while` / `do-while`
- `for` traditional
- **enhanced for** over arrays and `Iterable`

```java
for (int v : arr) {
    System.out.println(v);
}
```

## `break` and `continue`

`break` exits the nearest loop or `switch`. Labeled `break` can exit outer loops (rare).

## Key ideas

Keep loop bodies small. Extract methods when nesting exceeds two levels for readability.
""",
    ),
    (
        "01-arrays.md",
        "Arrays: creation, indexing, and multi-dimensional arrays",
        """
## Creation

```java
int[] a = new int[3];
int[] b = {1, 2, 3};
```

Length is `a.length` (field, not method).

## Bounds

Out-of-range access throws `ArrayIndexOutOfBoundsException`.

## Multi-dimensional

```java
int[][] grid = new int[3][4];
```

Ragged arrays are possible: each row can have different lengths.

## Copying

`System.arraycopy` or `Arrays.copyOf`.

## Key ideas

Prefer **lists** (`ArrayList`) for growable collections; arrays are fixed size and lower-level.
""",
    ),
    (
        "01-methods.md",
        "Methods, parameters, return values, and overloading",
        """
## Declaration

```java
public static int add(int a, int b) {
    return a + b;
}
```

`static` belongs to the class, not an instance.

## Overloading

Same method name, different parameter lists. Return type alone is **not** enough to overload.

## Varargs

```java
static int sum(int first, int... rest) { ... }
```

Varargs must be last parameter.

## Key ideas

Methods should be **short**, do one thing, and use names that read like intent: `computeTotalPrice`, not `doStuff`.
""",
    ),
]

LESSON_SPECS += [
    (
        "02-classes-and-objects.md",
        "Classes, objects, constructors, and `this`",
        """
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
""",
    ),
    (
        "02-packages.md",
        "Packages, modules (overview), and JAR basics",
        """
## Packages

```java
package com.example.app;

public class User { }
```

Directory structure must mirror package names. Packages avoid collisions and organize large codebases.

## Imports

`import java.util.List;` or wildcard `import java.util.*;` (use sparingly for readability).

## Module system (Java 9+)

The **Java Platform Module System** adds `module-info.java` to declare exported packages and required modules. Enterprise apps may still be classpath-based; learn modules when you ship libraries.

## JAR files

A **JAR** is a zip of `.class` files plus metadata. Executable JARs specify a `Main-Class` in the manifest.

## Key ideas

Naming packages by **reverse DNS** (`com.yourname.project`) is standard.
""",
    ),
    (
        "02-static-and-final.md",
        "`static`, `final`, and initialization order",
        """
## `static` members

Belong to the class. `static` methods cannot access instance fields directly.

## `static` blocks

Run once when the class is initialized:

```java
static {
    // class-level setup
}
```

## `final` fields

- Instance `final` must be definitely assigned by the end of every constructor.
- `static final` constants are common for configuration keys.

## Initialization order (simplified)

1. Superclass static initializers
2. Subclass static initializers
3. Superclass instance fields and instance initializers
4. Superclass constructor
5. Subclass instance fields and instance initializers
6. Subclass constructor

## Key ideas

Avoid complex initialization cycles across subclasses; keep constructors simple.
""",
    ),
    (
        "02-records-preview.md",
        "Records (Java 16+): data carriers",
        """
## Motivation

Boilerplate for data classes (constructors, getters, `equals`, `hashCode`, `toString`) is tedious and error-prone.

## Record declaration

```java
public record Point(int x, int y) {}
```

The compiler generates accessors `x()` and `y()`, constructor, `equals`, `hashCode`, `toString`.

## Canonical constructor customization

```java
public record Email(String value) {
    public Email {
        if (value == null || value.isBlank()) {
            throw new IllegalArgumentException("email required");
        }
    }
}
```

## Key ideas

Use records for **transparent data** with clear invariants. Use classes when you need extensive mutable state or inheritance hierarchies.
""",
    ),
]

LESSON_SPECS += [
    (
        "03-strings.md",
        "Strings, text blocks, and `StringBuilder`",
        r'''
## `String` immutability

`String` objects are immutable: methods return new strings.

## Concatenation

`+` creates a new string. In tight loops, use `StringBuilder`.

## `StringBuilder`

Mutable buffer:

```java
StringBuilder sb = new StringBuilder();
sb.append("a").append(123);
String s = sb.toString();
```

## Text blocks (Java 15+)

Java text blocks use a triple-double-quote delimiter; they are ideal for SQL, JSON, and HTML snippets.

```java
String sql = """
    SELECT id, name
    FROM users
    WHERE active = true
    """;
```

## Common APIs

`isEmpty`, `isBlank`, `strip`, `lines`, `formatted`, `repeat`.

## Key ideas

Never use `==` for string **content** equality; use `Objects.equals(a, b)` or `a.equals(b)` with null-safe patterns.
''',
    ),
    (
        "03-exceptions.md",
        "Exceptions: checked vs unchecked, try-with-resources",
        """
## Exception types

- **Checked**: must be declared or handled (`IOException`).
- **Unchecked**: extend `RuntimeException` (often programming errors).

## `try / catch / finally`

```java
try {
    risky();
} catch (IOException e) {
    // handle or wrap
} finally {
    // always runs (almost)
}
```

## try-with-resources

Auto-closes `AutoCloseable`:

```java
try (var in = Files.newInputStream(path)) {
    // use in
}
```

## Best practices

- Catch **specific** types first.
- Do not swallow exceptions silently.
- Prefer **meaningful** messages and preserve causes: `throw new ServiceException("...", e)`.

## Key ideas

Use exceptions for **exceptional** conditions, not normal control flow.
""",
    ),
    (
        "03-assertions.md",
        "Assertions and defensive programming",
        """
## `assert`

```java
assert x >= 0 : "x must be non-negative";
```

Assertions are disabled unless you run with `-ea`. Use them for **internal invariants**, not user input validation.

## Preconditions

For public APIs, validate arguments and throw `IllegalArgumentException` or `Objects.requireNonNull`.

## Key ideas

Separate **public contract checks** (always on) from **internal sanity checks** (assertions in dev/test).
""",
    ),
    (
        "03-enums.md",
        "Enums: type-safe constants with behavior",
        """
## Basic enum

```java
public enum Season { SPRING, SUMMER, FALL, WINTER }
```

## Constructors and fields

Enums are full classes: fields, methods, even per-constant class bodies.

## `EnumSet` and `EnumMap`

Compact, fast specialized collections for enum keys.

## Key ideas

Prefer enums over magic strings for fixed sets of alternatives.
""",
    ),
]

LESSON_SPECS += [
    (
        "04-generics-basics.md",
        "Generics: type parameters, wildcards, erasure",
        """
## Type parameters

```java
class Box<T> {
    private T value;
    public void set(T v) { value = v; }
    public T get() { return value; }
}
```

## Wildcards

- `List<?>` unknown element type (read mostly as `Object`)
- `List<? extends Number>` upper bounded
- `List<? super Integer>` lower bounded (PECS: producer `extends`, consumer `super`)

## Type erasure

Generic type parameters are erased at runtime (with bounds). This affects reflection and overload resolution edge cases.

## Key ideas

Generics catch errors at **compile time** and document intent: `List<String>` is clearer than `List`.
""",
    ),
    (
        "04-collections-overview.md",
        "Collections framework: `List`, `Set`, `Map`, `Queue`",
        """
## Core interfaces

- `Collection`, `List`, `Set`, `Queue`, `Deque`
- `Map` is not a `Collection`

## Implementations

- `ArrayList`: dynamic array, fast random access
- `LinkedList`: deque operations, less cache-friendly for middle access
- `HashSet`: average O(1) membership
- `TreeSet`: sorted, `NavigableSet`
- `HashMap`, `TreeMap`, `LinkedHashMap` (insertion-ordered)

## Iteration

Enhanced `for`, `Iterator.remove()` cautiously, `forEach` with lambdas.

## Key ideas

Choose the simplest structure that meets complexity needs; measure if unsure.
""",
    ),
    (
        "04-comparators.md",
        "`Comparable` vs `Comparator` and sorting",
        """
## `Comparable<T>`

Natural ordering: `a.compareTo(b)`.

## `Comparator<T>`

Multiple orderings:

```java
list.sort(Comparator.comparing(Person::lastName).thenComparing(Person::firstName));
```

## Stable sorts

`Collections.sort` / `List.sort` use TimSort: stable and good on real data.

## Key ideas

Avoid duplicating sort keys; extract comparators as constants for readability.
""",
    ),
    (
        "04-iterators-streams-intro.md",
        "Iterators and a first look at Streams",
        """
## Iterator

```java
for (Iterator<String> it = list.iterator(); it.hasNext(); ) {
    String s = it.next();
}
```

## Streams (preview)

A **Stream** is a sequence supporting aggregate operations. Streams can be parallel; understand **thread-safety** of underlying data sources.

```java
long count = names.stream().filter(n -> n.startsWith("A")).count();
```

## Key ideas

Streams excel at **pipeline** transformations; traditional loops excel when you need **early exits** or **mutations** across complex state machines.
""",
    ),
]

LESSON_SPECS += [
    (
        "05-inheritance.md",
        "Inheritance, overriding, and polymorphism",
        """
## `extends`

Subclass inherits superclass members (subject to visibility).

## Method overriding

Same signature, runtime dispatch on actual object type (`virtual` methods by default).

Use `@Override` to catch signature mistakes.

## `super`

Calls superclass implementation: `super.method()` or `super(...)`.

## `final` methods/classes

`final` class cannot be extended; `final` method cannot be overridden.

## Key ideas

Favor **composition over inheritance** when behavior varies widely; inheritance is a strong coupling.
""",
    ),
    (
        "05-abstract-classes.md",
        "Abstract classes and interfaces",
        """
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
""",
    ),
    (
        "05-sealed-classes.md",
        "Sealed classes and exhaustive pattern matching (overview)",
        """
## Sealed hierarchies

Restrict subclasses to a known set:

```java
public sealed interface Shape permits Circle, Rectangle { }
```

## Exhaustive `switch`

With sealed types, the compiler can verify you handled all permitted subtypes (when patterns are enabled and complete).

## Key ideas

Sealed types model **closed domains** (AST nodes, payment types) safely.

Learn `instanceof` patterns:

```java
if (shape instanceof Circle c) {
    System.out.println(c.radius());
}
```
""",
    ),
    (
        "05-nested-classes.md",
        "Nested and inner classes",
        """
## Kinds

- **static nested class**: like a top-level class scoped inside another type
- **inner class**: holds implicit reference to outer instance
- **local class**: inside a method
- **anonymous class**: quick one-off implementation (often replaced by lambdas)

## Key ideas

Inner classes can leak outer references; prefer `static` nested unless you truly need the outer instance.
""",
    ),
]

LESSON_SPECS += [
    (
        "06-lambdas-functional.md",
        "Lambdas, functional interfaces, and method references",
        """
## Functional interfaces

Single abstract method (SAM) interfaces such as `Runnable`, `Supplier<T>`, `Function<T,R>`, `Predicate<T>`, `Consumer<T>`.

## Lambda syntax

```java
Predicate<String> p = s -> s.isBlank();
```

## Method references

`String::isEmpty`, `this::save`, `MyClass::parse`.

## Key ideas

Lambdas capture variables that are **effectively final**.

Keep lambdas short; extract methods when logic grows.
""",
    ),
    (
        "06-streams-deep.md",
        "Streams: intermediate and terminal operations",
        """
## Pipeline

Source → intermediate ops (lazy) → terminal op (eager).

## Common operations

`map`, `flatMap`, `filter`, `distinct`, `sorted`, `peek` (debug), `takeWhile`, `dropWhile`.

Terminals: `collect`, `reduce`, `forEach`, `min`, `max`, `count`, `anyMatch`.

## Collectors

`toList()`, `toSet()`, `groupingBy`, `partitioningBy`, `joining`.

## Pitfalls

- Do not mutate shared state from parallel streams without synchronization.
- Do not use side-effect-heavy `forEach` when `collect` expresses intent better.

## Key ideas

Streams are about **declarative** data processing; measure readability vs loops.
""",
    ),
    (
        "06-optionals.md",
        "`Optional`: when and when not to use it",
        """
## Purpose

Model **absence** without `null` in APIs you control.

## Good uses

Return values from lookup methods; chain transformations with `map`, `flatMap`, `filter`.

## Poor uses

Fields, method parameters, collections of `Optional`, serializing to JSON without care.

## Key ideas

`Optional` is not a silver bullet for null safety; Kotlin and other languages bake nullability into types.
""",
    ),
]

LESSON_SPECS += [
    (
        "07-annotations.md",
        "Annotations and metadata",
        """
## Declaring

```java
public @interface Versioned {
    int value();
}
```

## Built-in

`@Override`, `@Deprecated`, `@SuppressWarnings`, `@FunctionalInterface`.

## Processing

Annotation processors run at compile time (e.g., code generation).

## Key ideas

Annotations document **framework contracts** (JPA, Spring, tests). Understand retention: `SOURCE`, `CLASS`, `RUNTIME`.
""",
    ),
    (
        "07-reflection-basics.md",
        "Reflection basics (carefully)",
        """
## Core classes

`Class`, `Method`, `Field`, `Constructor`.

## Example

```java
Method m = String.class.getMethod("length");
int len = (Integer) m.invoke("abc");
```

## Trade-offs

Reflection breaks compile-time checks, can break across versions, and may violate module access rules.

## Key ideas

Use reflection where frameworks require it; prefer normal types elsewhere.
""",
    ),
    (
        "07-modules-advanced.md",
        "Java modules: exports, requires, services",
        """
## `module-info.java`

```java
module com.example.app {
    requires java.net.http;
    exports com.example.api;
}
```

## Strong encapsulation

Modules hide internal packages even from reflection by default (with flags to loosen for migration).

## Key ideas

If you build libraries for wide use, plan JPMS compatibility early.
""",
    ),
]

LESSON_SPECS += [
    (
        "08-io-nio2.md",
        "I/O: `java.io` and NIO.2 (`java.nio.file`)",
        """
## Classic IO

`InputStream` / `OutputStream` for bytes; `Reader` / `Writer` for text.

## NIO.2

`Path`, `Files`, `FileSystems`. Modern file operations:

```java
String text = Files.readString(path);
Files.writeString(path, "hello");
```

## Charset always matters

Use `StandardCharsets.UTF_8` explicitly when converting bytes ↔ text.

## Key ideas

Prefer **try-with-resources** for any closeable stream.
""",
    ),
    (
        "08-serialization.md",
        "Serialization and safer alternatives",
        """
## Java serialization

`Serializable` + `ObjectOutputStream` can be convenient but risky: **gadget chains** and compatibility breakage.

## Safer patterns

JSON (Jackson), protobuf, flatbuffers, database tables.

## Key ideas

Treat serialized data as a **security boundary** if it crosses trust levels.
""",
    ),
    (
        "08-regex.md",
        "Regular expressions in Java",
        """
## `Pattern` and `Matcher`

```java
Pattern p = Pattern.compile("\\d+");
Matcher m = p.matcher("Room 101");
if (m.find()) {
    System.out.println(m.group());
}
```

## Common flags

`Pattern.CASE_INSENSITIVE`, `Pattern.MULTILINE`, `Pattern.DOTALL`.

## Key ideas

Regex is powerful but unreadable; comment complex patterns or split into named steps.
""",
    ),
]

LESSON_SPECS += [
    (
        "09-date-time.md",
        "`java.time`: modern date and time API",
        """
## Core types

- `Instant`: UTC timeline point
- `ZonedDateTime`: local + zone rules
- `LocalDate`, `LocalTime`, `LocalDateTime`: no zone
- `Duration` vs `Period`

## Parsing and formatting

`DateTimeFormatter.ofPattern("yyyy-MM-dd")` (thread-safe).

## Pitfalls

Do not mix legacy `java.util.Date` in new code unless integrating old APIs.

## Key ideas

Always know whether you mean **local civil time** or an **instant** on the timeline.
""",
    ),
    (
        "09-internationalization.md",
        "Locales, resource bundles, and formatting",
        """
## `Locale`

Language + country + variants.

## `ResourceBundle`

Externalize strings for translation.

## `NumberFormat` / `DateTimeFormatter` with locale

Display values appropriately per user region.

## Key ideas

Separate **business logic values** from **presentation formatting**.
""",
    ),
]

LESSON_SPECS += [
    (
        "10-threads-basics.md",
        "Concurrency: threads and synchronization basics",
        """
## Creating threads

- `new Thread(() -> { ... }).start()`
- `ExecutorService` for pooling (preferred)

## Shared mutable state

Synchronize access with `synchronized`, locks, or concurrent data structures.

## Visibility

The Java Memory Model defines **happens-before** rules; unsynchronized reads can see stale values.

## Key ideas

Concurrency bugs are **non-deterministic**; design immutability and clear ownership.
""",
    ),
    (
        "10-executor-futures.md",
        "Executors, `Future`, and `CompletableFuture`",
        """
## ExecutorService

```java
try (var pool = Executors.newVirtualThreadPerTaskExecutor()) {
    pool.submit(() -> work());
}
```

(Use platform thread pools when you need strict limits; virtual threads simplify blocking workloads on modern JDKs.)

## Futures

`future.get()` blocks; specify timeouts in production.

## CompletableFuture

Composable async pipelines: `supplyAsync`, `thenApply`, `thenCombine`, `exceptionally`.

## Key ideas

Understand **backpressure**: unlimited task submission can exhaust memory.
""",
    ),
    (
        "10-jmm-advanced.md",
        "Java Memory Model: `volatile`, atomics, and pitfalls",
        """
## `volatile`

Guarantees visibility and restricts reordering for the specific variable—not a mutex for compound actions.

## `java.util.concurrent.atomic`

Lock-free primitives for counters and references when contention patterns fit.

## Common bugs

Check-then-act races, lost updates, publishing partially constructed objects.

## Key ideas

Prefer **java.util.concurrent** utilities over low-level `wait/notify` for new code.
""",
    ),
    (
        "10-thread-safe-collections.md",
        "`ConcurrentHashMap`, queues, and copy-on-write",
        """
## Concurrent maps

`ConcurrentHashMap` supports safe concurrent updates with fine-grained locking.

## Queues

`ArrayBlockingQueue`, `LinkedBlockingQueue`, `PriorityBlockingQueue`.

## Copy-on-write

`CopyOnWriteArrayList` for read-heavy, write-rare scenarios.

## Key ideas

Iterator behavior differs from ordinary collections; many concurrent iterators are **weakly consistent**.
""",
    ),
]

LESSON_SPECS += [
    (
        "11-testing-junit.md",
        "Unit testing with JUnit 5 (conceptual)",
        """
## Why test

Tests document behavior, enable refactors, and catch regressions.

## JUnit 5 basics

`@Test`, lifecycle `@BeforeEach`, assertions (`assertEquals`, `assertThrows`).

## Good tests

Arrange-Act-Assert, one logical assertion cluster per test, meaningful names.

## Key ideas

Test **public contracts** and edge cases; avoid testing private implementation details unless necessary.
""",
    ),
    (
        "11-mocking.md",
        "Test doubles, mocking, and boundaries",
        """
## Types of doubles

Dummy, fake, stub, spy, mock.

## Mocking frameworks

Mockito is common in Java shops.

## Design for testability

Inject dependencies; avoid static singletons hiding I/O.

## Key ideas

If tests are painful, the code structure often needs improvement—not the test framework.
""",
    ),
    (
        "11-benchmarking.md",
        "Profiling and microbenchmarking cautions",
        """
## JVM warmup

JIT optimizes hot code; naive timing loops lie.

## JMH

Java Microbenchmark Harness is the standard for microbenchmarks.

## Profilers

CPU vs allocation profiling; async profilers (e.g., async-profiler) for production-like insight.

## Key ideas

Optimize measured bottlenecks, not guesses.
""",
    ),
]

LESSON_SPECS += [
    (
        "12-memory-gc.md",
        "Memory model of the JVM: heap, stack, GC ergonomics",
        """
## Stack vs heap

Local primitives and references live on thread stacks; objects live in the heap (with exceptions like scalarization optimizations).

## GC collectors

Modern JDKs use region-based collectors (G1, ZGC, Shenandoah depending on version/vendor).

## Tuning mindset

Measure pause times and throughput requirements; defaults are good for many apps.

## Key ideas

Avoid unnecessary object churn in hot loops; prefer clear algorithms first.
""",
    ),
    (
        "12-classloading.md",
        "Class loading, classifiers, and instrumentation (overview)",
        """
## ClassLoader hierarchy

Bootstrap → platform → application loaders.

## Custom class loaders

Used for plugins, isolation, hot reload in dev tools.

## Agents

`java.lang.instrument` can transform bytecode at load time (powerful and risky).

## Key ideas

Security-sensitive code must assume attackers can supply classes on the classpath.
""",
    ),
    (
        "12-performance.md",
        "Performance engineering without folklore",
        """
## Algorithm first

Big-O beats micro-optimizations.

## Collections costs

Resizing arrays, hashing collisions, boxing.

## IO costs

Batch reads, avoid tiny writes, use buffered streams appropriately.

## Key ideas

Use **profilers** to validate hypotheses; cache only with eviction and measured benefit.
""",
    ),
]

LESSON_SPECS += [
    (
        "13-security.md",
        "Secure Java coding: validation, crypto, deserialization",
        """
## Input validation

Treat all external input as hostile: sizes, encodings, unexpected fields.

## Crypto

Use modern algorithms (AES-GCM), secure random `SecureRandom`, never hard-code keys.

## Deserialization

Avoid Java serialization on untrusted data; prefer signed formats with schema validation.

## Key ideas

Follow OWASP guidance; keep dependencies updated.
""",
    ),
    (
        "13-logging.md",
        "Logging with SLF4J and backends",
        """
## Facade

SLF4J API with Logback or Log4j2 implementation.

## Levels

ERROR, WARN, INFO, DEBUG, TRACE—define policies per package.

## Structured logging

JSON logs integrate with observability stacks.

## Key ideas

Log **actionable** context (correlation ids), not secrets.
""",
    ),
    (
        "13-http-client.md",
        "`java.net.http.HttpClient` (Java 11+)",
        """
## Modern HTTP client

Supports HTTP/2, async requests, timeouts.

## Timeouts

Always set connect and request timeouts.

## Key ideas

For large ecosystems, frameworks (Spring WebClient) add resilience patterns (retries, circuit breakers).
""",
    ),
]

LESSON_SPECS += [
    (
        "14-design-patterns.md",
        "Design patterns as vocabulary",
        """
## Creational

Factory, Builder, Singleton (use sparingly).

## Structural

Adapter, Decorator, Facade, Proxy.

## Behavioral

Strategy, Template method, Observer, Command.

## Key ideas

Patterns name **forces** and **solutions**; do not force a pattern where simplicity suffices.
""",
    ),
    (
        "14-solid.md",
        "SOLID principles in Java terms",
        """
## SRP

One reason to change per class.

## OCP

Open for extension, closed for modification—often via interfaces.

## LSP

Subtypes must honor superclass contracts.

## ISP

Small interfaces; clients depend on what they use.

## DIP

Depend on abstractions; wire concretions at boundaries.

## Key ideas

Principles guide design reviews; they are not mathematical laws.
""",
    ),
    (
        "14-clean-architecture.md",
        "Layering, boundaries, and dependency direction",
        """
## Hexagonal / ports and adapters

Core domain isolated from IO frameworks.

## Package-by-feature vs layer

Both can work; consistency matters.

## Key ideas

Push **framework code** to the edges; keep domain logic testable without servers.
""",
    ),
]

LESSON_SPECS += [
    (
        "15-build-tools.md",
        "Maven and Gradle essentials",
        """
## Maven

`pom.xml`, coordinates (`groupId:artifactId:version`), lifecycle phases (`compile`, `test`, `package`).

## Gradle

Kotlin/Groovy DSL, tasks, incremental builds.

## Dependency management

Transitive dependencies, BOMs (e.g., Spring BOM), version catalogs.

## Key ideas

Reproducible builds pin versions; dependabot/renovate keep supply chains fresh.
""",
    ),
    (
        "15-ci-cd.md",
        "CI pipelines, artifacts, and release hygiene",
        """
## Typical pipeline

format → static analysis → unit tests → integration tests → package → deploy.

## Quality gates

Coverage thresholds cautiously; mutation testing for stronger signal.

## Key ideas

Fast feedback loops beat nightly-only integration.
""",
    ),
    (
        "15-spring-overview.md",
        "Spring Boot ecosystem (orientation)",
        """
## Inversion of Control

Spring container manages object graphs and lifecycles.

## Spring Boot

Opinionated auto-configuration, embedded server, actuator endpoints.

## Web stack

Spring MVC vs WebFlux (reactive) trade-offs.

## Key ideas

Framework mastery follows Java fundamentals; learn **dependency injection** and **HTTP** deeply.
""",
    ),
    (
        "15-databases-jdbc.md",
        "JDBC and persistence thinking",
        """
## JDBC

Connections, prepared statements (always parameterize), result sets.

## Connection pools

HikariCP is common.

## ORMs

JPA/Hibernate map objects to tables; understand SQL anyway.

## Key ideas

Migrations (Flyway/Liquibase) keep schema changes reviewable and repeatable.
""",
    ),
    (
        "15-rest-apis.md",
        "REST-ish HTTP APIs: design and implementation sketch",
        """
## Resources and verbs

Nouns in paths; HTTP methods express actions; status codes convey outcomes.

## DTOs

Separate wire models from domain models when boundaries differ.

## Validation

Bean Validation (`@NotNull`, etc.) at boundaries.

## Key ideas

Idempotency and safety (`GET`, `PUT`) matter for retries and caches.
""",
    ),
    (
        "15-microservices-caution.md",
        "Monoliths vs microservices: a pragmatic view",
        """
## Microservices buy distribution costs

Network latency, partial failures, distributed tracing, deployment complexity.

## When they help

Independent scaling, team autonomy, polyglot needs—when true.

## Key ideas

Start modular monolith; extract services when boundaries are proven.
""",
    ),
    (
        "16-capstone-guidance.md",
        "How to approach the capstone projects",
        """
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
""",
    ),
]

# Write markdown files
for filename, title, body in LESSON_SPECS:
    (LESSONS_DIR / filename).write_text(md(title, body), encoding="utf-8")


def challenge(instructions, starter, class_name="Main", hints=None):
    return {
        "instructions": instructions.strip(),
        "starterCode": starter.strip(),
        "className": class_name,
        "hints": hints or [],
    }


def section(sid, title, lessons, major_projects=None, projects_at_end=True):
    return {
        "id": sid,
        "title": title,
        "projectsAtEnd": projects_at_end,
        "lessons": lessons,
        "majorProjects": major_projects or [],
    }


curriculum = {
    "title": "Java: Beginner to Mastery",
    "subtitle": "Theory, coding challenges, mini-IDE, and major projects in one course.",
    "sections": [
        section(
            "orientation",
            "Orientation and the Java platform",
            [
                {
                    "id": "welcome",
                    "title": "Welcome",
                    "theoryPath": "lessons/00-welcome.md",
                    "challenge": challenge(
                        "Print two lines: your goal for learning Java, then the phrase `Hello, JVM`.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                        hints=["Use System.out.println twice."],
                    ),
                },
                {
                    "id": "jdk",
                    "title": "JDK and toolchain",
                    "theoryPath": "lessons/00-setup-jdk.md",
                    "challenge": challenge(
                        "Print the Java version string you expect to use locally (e.g., `JDK 21`) and print `javac` is the compiler.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                        hints=["This is output-only practice; any clear strings are fine."],
                    ),
                },
            ],
            major_projects=[
                {
                    "title": "Project 0 — Learning journal CLI",
                    "description": "Build a text-based menu program that lets you append dated notes to a file `journal.txt` (create if missing). Support: add note, list last 5 notes, exit. Parse input with `Scanner`.",
                    "stretchGoals": [
                        "Add search by keyword.",
                        "Refactor into small methods with clear names.",
                    ],
                }
            ],
        ),
        section(
            "fundamentals",
            "Syntax fundamentals: types, control flow, arrays, methods",
            [
                {
                    "id": "platform",
                    "title": "JVM and bytecode",
                    "theoryPath": "lessons/01-java-platform.md",
                    "challenge": challenge(
                        "Print one line explaining bytecode in your own words (10+ words).",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "types",
                    "title": "Types and variables",
                    "theoryPath": "lessons/01-types-and-variables.md",
                    "challenge": challenge(
                        "Declare a `byte`, a `long` literal, and a `double`. Print their sum as a `double`.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "operators",
                    "title": "Operators",
                    "theoryPath": "lessons/01-operators.md",
                    "challenge": challenge(
                        "Given `int a = 17, b = 5`, print integer division and remainder on separate lines.",
                        'public class Main {\n    public static void main(String[] args) {\n        int a = 17;\n        int b = 5;\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "control",
                    "title": "Control flow",
                    "theoryPath": "lessons/01-control-flow.md",
                    "challenge": challenge(
                        "Print the numbers 1 through 20, but print `Fizz` for multiples of 3, `Buzz` for multiples of 5, `FizzBuzz` for both.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "arrays",
                    "title": "Arrays",
                    "theoryPath": "lessons/01-arrays.md",
                    "challenge": challenge(
                        "Compute the average of `{2, 4, 6, 8}` using a loop and print it as a `double`.",
                        'public class Main {\n    public static void main(String[] args) {\n        int[] nums = {2, 4, 6, 8};\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "methods",
                    "title": "Methods",
                    "theoryPath": "lessons/01-methods.md",
                    "challenge": challenge(
                        "Write `static int max(int a, int b)` and print `max(9, 4)`.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n\n    // static int max(...)\n}',
                    ),
                },
            ],
            major_projects=[
                {
                    "title": "Project 1 — Terminal calculator",
                    "description": "Implement a REPL that reads lines like `3 + 4` or `10 / 2` (integer math is fine). Support `+ - * /` and `quit`. Handle divide-by-zero gracefully.",
                    "stretchGoals": [
                        "Add parentheses parsing (shunting-yard or recursive descent).",
                        "Add `double` mode toggle.",
                    ],
                }
            ],
        ),
        section(
            "oop-1",
            "Object-oriented Java: classes, packages, static/final, records",
            [
                {
                    "id": "classes",
                    "title": "Classes and objects",
                    "theoryPath": "lessons/02-classes-and-objects.md",
                    "challenge": challenge(
                        "Create a `BankAccount` class with `double balance`, `void deposit(double)`, `void withdraw(double)` (no negative balance). In `main`, print balance after a few operations.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO construct BankAccount and call methods\n    }\n}\n\n// class BankAccount { ... }',
                    ),
                },
                {
                    "id": "packages",
                    "title": "Packages (theory)",
                    "theoryPath": "lessons/02-packages.md",
                    "challenge": challenge(
                        "Explain in one printed line why reverse-DNS package names reduce collisions.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "static-final",
                    "title": "static and final",
                    "theoryPath": "lessons/02-static-and-final.md",
                    "challenge": challenge(
                        "Declare `static final double PI = 3.141592653589793` and print the circumference of a circle with radius 5.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "records",
                    "title": "Records",
                    "theoryPath": "lessons/02-records-preview.md",
                    "challenge": challenge(
                        "Define `record Book(String title, int pages)` and print a `Book` instance's `toString()`.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
            ],
            major_projects=[
                {
                    "title": "Project 2 — Library catalog",
                    "description": "Model `Book` and `Library` with add/list/search by title substring. Keep data in-memory. Provide a simple text menu.",
                    "stretchGoals": [
                        "Persist to a CSV file on exit and reload on start.",
                        "Add borrowing with due dates.",
                    ],
                }
            ],
        ),
        section(
            "strings-exceptions-enums",
            "Strings, exceptions, assertions, enums",
            [
                {
                    "id": "strings",
                    "title": "Strings and builders",
                    "theoryPath": "lessons/03-strings.md",
                    "challenge": challenge(
                        "Read no input: build the string `A-B-C-...-Z` using `StringBuilder` and print it.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "exceptions",
                    "title": "Exceptions",
                    "theoryPath": "lessons/03-exceptions.md",
                    "challenge": challenge(
                        "Write `static int parsePositiveInt(String s)` that throws `IllegalArgumentException` for null, blank, or non-positive values. In `main`, catch and print a friendly message.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO try parsePositiveInt with a few literals\n    }\n}',
                    ),
                },
                {
                    "id": "assertions",
                    "title": "Assertions",
                    "theoryPath": "lessons/03-assertions.md",
                    "challenge": challenge(
                        "Add an `assert` that `Math.sqrt(x) >= 0` for `x = 2` (note: assertions may be disabled unless `-ea`). Print a line explaining assertions are for internal invariants.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "enums",
                    "title": "Enums",
                    "theoryPath": "lessons/03-enums.md",
                    "challenge": challenge(
                        "Create `enum Direction { N, E, S, W }` and print all values using `values()`.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
            ],
            major_projects=[
                {
                    "title": "Project 3 — Robust CSV stats",
                    "description": "Read a small embedded CSV string in code (no file required) representing `name,score`. Parse with `String.split`, convert scores safely, skip bad rows with clear error messages, print min/max/average.",
                    "stretchGoals": [
                        "Read from a real file using `Files.readString` locally (IDE), keep embedded mode for the web runner.",
                        "Add median calculation.",
                    ],
                }
            ],
        ),
        section(
            "generics-collections",
            "Generics, collections, comparators, streams intro",
            [
                {
                    "id": "generics",
                    "title": "Generics",
                    "theoryPath": "lessons/04-generics-basics.md",
                    "challenge": challenge(
                        "Implement a simple `class Box<T>` with `void set(T v)` and `T get()`. Store a `String` and print it.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "collections",
                    "title": "Collections",
                    "theoryPath": "lessons/04-collections-overview.md",
                    "challenge": challenge(
                        "Create `ArrayList<Integer>`, add 3,1,4,1,5, remove all `1`s, print the list.",
                        'import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "comparators",
                    "title": "Sorting",
                    "theoryPath": "lessons/04-comparators.md",
                    "challenge": challenge(
                        'Sort `List<String>` `["bbb","a","cc"]` by length then lexicographically. Print the list.',
                        'import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "streams-intro",
                    "title": "Streams intro",
                    "theoryPath": "lessons/04-iterators-streams-intro.md",
                    "challenge": challenge(
                        "Given `List.of(1,2,3,4,5)`, print the sum of squares of even numbers using a stream pipeline.",
                        'import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
            ],
            major_projects=[
                {
                    "title": "Project 4 — Inventory with maps",
                    "description": "Track item SKU → quantity with `HashMap`. Support add/remove/adjust/print. Use `record Item(String sku, String name)` for metadata in another map if you like.",
                    "stretchGoals": [
                        "Add sorted reporting with `TreeMap`.",
                        "Persist map to JSON manually (string concat) for fun—or use Jackson locally.",
                    ],
                }
            ],
        ),
        section(
            "oop-2",
            "Inheritance, abstract types, sealed types, nested classes",
            [
                {
                    "id": "inheritance",
                    "title": "Inheritance",
                    "theoryPath": "lessons/05-inheritance.md",
                    "challenge": challenge(
                        "Model `Animal` with `String speak()` overridden by `Cat` and `Dog`. Print each speak.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "abstract",
                    "title": "Abstract classes and interfaces",
                    "theoryPath": "lessons/05-abstract-classes.md",
                    "challenge": challenge(
                        "Create interface `Drawable` with `String draw()`. Implement it for `Square`. Print `draw()`.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "sealed",
                    "title": "Sealed types",
                    "theoryPath": "lessons/05-sealed-classes.md",
                    "challenge": challenge(
                        "If your JDK supports it, write a tiny sealed interface `Shape` with `Circle` and `Rectangle` permits and print areas via `instanceof` pattern matching. If not supported in the runner, comment that and print a note.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "nested",
                    "title": "Nested classes",
                    "theoryPath": "lessons/05-nested-classes.md",
                    "challenge": challenge(
                        "Demonstrate a `static` nested class `Outer.Util` with a static method returning `int` sum.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
            ],
            major_projects=[
                {
                    "title": "Project 5 — Polymorphic simulation (tick-based)",
                    "description": "Create an `interface Entity { void tick(World w); }` and 2–3 entities with simple rules on a small grid printed as text. Run 10 ticks.",
                    "stretchGoals": [
                        "Add collisions.",
                        "Add a simple event log.",
                    ],
                }
            ],
        ),
        section(
            "functional",
            "Lambdas, streams deep dive, Optional",
            [
                {
                    "id": "lambdas",
                    "title": "Lambdas",
                    "theoryPath": "lessons/06-lambdas-functional.md",
                    "challenge": challenge(
                        "Use `Predicate<String>` to test blank strings and print results for `{\"a\",\"\", \" \"}`.",
                        'import java.util.function.*;\n\npublic class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "streams",
                    "title": "Streams",
                    "theoryPath": "lessons/06-streams-deep.md",
                    "challenge": challenge(
                        "Group words by first letter using streams: input list `List.of(\"apple\",\"apricot\",\"banana\")`, print map.",
                        'import java.util.*;\nimport java.util.stream.*;\n\npublic class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "optional",
                    "title": "Optional",
                    "theoryPath": "lessons/06-optionals.md",
                    "challenge": challenge(
                        "Write `static Optional<String> findShort(String s, int maxLen)` returning empty if null or longer than max. Demonstrate `orElse`.",
                        'import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
            ],
            major_projects=[
                {
                    "title": "Project 6 — Log query tool",
                    "description": "Model `record LogLine(Instant ts, String level, String msg)` (use `Instant.now()` fake times if easier). Provide filtering by level, substring search, and counting by level using streams.",
                    "stretchGoals": [
                        "Add time-window filtering.",
                        "Pretty-print histogram in ASCII.",
                    ],
                }
            ],
        ),
        section(
            "advanced-language",
            "Annotations, reflection (carefully), modules overview",
            [
                {
                    "id": "annotations",
                    "title": "Annotations",
                    "theoryPath": "lessons/07-annotations.md",
                    "challenge": challenge(
                        "Create `@interface Todo { String value(); }` and annotate `main` method (retention runtime optional). Print a line explaining metadata use.",
                        'import java.lang.annotation.*;\n\n@Retention(RetentionPolicy.SOURCE)\n@interface Todo {\n    String value();\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "reflection",
                    "title": "Reflection",
                    "theoryPath": "lessons/07-reflection-basics.md",
                    "challenge": challenge(
                        "Use reflection to print the declared methods of `String.class` count (not listing all if too long—print count only).",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "modules",
                    "title": "Modules",
                    "theoryPath": "lessons/07-modules-advanced.md",
                    "challenge": challenge(
                        "Print 2 lines: what `exports` does in `module-info.java`, and what `requires` does.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
            ],
            major_projects=[
                {
                    "title": "Project 7 — Mini plugin loader (classpath simulation)",
                    "description": "Define a `Greeter` interface and two implementations in the same file for simplicity. Select implementation name from `args[0]` via `switch` and print greeting (fake plugin loading without URLClassLoader).",
                    "stretchGoals": [
                        "Actually load from separate `.java` files locally and compile with `javac` script.",
                        "Add validation and helpful errors.",
                    ],
                }
            ],
        ),
        section(
            "io-time-i18n",
            "IO/NIO.2, serialization awareness, regex, time, i18n",
            [
                {
                    "id": "nio",
                    "title": "NIO.2",
                    "theoryPath": "lessons/08-io-nio2.md",
                    "challenge": challenge(
                        "Print a line recommending `Files.readString` for small text files and `BufferedInputStream` for large binary reads.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "serialization",
                    "title": "Serialization risks",
                    "theoryPath": "lessons/08-serialization.md",
                    "challenge": challenge(
                        "Print three bullet-like lines (plain text) describing risks of Java deserialization on untrusted data.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "regex",
                    "title": "Regex",
                    "theoryPath": "lessons/08-regex.md",
                    "challenge": challenge(
                        "Extract all integers from `\"a1b22c333\"` using `Pattern`/`Matcher` and print their sum.",
                        'import java.util.regex.*;\n\npublic class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "time",
                    "title": "java.time",
                    "theoryPath": "lessons/09-date-time.md",
                    "challenge": challenge(
                        "Print today's ISO local date using `LocalDate.now()` and the current instant using `Instant.now()`.",
                        'import java.time.*;\n\npublic class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "i18n",
                    "title": "Internationalization",
                    "theoryPath": "lessons/09-internationalization.md",
                    "challenge": challenge(
                        "Print numbers `1234567.89` formatted for `Locale.US` and `Locale.GERMANY` using `NumberFormat`.",
                        'import java.text.*;\nimport java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
            ],
            major_projects=[
                {
                    "title": "Project 8 — Time zone meeting planner (text)",
                    "description": "Given two zones and a list of candidate `LocalTime` windows, print which candidates are workable (simulate with fixed offsets using `ZoneOffset.ofHours`).",
                    "stretchGoals": [
                        "Use real `ZoneId` rules.",
                        "Add DST warnings using `ZoneRules`.",
                    ],
                }
            ],
        ),
        section(
            "concurrency",
            "Threads, executors, JMM, concurrent collections",
            [
                {
                    "id": "threads",
                    "title": "Threads basics",
                    "theoryPath": "lessons/10-threads-basics.md",
                    "challenge": challenge(
                        "Start two threads that each print 5 lines with their name (`Thread.currentThread().getName()`). Join both before exiting `main`.",
                        'public class Main {\n    public static void main(String[] args) throws Exception {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "executors",
                    "title": "Executors and futures",
                    "theoryPath": "lessons/10-executor-futures.md",
                    "challenge": challenge(
                        "Use `Executors.newFixedThreadPool(2)` to submit two `Callable<Integer>` tasks that sleep 100ms and return values; print sum of futures.",
                        'import java.util.concurrent.*;\n\npublic class Main {\n    public static void main(String[] args) throws Exception {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "jmm",
                    "title": "Memory model",
                    "theoryPath": "lessons/10-jmm-advanced.md",
                    "challenge": challenge(
                        "Print a careful explanation: why `volatile` alone may not fix `i++` races.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "conc-collections",
                    "title": "Concurrent collections",
                    "theoryPath": "lessons/10-thread-safe-collections.md",
                    "challenge": challenge(
                        "Demonstrate `ConcurrentHashMap.merge` to count word frequencies in a sentence.",
                        'import java.util.concurrent.*;\n\npublic class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
            ],
            major_projects=[
                {
                    "title": "Project 9 — Web crawler toy (single JVM)",
                    "description": "No real network required: simulate downloading URLs with `Thread.sleep` random ms. Use a fixed pool to process 20 URLs and collect statistics (min/max simulated latency).",
                    "stretchGoals": [
                        "Use `CompletableFuture` instead of raw futures.",
                        "Add cancellation after a timeout.",
                    ],
                }
            ],
        ),
        section(
            "quality-performance",
            "Testing concepts, profiling, JVM memory/GC, classloading",
            [
                {
                    "id": "junit",
                    "title": "JUnit concepts",
                    "theoryPath": "lessons/11-testing-junit.md",
                    "challenge": challenge(
                        "Write `static void assertEven(int n)` throwing `IllegalStateException` if odd. Call it from `main` with try/catch to simulate a test failure message.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "mocking",
                    "title": "Mocking",
                    "theoryPath": "lessons/11-mocking.md",
                    "challenge": challenge(
                        "Print two lines contrasting stubs vs mocks in your own words.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "bench",
                    "title": "Benchmarking",
                    "theoryPath": "lessons/11-benchmarking.md",
                    "challenge": challenge(
                        "Print why naive `System.nanoTime` loops can mislead without warmup.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "gc",
                    "title": "GC and memory",
                    "theoryPath": "lessons/12-memory-gc.md",
                    "challenge": challenge(
                        "Print a paragraph describing a scenario where creating many short-lived objects is OK due to generational GC (high-level).",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "classloading",
                    "title": "Classloading",
                    "theoryPath": "lessons/12-classloading.md",
                    "challenge": challenge(
                        "Explain in printed lines what a `ClassLoader` does at a high level.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "perf",
                    "title": "Performance",
                    "theoryPath": "lessons/12-performance.md",
                    "challenge": challenge(
                        "Print a checklist (5 items) for investigating a slow Java service before tuning JVM flags.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
            ],
            major_projects=[
                {
                    "title": "Project 10 — Deterministic simulation with property tests (manual)",
                    "description": "Implement a pure `Money` class (cents as `long`) with add/subtract and test it from `main` using a batch of assertions (throw on failure). No JUnit required in the runner.",
                    "stretchGoals": [
                        "Add JUnit locally in IntelliJ.",
                        "Generate random cases in `main` with a fixed seed.",
                    ],
                }
            ],
        ),
        section(
            "security-observability",
            "Security mindset, logging, HTTP client",
            [
                {
                    "id": "security",
                    "title": "Security",
                    "theoryPath": "lessons/13-security.md",
                    "challenge": challenge(
                        "Print 5 secure coding practices relevant to Java servers.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "logging",
                    "title": "Logging",
                    "theoryPath": "lessons/13-logging.md",
                    "challenge": challenge(
                        "Print an example log line including `level`, `thread`, `logger`, and `message` fields as JSON text.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "http",
                    "title": "HTTP client",
                    "theoryPath": "lessons/13-http-client.md",
                    "challenge": challenge(
                        "Print a code sketch (as comments) showing `HttpClient.newHttpClient().send(...)` with timeout—no need to actually call network.",
                        'public class Main {\n    public static void main(String[] args) {\n        /* TODO: sketch in comments */\n    }\n}',
                    ),
                },
            ],
            major_projects=[
                {
                    "title": "Project 11 — Audit log library (in-memory)",
                    "description": "Implement `AuditLog` storing immutable events (`Instant`, `String user`, `String action`). Provide query by user and export as CSV string.",
                    "stretchGoals": [
                        "Add ring buffer max size with drop policy.",
                        "Add checksum per batch.",
                    ],
                }
            ],
        ),
        section(
            "architecture",
            "Patterns, SOLID, layering",
            [
                {
                    "id": "patterns",
                    "title": "Design patterns",
                    "theoryPath": "lessons/14-design-patterns.md",
                    "challenge": challenge(
                        "Implement `interface PricingStrategy { int price(int cents); }` and two strategies (full price, 10% off). Print results for 1000 cents.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "solid",
                    "title": "SOLID",
                    "theoryPath": "lessons/14-solid.md",
                    "challenge": challenge(
                        "Pick one SOLID letter and print a Java-specific example scenario where it helps.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "clean",
                    "title": "Clean architecture",
                    "theoryPath": "lessons/14-clean-architecture.md",
                    "challenge": challenge(
                        "Print a layered diagram in ASCII (3 layers) for a hypothetical app: UI, domain, infrastructure.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
            ],
            major_projects=[
                {
                    "title": "Project 12 — Refactor spaghetti into layers",
                    "description": "Start from a purposely messy `main` that mixes IO and domain rules. Extract pure domain methods and separate printing. Keep behavior identical.",
                    "stretchGoals": [
                        "Introduce interfaces for repositories.",
                        "Add tests for domain methods locally.",
                    ],
                }
            ],
        ),
        section(
            "engineering",
            "Build tools, CI, Spring orientation, JDBC, REST, microservices caution",
            [
                {
                    "id": "maven-gradle",
                    "title": "Maven and Gradle",
                    "theoryPath": "lessons/15-build-tools.md",
                    "challenge": challenge(
                        "Print what `mvn verify` typically runs, in your own words, in 2–3 lines.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "ci",
                    "title": "CI/CD",
                    "theoryPath": "lessons/15-ci-cd.md",
                    "challenge": challenge(
                        "List 6 CI steps as separate println lines for a Java library.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "spring",
                    "title": "Spring Boot orientation",
                    "theoryPath": "lessons/15-spring-overview.md",
                    "challenge": challenge(
                        "Explain dependency injection in 3 println lines: what, why, example.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "jdbc",
                    "title": "JDBC and databases",
                    "theoryPath": "lessons/15-databases-jdbc.md",
                    "challenge": challenge(
                        "Print why `PreparedStatement` is preferred over string concatenation for SQL values.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "rest",
                    "title": "REST APIs",
                    "theoryPath": "lessons/15-rest-apis.md",
                    "challenge": challenge(
                        "Print example HTTP request line + headers for `GET /users/42` with `Accept: application/json`.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
                {
                    "id": "microservices",
                    "title": "Microservices caution",
                    "theoryPath": "lessons/15-microservices-caution.md",
                    "challenge": challenge(
                        "Print two pros and two cons of microservices from a Java team perspective.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                },
            ],
            major_projects=[
                {
                    "title": "Project 13 — Spring Boot local service (recommended)",
                    "description": "In IntelliJ, create a Spring Boot app with one `GET /hello` endpoint returning JSON `{message:\"...\"}`. This site cannot run Spring for you, but this is the bridge to industry skills.",
                    "stretchGoals": [
                        "Add Spring Data JPA entity + repository + H2.",
                        "Add validation and global exception handler.",
                    ],
                }
            ],
        ),
        section(
            "capstone",
            "Capstone guidance and mastery habits",
            [
                {
                    "id": "capstone-guide",
                    "title": "Capstone guidance",
                    "theoryPath": "lessons/16-capstone-guidance.md",
                    "challenge": challenge(
                        "Print your personal plan: 3 bullet lines with topics you will deepen next based on this course.",
                        'public class Main {\n    public static void main(String[] args) {\n        // TODO\n    }\n}',
                    ),
                }
            ],
            major_projects=[
                {
                    "title": "CAPSTONE A — Budget tracker with reports",
                    "description": "Categories, monthly totals, export CSV, and invariants (no negative balances unless credit). CLI or desktop optional.",
                    "stretchGoals": ["Charts in a local web UI.", "Import bank CSV."],
                },
                {
                    "title": "CAPSTONE B — Multi-user chat server ( sockets )",
                    "description": "Java `ServerSocket` accepts clients; broadcast messages; graceful shutdown; basic protocol (`JOIN`, `MSG`, `LEAVE`).",
                    "stretchGoals": ["TLS.", "User authentication.", "Persistence."],
                },
                {
                    "title": "CAPSTONE C — Build your own test runner",
                    "description": "Reflectively find `@Test` annotated methods (custom annotation) on classes you list, invoke, collect failures. This deepens reflection and classloading.",
                    "stretchGoals": ["Parallel execution with executor.", "JUnit-compatible XML report."],
                },
                {
                    "title": "CAPSTONE D — Plugin-based rule engine",
                    "description": "Define `Rule` interface, load rules from a config list, apply to a `Fact` map. Great for OOP + architecture practice.",
                    "stretchGoals": ["DSL parser for rules.", "Hot reload rules file."],
                },
            ],
            projects_at_end=True,
        ),
    ],
}

(DATA_DIR / "curriculum.json").write_text(json.dumps(curriculum, indent=2), encoding="utf-8")
print(f"Wrote {len(LESSON_SPECS)} lessons and curriculum.json")
