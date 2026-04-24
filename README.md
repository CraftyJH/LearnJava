# Java Mastery Platform

A **Spring Boot** web application that combines a large **Java curriculum** (theory as Markdown, coding challenges, and major project briefs) with a **mini-IDE**: the [Monaco](https://microsoft.github.io/monaco-editor/) editor in the browser and **server-side compile/run** via the JDK on the machine hosting the app.

## Why a website (not Android)

Iteration is fastest when you edit in the browser, click **Run**, and see compiler and program output immediately. Android builds, emulators, and deployment cycles are heavier for rapid practice loops.

## Requirements

- **JDK 21+** on the server (the app uses `javac` from the same runtime).

## Run locally

```bash
mvn spring-boot:run
```

Open `http://localhost:8080`.

## Curriculum content

Theory lives under `src/main/resources/static/lessons/`. The navigation tree and challenges are generated into `src/main/resources/static/data/curriculum.json` by:

```bash
python3 scripts/generate_curriculum.py
```

Edit `scripts/generate_curriculum.py` to add sections, lessons, challenges, or major projects, then re-run the script.

## Security note

The `/api/run` endpoint compiles and executes user-supplied Java in the **same JVM** as the server, with time limits and classpath isolation for user classes. **Do not expose this endpoint to untrusted Internet users** without a hardened sandbox (containers, separate JVM, quotas, etc.). It is intended for **local learning** or trusted environments.
