---
tags: 
locale: en-us
guid: 9ad139dd-e6af-4245-8dba-9185b2317192
app_type: traditional web apps, mobile apps, reactive web apps
---

# Built-in HTTP Status Codes

OutSystems uses the following HTTP status codes when working with exposed REST API methods:

Status Code | Reason Phrase | Description  
---|---|---  
200 | OK | Success.  
400 | Bad Request | Problem with the request. See the response body for more information.  
401 | Unauthorized | Missing Authorization header when the method uses Basic authentication.  
403 | Forbidden | The service requires SSL or allows access only according to the [Internal Network environment setting](<../../../../develop/security/restrict-access-to-an-internal-network.md>).  
404 | Not Found | The specified REST API or method doesn't exist.  
405 | Method Not Allowed | The REST API Method is not allowed to be used with the specified HTTP method (e.g. you are calling the REST API method with a PUT request instead of POST).  
406 | Not Acceptable | The 'Accept' header of the request requires a response media type that is not supported.  
415 | Unsupported Media Type | The method expects a different 'Content-Type' header value in the request.  
500 | Internal Server Error | Any unhandled exception that appears in the application logic. See the response body for more information.  
  
You can use the [SetStatusCode](<../../../apis/auto/httprequesthandler-api.final.md#SetStatusCode>) action of the [HTTPRequestHandler](<../../../apis/auto/httprequesthandler-api.final.md>) extension to set a custom status code. Please note that this is an advanced extensibility scenario, so be sure to test if it works as intended in your specific infrastructure.
