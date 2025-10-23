---
summary: Learn how to integrate Salesforce with OutSystems 11 (O11) by configuring a connected app and setting up permissions for seamless data exchange.
locale: en-us
guid: 32131311-38a7-41ec-84ca-8bfaf82ec229
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: salesforce integration, api configuration, oauth settings, connected apps, digital certificates
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - platform administrators
outsystems-tools:
  - integration builder
coverage-type:
  - apply
---

# How to integrate with Salesforce

Enable your OutSystems application to consume or share data with a Salesforce app. This process requires configuration steps in Integration Builder and in Salesforce. This article describes the steps a Salesforce admin takes to create a connected app. It also includes the information an OutSystems developer needs from the Salesforce admin to complete the setup process in Integration Builder.

## Prerequisites

* You need Salesforce administrator rights to complete these steps.
* This article assumes an OutSystems developer sent a request to the Salesforce admin through Integration Builder. The email request includes a unique authorization certificate. Alternatively, the Salesforce admin can use a private certificate.

## Create a connected app in Salesforce

1. Locate the email request with the title `[user_name] requests your help to create a Salesforce Connected App`. A unique authorization certificate is attached to this email. Alternatively, use a private certificate.

1. Go to Salesforce > **Service Setup Home**, and open **App Manager** (**User Interface** > **User Interface** > **App Manager**).

1. In the upper right, click **New Connected App**.

1. In the **Basic Information** section, fill in the required fields.

1. In **API (Enable OAuth Settings)**, select **Enable OAuth Settings**.

1. In the **Callback URL** box, paste the following URLs:

    ```
    https://integrationbuilder.outsystems.com/OSIntegrationManager/SF_Callback
    https://integrationbuilder.outsystems.com/IM_Salesforce/SF_Callback
    ```

1. Select **Use digital signatures**, and upload the certificate you received in the email request. Alternatively, upload a private certificate.

1. In **Selected OAuth Scopes**, add:

    * Access and manage your data (api)
    * Perform requests on your behalf at any time (refresh_token, offline_access)

1. Keep the default settings for other options and sections, and click **Save**. Then click **Continue**.

1. On the Manage Connected Apps summary page, in **API (Enable OAuth Settings)**, copy the **Consumer Key**.

1. Send the  **Consumer Key** to the developer who requested the connected app.

    If you used a private certificate, rather than the one attached to the email request, send the certificate as well, as the developer needs to upload it to Integration Manager.  

## Assign pre-authorized users

**Prerequisite:** Choose a dedicated user account for executing your application's requests. Using a user account solely for this purpose is advisable to avoid conflicts. Ensure this account is granted sufficient privileges to read, write, and manage data across Salesforce business objects. Once this is set up, proceed with the following steps.

1. **Create a Permission Set:**
   * In Salesforce, navigate to **Service Setup** > **Administration** > **Users** > **Permissions Sets**.
   * Click **New**, fill in the required fields (Label and API Name), and set the **License** to **None**.
   * Click **Save**.

1. **Manage Assignments:**
   * On the created **Permission Set** page, click **Manage Assignments** and then **Add Assignments**.
   * Select and assign the dedicated user account.

1. **Configure Connected App Access:**
   * Return to the **Permission Set** page, click **Assigned Connected Apps**, and click **Edit**.
   * Add the previously created Connected App to the Enabled list and save.

1. **Edit App Policies:**
   * Navigate back to **App Manager**.
   * Find your connected app, select **Manage** from the options, and then click **Edit Policies**.
   * Under **Permitted Users**, choose **Admin approved users are pre-authorized**.
   * Save your changes.

1. **Finalize Permission Set:**
   * Under **Permissions Sets**, click **Manage Permission Sets**.
   * Select the Permission Set created earlier and click **Save**.
