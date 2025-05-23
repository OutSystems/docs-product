---
summary: OutSystems 11 (O11) issues an "Invalid Response Format" error when a REST API method has an incorrect or unset 'Response Format' property.
locale: en-us
guid: b12fc7de-5897-4cf7-9e05-7b53cda233c0
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: rest api, error handling, api development, service studio, outsystems
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Invalid Response Format Error

The `Invalid Response Format` error is issued in the following situation:

* `(<method name>) method has an invalid Response Format property. Either change it, or remove the output parameters from the method`
  
    You have an invalid value in the 'Response Format' property of a REST API method, or you don't have any value set at all.

Double-click on the error line to take you directly to the REST API method's 'Response Format' property where the problem was detected.
