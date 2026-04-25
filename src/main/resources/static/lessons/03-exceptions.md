# Exceptions: checked vs unchecked, try-with-resources

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
