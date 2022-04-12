---
tags: Case Management; Case Management framework;
summary: Learn about extended groups for case management apps.
guid: d8d7450e-afb2-4019-95a2-92ffc7a31acf
locale: en-us
---

# Groups for case management apps

During the lifecycle of a case, several groups of users can interact with the case.
You can define groups of users with the Case Management framework by using the **GroupExtended** entity.

The **GroupExtended** entity is an extension to the Group system entity that in conjunction with the CaseServices_API’s methods allows you to assign activities in your cases to specific groups of users and also manage case permissions around groups. The GroupExtended entity also allows you to define hierarchies between groups (using the ParentId attribute) and assign working days to a group of users (using CalendarId attribute to reference an existing calendar).

## Set up the extended case management groups

Before you start make sure you [set up your app to work with the Case Management framework](bootstrap-app.md).

Before using groups in your case management app, follow these steps:

1. In the **&lt;app-name&gt;_Configuration** module, open  **Manage Dependencies**, and add the **GroupExtended_CreateOrUpdate** action from the **CaseConfigurations_API** producer.

1. In the **Data** tab, create a static entity and name it `GroupExtendedConfiguration`.

1. Set the **Public** property to **Yes**.

1. Delete the **Label** and **Order** attributes.

1. Change data type of **Id** to **Text**.

1. Add the following attributes:

    * `Name`, text data type with length set to 100. Set description as `Name of the group in GroupExtended entity.`.

    * `SystemName`, text data type with length set to 100. Set description as `Name of the group in the Group system entity.`.
    * `Description`, text data type with length set to 500. Set the description as `Description of the group in Group entity and GroupExtended entity.`.

1. In the **Processes** tab, add a new timer and name it `Bootstrap_Groups`.

1. Set the **Schedule** property of the timer as **When Published**.

1. In the **Action** property of the new timer, select **New Server Action**.

1. In the action flow, add an aggregate that fetches all records in **GroupExtendedConfiguration** by dragging the **GroupExtendedConfiguration** static entity between the Start and End.

1. After the aggregate created in the previous steps, add a **For Each**.

1. Set the **Record List** of the **For Each** as `GetGroupExtendedConfigurations.List` (the output list of the aggregate).

1. Add [**GroupExtended_CreateOrUpdate**](ref/auto/CaseConfigurations_API.final.md#GroupExtended_CreateOrUpdate) action next to the **For Each**.

1. Connect the **For Each** to the **GroupExtended_CreateOrUpdate**, and then connect the **GroupExtended_CreateOrUpdate** to the **For Each**.

1. Set the **GroupExtendedRec** of the **GroupExtended_CreateOrUpdate** as `GetGroupExtendedConfigurations.List.Current.GroupExtendedConfiguration`.

1. Set the inputs of the action with the data from the aggregate:

    * Set **Id** as `TextToIdentifier(Id)`.

    * Set **IsActive** as `Is_Active`.

    <div class="info" markdown="1">

    Ensure the following mapping is set:
        
    * **Name** = `Name`
    * **SystemName** = `SystemName`
    * **Description** = `Description`

    </div>

1. Publish the module by selecting **1-Click Publish**.

## Add a group to your case management app

After Set up the extended case management groups, add a group to your case management app by following these steps:

1. In the **&lt;app-name&gt;_Configuration** module, add a record to the **GroupExtendedConfiguration** static entity.

1. Set the **Identifier** attribute with text that represents the role.

1. Generate a GUID and paste that GUID into the value field of the **Id** attribute of the record.

    <div class="info" markdown="1">

    A Globally Unique IDentifier, or GUID, is used as a unique identifier to ensure integrity across environments.%%
    You can use an online GUID generator to create a GUID for each record.

    Check the [RFC 4122](https://www.ietf.org/rfc/rfc4122.txt) for more information on GUIDs.

    </div>

1. Set the remaining attributes.

1. Publish the module by selecting **1-Click Publish**.

After these steps the new group is created in the **Group** and **GroupExtended** entities.

