# Java modules: exports, requires, services

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
