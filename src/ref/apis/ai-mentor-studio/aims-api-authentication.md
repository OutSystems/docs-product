---
summary: Authenticating AI Mentor StudioAPI requests.
tags: article-page; support-application_development; support-Application_Lifecycle; support-devOps; support-Integrations_Extensions
locale: en-us
guid: FDBC3311-C94C-4C9C-8CC1-E7F26FC76F02
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=1607:3223
---

# AI Mentor Studio API authentication

The **AI Mentor Studio API** uses an API key to authenticate requests. All API requests must be made over a secure connection using HTTPS protocol. Calls made over plain HTTP fail. API requests without authentication also fail.  

Your API key provides access to your AI Mentor Studio information, so be sure to keep it secure. Don't share your API key in public areas such as GitHub or client-side code.  

You can generate and manage your API keys using AI Mentor Studio’s Maintenance menu.  

For authentication, you must include the following HTTP headers in your requests:

* x-api-key (your API key)

* x-activation-code ([your activation code](https://success.outsystems.com/Support/Enterprise_Customers/Licensing/Manage_and_Upgrade/Find_the_Activation_Code_and_the_Serial_Number))

The following is an example of Postman with both headers in use:

![Screenshot of Postman application showing example API request with x-api-key and x-activation-code headers](images/postman-example.png "Postman Example with Headers")

## Security considerations

When using AI Mentor Studio REST API, take the following security considerations into account:

* AI Mentor Studio doesn't store your API key. Consumer applications must store the API key securely. If a third party gets access to your API key, they have access to your infrastructure’s data.

* All communication between API consumers and the API server must be done over HTTPS.

## Prerequisites

To use the AI Mentor Studio API, you must have [full control permissions assigned as a default role](../../../building-apps/experience-builder/how-works.md#manage-architecture-dashboard-api).

## How to obtain a key { #obtain-key }

To generate your API key, follow these steps:

1. In **AI Mentor Studio**, navigate to the **Maintenance** tab and select **Configurations**.

1. In the **AI Mentor Studio API** section, click **Generate API key**.

    ![AI Mentor Studio interface with highlighted Generate API key button under Configurations](images/generate-key-ams.png "Generate API Key in AI Mentor Studio")

1. Copy the API key.  
    The **Copy API key** button changes to **Copied!** to inform you that you have successfully retrieved the key. Make sure to save your key in a safe location as you can’t access it again in AI Mentor Studio.

    ![AI Mentor Studio's API key copied confirmation with the button labeled 'Copied!'](images/copy-key-ams.png "Copy API Key in AI Mentor Studio")

1. Click **Done**.

    If you close the **Your API key** window without saving the key, there is no way of retrieving it again. If you need to replace your key, see the [How to replace a key](#replace-key) section.


## How to replace a key { #replace-key }

If you lost your API key, or if you have some security issues, you might need to replace your key. Follow these steps:

1. In **AI Mentor Studio**, navigate to the **Maintenance** tab and select **Configurations**.

1. In the **AI Mentor Studio API** section, click **Replace API key**. 

    ![AI Mentor Studio interface with highlighted Replace API key button under Configurations](images/replace-key-ams.png "Replace API Key in AI Mentor Studio")

    A window warns you that replacing your API Key takes immediate effect.

1. Click **Replace API key**.

    ![Confirmation window in AI Mentor Studio for replacing an API key with a warning about immediate effect](images/replace-key-window-ams.png "Replace API Key Confirmation Window")

1. Copy the API key.  
    The **Copy API key** button changes to **Copied!** to inform you that you have successfully retrieved the key. Make sure to save your key in a safe location as it will not be shown again, and then click **Done**.

    ![AI Mentor Studio's API key copied confirmation with the button labeled 'Copied!'](images/copy-key-ams.png "Copy API Key in AI Mentor Studio")

## How to revoke a key

To revoke your API key, follow these steps:

1. In **AI Mentor Studio**, navigate to the **Maintenance** tab and select **Configurations**.

1. In the **AI Mentor Studio API** section, click **Revoke API key**.

    ![AI Mentor Studio interface with highlighted Revoke API key button under Configurations](images/revoke-key-ams.png "Revoke API Key in AI Mentor Studio")

    A window warns you that revoking the API key immediately disables access to the AI Mentor Studio API, so any requests made after this, will be rejected.

1. Click **Revoke API key**.

    ![Confirmation window in AI Mentor Studio for revoking an API key with a warning about disabling access](images/revoke-key-window-ams.png "Revoke API Key Confirmation Window")

    Your API key is revoked. To obtain a new one, see the [How to obtain a key](#obtain-key) section.
