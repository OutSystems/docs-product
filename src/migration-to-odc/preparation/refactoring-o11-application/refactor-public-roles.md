---
summary: This article describes how to refactor from public roles in O11 to domain-specific roles in ODC.
guid: b81449f8-885f-4493-aaa9-289e8e56694a
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/daglmSUESdKw9J3HdT87a8/O11-to-ODC-migration?type=design&node-id=11%3A2&mode=design&t=blNAbpnofC4dwbOh-1
---

# Refactor public roles to be ODC-compatible

In O11, you can have public roles shared across domains. However, in ODC, public roles are not allowed.

![Diagram showing public roles shared across domains in O11](images/sharing-roles-across-domains-diag.png "Public Roles Across Domains")

This can cause issues when converting the horizontal domain with the foundation app to an ODC library since public roles are not allowed. To configure a public role in ODC, follow these steps:

1. Create a role in each vertical domain and ensure it's only consumed inside the domain.

    ![Diagram illustrating the creation of a role in each vertical domain for ODC](images/create-roles-in-domains-diag.png "Create Role in Each Domain")

1. Map your end users to both roles in the domain. For more information, refer to [End User Management](https://success.outsystems.com/documentation/outsystems_developer_cloud/user_management/roles/).
