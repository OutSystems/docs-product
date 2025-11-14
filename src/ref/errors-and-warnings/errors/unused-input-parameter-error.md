---
summary: Learn how to resolve the 'Unused Input Parameter' error in OutSystems 11 (O11) when a REST API method's input parameter is not utilized in the URL path.
locale: en-us
guid: d8e4aae9-26ab-4de7-af48-5bd5e2fd9962
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: rest api, api development, error handling, debugging, service studio
audience:
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Unused Input Parameter Error

The `Unused Input Parameter` error is issued in the following situation:

* `(<parameter name>) is not used by (<method name>) REST API method. Either use it in the (<method name>) URL path, change the (<parameter name>) Send In property, or delete it`

    You have an input parameter in a REST API method's list, but it's not part of the URL.

    Follow the instructions in the error message to solve it.

Double-click on the error line to take you directly to the REST API method's input parameter where the problem was detected.
