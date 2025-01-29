---
summary: Manage roles effectively in OutSystems platform by understanding the differences between O11 and ODC and ensuring proper role configuration to avoid migration issues.
locale: en-us
guid: 4751d001-d519-4214-ae71-bec2e5b72f24
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/design/daglmSUESdKw9J3HdT87a8/O11-to-ODC-migration?node-id=2350-7746
helpids: 30528
tags: role management, code migration, access control, user permissions, odc
audience:
  - full stack developers
  - frontend developers
  - mobile developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
  - understand
---
# Asset consuming a Role

In ODC, Assets can't have dependencies to Roles from other Assets.
This means that each App must define its own Roles and can't share them with other Apps.

<div class="info" markdown="1">

Public roles are available in ODC since November 2024. OutSystems is working on updating this documentation page. 

</div>

## How to solve

You must solve this pattern in O11, before proceeding with the code migration to ODC.

### Solve in O11

In O11, you can have public roles shared across domains. However, in ODC, public roles are not allowed.

![Diagram showing public roles shared across domains in O11](images/sharing-roles-across-domains-diag.png "Public Roles Across Domains")

This can cause issues when converting the horizontal domain with the foundation app to an ODC library since public roles are not allowed. To configure a public role in ODC, follow these steps:

1. Create a role in each vertical domain and ensure it's only consumed inside the domain.

    ![Diagram illustrating the creation of a role in each vertical domain for ODC](images/create-roles-in-domains-diag.png "Create Role in Each Domain")

1. Map your end users to both roles in the domain. For more information, refer to [End User Management](https://success.outsystems.com/documentation/outsystems_developer_cloud/user_management/roles/).
