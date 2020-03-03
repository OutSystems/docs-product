---
summary: Add basic authentication to the requests made to the REST APIs you are exposing.
tags: 
---

# Add Basic Authentication to an Exposed REST API

## Basic Authentication

Basic authentication is a simple authentication scheme built into the HTTP protocol. The client sends HTTP requests with the **Authorization** header that contains the word **Basic** followed by a space and a base64-encoded string username:password. For example, to authorize user demo with password p@55w0rd the client would send:

>Authorization: Basic ZGVtbzpwQDU1dzByZA==

>**Note:** Because base64 is easily decoded, Basic authentication should only be used together with other security mechanisms such as **HTTPS/SSL**.

If you want to know more about HTTP authentication, the [MDN Web Docs on HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication) is a good place to start.

## OutSystems Basic Authentication on REST API

OutSystems allows you to add basic authentication to the requests made to the REST APIs you are exposing.

For that, do the following:

1. In the **Logic** tab, open the **Integrations** folder. 

1. Select the exposed REST API you want to change and set its "Authentication" property to `Basic`. 

![](images/ss-rest-authentication-options.png)

As a result, OutSystems creates the "OnAuthentication" action in your REST API to handle basic authentication with:

* "Username" and "Password" input parameters holding the credentials passed in the request. This is automatically decoded from the Authorization HTTP header.
* The "User_Login" action to validate the credentials and identify the user

![](images/ss-rest-onauthentication-basic-flow.png)

All methods in the REST API will now require Basic Authentication. User credentials are managed in your end user management application (by default, the [Users application](../../../develop/security/end-user-manage/accessing-users.md)).

On the above example, the user is logged in and a session is created for the durations of the request. The GetUserID() method will return the user id and the CheckRole methods will also work, allowing you to create logic based on the user and his roles.
