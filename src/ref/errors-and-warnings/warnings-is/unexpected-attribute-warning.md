---
locale: en-us
guid: 94bc7cd0-af9e-41fe-9b49-cd95a1aa4b13
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Unexpected Attribute Warning

Message
:   `'<attribute>' is an invalid attribute name in <database>.`

Cause
:   You are using an Oracle database and the name of that attribute is a reserved word. The reserved words are as follows: `timestamp`, `number`, `blob`, `clob`, and `varchar2`.

Recommendation
:   Change the attribute name according to Oracle rules.
