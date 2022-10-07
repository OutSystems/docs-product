---
tags: 
locale: en-us
guid: 223d6f3f-6f3f-4204-a5f0-f135ca1a76a4
app_type: traditional web apps, mobile apps, reactive web apps
---

# Supported Media Types in REST API Requests

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
