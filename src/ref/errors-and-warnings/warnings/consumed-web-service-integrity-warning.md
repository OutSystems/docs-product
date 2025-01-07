---
summary: Learn how to address consumed web service integrity warnings in OutSystems 11 (O11) when the WSDL changes or the URL becomes inaccessible.
locale: en-us
guid: f80b680e-8d63-4def-bbf0-c3fdf279d3a2
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: soap web services, wsdl, api integration, service error handling, web service refresh
audience:
  - full stack developers
  - backend developers
  - platform administrators
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Consumed Web Service Integrity Warning

Message
:   `Consumed SOAP web service <consumed web service> is outdated. The WSDL has changed since the consumed SOAP web service was created/refreshed`

Cause
:   The WSDL has changed since the consumed SOAP web service was created or refreshed.

Recommendation
:   You should refresh the consumed SOAP Web Service before compiling it again.

---
Message
:   `Unable to access url <url> to verify if the <consumed web service> consumed SOAP web service is up-to-date`

Cause
:   It is not possible to access the URL of your SOAP Web Service.

Recommendation
:   Check whether the URL is correct and the consumed SOAP Web Service is still available. If both conditions are valid and you still cannot refresh the Web Service definition, you should contact your Systems Administrator.    
