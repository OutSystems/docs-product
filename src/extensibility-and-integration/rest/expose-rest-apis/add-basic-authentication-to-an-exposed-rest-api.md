---
summary: Add basic authentication to the requests made to the REST APIs you are exposing.
tags: 
locale: en-us
guid: fa99306b-0261-47c1-821f-80262d8dd45b
app_type: traditional web apps, mobile apps, reactive web apps
---

# Add Basic Authentication to an Exposed REST API

<div class="info" markdown="1">

We’ve been working on this article. Please let us know how useful this new version is by voting.

</div>

## Basic authentication

Basic authentication is a simple authentication scheme built into the HTTP protocol. The client sends HTTP requests with the "Authorization" header containing the word "Basic", a space character, and a "username:password" string encoded in Base64.

For example, to authorize the user "demo" with password "p@55w0rd" the client sends:

    Authorization: Basic ZGVtbzpwQDU1dzByZA==

In this example, the `ZGVtbzpwQDU1dzByZA==` string results from encoding the string `demo:p@55w0rd` in Base64.

<div class="warning" markdown="1">

**Note:** Because Base64 is easily decoded, you should only use basic authentication together with other security mechanisms such as **HTTPS/SSL**.

</div>

To learn more about HTTP authentication, check for example the MDN Web Docs on [HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication).

## Basic authentication in OutSystems REST APIs

OutSystems allows you to add basic authentication to the requests made to the REST APIs you are exposing.

For that, do the following:

1. In the **Logic** tab, open the **Integrations** folder.

1. Select the exposed REST API you want to change and set its "Authentication" property to `Basic`.

![](images/ss-rest-authentication-options.png)

As a result, OutSystems creates the "OnAuthentication" action in your REST API to handle basic authentication with:

* The "Username" and "Password" input parameters holding the credentials passed in the request (they're automatically decoded from the "Authorization" HTTP header)
* The "User_Login" action to validate the credentials and identify the user

![](images/ss-rest-onauthentication-basic-flow.png)

All methods in the REST API now require Basic Authentication. Manage user credentials in your end user management application (by default, the [Users application](../../../develop/security/end-user-manage/accessing-users.md)).

In the example above, OutSystems logs in the user and creates a session during the request. The GetUserId() function returns the user ID and you can call the CheckRole built-in functions, allowing you to create logic based on the user and the roles assigned to the user.
