---
summary: How to send a specific HTTP Status Code in the response of an exposed REST API method.
tags: 
locale: en-us
guid: c0c56e61-281f-410c-8fb2-a07561bbca46
---

# Change the HTTP Status Code of a REST API

OutSystems uses [a set of built-in HTTP Status Codes](<../../../ref/extensibility-and-integration/rest-apis/exposed-rest-api/built-in-http-status-codes.md>) in the Responses of your exposed REST API Methods.

However, there are situations where you might want to send a different HTTP Status Code. For example, when a record is successfully created, it's common to use the "201 Created" Status Code.

To set a different HTTP Status Code in the Response, do the following:

1. Go to **Manage Dependencies...** and add the [SetStatusCode](<../../../ref/apis/auto/httprequesthandler-api.final.md#SetStatusCode>) action of the [HTTPRequestHandler](<../../../ref/apis/auto/httprequesthandler-api.final.md>) extension. 
1. Use the [SetStatusCode](<../../../ref/apis/auto/httprequesthandler-api.final.md#SetStatusCode>) action in your REST API Method or callback flow right before the end node. 
1. Set its "StatusCode" property to the desired status code. 

![](images/ss-rest-change-http-code.png)
