---
summary: Explore OAuth 2.0 client flow authorization for REST API web services in OutSystems 11 (O11).
tags: oauth 2.0, rest api, security, authorization, api integration
locale: en-us
guid: beb761a2-ef08-44e6-aa0c-ee11bada5baa
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/jSgZ0l0unYdVymLxKZasno/Extensibility-and-Integration?type=design&node-id=410%3A79&mode=design&t=187UAgmZTPxcY0ZG-1
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
  - platform server
coverage-type:
  - apply
---

# Use OAuth 2.0 client flow authorization in consumed REST API web services

OAuth 2.0 (Open Authorization, OAuth) is a standard that lets web apps access resources in other web apps. As an authorization protocol, the purpose of OAuth is to grant access to resources, such as APIs or data. The OAuth standard uses access tokens with an expiration date.

<div class="info" markdown="1">

OAuth 2.0 is available in Platform Server 11.23.1 and later.

</div>

## Authentication of the client

Regardless of whether you are consuming single or multiple methods, OutSystems lets you use an additional property called **Client authentication**. The client authentication property determines how to send the client credentials to the authorization server. The choice of how to send the client credentials depends on the authorization server specifications.

You have two options:

* **Send as a Basic Auth header**. OutSystems encodes **Client ID** and **Client secret** to obtain a token and sends it as an authorization header to the authorization server. The token is a single Base64 encoded string, after the concatenation: `<Client ID>:<Client secret>`.
* **Send client credentials in body**. OutSystems sends the client credentials in the request body using the following parameters: `client_id` (refers to the **Client ID** property) and `client_secret` (refers to the **Client secret** property).

    ![Screenshot showing client authentication properties for OAuth 2.0 client credential flow in Service Studio](images/oauth-auth-properties-client-ss.png "Client Authentication Properties for OAuth 2.0 Client Credential Flow")

## Consuming several methods

When consuming several REST API methods described in an OpenAPI specification file that require an OAuth client credentials flow authentication, OutSystems automatically sets the values of the following properties:

* **Type** to **OAuth 2.0: client credentials**
* **Access token URL**, based on the OpenAPI specification file
* **Scopes**, based on the OpenAPI specification file

If the OpenAPI specification file doesn't define the requirement for OAuth, you can always set these properties manually after consuming the REST API.

![Screenshot of OAuth 2.0 authentication properties in Service Studio](images/oauth-auth-properties-ss.png "OAuth 2.0 Authentication Properties")

## Consuming a single method

When consuming a single method, under the **Headers and Authentication** tab of the **Consume Single API**:

* Set the **Authentication type** to **OAuth 2.0: client credentials**
* Provide the credentials to authenticate the app, **Client ID** and **Client secret**
* Set the **Access token URL** and **Scopes** properties

## Testing

When testing a REST API method using OAuth client credentials flow authentication, you can inspect the test result of:

* API request and response
* Authorization server request and response

You can test the REST API with OAuth client credentials flow authentication by:

* Consuming a single method
* Editing a method under the **Test** tab

    ![Screenshot of testing a REST API method with OAuth 2.0 client flow authentication in Service Studio](images/oauth-method-test-ss.png "Testing REST API with OAuth 2.0 Client Flow")

If you manually add the authorization header in the model or the OnBeforeRequest callback, you override the header if authentication is either **Basic authentication** or **OAuth 2.0: client credentials**.

## Example for consuming a REST API with OAuth 2.0 client credentials

OutSystems Developers can use REST APIs with OAuth 2.0 for the client credentials flow without using high-code or unsupported Forge assets.

The following example explains how a single REST API can be consumed with OAuth 2.0 credentials.

1. From the **Logic** tab, open the **Integrations** folder. Then right-click on the **REST** element and select **Consume REST API**.

1. In the **Consume REST API** dialog, select **Add Single Method** and then select **Continue**.

1. In the **Consume Single API** dialog, enter the URL information in the **Method URL** field.

    ![Screenshot showing the process of filling in the Method URL for a single method REST API with OAuth 2.0 in Service Studio](images/oauth-add-method-url-ss.png "Adding Method URL for REST API with OAuth 2.0")

1. To set the OAuth 2.0 authentication for the REST API you are consuming, open the **Headers and Authentication** tab and then from the **Authentication** list, select **OAuth 2.0: client credentials**.

    * To authenticate the app, enter the client credentials in the **Client ID** and **Client secret** fields.

    * In the **Access token URL** and **Scopes** fields, respectively, enter the URL and permission scopes based on the OpenAPI specification file.

    * To obtain a token and send it as an authorization header to the authorization server, from the **Client authentication** list, select **Send as a Basic Auth header**.

        ![Screenshot of adding OAuth 2.0 client credentials details in Service Studio](images/oauth-fill-authentication-details-ss.png "Adding OAuth 2.0 Client Credentials")

1. Open the **Test** tab and select **Test**. If the test is successful, you see the method's response in the Response area of **Test** tab. Then select **Finish**.

    ![Screenshot of testing the REST API with OAuth 2.0 client credentials in Service Studio](images/oauth-test-api-ss.png "Testing REST API with OAuth 2.0 Client Credentials")

The following shows how the OAuth2.0 client credentials display in the logic tab.

![Screenshot showing OAuth 2.0 client credentials details in the logic tab of Service Studio](images/oauth-details-in-logic-tab-ss.png "OAuth 2.0 Client Credentials in Logic Tab")
