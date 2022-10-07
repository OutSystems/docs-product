---
tags: Case Management; Case Management framework; Access control; CMf; AC;
summary: After enabling access control for a case definition, you can grant access to specific case instances of that case definition. Learn how to grant or remove access to a case instance for a user or a group of users.
guid: a2fd36f7-6635-4e07-a09e-a46b2e64987b
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
---

# How to grant or revoke access to a case instance

After [enabling access control for a case definition](how-enable-ac.md), you can grant access to a single case instances of that case definition.

Use this options in situations where a user or a group of users, should have access to a specific case instances of a case definition.

## Grant a user access to a case instance

To grant a user access to a case instance, follow these steps:

1. In a Server Action flow, add the **Case_GrantAccessToUser** action.

1. In the property pane of the **Case_GrantAccessToUser** action, set **CaseId** as the identifier of the case instance.

1. Set **UserId** as the user identifier of the user. You can find out the user identifier in the  **User** entity of the **(System)** producer.

1. If you want the user to have write permissions for the case definition, set **HasWritePermission** as `True`. Otherwise, leave the field empty or set it as `False`.

1. Publish the module by selecting **1-Click Publish**.

## Grant a group access to a case instance

To grant a group access to a case instance, follow these steps:

1. In a Server Action flow, add the **Case_GrantAccessToGroup** action.

1. In the property pane of the **Case_GrantAccessToGroup** action, set **CaseId** as the identifier of the case instance.

1. Set **GroupId** as the user identifier of the group. You can find out the user identifier in the **Group** entity of the **(System)** producer.

1. If you want the user to have write permissions for the case definition, set **HasWritePermission** as `True`. Otherwise, leave the field empty or set it as `False`.

1. Publish the module by selecting **1-Click Publish**.
