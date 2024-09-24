---
summary: Exposing REST APIs in your OutSystems applications.
tags: support-application_development; support-Integrations_Extensions
locale: en-us
guid: 08e6c830-5f88-4645-b86f-412e1c399a1f
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/jSgZ0l0unYdVymLxKZasno/Extensibility%20and%20Integration?node-id=410:100
---

# Expose REST APIs

OutSystems allows you to [expose methods using a REST API](<expose-a-rest-api.md>). These methods can be organized under multiple REST APIs.

<div class="info" markdown="1">

If you want to **consume** a REST API, check [Consume REST APIs](../consume-rest-apis/intro.md).

</div>


## REST API Method Flow

When a request to your REST API Method is received, OutSystems executes the following flow:

![Diagram illustrating the flow of execution when a REST API Method is called in OutSystems, including security validations, request preprocessing, authentication, parameter deserialization and validation, method execution, parameter serialization, and response customization.](images/rest-expose-method-flow-diag.png "REST API Method Execution Flow Diagram")

1. **Security Validations:** After receiving the REST API Method request, OutSystems executes the security validations according to the settings in [REST API properties](../../../ref/lang/auto/servicestudio-plugin-restservice-restservice.md) **HTTP Security** and **Internal Access Only**. 
1. **OnRequest():** OnRequest callback allows you to [run logic over the requests](<preprocess-rest-api-requests.md>) after receiving them. 
1. **OnAuthentication():** OnAuthentication callback allows you to add [basic authentication](<add-basic-authentication-to-an-exposed-rest-api.md>) or [custom authentication](<add-custom-authentication-to-an-exposed-rest-api.md>) to requests. 
1. **Parameters Deserialization and Validation:** Deserialization of the input parameters and validation of the data types, mandatory values, etc. 
1. **Execute Method:** Executes the action that implements the REST API Method. 
1. **Parameters Serialization:** Serialization of the output parameters to return in the response. 
1. **OnResponse():** OnResponse callback allows you to [run logic over the responses](<customize-rest-api-responses.md>) before sending them. It is always executed, even in an error situation. 
