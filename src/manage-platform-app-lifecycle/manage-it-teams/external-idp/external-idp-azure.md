---
summary: This guide details configuring Microsoft Azure AD authentication for OutSystems 11 (O11) as an identity provider.
tags: identity provider configuration, azure ad, authentication, security, sso
locale: en-us
guid: DA5BA9CA-066E-49E2-92C8-674CB644C370
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing-the-Applications-Lifecycle?type=design&node-id=1914%3A6373&mode=design&t=qy82U3bMoQChCp6y-1
audience:
  - platform administrators
  - frontend developers
  - backend developers
  - full stack developers
  - architects
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# Configuring Microsoft Entra authentication

To configure Microsoft Entra authentication, follow these steps:

1. [Register and name your app with Microsoft Entra](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app?tabs=certificate#register-an-application)

1. [Configure the platform settings for Web apps](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-redirect-uri) using the following settings:

    * Set the **Redirect URI** to the Service Center login page from the LifeTime environment:

        * ``https://<LT_ENV>/ServiceCenter/CentralizedLogin_AuthCodeFlow_TokenPart.aspx``

    * For each of the environments in your infrastructure, add a new URI for the Service Center login page:

        * ``https://<YOUR_ENV>/ServiceCenter/CentralizedLogin_AuthCodeFlow_TokenPart.aspx``

1. [Configure the platform settings for Mobile and Desktop apps](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-redirect-uri) using the following settings:

    * Set the **Custom redirect URIs** to the following Service Studio protocol:

        * ``servicestudio://auth``

    * Add the following URIs:

        * ``integrationstudio://auth``

        * ``servicestudiox11://auth``

        * ``https://experiencebuilder.outsystems.com/Authentication/OIDC_Callback``

        * ``https://workflowbuilder.outsystems.com/Authentication/OIDC_Callback``

        * ``https://integrationbuilder.outsystems.com/Authentication/OIDC_Callback``

        * ``https://aimentorstudio.outsystems.com/Authentication/OIDC_Callback``

    * For each OutSystems environment in your infrastructure (excluding LifeTime), add an Integration Manager's URI:

        * ``https://<YOUR_ENV>/OSIntegrationManager/OIDC_Callback``

1. [Configure the client secret](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-credentials?tabs=certificate)

    <div class="warning" markdown="1">

    Remember to copy the client secret value. You need this information when configuring the provider in LifeTime. **This value won't be displayed again, so ensure you save it now.**

    </div>

1. [Add delegated permissions to access Microsoft Graph](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-configure-app-access-web-apis#add-permissions-to-access-microsoft-graph)

1. [Configure Microsoft Entra as OpenId connect provider in LifeTime](external-idp-lifetime.md)
