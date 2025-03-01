---
summary: Explore common errors in OutSystems 11 (O11) when consuming SOAP Web Services, including invalid URLs and undefined elements.
locale: en-us
guid: 36e85bdb-7275-41cf-85eb-6a25b9b89e97
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: error handling, web services, soap protocol, troubleshooting, integration issues
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Invalid Consumed Web Service Error

The `Invalid Consumed Web Service` error is issued in the following situation:

* `URL of WSDL <> is invalid`
  
    The URL you provided to consume the SOAP Web Service is not valid.
    
    Please contact the Web Service provider to get the correct URL.

* `Children of <element> must contain a 'name' or 'ref' attribute in WSDL`
  
    The SOAP Web Service you are consuming is not well-defined according to the HTTP/SOAP protocol.
    
    Please contact the Web Service provider to identify what may be the problem.

* `Could not find nammodule for element <element> in WSDL`
  
    The SOAP Web Service you are consuming is not well-defined according with the HTTP/SOAP protocol.
    
    Please contact the Web Service provider to identify what may be the problem.

  * `No definition found for data type <type> in nammodule <> in WSDL`
  
    The SOAP Web Service you are consuming has a data type for which the definition is not included in the Web Service. 
    
    Please contact the Web Service provider in order to add the definition for this data type.

  * `(<consumed web service name>) must have at least one method`
  
    The SOAP Web Service you are consuming has no methods.
    
    Add at least one method or delete the web service.

These errors only appear when you first consume a SOAP Web Service.
