# Class loading, classifiers, and instrumentation (overview)

## ClassLoader hierarchy

Bootstrap → platform → application loaders.

## Custom class loaders

Used for plugins, isolation, hot reload in dev tools.

## Agents

`java.lang.instrument` can transform bytecode at load time (powerful and risky).

## Key ideas

Security-sensitive code must assume attackers can supply classes on the classpath.
