---
guid: b7c5599e-6bc0-40db-83d9-6d5557a601fc
locale: en-us
summary: This article provides guidelines for refactoring built-in functions usage to ensure compatibility with OutSystems Developer Cloud (ODC).
figma: 
coverage-type:
  - unblock
  - understand
topic: 
app_type: mobile apps,reactive web apps
platform-version: o11
audience:
  - frontend developers
  - full stack developers
  - mobile developers
tags: cloud-native applications,system entities,api development,data integration,platform version
outsystems-tools:
  - service studio
helpids: 30630
---

# Asset using unsupported O11 built-in function

Most of the [O11 built-in functions](../../ref/lang/auto/builtinfunctions.md) are available in ODC, however there are some functions that don't work with the cloud-native architecture of ODC.

## How to solve

You must solve this pattern in ODC, after proceeding with the code conversion to ODC.

### Solve in ODC

Depending on the scenario, do one of the following:

* If the built-in function functionality can be [achieved with a manual transformation](#manual-transformation), implement the changes in your ODC assets.

* If the built-in function functionality is [incompatible with ODC architecture](#incompatible), rethink your use case considering ODC architecture.

## Built-in functions changes in ODC { #changes }

This section describes the built-in functions that changed in ODC due to its different architecture when compared to O11.

### Built-in functions that require manual transformation { #manual-transformation }

The following lists the built-in functions that don't exist in ODC, but you can apply manual transformations to keep the logic working.

The information is divided by category and lists the action name and the manual transformation that can be applied.

#### Email

* **EmailAddressConcatenate:** Similar to the concatenation but with a different format, that includes name and e-mail.

#### Miscellaneous

* **Generate Password:** Use the new function called **GenerateSecurePassword**. For detailed information, refer to GenerateSecurePassword.
* **GetUserId:** In ODC, the Users table has changed, and the UserID is a text (Guid) and not an integer. Therefore, you must review all use cases where you have used GetUserId and UserId and change the data type. For example, if you have assigned User ID to an integer local variable now you modify it to text.
Roles
* **CheckRoles:** On creating a role, the corresponding server and client actions are created. Since there isn't a generic CheckRole, you must replace it with the function of that specific role.

#### Environment

* **GetExceptionURL:**  This action is typically used in the Logout flow. You must delete it manually.

### Built-in functions incompatible with ODC architecture { #incompatible }

The following lists built-in functions that you can't apply manual transformations to because they are incompatible with ODC architecture. You must revisit your code and adapt it to ODC architecture.

#### Built in functions not supported inside aggregates

The following list provides information on built-in functions that are still available in ODC but can't be used inside aggregates to filter attributes in entities. They aren't supported inside aggregate, such as when used to compute information of an entity attribute. For example, it's not possible to do `Round(Entity1.Attribute1)`.

The information is divided by category and lists the action name that can't be used inside an aggregate.

##### Date Time

The following list provides information on built-in actions in the Date Time category that can't be used inside aggregates.

* BuildDateTime
* NewDate
* NewDateTime
* NewTime

##### Text

Under the **Text** category, you can't use the **Replace** built-in function inside an aggregate.

##### Math

Under the **Math** category, you can't use the **Round** built-in function inside an aggregate.

#### Built-in functions not available in ODC

Following are built-in functions that are no longer available in ODC. You must revisit your code and delete these built-in functions. The information is divided by category and lists the action name and why they can't be transformed.

##### Environment

The following list provides information on built-in actions in the environment category that aren't available in ODC. You can't apply manual transformations.

* **GetApplicationServerType:** This function was used in O10 or earlier to check whether the server was .NET or Java but the server type in ODC is always the same. So this action is not necessary.
* **GetDatabaseProvider:** In ODC, the DB engine is always Aurora Postgres so this function is no longer required.
* **GetEntryEspaceId:** In ODC, apps are run in containers so this function is not needed.
* **GetObsoleteTenantId:** ODC doesn't support multi-tenant applications so this function is not needed.
* **GetOwnerEspaceIdentifier:** ODC doesn't have system tables so this function is not needed.

##### URL

The following list provides information on built-in actions in the URL category that aren't available in ODC. However, you can't apply manual transformations.

* **AddPersonalAreaToURLPath:** ODC doesn't support personal areas.
* **GetPersonalAreaName:** ODC doesn't support personal areas.
