---
summary: Learn how to connect to the Migration Assessment Tool before migrating yourr O11 apps and data to ODC
tags: 
guid: a4a2aea6-eee3-4224-8f6f-8f84da3057b2
locale: en-us
app_type: mobile apps, reactive web apps, traditional web apps
platform-version: o11
figma: https://www.figma.com/design/daglmSUESdKw9J3HdT87a8/O11-to-ODC-migration?node-id=2114-1320
---

# Connect to Migration Assessment Tool

<div class="info" markdown="1">

This article only applies to customers with access to the Migration Kit.

</div>

Before you can start migrating your O11 apps and data to ODC, you must connect to the Migration Assessment Tool. By doing this, the apps and data you've mapped in the Migration Assessment Tool are available to migrate to ODC.

## Prerequisites

* You must have the **O11 Migrations** > **Manage migrations** role.

* [Migration Assessment Tool has been set up in O11](../setup-assessement-tool.md).

## Connect to Migration Assessment Tool

![Diagram showing the current connect to migration assessment tool step in the migration process](images/execute-connect-to-tool-diag.png "Connect to Migration Assessment Tool")

To connect to the Migration Assessment Tool, follow these steps:

1. Log into ODC Portal.

1. Go to **Migrate O11** > **Configurations**.

1. Click **Configure migrations**.

1. Enter the following Migration Assessment Tool values:

    * **URL**:  The LifeTime environment URL of where you installed the Migration Assessment Tool engine.

    * **Auth Token**:  LifeTime  Service Account authentication token.

      **Note**: The Service Account must have the Administrator role. For more information about understanding the permission model in OutSystems, refer to [Roles](../../manage-platform-app-lifecycle/manage-it-teams/about-permission-levels.md#roles).

    For more information about the Migration Assessment Tool and these values, refer to [Set up the Migration Assessment Tool](../setup-assessement-tool.md).

1. Click **Save**

## Troubleshooting

You can export logs from the Migration Assessment Tool. Go to **Maintenance** > **View troubleshoot** > select **Export**.

## Next steps

* Ensure the IT user migrating the code has the **O11 Migrations** > **Migrate O11 code** role.

* [Migrate code](execute-how-to-migrate-code.md).
