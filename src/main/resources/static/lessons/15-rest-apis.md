# REST-ish HTTP APIs: design and implementation sketch

## Resources and verbs

Nouns in paths; HTTP methods express actions; status codes convey outcomes.

## DTOs

Separate wire models from domain models when boundaries differ.

## Validation

Bean Validation (`@NotNull`, etc.) at boundaries.

## Key ideas

Idempotency and safety (`GET`, `PUT`) matter for retries and caches.
