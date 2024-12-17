---
summary: Explore common `Invalid Join` error scenarios in OutSystems 11 (O11) related to entity and structure usage in join conditions.
locale: en-us
guid: 659d5361-cb0c-4aff-bab5-f021cc017017
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: error handling, database operations, entity relationships, data modeling, troubleshooting
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Invalid Join Error

The `Invalid Join` error is issued in the following situations:

* `Cannot use the <entity> entity twice in the same join condition. Change the join condition to use another entity`
  
    The same entity cannot be use in the same join condition.

    Edit the join condition to use two different entities.

* `<Structure> cannot be used in a join condition since it is a Structure`
  
    Cannot use a structure in a join condition.

    Remove the structure from your join condition.

Double-click on the error line to take you directly to the source of the error.
