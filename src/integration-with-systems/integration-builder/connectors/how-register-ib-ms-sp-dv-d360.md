---
summary: Register Integration SharePoint Online, Microsoft Dataverse, or Microsoft Dynamics 365 applications in Azure AD to authenticate and authorize users. 
locale: en-us
guid: 50a76d12-73cb-4924-b36f-e76b68a00cb5
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/jSgZ0l0unYdVymLxKZasno/Extensibility-and-Integration?type=design&node-id=1019%3A6377&mode=design&t=187UAgmZTPxcY0ZG-1
---
# How to register SharePoint Online, Microsoft Dataverse, or Microsoft Dynamics 365 apps in the Azure Active Directory

OutSystems owns and manages the Azure Active Directory application you are using for authentication and authorization. This provides another level of trust for our customers. Microsoft uses the Azure portal to authenticate and authorize services for your app and users. To use the authentication and authorization services, you must register your app in the Azure AD (Active Directory). Integration Builder can then access your Microsoft SharePoint. Microsoft Dataverse, or Microsoft Dynamics 365 environments through the Azure AD application.


The procedure to register your application includes the following:

* Registering your app
* Adding and requesting API permissions
* Managing certificates and secrets

<div class="info" markdown="1">

  If the left menu pane is not open, click the Hamburger icon. These procedures use the left menu pane to access the integration options.

</div>

## Registering your app

1. Sign into the [Microsoft Azure Portal](https://portal.azure.com/).

1. From the left menu pane, click **Azure Active Directory**.

1. From the left menu pane, click **App registrations**.

1. From the top menu bar, click **+ New Registration**.

    ![Screenshot of the Azure Portal top menu bar with the 'New Registration' button highlighted](images/ms-azure-top-menu-bar.png "Azure Portal Top Menu Bar")

1. In the name field, **copy and paste** one of the following:  

    * For **SharePoint Online**: `OutSystems SharePoint`
    * For **Microsoft Dataverse**:  `OutSystems Dataverse`
    * For **Microsoft Dynamics 365**: `OutSystems Dynamics 365`

1. In the Supported account types section, select **Accounts in this organizational directory only (\<organization name\> only - Single tenant)**.

    <div class="info" markdown="1">

    Leave the **Redirect URL (optional)** section blank.

    </div>

1. Click **Register**.

## Adding and requesting application permissions

To add and request application permissions for your environment, choose either the SharePoint Online, Microsoft Dataverse / Microsoft Dynamics 365 procedure.

### Adding SharePoint Online permissions

1. From the left menu pane, click **API permissions**.

1. Below Configured permissions, click **Add a permission** to open the Request API permissions window.

1. Click **SharePoint**.

1. Select **Application Permissions**.

1. From the list of permissions, continue to scroll, click **Sites** and select **Sites.ReadWrite.All**. Click **Add permissions**.

    <div class="info" markdown="1">

    A warning message may display in the Add a Permissions list, indicating the permission was not granted for OutSystems Integration team.

    </div>

1. Click the **Grant admin consent for `<your organization name>`** link.

### Adding Microsoft Dataverse or Microsoft Dynamics 365 permissions

1. From the left menu pane, click **API permissions**.

1. Below Configured permissions, click **Add a permission** to open the Request API permissions window.

   ![Screenshot showing the API permissions section in Azure Portal with 'Add a permission' button selected](images/ms-azure-permission-selected.png "Azure Portal API Permissions")

1. Under Request API permission, click in the **Dynamics CRM** box.

   ![Screenshot of the Dynamics CRM permission option in Azure Portal's Request API permissions window](images/ms-azure-dynamics-crm.png "Azure Portal Dynamics CRM Permission")

1. Under Permissions, select **user_impersonation**.

1. Scroll to the bottom of the list and click the **Add permissions** button again.

    <div class="info" markdown="1">

    A warning message may display in the Add a Permissions list, indicating the permission was not granted for OutSystems Integration team.

    </div>

1. Optionally, to grant permission, click the **Grant admin consent for `<your organization name>`** link.

    ![Screenshot of the Azure Portal with the 'Grant admin consent for your organization' link highlighted](images/ms-azure-grant-permission.png "Azure Portal Grant Permission")

#### Adding Application Users in Power Apps

After registering your application in Azure Active Directory, you must add Application Users for the same application in Power Apps. This step is mandatory in order to have Dataverse and Dynamics connections working in Integration Builder. This is not required for SharePoint connections.

1. Sign into the [Microsoft Power Apps](https://make.powerapps.com/).

1. From the top bar, click **Settings** > **Admin Center**.

1. From the menu, click **Environments**.

1. From the list of **Environments**, select your environment.

1. From the top menu, click **Settings**.

1. Expand **Users + permissions** and click **Application** users.

1. From the top menu, click **+ New App User**.

1. From the right panel, click **+ Add an app**.

1. Search for the application that you have previously created in Azure Active Directory, select it and click **Add**.

1. Still in the right panel, select the **Business Unit**.

1. In **Security Roles**, select **System Administrator** and click **Save**.
    System Administrator role ensures that you are providing the required permissions. But other permissions may work as well.

## Managing certificates and secrets

<div class="info" markdown="1">

Before beginning this procedure, make sure to download the OutSystems certificate that Integration Builder emailed to you. (If you prefer you can use your own certificate.)

</div>

1. From the left menu pane, click **Certificates & secrets**.

1. Below Certificates, click **Upload Certificate**.

1. Click the **File** button and navigate to the location in which you placed the certificate.

1. Click **Open** and then click **Add**. The certificate is added to your app.  
