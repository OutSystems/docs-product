---
summary: Learn how to resolve the "invalid attribute name in Oracle" error in OutSystems 11 (O11) by renaming attributes that conflict with Oracle reserved words.
locale: en-us
guid: 16902581-2d4e-4919-b101-7db15909734f
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: database management, oracle errors, entity modeling, database compatibility, reserved words
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
:   `<attribute> is an invalid attribute name in Oracle`

Cause
:   Your module is prepared to use an Oracle database or both databases, and you have an attribute with a name that is a reserved word in Oracle.

Recommendation
:   You should edit the entity attribute and change the name. The Oracle reserved words are as the following: `timestamp`, `number`, `blob`, `clob`, and `varchar2`.
