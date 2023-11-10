---
tags: Case Management; Case Management framework; Access control; CMf; AC;
summary: Learn how to grant access to a case instance to a user or a group of users.
guid: 7409d714-7beb-4222-acc6-9310bba1477a
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# How to grant access to a case instance to a user

After [enabling access control for a case definition](how-enable-ac.md), you can grant access to all cases of that case definition.
Grating access to a case instance means that access is granted to all existing and future case instances of that case definition.
Use this options in situations where a user or a group of users, who deal with a specific type of case should have access by default to all existing and future case instances of that case definition.

## Grant a user access to a case definition

To grant a user access to a case definition, follow these steps:

1. In a Server Action flow, add the **CaseDefinition_GrantAccessToUser** action.

1. In the property pane of the **CaseDefinition_GrantAccessToUser** action, set **CaseDefinitionId** as the GUID of the case definition.

1. Set **UserId** as the user identifier of the user. You can find out the user identifier in the  **User** entity of the **(System)** producer.

1. If you want the user to have write permissions for the case definition, set **HasWritePermission** as `True`. Otherwise, leave the field empty or set it as `False`.

1. Publish the module by selecting **1-Click Publish**.

## Grant a group access to a case definition

To grant a group access to a case definition, follow these steps:

1. In a Server Action flow, add the **CaseDefinition_GrantAccessToGroup** action.

1. In the property pane of the **CaseDefinition_GrantAccessToGroup** action, set **CaseDefinitionId** as the GUID of the case definition.

1. Set **GroupId** as the user identifier of the group. You can find out the user identifier in the **Group** entity of the **(System)** producer.

1. If you want the user to have write permissions for the case definition, set **HasWritePermission** as `True`. Otherwise, leave the field empty or set it as `False`.

1. Publish the module by selecting **1-Click Publish**.
