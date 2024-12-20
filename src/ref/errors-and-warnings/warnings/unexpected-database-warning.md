---
summary: Explore solutions for the database warning in OutSystems 11 (O11) when module and server database types mismatch.
locale: en-us
guid: dc568697-e3e5-4dae-9f80-7c4663228e68
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: database configuration, compatibility issues, platform configuration, sql query optimization, error resolution
audience:
  - full stack developers
  - platform administrators
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Unexpected Database Warning

Message
:   `module 'Database' property (<database>) does not match Platform Server database type (<database>)`

Cause
:   The Database module property is different from the type of the OutSystems database.

Recommendation
:   You should set this property with the exact database type or choose '(Both)'. Besides, you should also validate whether your SQL queries are compliant with the database type you are using.
