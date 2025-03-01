---
summary: Learn how to resolve the "Invalid Group" error in OutSystems 11 (O11) when columns are incorrectly grouped without using an entity attribute.
locale: en-us
guid: 3a0036d4-b992-4050-a1eb-fccbccdd2e86
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: error handling, entity attributes, data modeling, ide error messages, outsystems development
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Invalid Group Error

The `Invalid Group` error is issued in the following situations:

* `The <column> column cannot be grouped as <grouped column> since it does not use an entity attribute in its formula. Delete the <grouped column> column, or change the <column> formula to start using an entity attribute`
  
    You have created a new column by grouping an existing column, but it does not refer any Entity Attribute.

    Delete the new column, or edit the existing one to make it use an Entity Attribute in its formula.

* `The <column> column cannot be grouped since it does not use an entity attribute in its formula. Delete the <column> column, or change it to start using an entity attribute`
  
    You have created a new column by grouping an existing column, but it does not refer any Entity Attribute.

    Delete the new column, or edit the existing one to make it use an Entity Attribute in its formula.

Double-click on the error line to take you directly to the source of the error.
