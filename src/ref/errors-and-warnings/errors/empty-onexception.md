---
summary: OutSystems 11 (O11) issues an 'Empty 'OnException'' error when an OnException action lacks an initial Exception Handler node.
locale: en-us
guid: 9428412d-0b04-497d-a0a9-a1eb18d2a797
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: error handling, exception handling, flow design, debugger, application logic
audience:
  - full stack developers
  - frontend developers
  - mobile developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Empty 'OnException'

The `Empty 'OnException'` error is issued in the following situations:

* `'OnException' action must have at least one Exception Handler node.`

    You have an OnException action that does not begin with an Exception Handler node.

    Begin the action flow of the OnException action with an Exception Handler node.

Double-click on the error line to take you directly to the source of the error.
