# Serialization and safer alternatives

## Java serialization

`Serializable` + `ObjectOutputStream` can be convenient but risky: **gadget chains** and compatibility breakage.

## Safer patterns

JSON (Jackson), protobuf, flatbuffers, database tables.

## Key ideas

Treat serialized data as a **security boundary** if it crosses trust levels.
