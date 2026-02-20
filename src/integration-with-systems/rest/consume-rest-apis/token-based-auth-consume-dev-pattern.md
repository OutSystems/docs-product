---
summary: Learn a development pattern for consuming REST APIs that use JWT-based token authentication in OutSystems 11 (O11).
tags: jwt,token-based authentication,access token,rest api,api authentication
locale: en-us
guid: e475d7de-23dc-40ff-9308-0c64c3ae6c87
app_type: traditional web apps,mobile apps,reactive web apps
platform-version: o11
audience:
  - backend developers
  - full stack developers
  - mobile developers
outsystems-tools:
  - service studio
coverage-type:
  - understand
  - apply
topic:
  - webservice-authentication
  - rest-webservice-data
helpids: 
figma: https://www.figma.com/design/jSgZ0l0unYdVymLxKZasno/Integration-with-external-systems?node-id=4115-265
---

# Token-based authentication for consumed REST APIs

Many REST APIs use **[JSON Web Tokens (JWT)](https://en.wikipedia.org/wiki/JSON_Web_Token)** to authenticate and authorize requests. You can consume these APIs in OutSystems 11 (O11) by implementing the logic to obtain, store, and attach tokens to each request.

This article describes a **technology-agnostic development pattern** for consuming REST APIs that use token-based authentication with JWTs. The pattern isn't tied to a specific module or component.

<div class="info" markdown="1">

For interoperability between O11 and ODC, see also the [development pattern for securing exposed REST APIs in ODC with JWT-based tokens](https://www.outsystems.com/tk/redirect?g=941955cc-75d6-46d7-ba71-5fe9f89da4de). If you prefer to start from a prebuilt accelerator instead of implementing the pattern from scratch, consider using the [**ODC Service Account Manager – Secure Token Auth for O11**](https://www.outsystems.com/forge/component-overview/23311/odc-service-account-manager-odc) (ODC, server-side) Forge component.

This Forge component is a community-provided accelerator and **isn't officially supported by OutSystems**. Review the source code, perform a security assessment, and validate that it meets your organization's requirements before using it in production.

O11 provides built-in support for [OAuth 2.0 client flow authorization](./rest-oauth2-authorization.md) and handles the client ID and client secret.

</div>

## When to use this pattern

Use the pattern for consuming REST APIs that use token-based authentication with JWTs when:

* You consume REST APIs that:
    * Require an `Authorization: Bearer <token>` header, where the token is a JWT.
    * Follow OAuth 2.0 or a similar token-based authorization flow.
    * Implement custom token endpoints that issue JWTs after validating credentials.
* You need to:
    * Centralize token acquisition and reuse across multiple REST APIs.
    * Control how and when tokens are refreshed.
    * Ensure tokens are handled securely and not scattered across your app logic.

## Token flows for different scenarios

When you integrate with a token-based API, the API provider typically uses one of the following flows:

| Scenario | Recommended flow | What it validates |
| :--- | :--- | :--- |
| **Only applications** call the API (machine-to-machine) | **Service account** | App identity |
| **Users** call the API through an application | **Credentials + service account** | User identity + app identity |
| **Users** call the API directly | **Credentials only** | User identity only |

Your O11 app must follow the flow required by the API provider. The rest of this article applies to all three flows.

This pattern applies both when you consume:

* REST APIs exposed from other internal systems that follow the matching token-based authentication pattern.
* Third-party APIs that use JWT-based authorization.

<div class="info" markdown="1">

OutSystems (Platform Server 11.23.1 and later) includes built-in OAuth 2.0 client credentials flow support. For more details, refer to [Use OAuth 2.0 client flow authorization in consumed REST API web services](rest-oauth2-authorization.md).

</div>

### Service account token flow

The service account token flow is the following. In this scenario, your O11 app is the client that obtains the token and calls the external REST API.

![Diagram showing a service account token flow where an application obtains a token and calls the exposed REST API.](images/token-app-diag.png "Service Account Token Flow for Exposed REST APIs")

1. **Request token**: The user requests a token for the app from the auth service backoffice.
1. **Create token**: The auth service backoffice creates an app token.
1. **Configure app**: The user configures the token in the client application's service account settings. This ensures the app can authenticate itself.
1. **Request data**: The user interacts with the app to request data (for example, selecting a "View Report" button).
1. **Call API**: The app retrieves the service account token and sends it in the `Authorization` header to the REST API.
1. **Validate request**: The REST API sends the `Authorization` header to the auth service for validation.
1. **Verify token**: The auth service validates the token.
1. **Return validation**: The auth service returns the validation result to the REST API.
1. **Process request**: The REST API verifies the token signature to detect tampering. It uses a JWK the issuer provides or retrieves the public JWK from the issuer’s JWKS endpoint. Then the REST API processes the request.
1. **Return response**: The REST API sends the response to the app.
1. **Show data**: The app returns the response to the user.

### Credential-based token flow

In a credential-based flow, your app (as the client application) authenticates on behalf of the user and calls the external REST API with the token:

![Diagram showing a credential-based token flow between the client, token issuer, and exposed REST API.](images/token-credentials-diag.png "Credential-based Token Flow for Exposed REST APIs")

1. **Request login**: The app users log in with username and password.
1. **Create token**: The auth provider validates and creates an access token.
1. **Return token**: The auth provider returns the access token to the app.
1. **Store token**: The app saves the token to use on next calls.
1. **Call API**: The app retrieves the access token and sends it in the `Authorization` header to the REST API.

    ```http
    Authorization: Bearer <access_token>
    ```

1. **Validate request**: The REST API sends the `Authorization` header to the auth provider for validation.
1. **Validate token**: The auth provider validates the access token.
1. **Return validation**: The auth provider returns the token validation to the server API.
1. **Process request**: The REST API verifies the token signature to detect tampering. It uses a JWK the issuer provides or retrieves the public JWK from the issuer’s JWKS endpoint. Then the REST API processes the request.
1. **Return response**: The server API returns the response to the app.

Different projects can implement the authentication side in different ways (externally with access tokens, or internally with JWT or custom tokens).

## Applying this pattern in your O11 app

To apply this pattern in your O11 app, follow these steps:

1. [Design the token manager module](#design-the-token-manager-module)
1. [Attach tokens in OnBeforeRequest and handle failures](#attach-tokens-in-onbeforerequest-and-handle-failures)

### Design the token manager module {#design-the-token-manager-module}

* **Encapsulate token logic in a module**
    * Create a dedicated module that exposes server actions to:
        * Request a new token from the external token endpoint.
        * Store and retrieve the token and its metadata (for example, expiration time).
        * Decide whether to reuse or refresh the token.
    * Use this module from all apps and REST integrations that need the same token.
* **Choose a storage strategy**
    * Treat access tokens as secrets.
    * Prefer storing tokens:
        * On the server side, in an entity in an **encrypted** format or in a [secret site property](../../../ref/lang/auto/class-site-property.md#example-2). Decrypt them only inside the token manager when they're needed for outgoing API calls.
    * Avoid long-lived tokens and avoid storing them in locations that are directly accessible from untrusted clients.
* **Align with the authorization flow**
    * If the API uses OAuth 2.0 client credentials flow, start with [Use OAuth 2.0 client flow authorization in consumed REST API web services](rest-oauth2-authorization.md).
    * If the API uses a custom JWT flow, design an equivalent server action that:
        * Calls the token endpoint with the required credentials.
        * Parses the response and extracts the JWT access token and expiration details.

The goal is to have a single place that knows **how to get a token**, **how long it is valid**, and **how to store it securely**.

### Attach tokens in OnBeforeRequest and handle failures {#attach-tokens-in-onbeforerequest-and-handle-failures}

After your app obtains a token from the external provider, you must attach it to every REST API call that requires authentication. In O11, attach the token in the **OnBeforeRequest** callback of the consumed REST API:

1. **Configure the OnBeforeRequest callback**
    * In Service Studio, open the consumed REST API.
    * Set the **OnBeforeRequest** property to a server action that runs before each request.
1. **Retrieve the token**
    * In the OnBeforeRequest action, call your token manager to get the current token.
    * If the token manager returns an expired token or an error, handle it (for example, raise an exception or attempt a refresh).
1. **Add the Authorization header**
    * Add the `Authorization` header to the request.
    * Format the header value as:

        ```
        Bearer <access_token>
        ```

    * Ensure there is a space between `Bearer` and the token value.
1. **Handle token refresh on failure**
    * If the API call returns HTTP 401 (Unauthorized) or 403 (Forbidden), consider:
        * Invalidating or marking the stored token as invalid.
        * Triggering a token refresh using your token manager.
        * Retrying the request once with the new token, when it makes sense for the operation you're performing.
    * Use exception handlers around your REST calls, as described in [Handling REST Errors](handling-rest-errors.md), to capture token-related errors and inspect the details (for example, error messages or response bodies).
    * Avoid infinite retries. If a refreshed token still fails, treat it as a configuration or credential issue that needs investigation.
    * In more advanced scenarios, use the **OnAfterResponse** callback to inspect error responses at a lower level before OutSystems raises an exception.

This pattern keeps token handling close to the REST integration. The consumed REST API attaches tokens in **OnBeforeRequest**, while the token manager controls how tokens are acquired, stored, and reused.

For a detailed example of adding a header to a request, refer to [Example use case: Adding a header for token-based authentication](simple-customizations.md#example-use-case-adding-a-header-for-token-based-authentication).

## Security best practices for consumers

When you design token-based consumption patterns in O11, apply the following security guidance:

* **Protect tokens in storage and in logs**
    * Encrypt tokens at rest when you store them in entities or configuration records.
    * Never write full tokens to logs or error messages.
    * For more information about redacting sensitive data, refer to [Redact sensitive info from logs](redact-info-from-logs.md).
* **Limit privileges**
    * Request and use only the scopes or roles the app needs to call the API.
    * Align scopes, roles, and API method permissions with your overall security model.
* **Integrate with broader access controls**
    * Combine token-based API authentication with other controls, such as:
        * MFA and adaptive authentication in the identity provider.
        * Role-based access control in your O11 app.
    * Use token claims (for example, scopes, roles, organization) as inputs to your app-level authorization logic where appropriate.

By following these practices, you minimize the risk associated with token leakage, replay, and misuse.

## Related resources

* [Consume REST APIs](intro.md)
* [Token-based authentication for exposed REST APIs in ODC](https://www.outsystems.com/tk/redirect?g=941955cc-75d6-46d7-ba71-5fe9f89da4de)
