---
summary: Register Integration Builder app in Salesforce.
locale: en-us
guid: 32131311-38a7-41ec-84ca-8bfaf82ec229
app_type: traditional web apps, mobile apps, reactive web apps
---
# How to integrate with Salesforce

Enable your OutSystems application to consume or share data with a Salesforce app. This process requires configuration steps in Integration Builder and in Salesforce. This article describes the steps a Salesforce admin takes to create a connected app. It also includes the information an OutSystems developer needs from the Salesforce admin to complete the setup process in Integration Builder.

## Prerequisites

* You need Salesforce administrator rights to complete these steps.
* This article assumes an OutSystems developer sent a request to the Salesforce admin through Integration Builder. The email request includes a unique authorization certificate. Alternatively, the Salesforce admin can use a private certificate. 

## Create a connected app in Salesforce

1. Locate the email request with the title ```[user_name] requests your help to create a Salesforce Connected App```. A unique authorization certificate is attached to this email. Alternatively, use a private certificate.

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
 
 1. In Salesforce Service Setup, go to **Administration** > **Users** > **Permissions Sets**. 

1. Click **New**.

1. Fill in the fields; note the following:

    * After you type the Label, the API Name should autocomplete.
    * Leave the **License** drop-down as **None**

1. Click **Save**. 

1. On the **Permission Set** page you just created, click **Manage Assignments**, and then click **Add Assignments**.

1. Select and assign a user. We recommend assigning a specific user, and that user should have permission to read, write, and delete data from Salesforce business objects.

1. Navigate back to **App Manager**. 

1. For the app you created, click the arrow on the right and select **Manage**.

1. Click **Edit Policies.**

1. In **Permitted Users**, select **Admin approved users are pre-authorized**, and click **Save**.

1. In **Permissions Sets**, click **Manage Permission Sets**.

1. Select the Permission set you created, and click **Save**. 
