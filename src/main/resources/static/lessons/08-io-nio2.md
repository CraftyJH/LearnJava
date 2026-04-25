# I/O: `java.io` and NIO.2 (`java.nio.file`)

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
