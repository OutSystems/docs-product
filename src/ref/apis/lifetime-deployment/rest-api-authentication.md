---
summary: Using OutSystems service account tokens to authenticate REST API method calls.
tags: support-application_development; support-Integrations_Extensions
locale: en-us
guid: 1f0c3b37-45b9-4a4d-b640-016dac5f5d6b
app_type: traditional web apps, mobile apps, reactive web apps
---

# REST API Authentication

To invoke the REST methods of [LifeTime API](<../auto/lifetime-deployment-api-v2.final.md>) you will need a special type of account, called a **service account**.

A service account is a special account created in LifeTime used in machine-to-machine interactions with OutSystems. Service accounts follow the same permission model of regular user accounts, using roles and teams to define access privileges.

After creating a service account, LifeTime provides you with an **authentication token** string that you need to include in all REST API requests. Each authentication token contains all the required information to authenticate a specific service account. 

From LifeTime 11.16.0 and Platform Server 11.18.0 onwards, service accounts can also be used in [Performance Monitoring API](<../performancemonitoring-api.md>).

## Security Considerations

All REST API method calls are audited and can be traced back to the service account through the authorization token in the request. The logs can be viewed in LifeTime in the activity log of the service account.

Take the following security considerations into account when using OutSystems REST APIs:

* Authentication tokens are not stored in the platform, and consumers must store the authentication tokens securely. If a third-party gets access to an authentication token, it will have access to your infrastructure.
* All communication between API consumers and the API server must be done over HTTPS.
* Service Account tokens are valid for a duration of 6, 12, or 24 months, after which they become invalid.

The following sections show how to manage service accounts and tokens and how to authenticate REST API calls.

## Creating a service account

To create a service account in LifeTime, do the following:

1. In the LifeTime management console of your infrastructure, open the **User Management** tab and select the **Service Accounts** sub-menu. 

    ![](images/lt_service_accounts.png)

1. Select **New Service Account**. 

1. Enter the service account username and description, select the desired role, select the duration for the token, and click the **Create** button. 

    After creating the service account, you are provided with the authentication token that you must include in each REST API method call to authenticate the request.

    ![](images/lt_auth_token_blurred.png)
    
    **Note**: As a security measure, the authentication token is only shown once.If you lose the token, you must generate a new one, and the previous token is no           longer valid.

## Authenticating REST API calls

To authenticate each REST API method call you will need to provide the authentication token of an active service account. The token should be included as an additional HTTP header of the REST API request, according to the following format:

    Authorization: Bearer <authentication_token>


## Revoking an authentication token

If you need to revoke or deprecate a given authentication token, you should generate a new token for the corresponding service account as follows:

1. Navigate to **User Management** tab, and select the **Service Accounts** sub-menu. 

1. Click the link corresponding to the service account whose token you want to revoke/deprecate. 

1. Click the **Generate new Authentication Token** link. 

    ![](images/lt_gen_new_auth_token.png)

1. Click **Continue** to confirm that you want to generate a new token, and that you’re fully aware that the previous token will be revoked/deprecated and will no longer work. 

A new token is generated and displayed for the current service account. Take note of the generated token as it will not be shown again.
