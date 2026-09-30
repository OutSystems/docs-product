---
summary: Learn how to migrate O11 data and end users to ODC using the app conversion tool.
guid: 0ae16d20-7ffc-4894-9e95-254bd89c4353
locale: en-us
app_type: mobile apps, reactive web apps, traditional web apps
tags:
  - Data
  - End-users
platform-version: o11
figma:
audience:
  - Developer
  - Platform administrator
outsystems-tools:
  - odc portal
coverage-type:
  - apply
topic:
  - cancel-data-migration
  - execute-data-migration
isautopublish: true
---

# Migrate data using the tool

This article explains how to migrate O11 data and end users to ODC using the app conversion console available in the ODC Portal.

## Prerequisites

Before you migrate the data and end users of the O11 apps in a [conversion plan](https://www.outsystems.com/tk/redirect?g=ab447daa-dffc-4374-8ae6-986c8f3d63c4), ensure you:

* Have a valid infrastructure setup for data migration. For further details, see the [app conversion limitations](execute-intro.md#limitations).

* [Converted the O11 apps code to ODC](execute-how-to-migrate-code.md).

    * If the converted apps were modified in O11 after the code conversion, make sure you run a new [code conversion](execute-how-to-migrate-code.md) before proceeding with the data migration.

* [Adjusted the code](execute-adjust-converted-code.md) of the converted apps and libraries, and [published them in the ODC target stage](execute-how-to-migrate-code.md#publish).

* In ODC, have the **App conversion** > **Migrate O11 data** permission for the target stage of the data migration.

* Have gained an understanding about [migrating end users](execute-about-migrate-data.md#end-users). If you are performing the end-user migration, ensure the end users are [ready to migrate](execute-about-migrate-data.md#ready).

* Don't have invalid data patterns in the O11 source environment:<!--TODO: Replace links with relative path-->

    * [Text data type record exceeding 100 000 000 characters](https://www.outsystems.com/tk/redirect?g=c488d2e0-29de-4728-a770-3a31006d7e59)
    * [Binary data record exceeding 20 MB](https://www.outsystems.com/tk/redirect?g=61073980-baa9-4391-93f5-921d5ca0517a)
    * [Module with a user provider different than Users](https://www.outsystems.com/tk/redirect?g=a38b687f-5515-4cb5-a12d-85a7662a8c22)
    * [Module with data in multiple tenants](https://www.outsystems.com/tk/redirect?g=10a12023-68a5-44db-bc0d-c13a8fc2b05a)

## Data migration

To migrate O11 app data and end-users to ODC, follow these steps:

1. Log in to the **ODC Portal**.

1. Under the **Management** menu, go to **OUTSYSTEMS 11 > App Conversion**.

1. Select the plan you want to migrate data for. The selected plan must have completed the code conversion.

1. To start a new data migration, click **Migrate data**.

1. Select the **Migration type**. App downtime depends on the [type of data migration](execute-about-migrate-data.md#types-of-migration) that you choose.

1. Select the **O11** source environment to migrate data from.

1. Select the **ODC** target stage to migrate the data to.

1. If you are performing a **Non-Production** migration and you want to [skip the end-user migration](execute-about-migrate-data.md#skip-end-users), make sure you clear the **Migrate end users** checkbox on the **End-User Migration** section. Keep the checkbox selected to perform the end-user migration.

    <div class="info" markdown="1">

    You can't skip the end-user migration when performing a **Test production** or **Production final** migration.

    </div>

1. Click **Continue**.

1. Confirm that the data migration setup details are correct.

1. Click **Migrate data**.

The data migration begins, and you can view the following details as the migration runs in the background:

* Migration logs as the data migration occurs.

* The total number of migrated entities.

* The time elapsed since the migration started.

Once the migration is complete, you can view a list of migrated entities for every ODC app.

<div class="info" markdown="1">

If you selected the **Production final** data migration type with app downtime, but you still want your end users to keep using any of the O11 apps after the data migration concludes, you must enable those apps in the Service Center console.

</div>

If the data migration fails with a data model inconsistency error, refer to [Troubleshooting data migration issues](execute-troubleshooting.md#data-issues).

### Cancel a data migration {#cancel-migration}

If you need to cancel a data migration for a plan while it's still running, follow these steps:

1. In the ODC Portal **Management** menu, go to **OUTSYSTEMS 11 > App Conversion**.

1. Select the plan with the running data migration that you want to cancel.

1. Click the running data migration row to open the process details for that migration.

1. Click **Cancel migration** and confirm the operation.

After you cancel the migration, verify application data and end-user state in ODC. For more information, refer to [Canceling a data migration](execute-about-migrate-data.md#cancel-migration).

If you need to run a new data migration, ensure the [needed prerequisites](#prerequisites) and fix any underlying issue in O11 before you start.
