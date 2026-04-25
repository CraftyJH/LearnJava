# `java.time`: modern date and time API

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
