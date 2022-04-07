---
locale: en-us
guid: cc89e846-d1a0-41bb-b604-c2ecef4bbf6c
---

# Invalid User Function Error

The `Invalid User Function` error is issued in the following situations:

* `Action <action> must have exactly one output parameter to be available as a function`

    You have a user-defined action with the property Function set to Yes that either has none or more than one output parameter.

    Set the Function property to No or have only one output parameter in the action.

Double-click on the error line to take you directly to the user-defined action offending property.
