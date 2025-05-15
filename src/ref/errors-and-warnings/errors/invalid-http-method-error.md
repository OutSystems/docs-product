---
summary: Learn how to resolve the 'Invalid HTTP Method' error in OutSystems 11 (O11) when using GET methods with body parameters.
locale: en-us
guid: 2bcfc8f0-9630-4a74-a218-fcd00359bdb2
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: http methods, rest api, error handling, outsystems development, service studio troubleshooting
audience:
  - frontend developers
  - full stack developers
  - mobile developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Invalid HTTP Method Error

The `Invalid HTTP Method` error is issued in the following situation:

* `Input parameters with Send In property set to 'Body' are not allowed for GET methods. Either change the (<method name>) method, or remove the input parameter`
  
    You are trying to change the place where the input parameter is sent, from URL to Body, and this is incompatible with the HTTP Method of the REST API Method, which is set to GET.

    Either change the (`<method name>`) method, or remove the input parameter.

Double-click on the error line to take you directly to the REST API method's property where the problem was detected.
