---
summary: A JavaScript API that provides methods to get information about the current request and session.
tags: runtime-traditionalweb; support-application_development; support-webapps
locale: en-us
guid: fd316f0d-9003-4b26-a137-96c4b65afd08
---

# outsystems.api.requestInfo API

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

A JavaScript API that provides methods to get information about the current request and session.

The outsystems.api.requestInfo global object is defined for all OutSystems applications.

## Methods

All of the following methods return a String.

Method | Description  
---|---  
getApplicationKey() | Returns the identifier of the current application. The key is unique to the application, and it is consistent across different environments.  
getApplicationName() | Returns the name of the current application.  
getEnvironmentKey() | Returns the identifier of the current environment.  
getEnvironmentName() | Returns the name of the current environment.  
getEspaceKey() | Returns the identifier of the current module. It is unique to the module, and it is consistent across different environments.  
getEspaceName() | Returns the name of the current module.  
getFrontendKey() | Returns the identifier of the front-end server where the current request was processed.  
getRequestKey() | Returns a GUID that uniquely identifies the current request.  
getSessionKey() | Returns the unique identifier of the session associated with the current request.  
getTenantKey() | Returns the identifier of the tenant associated with the current request.  
getTenantName() | Returns the name of the tenant associated with the current request.  
getUserKey() | If the visitor is logged in during the current request, returns the user identifier associated with the user. <br/>Otherwise it returns an empty string.  
getVisitorKey() | Returns the unique identifier of the visitor associated with the current request. <br/>A visitor is a combination of a device and a browser. <br/>The key is created at the first time the visitor accesses the website's domain using a given device and browser. <br/>The same key is used until the browser cookies are cleared.  
getVisitKey() | Returns the unique identifier of the visit associated with the current request. <br/>A visit is defined as a series of page requests from the same visitor. A visit is considered ended when no requests have been recorded for 30 minutes.  
getWebScreenKey() | Returns a unique identifier key for the current web screen. The key is unique to the web screen inside the module, and it is consistent across different environments.  
getWebScreenName() | Returns the name of the current web screen.  
  
## Example

Here is an example of how to use the above methods in a JavaScript on your screen:

```javascript    
// Use the outsystems.api.requestInfo to get information about
// the current screen.
var info = {
    'ApplicationName': outsystems.api.requestInfo.getApplicationName(),
    'ModuleName': outsystems.api.requestInfo.getEspaceName(),
    'ScreenName': outsystems.api.requestInfo.getWebScreenName(),
};
console.log(info);

// This example returns
// Object {ApplicationName: "Phone Book", ModuleName: "PhoneBook", ScreenName: "Login"}
```
