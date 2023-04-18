---
summary: OutSystems allows your IT users to authenticate an external IdP via OpenID Connect.
tags:
locale: en-us
guid: DA5BA9CA-066E-49E2-92C8-674CB644C370
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Configuring Microsoft Azure AD authentication

To configure Microsoft Azure AD authentication, follow these steps:

1. [Register an application](#register-an-application)

1. [Configure the platform - Web apps](#configure-the-platform---web-apps)

1. [Configure the platform - Mobile and desktop apps](#configure-the-platform---mobile-and-desktop-apps)

1. [Configure the client secret](#configure-the-client-secret)

1. [Configure permissions](#configure-permissions)

## Register an application

1. Access the Microsoft Azure portal.

1. Go to **Azure Active Directory** -> **App registrations**.

1. Click  **+ New registration**.

    ![URI metadata](images/new-reg-az.png)

1. Enter the **Name** and **Supported account type**.

    Example:

    * **Name**: OutSystems Platform

    * **Supported account type**: Accounts in this organizational directory only

1. Click **Register**.

## Configure the platform - Web apps

1. Go to **Authentication** and click **+ Add a platform**.

    ![Add a platfrom](images/add-platform-az.png)

1. From the **Configure platforms** screen, click **Web**.

    ![Choose web platform](images/web-az.png)

1. Set the **Redirect URI** to the Service Center login page from the LifeTime environment:

    * ``https://<LT_ENV>/ServiceCenter/CentralizedLogin_AuthCodeFlow_TokenPart.aspx``

    ![Set redirect URI](images/redirect-az.png)

1. Set the **Front-channel logout URL** to the Lifetime logout page from the LifeTime environment:

    * ``https://<LT_ENV>/LifeTimeSDK/CentralizedLogoutPage.aspx``

    ![Set the Front-channel logout URL](images/front-channel-az.png)

1. Click **Configure**.

1. For each of the environments in your infrastructure, add a new URI for the Service Center login page:

    * ``https://<YOUR_ENV>/ServiceCenter/CentralizedLogin_AuthCodeFlow_TokenPart.aspx``

    ![Add new URI for ech environment](images/redirect-uri-az.png)

1. Click **Save**.

## Configure the platform - Mobile and desktop apps

1. Go to **Authentication** and click **+ Add a platform**.

    ![Add a platfrom](images/add-platform-az.png)

1. From the **Configure platforms** screen, click **Mobile and desktop applications**.

    ![Choose mobile and desktop applications](images/mob-desktop-az.png)

1. Set the **Custom redirect URIs** to the following Service Studio protocol:

    * ``servicestudio://auth``

    ![Set custom redirect URI](images/custom-uri-az.png)

1. Click **Configure**.

1. Add the following URIs to the **Mobile and desktop applications** section:

    * ``integrationstudio://auth``

    * ``servicestudiox11://auth``

    * ``https://experiencebuilder.outsystems.com/Authentication/OIDC_Callback``

    * ``https://workflowbuilder.outsystems.com/Authentication/OIDC_Callback``

    * ``https://integrationbuilder.outsystems.com/Authentication/OIDC_Callback``

    * For each OutSystems environment in your infrastructure (excluding LifeTime), add an Integration Manager’s URI:

        * ``https://<YOUR_ENV>/OSIntegrationManager/OIDC_Callback``

1. Click **Save**.

## Configure the client secret

1. Go to the **Certificates & Secrets** > **Client  secrets** and click **+ New client secret**.

    ![Add new client secret](images/add-secret-az.png)

1. On the **Add a client secret** screen, enter the following details:

    * **Description**: Platform Consoles

    * **Expires**: Recommended: 6 months

    ![Enter secret details](images/secret-details-az.png)

1. Click **Add**.

1. On the **Client secrets** tab, copy the secret in the **Value** column and store it somewhere safe.

    <div class="warning" markdown="1">

     You need this information when configuring the provider in LifeTime. **This value won't be displayed again, so ensure you save it now.**

    </div>

    ![Enter secret details](images/secret-value-az.png)

## Configure permissions

1. Go to **API Permissions** and click **+ Add a permission**.

    ![Add a permission](images/add-permission-az.png)

1. From the **Request API permissions** screen, go to **Microsoft APIs** and select **Microsoft Graph**.

    ![Select Microsoft Graph](images/graph-az.png)

1. Select **Delegated permissions**.

    ![Select delegated permissions](images/delegated-permissions-az.png)

1. Select all **OpenId permissions**.

    ![Select OpenId permissions](images/openid-permissions-az.png)

1. Click **Add Permissions**.

1. Go to the **Overview** screen and copy the **Application (client) ID.**

    **Note**: You need this information when configuring the provider in Lifetime

    ![Copy application client id](images/app-client-id-az.png)

1. Go to **Endpoints** and copy the **OpenID Connect metadata document** URI.

    ![Copy OpenId metadata document](images/endpoint-az.png)

1. To configure and activate the provider, follow the steps in the [LifeTime](external-idp-lifetime.md) section using following details for the OIDC provider information:

    * **Name:** Azure AD

    * **OpenID Connect metadata document**: OpenID Connect metadata document URI

    * **Client Id**: Application (client) ID

    * **Client Secret**: Platform Consoles Client Secret











