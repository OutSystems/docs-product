---
summary: Explore how to resolve the Incompatible Action Error in OutSystems 11 (O11) by using the SOAP Extensibility API for consumed SOAP Web Services.
helpids: 30202
locale: en-us
guid: 45f3d12c-cd89-4141-be22-c0005c1a6530
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: soap web services, error resolution, web service customization, api usage, outsystems platform
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Incompatible Action Error

The `Incompatible Action Error` error is issued in the following situation:

* `The '<action>' Server Action cannot be used with the '<soap_service_name>' consumed SOAP Web Service created in OutSystems 11. Use the SOAP Extensibility API instead.`
  
    The EnhancedWebReferences API was deprecated in OutSystems 11 and cannot be used to customize the behavior of consumed SOAP Web Services created in OutSystems 11.  
    OutSystems 11 includes a new implementation of consumed SOAP Web Services for all services that were not upgraded from earlier versions. This implementation is not compatible with the deprecated EnhancedWebReferences API.
    
    To extend and customize the behavior of consumed SOAP Web Services created in OutSystems 11 you must use the [SOAP Extensibility API](../../apis/soap-extensibility-api.md).
