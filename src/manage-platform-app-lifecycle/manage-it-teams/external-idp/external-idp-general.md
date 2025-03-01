---
summary: Explore how to integrate external identity providers using OIDC with OutSystems 11 (O11) for enhanced authentication across web and native applications.
tags: oidc integration, authentication, identity providers, openid connect discovery, token configuration
locale: en-us
guid: 7486CF76-C3FC-41E0-B2E9-F6C6512FAB44
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - platform administrators
  - full stack developers
  - frontend developers
outsystems-tools:
  - service studio
  - service center
  - lifetime
coverage-type:
  - understand
  - apply
---

# Generic external identity provider supporting OIDC

This article describes the generic configuration points to integrate with other identity providers.

The external IdP must implement the [OpenID Connect Discovery](https://openid.net/specs/openid-connect-discovery-1_0.html). This enables the retrieval of configuration information from a well-known location as a JSON document (also known as a well-known URI).

The external IdP must support the following scopes:
* email
* openid
* profile

You must configure the authorization and refresh tokens in the external IdP. By default, the **prefered_username** claim matches the **username** field of the user configured in LifeTime.

The redirect URIs configuration is split into Web Applications (Consoles) and Native Application (Development Tools), but depending on the external provider, the redirects configuration can be configured together, like on Microsoft Entra, or separately, like on Okta.


##  Integrating with OutSystems Consoles

To integrate with OutSystems Consoles, follow these steps:

1. **Sign-in redirect URIs**:

    * In the external IdP, for each of the environments on your infrastructure (including Lifetime), add a new URI for the Service Center login page :

        * ``https://<YOUR_ENV>/ServiceCenter/CentralizedLogin_AuthCodeFlow_TokenPart.aspx``

1. **Sign-out redirect URIs**:

    * In the external IdP, for each of the environments on your infrastructure (including Lifetime), add a new URI for the Service Center logout page:

        * ``https://<YOUR_ENV>/ServiceCenter/CentralizedLogout_CallbackEndpoint.aspx``

## Integrating with OutSystems Development Tools

To integrate OutSystems Development Tools, follow these steps:

1. **Sign-in redirect URIs**:

    * ``servicestudio://auth``

    * ``integrationstudio://auth``

    * ``servicestudiox11://auth``

    * ``https://experiencebuilder.outsystems.com/Authentication/OIDC_Callback``

    * ``https://workflowbuilder.outsystems.com/Authentication/OIDC_Callback``

    * ``https://integrationbuilder.outsystems.com/Authentication/OIDC_Callback`` 

    * ``https://aimentorstudio.outsystems.com/Authentication/OIDC_Callback``

    * For each OutSystems environment in your infrastructure (excluding LifeTime), add an Integration Manager’s URI:
        *   ``https://<YOUR_ENV>/OSIntegrationManager/OIDC_Callback``


1. **Sign-out redirect URIs**:

    * ``servicestudio://auth``

    * ``integrationstudio://auth``

    * ``servicestudiox11://auth``

    * ``https://www.outsystems.com``

