---
summary: Learn how to add basic authentication to a consumed REST API in OutSystems 11 (O11) and how to set credentials for each environment.
tags:
  - Authentication
  - REST
  - Security
locale: en-us
guid: 491a1148-764d-4064-b2c6-aa4197c72e07
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - service studio
  - service center
coverage-type:
  - apply
topic:
  - configure-rest-basic-auth
isautopublish: true
---

# Add basic authentication to a consumed REST API

Basic authentication is a scheme built into the HTTP protocol. The client sends an `Authorization` header with the word `Basic`, a space, and a `username:password` string encoded in Base64.

For example, to authorize the user `demo` with the password `p@55w0rd`, the client sends:

```http
Authorization: Basic ZGVtbzpwQDU1dzByZA==
```

The `ZGVtbzpwQDU1dzByZA==` string is the Base64 encoding of `demo:p@55w0rd`.

<div class="warning" markdown="1">

Base64 encoding doesn't encrypt the credentials. Use basic authentication only together with other security mechanisms, such as **HTTPS/SSL**.

</div>

## Set basic authentication in Service Studio

To set basic authentication for a consumed REST API method, follow these steps:

1. In the **Logic** tab, open the **Integrations** folder.

1. Right-click the **REST** element, and select **Consume REST API**.

1. In the **Consume REST API** dialog, select **Add Single Method**.

1. Open the **Headers and Authentication** tab.

1. Enter a **Method URL**.

1. From the **Authentication** list, select **Basic authentication**.

1. Enter the **Username** and **Password** the REST API expects for the API.

1. Click **Finish**.

The authentication setting applies to all methods in the REST API, so you don't need to set it for each method.

## Set credentials for each environment

The credentials you set in Service Studio are the default values. You can override them for each environment in Service Center, without changing or republishing the module.

For more information about setting the credentials for each environment in Service Center, refer to [Configure a consumed REST API at runtime](configure-a-consumed-rest-api-at-runtime.md).

## Replace the authorization header manually

If you add an `Authorization` header manually, in the model or in the **OnBeforeRequest** callback, that header overrides the basic authentication setting.

## Related resources

For more information about the tasks and concepts covered on this page, refer to the following topics.

* [Consume one or more REST API methods](consume-a-rest-api.md)

* [Configure a consumed REST API at runtime](configure-a-consumed-rest-api-at-runtime.md)

* [Use OAuth 2.0 client flow authorization in consumed REST API web services](rest-oauth2-authorization.md)

* [Redact information from logs](redact-info-from-logs.md)
