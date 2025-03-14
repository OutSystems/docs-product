---
summary: OutSystems 11 (O11) triggers an 'Invalid User Function' error when a function-set action lacks exactly one output parameter.
locale: en-us
guid: cc89e846-d1a0-41bb-b604-c2ecef4bbf6c
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: error handling, debugging, application development, platform troubleshooting, functionality configuration
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Invalid User Function Error

The `Invalid User Function` error is issued in the following situations:

* `Action <action> must have exactly one output parameter to be available as a function`

    You have a user-defined action with the property Function set to Yes that either has none or more than one output parameter.

    Set the Function property to No or have only one output parameter in the action.

Double-click on the error line to take you directly to the user-defined action offending property.
