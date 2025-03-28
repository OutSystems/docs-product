---
summary: OutSystems 11 (O11) generates a "Required Output Parameter" error when REST API method settings are incorrectly configured.
locale: en-us
guid: 7f2767bd-fc33-43f2-b074-0073230a18d6
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: rest api, error handling, api configuration, service studio, outsystems
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Required Output Parameter Error

The `Required Output Parameter` error is issued in the following situation:

* `(<method name>) method requires an output parameter with (<data type>) data type and Received In property set to 'Body'`

    You are trying to change the 'Response Format' of a REST API method, or the 'Data Type' or 'Received In' properties of an output parameter in a REST API method.

    Follow the instructions in the error message to solve it.

Double-click on the error line to take you directly to the REST API method's 'Response Format' property where the problem was detected.
