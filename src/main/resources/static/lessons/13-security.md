# Secure Java coding: validation, crypto, deserialization

## Input validation

Treat all external input as hostile: sizes, encodings, unexpected fields.

## Crypto

Use modern algorithms (AES-GCM), secure random `SecureRandom`, never hard-code keys.

## Deserialization

Avoid Java serialization on untrusted data; prefer signed formats with schema validation.

## Key ideas

Follow OWASP guidance; keep dependencies updated.
