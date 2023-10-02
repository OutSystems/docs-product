---
summary: Consume REST APIs in your OutSystems applications.
tags: support-application_development; support-Integrations_Extensions; support-Integrations_Extensions-overview
locale: en-us
guid: 5a949da9-dd60-4ea9-a05b-70c27bc53655
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Consume REST APIs

When you want to retrieve or manipulate data from another system that offers REST APIs, you can use those APIs in your app.  

Start by looking into the documentation of the REST API you want to use and understand how it works. You will need to gather the following information:

* Base URL
* Security/Authentication requirements
* Methods definition (HTTP Method, URL Path, response format)

Check how you can [Consume one or more REST API Methods](consume-a-rest-api.md) in Service Studio.

<div class="info" markdown="1">

If you want to **expose** an OutSystems REST API, check [Expose REST APIs](../expose-rest-apis/intro.md).

</div>

## REST API Authentication

Every REST API you consume has its own security and authentication process, which implies you must create an account, register for an API key, or use tokens. To consume a REST API in OutSystems you must understand and follow the provider's security model.

OutSystems has built-in support for REST APIs with:

* Basic authentication
* [OAuth 2.0 client credentials flow](rest-oauth2-authorization.md)

You can use the REST customization capabilities to add support for other authentication methods:

* For **token-based authentication** you can use [OAuth 2.0 client credentials flow](rest-oauth2-authorization.md). Another method is adding the authorization info to the header with [OnBeforeRequest callback in Simple Customizations](simple-customizations.md).

* For **client certificate authentication**, use the OnBeforeRequestAdvanced callback, together with .NET code in an extension, to customize the outgoing requests. For detailed information about a possible implementation, refer to [HTTPS Consumer](https://www.outsystems.com/forge/component-overview/3591/https-consumer) component provided by the OutSystems Community. For more information about implementing advanced use cases, refer to [Advanced Customizations](advanced-customizations.md).

* For **other authentication methods**, check the [Advanced Customizations](advanced-customizations.md) topic on how you can use the [REST Extensibility API](../../../ref/apis/rest-extensibility-api.md) to implement advanced REST use cases.
