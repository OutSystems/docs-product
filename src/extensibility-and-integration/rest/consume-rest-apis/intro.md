---
summary: Consume REST APIs in your OutSystems applications.
tags: support-application_development; support-Integrations_Extensions; support-Integrations_Extensions-overview
locale: en-us
guid: 5a949da9-dd60-4ea9-a05b-70c27bc53655
app_type: traditional web apps, mobile apps, reactive web apps
---

# Consume REST APIs

When you need to retrieve or manipulate information from another system, and that system provides REST APIs for that effect, you can consume a REST API in your application.  
Start by looking into the documentation of the REST API you want to use and understand how it works. You will need to gather the following information:

* Base URL
* Security/Authentication requirements
* Methods definition (HTTP Method, URL Path, response format)

Check how you can [Consume one or more REST API Methods](consume-a-rest-api.md) in Service Studio.

<div class="info" markdown="1">

If you want to **expose** an OutSystems REST API, check [Expose REST APIs](../expose-rest-apis/intro.md).

</div>

## REST API Authentication

Each consumed REST API will have their own model of security and authentication process, which may imply the creation of an account, the registration for an API key or the usage of tokens. To consume a REST API in OutSystems you must understand and follow the provider's security model.

REST APIs using **Basic Authentication** are supported out of the box in the "Consume REST API Method" dialog box described below. You can use the REST customization capabilities to add support for other authentication methods:

* For **token-based authentication**, use the "OnBeforeRequest" callback to add the required HTTP authorization header to the outgoing requests. Check [Simple Customizations](simple-customizations.md) for more information.

* For **client certificate authentication**, use the "OnBeforeRequestAdvanced" callback, together with .NET code in an extension, to customize the outgoing requests. Check the [HTTPS Consumer](https://www.outsystems.com/forge/component-overview/3591/https-consumer) component provided by the OutSystems Community for a possible implementation.  
    Additionally, check the [Advanced Customizations](advanced-customizations.md) topic for more information on how you can implement advanced use cases. 

* For **other authentication methods**, check the [Advanced Customizations](advanced-customizations.md) topic on how you can use the [REST Extensibility API](../../../ref/apis/rest-extensibility-api.md) to implement advanced REST use cases.
