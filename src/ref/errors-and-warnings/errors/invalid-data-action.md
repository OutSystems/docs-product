---
summary: Learn how to resolve the 'Invalid Data Action' error in OutSystems 11 (O11) by ensuring Data Actions have properly assigned output parameters.
locale: en-us
guid: b3d0a226-12a9-4e71-8d5e-059cf703bf99
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: error handling, data actions, output parameters, debugging, service studio
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Invalid Data Action

The `Invalid Data Action` error is issued in the following situations:

* `<Data Action> must set a value to the <Output Parameter> output parameter.`

    You have a Data Action that does not set the value of the Output Parameter.

    Assign a value of the correct type to the Output Parameter.

* `<Data Action> must have at least one output parameter.`

    You have a Data Action that does not have any Output Parameters.

    Create at least one Output Parameter on the Data Action and assign values of the correct types to the new Output Parameters.

Double-click on the error line to take you directly to the source of the error.
