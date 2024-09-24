---
summary: Learn more about how you can migrate your O11 application data and end-users to ODC 
tags: 
guid: 8073a9f1-f82c-4c11-991f-248ae59b09a9
locale: en-us
app_type: mobile apps, reactive web apps, traditional web apps
platform-version: o11
figma: https://www.figma.com/design/daglmSUESdKw9J3HdT87a8/O11-to-ODC-migration?node-id=2148-27
---

# Migrate data

<div class="info" markdown="1">

This article only applies to customers with access to the Migration Kit. 

</div>

![Diagram showing the current migrate data step in the migration process](images/execute-migrate-data-diag.png "Migrate data")

After migrating the O11 code to ODC and publishing the ODC apps and libraries in the ODC target stage, you are ready to migrate the O11 app data and end users to ODC.

<div class="info" markdown="1">

You can migrate only data stored within the O11 platform to ODC. If you are using external databases, you must configure the external database connection in ODC. 

</div>

The data migration scope includes the following:

* The entire volume of data within all entities of mapped O11 apps in the Assessment Tool.
* End users in the User table with valid and unique emails set on the email field, including active and inactive users.

You can perform data migration multiple times at each stage. However, each time you migrate the O11 data, it overwrites the existing app data in ODC. For end users, the migration doesn't overwrite existing users in ODC; it updates them instead.

On successful data migration:

* The ODC apps can use the migrated app data without further adjustments.
* The end users can log in to the ODC app using their existing O11 email address. However, they must first set a new password.

## Preventing data changes during migration

When starting a data migration, you can choose to enforce downtime in your O11 and ODC apps to ensure data consistency by preventing changes to data while the migration runs.

These options lead to downtime and increase the duration of the data migration process. Use them only on your last data migration to the production stage when you are ready to sunset your O11 apps.

### Stop O11 source environment

Stop environment makes the source O11 environment inaccessible to developers and makes all apps in that environment inaccessible to end users. Stopping the environment prevents changes to the app data. This option increases the duration of the data migration.

<div class="warning" markdown="1">

This option means **all O11 apps in the source O11 environment can't be accessed**, whether they're part of the migration or not.

</div>

After the data migration ends, the environment isn't automatically restarted, so the downtime lasts until you [restart the O11 environment](https://success.outsystems.com/support/troubleshooting/infrastructure_management/restart_services_on_outsystems_cloud/).

### Undeploy ODC apps

Undeploy apps makes the ODC apps (mapped in the Migration Aseessment Tool) in the target ODC stage inaccessible to end users. Undeploying the apps prevents changes to the app data. This option increases the duration of the data migration.

## About migrating end users

The migration process includes end users along with app data, from the source O11 environment to the target ODC stage.

In O11, you can authenticate end users either using an external identity provider (IdP) or built-in authentication.

In O11, with built-in authentication, the end users login with any username and password. The username in O11 can be a name, an acronym, or an email address. However in ODC, the end users can login only with their email address. During data migration, only the end users' email addresses are migrated to ODC. Due to security reasons, their passwords are not migrated. Therefore, the end user must set a new password and then use their email address instead of their O11 username to login to the ODC app.

### How are users and roles migrated

When you migrate end users to ODC, you also migrate their roles with permissions and access levels. The end users are assigned the same roles they had in O11. However, if you migrate data from a different environment later, the roles of the  existing end users in ODC are updated to match those from the new environment.

The migration of the group roles from O11 to ODC is not supported.

When setting up user groups, create them manually in ODC and add the roles migrated from O11. You can manage roles in ODC Portal > **End-user groups**. For more information, see [Roles in ODC](https://success.outsystems.com/documentation/outsystems_developer_cloud/user_management/roles/).

### Getting ready to migrate end users

![A diagram about migrating end users](images/migrate-end-user-diag.png "Migrating end users")

To ensure your end users are properly migrated during the data migration process, follow these steps:

1. If you are using built-in authentication, ensure your [O11 end users have emails that have been validated](#validate-end-user-emails). You can skip this step if you use an external IdP to authenticate users in O11.
1. If you use fields that aren't available in the ODC users table, [create a new user extension table ](#create-and-populate-user-extension-table)to store these additional user details you want to migrate to ODC.

For detailed information about how to migrate end users using the data migration tool, refer to [Migrate data using the tool](execute-how-to-migrate-data.md)

#### Validate end user emails

To migrate end users from a source O11 environment, ensure the following:

* All end users in that O11 environment have an email address defined.
* The end user's email address is valid. Since OutSystems does not migrate passwords for security reasons, users need a valid email to receive password reset instructions after their first login. If any email addresses are invalid, update or remove them in the Users app.
* All end users have a unique email address since in ODC an end user's email address is used to login to ODC app.  

To check if all end users have email addresses defined, follow these steps:

1. In the Users app, export your end users to an Excel file.
1. Filter the Excel file to find users without emails.
1. In the Users app, modify emails or deactivate users without emails.

#### Create and populate user extension table

In ODC, by default the user table consists of **Id**, **Name**, **Email**, and **PhotoUrl**. In O11, the end user table includes extra fields.

You can skip this section if you don't want to migrate any additional user details from O11 to ODC.

To migrate additional user details such as MobilePhone, CreationDate, follow these steps:

1. Create a new user extension table in O11. OutSystems recommends creating a dedicated app to hold the user extension table.
1. Expose the user extension table for read and write operations using Service or Server actions.
1. Populate the user extension table with data from the O11 Users table.
1. [Map the app](../plan/plan-map-apps.md) that holds the user extension table in the assessment tool and migrate it to ODC.

OutSystems recommends creating the following new field in the user extension table:

* **Is_Active**: This boolean or other data type field checks if the user can request the password reset mechanism on the ODC side. Inactive users cannot reset their passwords. This field is useful since, unlike the usual ODC behavior, migrated O11 inactive users still appear in the ODC Users table.

![A screenshot about creating the UserExtend table in O11](images/user-extend-table.png "UserExtend table creation")

## Next step

[Migrate data using the tool](execute-how-to-migrate-data.md)
