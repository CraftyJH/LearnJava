# Iterators and a first look at Streams

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
