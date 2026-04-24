# Regular expressions in Java

## `Pattern` and `Matcher`

```java
Pattern p = Pattern.compile("\d+");
Matcher m = p.matcher("Room 101");
if (m.find()) {
    System.out.println(m.group());
}
```

## Common flags

`Pattern.CASE_INSENSITIVE`, `Pattern.MULTILINE`, `Pattern.DOTALL`.

## Key ideas

Regex is powerful but unreadable; comment complex patterns or split into named steps.
