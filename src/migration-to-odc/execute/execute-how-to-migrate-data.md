---
summary: Learn how to migrate O11 data and end users to ODC using the data  migration tool.
tags: 
guid: 0ae16d20-7ffc-4894-9e95-254bd89c4353
locale: en-us
app_type: mobile apps, reactive web apps, traditional web apps
platform-version: o11
figma: 
---

# Migrate data using the tool

<div class="info" markdown="1">

This article only applies to customers with access to the Migration Kit.

</div>

This article explains how to use the data migration tool in the ODC portal to migrate the O11 application data and end-users to ODC.

## Prerequisites

Before migrating O11 application data and end users, ensure you:

* Have gained an understanding [About migrating end users](execute-about-migrate-data.md), and have done the following:

    * [In O11, validate end user emails](execute-about-migrate-data.md#validate-end-user-emails)

    * (Optional) [In O11, create and populate user extension table](execute-about-migrate-data.md#create-and-populate-user-extension-table). In ODC, by default the user table consists of Id, Name, Email, and PhotoUrl. You can skip this section if you don't want to migrate any additional user details

* [Migrate O11 code to ODC](execute-how-to-migrate-code.md).

* Modify your converted SQL queries on each migrated ODC asset to ODC equivalent Aurora PostgreSQL queries. For detailed information, refer to  [SQL queries compared to OutSystems 11](https://success.outsystems.com/documentation/outsystems_developer_cloud/onboarding_developers/sql_queries_compared_to_outsystems_11/).

## Data migration

To migrate O11 app data and end-users to ODC, follow these steps:

1. Login to the ODC portal.

1. Under **Migrate O11**, click **Data migration**.

    A list of data migrations is displayed.

1. To start a new data migration, click **Migrate data**.

1. On the Migration setup page, do the following:

    1. Select the O11 source environment to migrate data from.

    1. Select whether you want to stop or not stop your O11 environment:
    
        * **Stop environment** makes the source O11 environment inaccessible to developers and makes all apps in that environment inaccessible to end users. This prevents changes to the app data while the environment is stopped. After the data migration ends, the environment isn't automatically restarted. This option increases the duration of the data migration.

            <div class="warning" markdown="1">

            This option leads to downtime, during which **all O11 apps in the source O11 environment can't be accessed**. The downtime lasts until you [restart the O11 environment](https://success.outsystems.com/support/troubleshooting/infrastructure_management/restart_services_on_outsystems_cloud/).

            This option is only recommended in case you are doing your last data migration, to the Production stage, right before sunsetting your O11 app.
            As such, after the data migration ends, the O11 environment isn't automatically restarted.

            </div>

        * **Keep environment running** keeps the O11 environment running. This means that O11 apps are available to developers and end users during the data migration and they may use the app to change data. These changes aren't migrated if they are done during the data migration.

    1. Select the ODC target stage to migrate the data.

        A list of all code-migrated ODC apps with entities, including **Unpublished** apps, is displayed.  

        You can migrate data only when all apps are published and deployed to the target ODC stage.

    1. Select whether you want to undeploy your ODC apps or keep them deployed and available on the target stage:

        * **Undeploy apps** makes the ODC apps in the target stage inaccessible to end users. This prevents changes to the app data while they are undeployed. This option increases the duration of the data migration.

            <div class="warning" markdown="1">

            The option leads to downtime, during which the mapped ODC apps in the target stage are undeployed. The downtime is dependent on the size of the database.

            </div>

        * **Keep apps deployed** keeps the apps deployed in the target ODC stage. This means users can change app data during the migration. These data changes may be lost after the data migration finishes.

1. Click **Continue**.

1. Confirm that the data migration setup details are correct.

1. Click **Migrate data**.

1. The data migration begins, and you can view the following details as the migration runs in the background:

   * Migration logs as the data migration occurs.

   * The total number of migrated entities.

   * Time elapsed since the migration started.

Once the migration is complete, you can view a list of migrated entities for every ODC app.

<div class="info" markdown=1>

If you selected the **Stop environment** option for your source O11 environment, and you still want your end users to keep using any of the O11 apps in that O11 environment, [restart the O11 environment](https://success.outsystems.com/support/troubleshooting/infrastructure_management/restart_services_on_outsystems_cloud/).

</div>
