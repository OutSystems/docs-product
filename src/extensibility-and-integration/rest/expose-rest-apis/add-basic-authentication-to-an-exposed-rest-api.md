---
summary: Add basic authentication to the requests made to the REST APIs you are exposing.
tags: 
---

# Add Basic Authentication to an Exposed REST API

OutSystems allows you to add basic authentication to the requests made to the REST APIs you are exposing.

For that, do the following:

1. In the **Logic** tab, open the **Integrations** folder. 

1. Select the exposed REST API you want to change and set its "Authentication" property to `Basic`. 

![](images/ss-rest-authentication-options.png)

As a result, OutSystems creates the "OnAuthentication" action in your REST API to handle basic authentication with:

* "Username" and "Password" input parameters holding the credentials passed in the request
* The "User_Login" action to validate the credentials and identify the user

![](images/ss-rest-onauthentication-basic-flow.png)

All methods in the REST API will now require Basic Authentication. User credentials are managed in your end user management application (by default, the [Users application](../../../develop/security/end-user-manage/accessing-users.md)).
