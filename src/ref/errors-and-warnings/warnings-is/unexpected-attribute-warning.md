---
summary: Explore how OutSystems 11 (O11) handles Oracle database reserved words and recommended attribute naming solutions.
locale: en-us
guid: 94bc7cd0-af9e-41fe-9b49-cd95a1aa4b13
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: database management, oracle database, reserved words, attribute naming, error handling
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Unexpected Attribute Warning

Message
:   `'<attribute>' is an invalid attribute name in <database>.`

Cause
:   You are using an Oracle database and the name of that attribute is a reserved word. The reserved words are as follows: `timestamp`, `number`, `blob`, `clob`, and `varchar2`.

Recommendation
:   Change the attribute name according to Oracle rules.
