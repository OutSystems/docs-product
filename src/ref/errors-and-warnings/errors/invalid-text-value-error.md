---
summary: OutSystems 11 (O11) addresses the 'Invalid Text Value' error by guiding users to adjust text properties that do not meet character limits.
locale: en-us
guid: cfa237a8-7738-48a4-8561-bacf28c6e379
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: error handling, debugging, user interface development, data validation, outsystems development
audience:
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Invalid Text Value Error

The `Invalid Text Value` error is issued in the following situation:

* `<Property> value must have at least <number> characters`

    You have a Text property with a number of characters that is less than the ones allowed.

    Edit the property and fix its value.

* `<Property> value cannot have more than <number> characters`

    You have a Text property with a number of characters that is greater than the ones allowed.

    Edit this property and fix its value.

Double-click on the error line to take you directly to the invalid value.
