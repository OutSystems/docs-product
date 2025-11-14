---
summary: OutSystems 11 (O11) allows customization of HTTP Status Codes in REST API responses by using the SetStatusCode action.
tags: rest apis, http status codes, api development, web development, outsystems platform
locale: en-us
guid: c0c56e61-281f-410c-8fb2-a07561bbca46
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/jSgZ0l0unYdVymLxKZasno/Extensibility%20and%20Integration?node-id=415:26
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
  - httprequesthandler
coverage-type:
  - apply
topic:
  - error-codes
---

# Change the HTTP Status Code of a REST API

OutSystems uses [a set of built-in HTTP Status Codes](<../../../ref/integration-with-systems/rest-apis/exposed-rest-api/built-in-http-status-codes.md>) in the Responses of your exposed REST API Methods.

However, there are situations where you might want to send a different HTTP Status Code. For example, when a record is successfully created, it's common to use the "201 Created" Status Code.

To set a different HTTP Status Code in the Response, do the following:

1. Go to **Manage Dependencies...** and add the [SetStatusCode](<../../../ref/apis/auto/httprequesthandler-api.final.md#SetStatusCode>) action of the [HTTPRequestHandler](<../../../ref/apis/auto/httprequesthandler-api.final.md>) extension.
1. Use the [SetStatusCode](<../../../ref/apis/auto/httprequesthandler-api.final.md#SetStatusCode>) action in your REST API Method or callback flow right before the end node.
1. Set its "StatusCode" property to the desired status code.

![Screenshot showing how to set a custom HTTP Status Code in OutSystems REST API method](images/ss-rest-change-http-code.png "Setting a Custom HTTP Status Code in OutSystems")
