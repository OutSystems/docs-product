---
summary: Explore supported media types in REST API requests with OutSystems 11 (O11), detailing rules based on input parameter data types.
tags: rest api, content-type header, media types, error handling, http status codes
locale: en-us
guid: 223d6f3f-6f3f-4204-a5f0-f135ca1a76a4
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Supported media types in REST API requests

OutSystems supports many media types in the Content-Type header of REST API requests. However, depending on the input parameter's data type, the following rules apply:

Input Parameter Data Type | Accepted Request Media Type  
---|---  
Record, List | application/json  
[Basic Data Types](<../../../data/data-types/available-data-types.md#basic-data-types>) |  text/&lt;any_subtype&gt; <br/>application/json <br/>application/x-www-form-urlencoded  
Binary | any  
  
If you send a request with a Content-Type header that the method doesn't support, you receive a response with status code 415. Additionally, you get the following error message in the response body:

```javascript   
{
    "Errors": [
        "The request entity's media type 'text/plain' is not supported for this resource."
    ],
    "StatusCode": 415
}
```
## Default encoding when exposing REST APIs

When exposing REST APIs, the default character decoding behavior depends on the content type:
* Text-based content (text/plain, text/html): Decoded using ISO-8859-1 by default, unless charset=utf-8 is specified in the request header.
* JSON (application/json): Always decoded using UTF-8, regardless of charset specification.
* Query and Path Parameters: Always decoded using UTF-8 URL-encoding rules.

All responses from OutSystems REST services are UTF-8 encoded, regardless of input encoding.
