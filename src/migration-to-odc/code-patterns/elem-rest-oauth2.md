---
summary: Understand how to implement OAuth 2.0 authentication for REST APIs on OutSystems Developer Cloud (ODC) compared to OutSystems 11 (O11) and solve code migration issues.
locale: en-us
guid: 79fb29aa-b210-4042-bd0f-83efb26f893c
app_type: mobile apps, reactive web apps
platform-version: o11
figma:
helpids: 30631
tags: oauth 2.0 authentication, rest api, outsystems migration, custom authentication flow, odc migration
audience:
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
  - understand
---

# Asset contains REST APIs using built-in OAuth 2.0 authentication flow

Currently, the way you enable OAuth 2.0 authentication while consuming REST is different in ODC and O11:

* In O11, you can choose between [using the built-in OAuth 2.0 authentication flow](../../integration-with-systems/rest/consume-rest-apis/rest-oauth2-authorization.md), or implement your own authentication flow logic.

* In ODC, for now, you must implement your own authentication flow logic.

## How to solve

You must solve this pattern in ODC, after proceeding with the code migration to ODC.

### Solve in ODC

After migrating your application to ODC, you need to manually implement the OAuth 2.0 flow to authenticate requests to the consumed REST API. This typically involves the following steps within your migrated app:

1. **Build the token request logic:** Create logic to handle the interaction with the API provider's token endpoint. For common flows, such as Client Credentials, this usually involves sending a POST request with the client credentials to obtain the access token.
1. **Manage the tokens:** Implement logic to securely store the retrieved access token (and refresh token, if applicable) for reuse in subsequent API calls.
1. **Inject the Authorization header:** Implement the logic to add the `Authorization` header to outgoing requests using the **OnBeforeRequest** callback for the consumed REST API. Check this example on [how to add a header for token-based authentication](../../integration-with-systems/rest/consume-rest-apis/simple-customizations.md#example-use-case-adding-a-header-for-token-based-authentication).
1. **Handle token expiration:** Add logic to manage token expiration based on the provider's specifications, either by requesting a new token proactively or using a refresh token (if supported by the API) to obtain a new access token when needed.


