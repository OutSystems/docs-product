---
summary: OutSystems 11 (O11) facilitates Azure Active Directory app registration for SharePoint, Dataverse, and Dynamics 365 integration.
locale: en-us
guid: 50a76d12-73cb-4924-b36f-e76b68a00cb5
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/jSgZ0l0unYdVymLxKZasno/Extensibility-and-Integration?type=design&node-id=1019%3A6377&mode=design&t=187UAgmZTPxcY0ZG-1
tags: azure active directory, app registration, sharepoint integration, dataverse integration, dynamics 365 integration
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

# How to register SharePoint Online, Microsoft Dataverse, or Microsoft Dynamics 365 apps in Microsoft Entra

OutSystems owns and manages the Microsoft Entra application you are using for authentication and authorization. This provides another level of trust for our customers. Microsoft uses the Microsoft Entra portal to authenticate and authorize services for your app and users. To use the authentication and authorization services, you must register your app in Microsoft Entra. Integration Builder can then access your Microsoft SharePoint. Microsoft Dataverse, or Microsoft Dynamics 365 environments through the Microsoft Entra application.

The procedure to register your application includes the following:

* [Registering your app with Microsoft Entra](#registering-your-app)
* [Adding and requesting API permissions](#adding-and-requesting-application-permissions)
* [Managing certificates and secrets](#managing-certificates-and-secrets)

## Registering your app

1. Sign into the [Microsoft Entra admin center](https://entra.microsoft.com/#home) and [register your app](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/walkthrough-register-app-azure-active-directory).

1. In the **Name** field, enter one of the following:  

    * For **SharePoint Online**: `OutSystems SharePoint`
    * For **Microsoft Dataverse**:  `OutSystems Dataverse`
    * For **Microsoft Dynamics 365**: `OutSystems Dynamics 365`

1. In the **Supported account types** section, select **Accounts in this organizational directory only (\<organization name\> only - Single tenant)**.

    <div class="info" markdown="1">

    Leave the **Redirect URL (optional)** section blank.

    </div>

## Adding and requesting application permissions

To add and request application permissions for your environment, choose either the SharePoint Online, Microsoft Dataverse/Microsoft Dynamics 365 procedure.

### Adding SharePoint Online permissions

1. Add the [**Sites.ReadWrite.All**](https://learn.microsoft.com/en-us/graph/permissions-reference#sitesreadwriteall) application permissions.

1. Grant admin consent for `<your organization name>`.

### Adding Microsoft Dataverse or Microsoft Dynamics 365 permissions

1. Set the **user_impersonation** permissions for **Dynamics CRM**.

1. Optionally, grant admin consent for `<your organization name>`.

#### Adding Application Users in Power Apps

After registering your application in Azure Active Directory, you must add Application Users for the same application in Power Apps. This step is mandatory in order to have Dataverse and Dynamics connections working in Integration Builder. This is not required for SharePoint connections.

1. Sign into the [Microsoft Power Apps](https://make.powerapps.com/) and [create application users](https://learn.microsoft.com/en-us/power-platform/admin/manage-application-users#create-an-application-user) for your app.

1. To ensure you are providing the required permissions, set the **System Administrator** security role.

## Managing certificates and secrets

1. Download the OutSystems certificate that Integration Builder emailed to you. (If you prefer you can use your own certificate.)

1. In the Microsoft Entra admin center, [upload that certificate](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal#option-1-recommended-upload-a-trusted-certificate-issued-by-a-certificate-authority).
