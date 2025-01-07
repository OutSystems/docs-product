---
summary: OutSystems 11 (O11) triggers an "Invalid Receive In" error for incorrect output parameter settings in REST APIs.
locale: en-us
guid: 90a4dbc8-4410-4801-87ad-9a93ad6609b0
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: rest api, error handling, parameter configuration, rest integration, api development
audience:
  - frontend developers
  - full stack developers
  - backend developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Invalid Receive In Error

The `Invalid Receive In` error is issued in the following situation:

* `Output parameters with (<data type>) data type can only be received in the request body`
  
    In a REST API method, you are trying to change the 'Receive In' property or the 'Data Type' property of an output parameter.

    Change the 'Receive In' property of the parameter as indicated in the error message. 
    
Double-click on the error line to take you directly to the element where this situation was detected.
