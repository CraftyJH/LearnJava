# Generics: type parameters, wildcards, erasure

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
