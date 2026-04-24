# `Optional`: when and when not to use it

## Purpose

Model **absence** without `null` in APIs you control.

## Good uses

Return values from lookup methods; chain transformations with `map`, `flatMap`, `filter`.

## Poor uses

Fields, method parameters, collections of `Optional`, serializing to JSON without care.

## Key ideas

`Optional` is not a silver bullet for null safety; Kotlin and other languages bake nullability into types.
