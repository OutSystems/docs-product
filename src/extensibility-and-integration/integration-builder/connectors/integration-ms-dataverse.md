---
summary: Learn more about the Microsoft Dataverse (previously known as Microsoft Common Data Service) integration.
locale: en-us
guid: ea253851-f067-457e-81e9-8fe3e106decc
---

# Microsoft Dataverse integration

The Microsoft Dataverse integration allows you to perform operations on entities available in Microsoft Dataverse from your OutSystems applications.

<div class="info" markdown="1">

Microsoft Dataverse was formerly known as Microsoft Common Data Service or **Microsoft CDS**.

</div>

## Prerequisites

Verify the following:

* You meet the general [Integration Builder prerequisites](../set-up.md#prerequisites).
* The Microsoft Dataverse integration deployed in your OutSystems development environment can make HTTPS outbound requests (port 443) to your Microsoft Dataverse service.
* You have a Microsoft account with Microsoft Dataverse and Azure Administrator privileges. These admin privileges are required to access your Azure Active Directory (AD) tenant and to create security roles and application users.

## Authorizing Integration Builder in your Microsoft account

Follow the instructions provided in [Creating and using an integration](../use.md#create-use). You must authorize Integration Builder to access your data in Microsoft Dataverse through your Microsoft account.

![Authorizing Integration Builder to access your Microsoft account data](images/ms-authorization-1.png)

Integration Builder uses this authorization to obtain the available objects for building a Microsoft Dataverse integration.

Additionally, when you're creating a connection, Integration Manager connects to Integration Builder, requesting the creation of an Azure app and other related objects. This operation uses the same authorization, since only Integration Builder has the access tokens for this authorization.

### About environment instances

If you have several Microsoft Dataverse environment instances in your Microsoft account, Integration Builder asks you which environment you want to use when connecting to Microsoft Dataverse.

According to Microsoft, an environment instance in Microsoft Dataverse is "a space to store, manage, and share your organization's business data, apps, and flows". When you're creating a Microsoft Dataverse integration, Integration Builder registers an Azure application in the environment you choose.

## Authorizing a Microsoft Dataverse connection { #authorize-integration }

Microsoft Dataverse integrations generated with Integration Builder use a certificate to authenticate requests done at runtime, using the connection you configured.

Request authentication is handled transparently when you call Server Actions exposed by the service module (the module with a "_IS" suffix, by default). The Server Actions obtain the certificate info from the connection that you previously associated with the integration in Integration Manager. Therefore, you don't need to provide any authentication information as input parameters.

### If you have administrator permissions in Azure Active Directory

Integration Builder registers an app with Azure Active Directory at the request of Integration Manager. When you create a connection, Integration Manager requests Integration Builder to create and associate a certificate with this app, saving the certificate details in an encrypted way as part of the connection information.

### If you don't have administrator permissions in Azure Active Directory

Creating a connection without administrator credentials requires parameters from the Azure Active Directory platform. The Azure Active Directory account administrator needs to create a new Azure app to obtain these parameters.

Integration Builder can send an email to the administrator requesting the information you need. The email includes a unique authorization certificate, and [instructions on how the administrator proceeds](how-register-ib-ms-sp-dv-d360.md).

Once you receive the information, enter it into Integration Builder, and select **Create connection**.

### Editing a connection in Integration Manager

Each connection to Microsoft Dataverse you create in Integration Manager is tied to an application registered in Azure AD. To edit the connection, you must use a Microsoft account with access to Azure AD and authorize Integration Builder to connect on this user's behalf.

This authorization is only valid for a specific user. If another user wants to edit a connection or integration, they also need to authorize Integration Builder.

### Use the integration in Service Studio

For more information, see [how to use the integration in Service Studio](../use.md#use).
