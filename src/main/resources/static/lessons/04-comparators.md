# `Comparable` vs `Comparator` and sorting

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
