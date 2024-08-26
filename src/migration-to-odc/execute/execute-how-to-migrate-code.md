---
summary: Learn how to migrate O11 code to ODC using the code migration tool.
tags: 
guid: 4748549a-2df3-4763-bcfc-73be131cf9ff
locale: en-us
app_type: mobile apps, reactive web apps, traditional web apps
platform-version: o11
figma: 
---

# Code migration using the tool

<div class="info" markdown="1">

This article only applies to customers with access to the Migration Kit.

</div>

This article explains how to migrate O11 code to ODC using the code migration tool available in the ODC portal.

## Prerequisites

Before you migrate your O11 code, do the following:

* [Map O11 apps to ODC apps](../plan/plan-map-apps.md) in the Assessment tool.

* [Identify and fix any issues highlighted in the Assessment Tool until all apps are marked as ](../prepare/prep-refactor-o11-apps.md) **Ready for ODC** status.

* [Tag O11 apps in LifeTime](execute-about-migrate-code.md#tagging-your-apps) after mapping the O11 apps to ODC in the Migration Assessment tool.

* [Connect to the Migration Assessment Tool](execute-connect-to-tool.md).

* Ensure you have the **O11 Migrations** > **Migrate O11 code** role in ODC.

## Code migration

To migrate O11 code to ODC, follow these steps:

1. Log into ODC portal.

1. Go to  **Migrate O11** >  **Code Migrations**.

1. Select the environment from where you want to migrate the O11 app.

1. Verify that the status of all O11 apps is **Ready for ODC**. If not, you must [modify and refactor your O11 implementation](../prepare/prep-refactor-o11-apps.md).

    You cannot migrate until the status of all apps is **Ready for ODC**.

1. Click **Migrate**.

    A list of O11 apps is displayed. You can click each app to review its corresponding modules and their revision number.

1. To confirm the migration, again Click **Migrate**.

    The migration process begins, and the status of apps moves to **Migrating**.

If the migration is successful, the process ends with **Finished** status. The O11 apps mapped in the Assessment tool are converted to ODC apps and libraries. These ODC apps and libraries are still **Unpublished**. 
Now, in ODC, you must [publish the ODC apps and libraries](#publish-odc-apps-and-libraries).

If the migration is unsuccessful, the process ends with a **Finished with errors** status. You cannot open the app or the library in the ODC Studio. 
Contact OutSystems support for guidelines on how to fix the errors and include the data and time the migration was started in your request.

### Publish ODC apps and libraries

The tool displays a list of apps and libraries, with producers at the top and consumers at the bottom. To prevent dependency errors in ODC, you must publish the apps and libraries in the order they appear.

To publish an ODC app or a library, follow these steps:

1. Select an app or library with the Unpublished status and click **Download** in the order as in the list. The file is downloaded to your local machine. 

1. Open the file in **ODC Studio**.

1. Select **App** > **Check for dependency updates**.

1. Modify the app or library until no TrueChange errors exist.

1. Publish the app or library to the target ODC stage.

1. If it's a Library, [release that library](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/libraries/#release-library). 

1. Repeat steps 1 to 6 until all apps and libraries are published in ODC.

## Next steps

* [Configure migrated apps](execute-configure-migrated-apps.md)
* [Adapt SQL queries](execute-adapt-sql-queries.md)
* [Adapt login flow](execute-adapt-login-flow.md)
