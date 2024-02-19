---
summary: Configure PingFederate as an external identity provider
tags:
locale: en-us
guid: 8c57419b-f92a-4e5d-bcbc-f2b89abb2a28
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Configuring PingFederate as an external identity provider

## Prerequisites

* A running instance of PingFederate server
* Existing users in the server's active directory's user store.
To configure PingFederate as an external IdP, follow these steps:

## 1. Configure an active directory as a user datastore

Establish an Active Directory datastore connection for retrieving user attributes for outbound connections.

**LDAP configuration details:**

* **Authentication method**: Simple
* **User DN**: Distinguished name of the active directory user used to authenticate the user store.
* **Password**: Active directory user password

For more information, refer to  [Configuring an Active Directory datastore](https://docs.pingidentity.com/r/en-us/solution-guides/htg_config_ad_datastore_pingfed).

## 2. Create a password credential validator instance

**Instance configuration details:**

* **Search Filter**: ``(|(sAMAccountName=${username})(userPrincipalName=${username}))``
* **Scope of Search**: Subtree

For more information, refer to [Creating an LDAP Username Password Credential Validator instance](https://docs.pingidentity.com/r/en-us/pingfederate-112/pf_creat_ldap_username_pass_credent_validat_instanc).

## 3. Configure the authorization server settings

The **Authorization Server Settings** window provides controls over the usage and behavior of PingFederate as an authorization server (AS), including the policies and settings for various grant types, refresh tokens, persistent grants, and ID tokens.

Make sure to add the **email** and **preferred_username** as **Persistent Grant Extended Attributes**.

For more information, refer to [Configuring authorization server settings](https://docs.pingidentity.com/r/en-us/pingfederate-112/help_authorizationserversettingstasklet_oauthauthorizationserversettingsstate).

## 4. Configure scopes

In addition to OAuth, PingFederate supports the use of scopes to constrain and define access privileges.

**openid**, **email**, **profile**, and **offline_access** scopes are mandatory settings.

For more information, refer to [Scopes](https://docs.pingidentity.com/r/en-us/pingfederate-111/pf_scopes).

## 5. Configure access token management

Define your access token management instance. This capability allows you to configure different access token policies and attribute contracts for different OAuth clients. It also allows you to control the validation of access tokens to one or more resource servers.

For more information, refer to [Defining an access token management instance](https://docs.pingidentity.com/r/en-us/pingfederate-101/help_beareraccesstokenmgmtplugintasklet_selectadaptertypestate).

## 6. Configure access token mappings

To define how access tokens are created, use the **Access Token Manager Mapping** tab to associate one or more access token manager instances with the connection.

For more information, refer to [Configuring access token manager mappings](https://docs.pingidentity.com/r/en-us/pingfederate-112/help_oauthsamlgrantattributemappingtasklet_oauthsaml2targetmappingliststate). 

## 7. Configure OpenID Connect policy management

This configuration allows you to define OpenID Connect policies for client access to attributes mapped according to OpenID specifications.

For more information, refer to [Configuring OpenID Connect policies](https://docs.pingidentity.com/r/en-us/pingfederate-101/help_policiesmanagementtasklet_policiesmanagementstate). 

## 8. Configure IdP adapters

For more information, refer to [Configuring the IdP adapter](https://docs.pingidentity.com/r/en-us/solution-guides/gdn1597773067220).

## 9. Configure IdP adapter grant mapping

For more information, refer to [Managing IdP adapter grant mapping](https://docs.pingidentity.com/r/en-us/pingfederate-100/help_oauthsource2targetmappingtasklet_oauthidpadapter2targetmappingsstate).

## 10. Create clients (Web and Desktop) 

#### Web client

**Redirect URIs**: 
``https://<LT_ENV>/ServiceCenter/CentralizedLogin_AuthCodeFlow_TokenPart.aspx``

**Allowed Grant Types**: Select Authorization Code, Implicit, Refresh Token, Client Credentials.

#### Native client

**Redirect URIs**: Add the following redirect URIs for mobile and desktop applications:
* ``integrationstudio://auth``
* ``servicestudiox11://auth``
* ``https://experiencebuilder.outsystems.com/Authentication/OIDC_Callback``
* ``https://workflowbuilder.outsystems.com/Authentication/OIDC_Callback``
* ``https://integrationbuilder.outsystems.com/Authentication/OIDC_Callback``
* ``https://aimentorstudio.outsystems.com/Authentication/OIDC_Callback``
* For each OutSystems environment in your infrastructure (excluding Lifetime), add an **Integration Managers URI**: ``https://<YOUR_ENV>/OSIntegrationManager/OIDC_Callback``

**Allowed Grant Types**: Select Authorization Code, Implicit and Refresh Token.

For more information, refer to [Configuring an OAuth client](https://docs.pingidentity.com/r/en-us/solution-guides/mzt1663945300370).

## 11. Return scopes as part of ID token response

To return scopes as part of token response, follow these steps:

1. Open the ``/pingfederate/server/default/data/config-store/oauth-scope-settings.xml`` file.
1. Change the value of the ``always-return-scope-for-authz-code`` item from **False** to **True**. For example, ``<z:item name="always-return-scope-for-authz-code">true</z:item>``.
1. Restart the PingFederate service.
    
    **Note**: Skip this step if you are not using Integration Studio.

## 12. Configure PingFederate as OpenID connect provider in Lifetime

You can configure PingFederate as an external IdP by following thse steps:

1. Navigating to **Lifetime**> **User Management** > **Authentication Settings** 
1. Enter the details for the OIDC provider information:

    * **Provider name**: Anything of choice
    * **Well-known Configuration URL**: ``https://<PingFederateHostname>/.well-known/openid-configuration``
    * **Client ID Type**: Different Client ID for Desktop and Web tools
    * **Client ID for Web tools**: Web client ID
    * **Client ID for Desktop tools**: Desktop client ID
    * **Username Claim**: preferred_username
    * **Scopes**: Click the **Test** button next to the well-known configuration URL. It adds recommended scopes.
1. Click **Save Provider**, then **Activate Provider**. 
1. Enter the client secret and click **Activate and Log Out**.
