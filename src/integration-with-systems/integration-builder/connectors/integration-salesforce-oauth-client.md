---
summary: Learn how to integrate Salesforce with OutSystems 11 (O11) by configuring an external client app and setting up permissions for seamless data exchange.
locale: en-us
guid: 32131311-38a7-41ec-84ca-8bfaf82ec229
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags:
  - Authentication
  - Authorization
  - External Authentication
  - OAuth
  - Security
audience:
  - Developer
  - Platform administrator
outsystems-tools:
  - integration builder
coverage-type:
  - apply
isautopublish: true
---

# How to integrate with Salesforce

You can enable your OutSystems app to consume or share data with a Salesforce app. This process requires configuration steps in Integration Builder and in Salesforce. This article describes the steps a Salesforce admin takes to create an external client app (ECA). It also includes the information an OutSystems developer needs from the Salesforce admin to complete the setup process in Integration Builder.

## Prerequisites

Before you begin, make sure you meet the following requirements:

* You have Salesforce administrator rights to complete these steps.
* This article assumes an OutSystems developer sent a request to the Salesforce admin through Integration Builder. The email request includes a unique authorization certificate. Alternatively, the Salesforce admin can use a private certificate.

## Create a permission set in Salesforce

### Prerequisites

Before you begin, make sure you meet the following requirements:

* You have chosen a dedicated Salesforce user account for executing your application's requests.
* The account has sufficient privileges to read, write, and manage data across Salesforce business objects. Using a user account solely for this purpose avoids conflicts.

1. **Create a Permission Set:**
   * In Salesforce, navigate to **Setup** > **Administration** > **Users** > **Permissions Sets**.
   * Click **New**, fill in the required fields (Label and API Name), and set the **License** to **None**.
   * Click **Save**.

1. **Manage Assignments:**
   * On the created **Permission Set** page, click **Manage Assignments** and then **Add Assignments**.
   * Select and assign the dedicated user account.

## Create an external client app

1. Locate the email request with the title `[user_name] requests your help to create a Salesforce External Client App`. A unique authorization certificate is attached to this email. Alternatively, use a private certificate.

1. Go to Salesforce, navigate to **Setup** > **Platform Tools** > **Apps** and open **App Manager**.

1. In the upper right, click **New External Client App**.

1. In the **Basic Information** section, fill in the required fields.

1. In **API (Enable OAuth Settings)**, select **Enable OAuth**.

1. In the **Callback URL** box, paste the following URLs:

    ```
    https://integrationbuilder.outsystems.com/OSIntegrationManager/SF_Callback
    https://integrationbuilder.outsystems.com/IM_Salesforce/SF_Callback
    ```

1. In **OAuth Scopes**, select:
   * Manage user data via APIs (api)
   * Perform requests at any time (refresh_token, offline_access)

1. In **Flow Enablement**, select **Enable JWT Bearer Flow** and upload the certificate you received in the email request. Alternatively, upload a private certificate.

1. Keep the default settings for other options and sections, and click **Create**.

1. On the details page of the created app, open the **Policies** tab and click **Edit**.

1. Open the **OAuth Policies** section and, in **Permitted Users**, choose **Admin approved users are pre-authorized**.

1. Inside the **App Policies** section, there is now the option to **Select Permission Sets**. Select the previously created one.

1. Back in the **OAuth Policies** section, in **App Authorization** > **IP Relaxation**, choose your preferred option. If you do not wish to enforce any kind of IP restriction, choose **Relax IP restrictions**.

1. Click **Save**.

1. Open the **Settings** tab.

1. Inside the **OAuth Settings** section, click **Consumer Key and Secret**.

1. On the new page that opens, copy the **Consumer Key**.

1. Send the **Consumer Key** to the developer who requested the external client app.

    If you used a private certificate, rather than the one attached to the email request, send the certificate as well, as the developer needs to upload it to Integration Manager.  
