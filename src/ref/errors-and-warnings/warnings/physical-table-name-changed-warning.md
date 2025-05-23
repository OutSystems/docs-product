---
summary: Explore how OutSystems 11 (O11) handles existing database table name conflicts by automatically renaming physical table names.
locale: en-us
guid: 7e812677-ceb0-4d0d-8e79-b56f14a7a28b
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: database management, entity modeling, conflict resolution, application development, data migration
audience:
  - mobile developers
  - frontend developers
  - backend developers
  - full stack developers
  - platform administrators
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Physical Table Name Changed Warning

Message
:   `Entity <entity> physical table name was set  to <table'> because an external table name <table> already exists.`

Cause
:   The name of the physical table name associated to the entity already exists in the database. Service Studio automatically renamed the physical table name to `<table'>` to avoid name clashing in the database.
