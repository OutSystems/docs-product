---
summary: How to configure Azure AD end user authentication for your applications.
tags: runtime-traditionalwebandreactiveweb
---

# Configure Azure AD Authentication

<div class="info" markdown="1">

Requires Platform Server Release Jul.2019 CP2 (11.0.542.0) or later.

</div>

The configuration of the Azure Active Directory (AD) authentication method is quite similar to the [SAML 2.0](configure-saml.md) one, but in this case the "Claims" settings are already filled in with Azure AD default values.

Additionally, you can fill in the configuration settings for Azure AD authentication by uploading/downloading files with metadata, which helps avoid human errors.

<div class="info" markdown="1">

Check the [limitations of the current SAML 2.0 implementation](configure-saml.md#current-limitations) which also apply to the Azure AD authentication method.

</div>

## Configuring Azure Active Directory

To configure Azure AD authentication you must take these general steps:

1. Configure general Azure AD settings in Users app
1. Create and configure application in Azure AD portal
1. Finish configuration in the Users app
1. Assign user or group to Azure application
1. Test your configuration
1. Configure user roles in the Users app
1. Perform some final checks and configurations

The following sections describe these steps in detail.

### Configure general Azure AD settings in Users app

1. In the [Users application](../accessing-users.md), click **Configure Authentication** in the right sidebar.

1. In **Authentication** choose `Azure AD` (A).

    ![Configure authentication in Users app](images/azuread-config-auth-usr.png)

1. Check the settings values in **1. Service Provider Connector Settings** (B).  
    OutSystems provides default values for the required options and also an auto-generated keystore.

1. Download the Service Provider metadata file by clicking **Download SP Metadata XML**.

    ![Download the Service Provider metadata file in Users app](images/azuread-download-sp-metadata-usr.png)

### Create and configure application in Azure AD portal

On the Azure side, create a new enterprise application from a template and configure SAML sign-on. Do the following:

1. Sign in to the [Azure Active Directory portal](https://aad.portal.azure.com/).

1. In the left navigation menu, click **Enterprise applications**.

1. Click **New application** to create your own application.

    ![Click New application](images/azuread-new-application.png)

1. Search for the **OutSystems Azure AD** application on Azure AD app gallery (A) and select the application from the search results (B).

    ![Search for OutSystems Azure AD application](images/azuread-search-application.png)

1. A sidebar with options opens at the right side of the page. Define a name for your Azure application in the **Name** field (C) and click **Create** (D).

    Wait a few seconds while Azure creates your application.

    ![Add Azure AD application](images/azuread-add-application.png)

1. After the app has been created, click **Single sign-on** on the left navigation menu and select the **SAML** single sign-on method.

    ![Select SAML Single Sign-On](images/azuread-select-saml.png)

1. Click **Upload metadata file** to upload the XML metadata file downloaded from the Users app.

    ![Upload metadata file in Azure AD portal](images/azuread-upload-metadata.png)

1. Select the XML metadata file and click **Add**.

1. A sidebar with options appears at the right side of the page. Click **Save**.

    ![Save metadata options](images/azuread-save-metadata.png)

    <div class="info" markdown="1">

    One particular configuration in the Azure application depends on the value of a setting in the Users app.

    Get back to the Users app, scroll to the **1. Service Provider Connector Settings** section, and click **Show Advanced Options**.

    ![Accept Only Signed Login Responses option in the Users app](images/azuread-signed-login-responses-usr.png)

    If the option **Accept Only Signed Login Responses** is **enabled**, activate the corresponding option in Azure by following these sub-steps:

    a) In the Azure portal, edit the **SAML Signing Certificate** settings by clicking the pencil icon on the right.

    ![Edit SAML Signing Certificate settings in Azure AD portal](images/azure-saml-signing-certificate.png)

    b) In the **Signing Option** drop-down, select **Sign SAML response and assertion**.

    ![Set Signing Option in Azure AD portal](images/azure-saml-signing-option.png)

    c) Click **Save** and then close the side window.

    </div>

1. Download the Federation Metadata XML by clicking the corresponding **Download** link.

    ![Download federation metadata file in Azure AD portal](images/azuread-download-federation-metadata.png)

### Finish configuration in the Users app

Back in the Users application, upload the XML file you downloaded in the previous step.

1. Locate the **2. IdP Server Settings** section in the **Configure Authentication** page.

1. Click **Upload from IdP/Federation Metadata XML**.

    ![Upload metadata file in Users app](images/azuread-upload-federation-metadata-usr.png)

1. Select the Federation Metadata XML file you downloaded from Azure.

1. Click **Save**.

    **Note**: A warning message about enabling SSO between app types is displayed. **Enabling this functionality is optional.**

    ![SSO warning](images/azuread-warning.png)

    To enable IdP in Reactive Apps, do the following:
    
    1. Go to the Service Center management console of your OutSystems environment.

    1. Go to the **Administration** section and select the **Security** tab.

    1. In the **Common Login** section, select the **Single Sign-On Between App Types** checkbox, and click **Apply**.

       ![Applications Authentication](images/azuread-sso.png)

    For more information about application authentication, see [Configure App Authentication](../../../../managing-the-applications-lifecycle/secure-the-applications/configure-authentication.md). 

### Assign user or group to Azure application { #assign-user-azure-app }

In the Azure portal, assign a user or a group to the Azure application you created.

Check [Assign users or groups to an app via the Azure portal](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/assign-user-or-group-access-portal#assign-users-or-groups-to-an-app-via-the-azure-portal) in Microsoft documentation for step-by-step instructions.

### Test your configuration

1. Still in Azure portal, navigate back to your Azure application's single sign-on settings.

    **Tip:** Here's how you can get there: click **Enterprise applications**, search for your app and open it, and select **Single Sign-on** on the left navigation menu.

1. Click **Test** to open the test options.

    ![Test SAML configuration in Azure AD portal](images/azuread-test.png)

1. A sidebar appears at the right side of the page. Click **Sign in as current user**.

    ![Click Sign in as current user button in Azure AD](images/azuread-sign-in-as-current-user.png)

1. Enter the credentials of a user you previously associated with the Azure application in [Assign user or group to Azure application](#assign-user-azure-app).

If the authentication is **successful**, the browser redirects you back to the Users app and you get an error message about not having permissions to view the screen.

![Getting Invalid Permissions error in Users app](images/azuread-invalid-permissions-usr.png)

This happens because the user you used for testing Azure AD authentication doesn't have any assigned OutSystems roles yet. You need to grant user roles in the Users app after the user logs in for the first time using Azure AD authentication, so that the user already exists in the OutSystems database.

If the authentication is unsuccessful, double-check your configuration settings.

### Configure user roles in the Users app

You're currently logged in with a user account that doesn't have the required permissions to grant roles to end users. You must first log in with an administrator account.

Do the following:

1. Log out of the Users app, since the current user doesn't have the required role.

1. Open the following URL:

    `https://<your_server_name>/Users/Login.aspx`

    Using this specific URL allows you to log in to the Users app skipping the external authentication method that's currently configured (Azure AD).

1. Log in with an administrator account.

You now have permissions to grant OutSystems roles to users. Check [Grant a role to an end user](../end-user-roles.md#grant-role) for detailed instructions.

### Configure group roles 

If you want to leverage the AD groups that exist in Azure AD to assign OutSystems roles and control the permissions in your OutSystems apps, you need to first configure the AD so that the security roles are sent in the SAML response. 

Do the following:

1. Access the Azure AD single sign-on configurations.

1. Add the security groups as a Group Claim:

    ![image](https://user-images.githubusercontent.com/16402779/120032469-15bfb780-bfaf-11eb-95d1-2503768c1ddd.png)

1. Access the configurations on the Users app and make sure that the Groups information is mapped according to the response that you're getting from Azure AD:

    ![image](https://user-images.githubusercontent.com/16402779/120033062-f1b0a600-bfaf-11eb-992a-d8c353b93d7e.png)

This should enable Azure AD to send the group ids (object id in Azure), which will be created upon user authentication (if they don't exist already).
Unfortunately it's not possible to send the group name as they're not unique in Azure, but you can access the Users app and add a relevant description to the groups.

Note: There's a limitation of 150 group ids as of May 2021. There's an alternative way of overcoming this issue. More details can be found on this forum thread: https://www.outsystems.com/forums/discussion/67980/not-working-with-large-number-of-groups-azure-ad/

After having the groups synchronized you should be able to access the OutSystems groups in the Users app and assign the desired OutSystems roles accordingly.

### Perform some final checks and configurations

Just like when using SAML 2.0 authentication, you must perform these two final tasks:

1. [Check if the authentication flows of your OutSystems application already support external authentication](configure-saml.md#change-auth-flows). The instructions provided for the SAML 2.0 authentication method are also applicable to Azure AD authentication.

1. If you're using Azure AD authentication in **Reactive Web Apps**, [enable the "Single Sign-On Between App Types" setting](configure-saml.md#enable-sso-between-app-types) in Service Center.

## Troubleshooting Azure AD authentication issues

Since the Azure AD authentication method is very similar to the SAML 2.0 authentication method, you can troubleshoot them in the same way:

* Check the [SAML Message Logs page](configure-saml.md#logs) for detailed information on Azure AD messages exchanged for end user authentication.

* Use the same method for [accessing the Users application when you're locked out](configure-saml.md#locked-access) due to incorrect configuration settings in end user authentication.
