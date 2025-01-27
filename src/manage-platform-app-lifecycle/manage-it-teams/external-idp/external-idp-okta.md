---
summary: This guide details configuring Okta authentication for OutSystems 11 (O11) applications and development tools.
tags: authentication, okta, security, oidc, configuration
locale: en-us
guid: 5F1E1CC1-A4E7-497F-A176-7A8671CC5D8B
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing%20the%20Applications%20Lifecycle?node-id=1914:6837
audience:
  - platform administrators
  - full stack developers
  - frontend developers
  - backend developers
outsystems-tools:
  - service studio
  - lifetime
coverage-type:
  - apply
---

# Configuring Okta authentication

To configure Okta authentication, follow these steps:

1. [Create an application in the Okta portal for the OutSystems Consoles](#create-an-application-in-the-okta-portal-for-the-outsystems-consoles)

1. [Create an application in the Okta portal for the OutSystems Development Tool (Service Studio and Integration Studio)](#create-an-application-in-the-okta-portal-for-the-outsystems-development-tools-service-studio-and-integration-studio)

1. [Activate Okta configuration](#activate-okta-configuration)

## Create an application in the Okta portal for the OutSystems Consoles

1. Access the Okta administration portal.

1. Go to **Applications** > **Applications** and click **Create App Integration**.

    ![Screenshot of the Okta portal showing the 'Create App Integration' button](images/create-app-ok.png "Creating an App Integration in Okta")

1. On the **Create a new app integration** screen, select the following options and click **Next**.

    * **Sign-in method**: OIDC - OpenID Connect
    
    * **Application type**: Web Application

    ![Screenshot of Okta's 'Create a new app integration' screen with 'OIDC - OpenID Connect' and 'Web Application' selected](images/select-app-type-ok.png "Selecting Application Type in Okta")

1. Complete the configuration with the following details and click **Save**.

    * **App integration name**: OutSystems Consoles

    * **Grant type**: Refresh token

    * **Sign-in redirect URIs**:

        * For each of the environments on your infrastructure (including Lifetime), add  a new URI for the Service Center login page:
        ``https://<YOUR_ENV>/ServiceCenter/CentralizedLogin_AuthCodeFlow_TokenPart.aspx``

    * **Sign-out redirect URIs**:

        * For each of the environments on your infrastructure (including Lifetime), add a new URI for the Service Center logout page: ``https://<YOUR_ENV>/ServiceCenter/CentralizedLogout_CallbackEndpoint.aspx``

    * **Controlled access**: Select the option that suits your requirements

        ![Screenshot detailing the configuration options for OutSystems Consoles app integration in Okta](images/config-consoles-ok.png "Configuring OutSystems Consoles in Okta")

1. From the **OutSystems Consoles** application integration screen, copy the **Client ID** and the **Client Secret** details.

    <div class="warning" markdown="1">

     You need this information when configuring the provider in LifeTime. **The client secret won't be displayed again, so ensure you save it now.**

    </div>

    ![Screenshot showing the 'Client ID' and 'Client Secret' for the OutSystems Consoles application in Okta](images/client-cred-ok.png "Client Credentials for OutSystems Consoles")

## Create an application in the Okta portal for the OutSystems Development Tools (Service Studio and Integration Studio).

1. Go back to the **Applications** screen and click **Create App Integration**.

1. On the **Create a new app integration** screen, select the following options and click **Next**:

    * **Sign-in method**: OIDC - OpenID Connect

    * **Application type**: Native Application

    ![Screenshot of Okta's 'Create a new app integration' screen with 'OIDC - OpenID Connect' and 'Native Application' selected](images/native-ok.png "Selecting Native Application Type in Okta")

1. Complete the configuration details with the following details and click **Save**.

    * **App integration name**: OutSystems Development Tools

    * **Grant type**: Refresh token

    * **Sign-in redirect URIs**:

        * ``servicestudio://auth``

        * ``integrationstudio://auth``

        * ``servicestudiox11://auth``

        * ``https://experiencebuilder.outsystems.com/Authentication/OIDC_Callback``

        * ``https://workflowbuilder.outsystems.com/Authentication/OIDC_Callback``

        * ``https://integrationbuilder.outsystems.com/Authentication/OIDC_Callback``

        * ``https://aimentorstudio.outsystems.com/Authentication/OIDC_Callback``

        * For each OutSystems environment in your infrastructure (excluding LifeTime), add an Integration Manager’s URI:

            * ``https://<YOUR_ENV>/OSIntegrationManager/OIDC_Callback``

    * **Sign-out redirect URIs**:

        * ``servicestudio://auth``

        * ``integrationstudio://auth``

        * ``servicestudiox11://auth``

        * ``https://www.outsystems.com``

    * **Controlled access**: Select the option that suits your requirements

    ![Screenshot detailing the configuration options for OutSystems Development Tools app integration in Okta](images/config-tools-ok.png "Configuring OutSystems Development Tools in Okta")

1. From the **OutSystems Development Tools** app integration screen copy the **Client ID**.

    **Note**: You’ll need this information later when you configure the provider in Lifetime.

    ![Screenshot showing the 'Client ID' for the OutSystems Development Tools application in Okta](images/client-id-ok.png "Client ID for OutSystems Development Tools")

## Configure Okta as OpenId connect provider in LifeTime

Follow the steps mentioned [here](external-idp-lifetime.md).