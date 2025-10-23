---
summary: Learn how to migrate O11 data and end users to ODC using the app conversion tool.
tags: data migration, app conversion, database queries, postgresql, user management
guid: 0ae16d20-7ffc-4894-9e95-254bd89c4353
locale: en-us
app_type: mobile apps, reactive web apps, traditional web apps
platform-version: o11
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - platform administrators
outsystems-tools:
  - odc portal
coverage-type:
  - apply
---

# Migrate data using the tool

<div class="info" markdown="1">

This article only applies to customers with access to the App Conversion Kit.

</div>

This article explains how to migrate O11 data and end users to ODC using the app conversion console available in the ODC portal.

## Prerequisites

Before you migrate the data and end users of the O11 apps in a [conversion plan](../plan/plan-define-migration-plans.md), ensure you:

* Have gained an understanding about [migrating end users](execute-about-migrate-data.md#end-users), and ensured the end users are [ready to migrate](execute-about-migrate-data.md#ready).

* In the Conversion Assessment Tool, solve all the findings related to [data patterns](../code-patterns/intro.md#data-patterns)

* [Converted the O11 apps code to ODC](execute-about-migrate-code.md).

* Modified your converted SQL queries on each converted ODC asset to ODC equivalent Aurora PostgreSQL queries. For detailed information, refer to [SQL queries compared to OutSystems 11](https://success.outsystems.com/documentation/outsystems_developer_cloud/onboarding_developers/sql_queries_compared_to_outsystems_11/).

* In ODC, have the **OutSystems 11** > **Migrate O11 data** permission for the target stage of the data migration.

## Data migration

To migrate O11 app data and end-users to ODC, follow these steps:

1. Log in to the ODC portal.

1. Under **OUTSYSTEMS 11**, click **App Conversion**.

1. Select the plan you want to migrate data for. The selected plan must have completed the code conversion.

1. To start a new data migration, click **Migrate data**.

1. Select the **Migration type**. App downtime depends on the [type of data migration](execute-about-migrate-data.md#types-of-migration) that you choose.

1. Select the **O11** source environment to migrate data from.

1. Select the **ODC** target stage to migrate the data to.

1. Click **Continue**.

1. Confirm that the data migration setup details are correct.

1. Click **Migrate data**.

The data migration begins, and you can view the following details as the migration runs in the background:

* Migration logs as the data migration occurs.

* The total number of migrated entities.

* The time elapsed since the migration started.

Once the migration is complete, you can view a list of migrated entities for every ODC app.

<div class="info" markdown=1>

If you selected the **Production final** data migration type with app downtime, but you still want your end users to keep using any of the O11 apps after the data migration concludes, you must enable those apps in the Service Center console.

</div>
