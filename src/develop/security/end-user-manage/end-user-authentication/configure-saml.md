---
summary: How to configure SAML 2.0 end user authentication for your applications.
tags: runtime-traditionalwebandreactiveweb
---

# Configure SAML 2.0 Authentication

<div class="info" markdown="1">

Requires Platform Server Release Jul.2019 CP2 (11.0.542.0) or later.

</div>

You can integrate OutSystems in your Federated Authentication system using the SAML 2.0 protocol to connect to an external Identity Provider (IdP), allowing for Single Sign-On (SSO) and single logout operations.

The general authentication workflow is the following:

1. A non-logged in user tries to access an OutSystems application, known in SAML as the Service Provider (SP).

1. The browser redirects the user to a web page, known as the enterprise's login manager, where they must enter their enterprise username and password.

1. Upon verification of the user's login, the enterprise Identity Provider informs OutSystems application of the verified identity for the user who is logging in, and the browser redirects the user back to the portal website.

## Current limitations { #current-limitations }

The current SAML 2.0 implementation in OutSystems has some limitations outlined below. Since the OutSystems platform is being continuously improved, be sure to check this page regularly for an updated list of limitations.

* The SAML 2.0 support provided by the Users module is only applicable to **Traditional Web Apps** and **Reactive Web Apps**. To use SAML 2.0 in Mobile apps you can use Forge components that address those use cases, like [IdP Connector](https://www.outsystems.com/forge/component-overview/599/idp) and [IdP Mobile](https://www.outsystems.com/forge/component-overview/2044/idp-mobile).  
    _Note:_ The Forge components mentioned above aren't supported by OutSystems and are maintained by the Forge community.
* To implement single logout you may need to change the authentication flows of your OutSystems application. Check below for details.

* Though the Users application is multi-tenant, multi-tenancy isn't supported when using SAML 2.0, Azure AD or Okta authentication methods.

If you have some logic that must run at each login, or if your IdP has some particular configuration not supported by the Users application, consider cloning the Users module of the Users application and extend it to fulfill your specific requirements.

## Using SAML in your OutSystems applications

To configure SAML 2.0 end user authentication you need to take the following steps:

1. Configure SAML 2.0 authentication in the Users application.

1. Check if your application authentication flows (login/logout) already support SAML 2.0. If not, you must change these flows according to the provided instructions.

1. To use SAML 2.0 authentication in Reactive Web Apps, you must enable **Single Sign-On Between App Types** in the environment configuration.

### Configure SAML 2.0 authentication in the Users application { #configure-users }

Make sure you gather all the required information from your Identity Provider beforehand to be able to configure SAML 2.0 authentication in the Users application.

Do the following:

1. In the Users application, click **Configure Authentication** in the sidebar.

1. Choose `SAML 2.0` in the **Authentication** drop-down list.

1. Provide the required configuration values according to the Identity Provider you're going to use.

    If the option **Accept Only Signed Login Responses** in the OutSystems Users application is active (it's enabled by default), make sure you activate the corresponding setting in your Identity Provider.  
    The option **Accept Only Signed Login Responses** is available in **1. Service Provider Connector Settings**, under **Advanced Options**.

    **Note:** The Users app requires SAML assertions to be **signed**. Make sure you activate the assertion signing setting in your Identity Provider.

    ![Accept Only Signed Login Responses option in Configure Authentication](images/saml-option-signed-login-responses.png)

**Tip:** To speed up configuration, and if your Identity Provider (IdP) has this feature, you can export a Service Provider (SP) metadata XML file in the Users application to import it in your IdP.  
Similarly, you can import a Federation metadata XML file containing the IdP Server Settings in the Users application if your IdP has the option to export this metadata file.

### Check the authentication flows of your OutSystems applications { #change-auth-flows }

Depending on the version of OutSystems UI Web (for Traditional Web Apps) or OutSystems UI Reactive Templates (for Reactive Web Apps) installed in your development environment when you created your application, you may need to update the login/logout flows of your app to make them compatible with SAML 2.0 authentication.

For more information, check the following topics according to your application type:

* For **Reactive Web Apps** check [Updating the login/logout flows of your Reactive Web App to support SAML 2.0](https://success.outsystems.com/Support/Enterprise_Customers/Upgrading/Updating_the_login%2F%2Flogout_flows_of_your_Reactive_Web_App_to_support_SAML_2.0).
* For **Traditional Web Apps** check [Updating the logout flow of your Traditional Web App to support SAML 2.0](https://success.outsystems.com/Support/Enterprise_Customers/Upgrading/Updating_the_logout_flow_of_your_Traditional_Web_App_to_support_SAML_2.0). 

### Enable single sign-on between app types to use SAML 2.0 in Reactive Web Apps { #enable-sso-between-app-types }

To use SAML 2.0 authentication in Reactive Web Apps, you must enable **Single Sign-On Between App Types** in the environment configuration. This also applies to SAML-based authentication methods like Azure AD and Okta.

Additionally, this configuration requires you to enable some additional security settings at the environment level.

To enable all the required settings do the following:

1. Open Service Center.

1. Navigate to **Administration** > **Security**.

1. Enable the following settings:

    – Secure Connections > **Enable HTTP Strict Transport Security (HSTS)**  
    – Cookies > **Secure**

1. Click **Save**.

1. Click **Applications Authentication** under the **Environment Security** heading.

1. Enable **Single Sign-On Between App Types**.

    <div class="info" markdown="1">

    Having different session timeout values for Traditional Web and Reactive Web applications may lead to issues during authentication flows.

    If you are running **Platform Server 11.14.1 or later**, the default value of the session timeout for Reactive Web Apps matches the default value of the session timeout for Traditional Web Apps (20m). In this case, if you haven't changed the session timeout default values, you can skip Step 7.

    If you are running **Platform Server 11.14.0 or earlier**, execute Step 7 to make sure both values match, thus preventing authentication issues.

    </div>

1. In **Session Login Settings**, ensure the **Max. Idle Time** has the same value as the **Session Timeout** for Traditional Web Apps (see [here](../../../data/session.md#session-timeout) how to configure the session timeout for Traditional Web Apps).

1. Click **Save and Apply Settings to the Factory** to apply all the new runtime settings.

For more information on application authentication check [Configure App Authentication](../../../../managing-the-applications-lifecycle/secure-the-applications/configure-authentication.md).

## Mapping Identity Provider Server Groups to OutSystems Groups

You can configure the **Groups** claim in the "Configure Authentication" screen of the Users application. When this claim has a value and a user login occurs, OutSystems tries to match each group name received from the external SAML-based Identity Provider with the groups configured in the platform.

When there is a match, the Users application associates the user logging in to the existing OutSystems group. If there's no match, OutSystems first creates a new group with the same name as the Identity Provider Server group and then associates the user to that group.

_Known limitation:_ In Azure AD, group names received from the Identity Provider Server consist only of a globally unique identifier (GUID). This means that to have a match between Azure AD groups and OutSystems groups you must name the OutSystems groups using these GUID values.

## Troubleshooting SAML authentication issues

### Accessing message logs { #logs }

The SAML Message Logs page is very useful when troubleshooting SAML configuration or authentication issues. It's available from the right sidebar by clicking "SAML Message Logs".

![SAML Message Logs page](images/saml-message-logs.png?width=800)

These logs are available for 7 days by default. You can customize this retention period using the `DeleteSAMLLogsOlderThen` multi-tenant Site Property of the Users module.

To customize the value of this site property, do the following:

1. Open Service Center, navigate to **Factory** > **Modules** and open the Users module.
1. Open the **Tenants** tab and click the "Users" link to navigate to the Users tenant detail page.
1. In the **Site Properties** tab, click the link to edit the `DeleteSAMLLogsOlderThen` property and enter the new value for the site property.

### Accessing the Users application when locked out { #locked-access }

If your authentication configuration is incorrect and preventing you from logging in using SAML you can still login with an administrator account (it must be a user with the UserManager role) by navigating to the default Users app login page. This bypasses the configured authentication method, allowing you to log in and fix the incorrect settings.

The default Users app login page is available at the following URL:

`https://<your_server_name>/Users/Login.aspx`

### Common SAML configuration errors { #common-saml-errors }

### "Error processing response. Unable to decrypt the assertion."

* [Error processing SAML response - Unable to decrypt the assertion](https://success.outsystems.com/Support/Enterprise_Customers/Troubleshooting/Error_processing_SAML_response_-_Unable_to_decrypt_the_assertion)
