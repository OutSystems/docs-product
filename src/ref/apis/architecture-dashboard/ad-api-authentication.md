---
summary: Authenticating Architecture Dashboard API requests.
tags: article-page; support-application_development; support-Application_Lifecycle; support-devOps; support-Integrations_Extensions
locale: en-us
guid: FDBC3311-C94C-4C9C-8CC1-E7F26FC76F02
app_type: traditional web apps, mobile apps, reactive web apps
---

# Architecture Dashboard API authentication

The **Architecture Dashboard API** uses an API key to authenticate requests. All API requests must be made over a secure connection using HTTPS protocol. Calls made over plain HTTP fail. API requests without authentication also fail.  

Your API key provides access to your Architecture Dashboard information, so be sure to keep it secure. Don't share your API key in public areas such as GitHub or client-side code.  

You can generate and manage your API keys using Architecture Dashboard’s Maintenance menu.  

For authentication, you must include the following HTTP headers in your requests:

* x-api-key (your API key)

* x-activation-code ([your activation code](https://success.outsystems.com/Support/Enterprise_Customers/Licensing/Manage_and_Upgrade/Find_the_Activation_Code_and_the_Serial_Number))

The following is an example of Postman with both headers in use:

![Example of a request in Postman, using the authentication headers.](images/postman-example.png)

## Security considerations

When using Architecture Dashboard REST API, take the following security considerations into account:

* Architecture Dashboard doesn't store your API key. Consumer applications must store the API key securely. If a third party gets access to your API key, they have access to your infrastructure’s data.

* All communication between API consumers and the API server must be done over HTTPS.

## Prerequisites

To be able to use the Architecture Dashboard API, you need to have [full control permissions assigned as a default role](../../../managing-the-applications-lifecycle/manage-tech-debt/how-works.md#manage-architecture-dashboard-api).

## How to obtain a key { #obtain-key }

To generate your API key, follow these steps:

1. In **Architecture Dashboard**, navigate to the **Maintenance** tab and select **Configurations**.

1. In the **Architecture Dashboard API** section, click **Generate API key**.

    ![Architecture Dashboard's Maintenance menu showing the Configurations.](images/generate-key-ad.png)

1. Copy the API key.  
The **Copy API key** button changes to **Copied!** to inform you that you have successfully retrieved the key. Make sure to save your key in a safe location as you can’t access it again in Architecture Dashboard.

    ![Window showing the generated API key.](images/copy-key-ad.png)

1. Click **Done**.

    If you close the **Your API key** window without saving the key, there is no way of retrieving it again. If you need to replace your key, see the [How to replace a key](#replace-key) section.


## How to replace a key { #replace-key }

If you lost your API key, or if you have some security issues, you might need to replace your key. Follow these steps:

1. In **Architecture Dashboard**, navigate to the **Maintenance** tab and select **Configurations**.

1. In the **Architecture Dashboard API** section, click **Replace API key**. 

    ![Architecture Dashboard's Maintenance menu showing the Configurations.](images/replace-key-ad.png)

    A window warns you that replacing your API Key takes immediate effect.

1. Click **Replace API key**.

    ![Window asking for confirmation to replace API key.](images/replace-key-window-ad.png)

1. Copy the API key.  
The **Copy API key** button changes to **Copied!** to inform you that you have successfully retrieved the key. Make sure to save your key in a safe location as it will not be shown again, and then click **Done**.

    ![Window showing the generated API key.](images/copy-key-ad.png)

## How to revoke a key

To revoke your API key, follow these steps:

1. In **Architecture Dashboard**, navigate to the **Maintenance** tab and select **Configurations**.

1. In the **Architecture Dashboard API** section, click **Revoke API key**.

    ![Architecture Dashboard's Maintenance menu showing the Configurations.](images/revoke-key-ad.png)

    A window warns you that revoking the API key immediately disables access to the Architecture Dashboard API, so any requests made after this, will be rejected.

1. Click **Revoke API key**.

    ![Window asking for confirmation to revoke API key.](images/revoke-key-window-ad.png)

    Your API key is revoked. To obtain a new one, see the [How to obtain a key](#obtain-key) section.
