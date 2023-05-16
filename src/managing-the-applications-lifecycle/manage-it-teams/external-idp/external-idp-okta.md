---
summary: OutSystems allows your IT users to authenticate an external IdP via OpenID Connect.
tags:
locale: en-us
guid: 5F1E1CC1-A4E7-497F-A176-7A8671CC5D8B
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Configuring Okta authentication

To configure Okta authentication, follow these steps:

1. [Create an application in the Okta portal for the OutSystems Consoles](#create-an-application-in-the-okta-portal-for-the-outsystems-consoles)

1. [Create an application in the Okta portal for the OutSystems Development Tool (Service Studio and Integration Studio)](#create-an-application-in-the-okta-portal-for-the-outsystems-development-tools-service-studio-and-integration-studio)

1. [Configure Okta as OutSystems' Identity Provider](#configure-okta-as-outsystems-identity-provider)

## Create an application in the Okta portal for the OutSystems Consoles

1. Access the Okta administration portal.

1. Go to **Applications** > **Applications** and click **Create App Integration**.

    ![Click create app integration](images/create-app-ok.png)

1. On the **Create a new app integration** screen, select the following options and click **Next**.

    * **Sign-in method**: OIDC - OpenID Connect
    * **Application type**: Web Application

    ![Click sign-in method and app type](images/select-app-type-ok.png)

1. Complete the configuration with the following details and click **Save**.

    * **App integration name**: OutSystems Consoles

    * **Grant type**: Refresh token

    * **Sign-in redirect URIs**:

        * For each of the environments on your infrastructure (including Lifetime), add  a new URI for the Service Center login page:
        ``https://<YOUR_ENV>/ServiceCenter/CentralizedLogin_AuthCodeFlow_TokenPart.aspx``

    * **Sign-out redirect URIs**:

        * For each of the environments on your infrastructure (including Lifetime), add a new URI for the Service Center logout page: ``https://<YOUR_ENV>/ServiceCenter/CentralizedLogout_CallbackEndpoint.aspx``

        * For the Lifetime environment, add a new URI for the Lifetime logout page: ``https://<LT_ENV>/LifeTimeSDK/CentralizedLogoutPage.aspx``

    * **Controlled access**: Select the option that suits your requirements

        ![Enter configuration details](images/config-consoles-ok.png)

1. From the **OutSystems Consoles** application integration screen, copy the **Client ID** and the **Client Secret** details.

    <div class="warning" markdown="1">

     You need this information when configuring the provider in LifeTime. **The client secret won't be displayed again, so ensure you save it now.**

    </div>

    ![Copy client id and client secret](images/client-cred-ok.png)

## Create an application in the Okta portal for the OutSystems Development Tools (Service Studio and Integration Studio).

1. Go back to the **Applications** screen and click **Create App Integration**.

1. On the **Create a new app integration** screen, select the following options and click **Next**:

    * **Sign-in method**: OIDC - OpenID Connect

    * **Application type**: Native Application

    ![Select OIDC and Native app](images/native-ok.png)

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

    ![Enter configuration details](images/config-tools-ok.png)

1. From the **OutSystems Development Tools** app integration screen copy the **Client ID**.

    **Note**: You’ll need this information later when you configure the provider in Lifetime.

    ![Copy Client Id](images/client-id-ok.png)

## Configure Okta as OutSystems' Identity Provider

To finalize and activate the Okta configuration for both Consoles and Development Tools, follow these steps:

1. Access the Lifetime console.

1. Go to **User Management** > **Authentication Settings** and click **Add OpenId Connect Provider**.

1. Enter the following details according to the OIDC provider you are using:

    1. **Name**: ID Provider (e.g., OKTA OIDC)

    1. **Well-known Configuration URL**: OpenID Connect metadata document URI.
    
        **Note** This URI can be found in OKTA's portal by navigating to **Security** > **API**, and from the default **Authorization Servers** tab, click your authorization server name.

        ![URI metadata](images/metadata-ok.png) 

    1. **Client ID Type**: Select the option **Different Client ID for Desktop and Web tools**.

    1. **Client ID dor Desktop Tools**: Fill in with the ID of the application used in section [Create an application in the Okta portal for the OutSystems Development Tool (Service Studio and Integration Studio)](#create-an-application-in-the-okta-portal-for-the-outsystems-development-tools-service-studio-and-integration-studio)
    
    1. **Client ID for Web Tools**: Fill in with the ID of the application used in section [Create an application in the Okta portal for the OutSystems Consoles](#create-an-application-in-the-okta-portal-for-the-outsystems-consoles)
        
    1. **Username Claim**: The claim used to match the username field of the user configured in LifeTime which will need to be  ``preferred_username`` for OKTA. For more information about claims, see [Standard Claims](https://openid.net/specs/openid-connect-core-1_0.html#StandardClaims).

1. Click **Save Changes**.

1. Before make Okta as the effective IdP, make sure to test the configuration and ensure that the Okta's users have a corresponding user created in the OutSystems platform first.

1. Click **Activate**.

1. In the pop-up window that will appear, fill in the **Client Secret** stored earlier.

1. Click the **Activate and Logout** button to start using Okta as the external Identity Provider of the OutSystems platform.
