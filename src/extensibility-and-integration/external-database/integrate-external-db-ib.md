---
summary: Integrating your applications with external databases using Integration Builder
tags: external database; integration builder
---

# Technical Preview - Integrate with an external database using Integration Builder 

You can integrate your applications with external databases including DB2 iSeries, MySQL, Oracle, Azure SQL, and SQL Server using Integration Builder. Once you establish a database connection, you can develop apps in Service Studio that query and aggregate data that resides in the external database. Your app can extract, load, transform, and update data from the external database.

For more information about the supported databases and the systems that are certified to integrate with OutSystems, see [Integration with external systems](../../setup/system-requirements.md).

## Prerequisites

Platform Server 11.14.0 or later

## Known limitations 

* Previous external database extensions created in Integration Studio can not be edited in Integration Builder.

* External database extensions created in Integration Builder can not be edited in Integration Studio.

* An external database integration created in Integration Builder only supports one database at a time. If you require various tables from different databases, you must create several integrations.

* It is not possible to define the following fields at attribute level: data types, length, ignore, mandatory, autonumber, delete rule, and description. 

* It is not possible to rename entities.

<div class="info" markdown="1">

**Note**: If you use the Internal Network configuration in the Configuration tool, you must add the Integration Builder IPs or the SIPO IPs in the case that SIPO is already live.

</div>

## Process overview

To integrate with an external database using Integration Builder:

1. Log into Integration Builder with your development environment URL, your username and password.

1. Create a new integration for an external system and configure its settings.

1. Select a connection or create a new one to allow your integration to access the data in your external database.

1. Select a database and the tables you want the integration to consume.

1. Publish the integration to your environment.

1. Use the integration in your application.

    ![integrating with an external database using Integration Builder process overview](<images/integrate-external-db-process-diag.png>)

Previous integrations created in Integration Studio must be maintained and evolved in Integration Studio. Integration Builder cannot maintain those integrations. For new integrations, use Integration Builder.

To establish communication between external databases and Integration Builder, it is not required to have Integration Builder directly connected to your external database. However, Service Center must be connected to your external database.

## How to integrate with an external database

The following steps are an example of an integration with MySQL.

### Log into Integration Builder

1. Open Integration Builder, available at https://integrationbuilder.outsystems.com.

1. In the **Environment** field, enter the address of your OutSystems development environment and click **Next**.

   ![Log into Integration Builder](<images/login-ib.png>)

    For security and governance reasons, you can only connect to a development environment. Once Integration Builder publishes the integration, it is available for you to use in the environment you enter on the login page.

1. Enter your username and password and click **Log in**.

  ![Enter username and password](<images/login-user-ib.png>)

### Create a new integration

1. On the **My integrations** screen, click **Create integration**.

   ![Click Create integration button](<images/create-integration-ib.png>)

1. Choose a provider.

   ![Choose a provider](<images/choose-provider-ib.png>)

1. Validate your credentials and click **Confirm**. 

    **Note:** This step only occurs if you are using a personal environment. 

   ![Validate your credentials](<images/validate-credentials-ib.png>)

1. Follow the wizard steps to configure the integration. 

### Connect integration

You can connect an integration in the following ways:

* [**Option 1**](#option-1): If you already have a database connection, you can **select a connection** from the list of available connections.

* [**Option 2**](#option-2): If you need a new database connection and have the required [permissions](../../managing-the-applications-lifecycle/manage-it-teams/about-permission-levels.md), you can **create a new connection**.

* [**Option 3**](#option-3): If you need a new connection but don't have the required permissions, you can **request a new connection**. 

**Option 1**

1. Select a connection, click **Next**, and then continue with with [selecting a database](#select-database).

    **Note**: The list of connections only displays the connections you have permissions to view.
    
    ![Select a connection](<images/select-connection-ib.png>) 

**Option 2**

1. Click **+ Create a connection**.

1. Click **Create connection in Service Center**. 

    ![Create a connection in Service Studio](<images/create-connection-ib.png>)

1. In Service Center, enter the mandatory details and click **Create**.

    ![Create a database connection in Service Center](<images/create-db-connection-sc.png>)

    When the database is created, it appears in your connection list in Integration Builder. 

1. Go back to Integration Builder, select a connection, click **Next**, and then continue with [selecting a database](#select-database).

**Option 3**

1. If your credentials do not allow you to create a connection, you can request your OutSystems Administrator to create it by clicking **Request a new connection**.

    ![Request a new connection](<images/create-connection-ib.png>)
 
 1. Enter all connection details to allow an OutSystem Administrator to create the connection and click **Send request**.

    ![Send Request](<images/send-request-new-db-ib.png>)

    When your request is approved it will appear in your connection list in Integration Builder. 

1. Go back to Integration Builder, select a connection, click **Next**, and then continue with [selecting a database](#select-database).

### Select database

1. Select the database to consume with the integration and click **Next**.

    ![Select database](<images/select-database-ib.png>)

### Add tables

1. Select the tables to consume with the integration and click **Next**.
    
    To view the attributes of a table, select the relevant table. 

    When you publish the integration, these tables are represented as entities in Service Studio.

     ![Add tables](<images/add-tables-ib.png>)

   **Note:** You can select more tables later on by editing the published integration in Integration Builder.

### Review integration and publish

1. Review the integration information, update if necessary, and click **Publish**.

    The published integration is now available in your environment and ready to be used in your OutSystems applications. 

    ![Add tables](<images/review-integration-ib.png>)

### Use the integration in your application

1. In your application, go to **Module** -> **Manage Dependencies**.

1. Add a dependency to the integration and select the entities you want to use in your application.

    ![Add dependency](<images/add-dep-ss.png>)

    You can now use the entities of the integration to manipulate data on the external databases just like you do with the standard OutSystems entities.

## Null and default values

When creating an external database integration, you can select one of the following options for null and default values:

* Overwrite database NULLs 

* Preserve database NULLs 

    ![Review null and default value behaviors](<images/review-default-values-ib.png>)

### Entity properties

|**Property** | **Description** |  **Optionality** | **Default value** |
|---|---|---|---|
|Null and default values|<ul><li>Overwrite database NULLs: Always write platform default values to the database. Database NULLs are read as platform default values.</li><li>Preserve database NULLs: Always write platform default values as database NULL. Database NULLs are read as Integration Builder default values.</li></ul>|Mandatory|Overwrite database NULLs|

### Integration Builder default values

|**Type** | **Platform default value** |  **Integration Builder default value** | **Example** |
|---|---|---|---|
|Binary Data|Byte array with no elements|Byte array with no elements|N/A|
|Boolean|False|False|True or Flase|
|Currency|0.0|0.0|545870.025|
|Date|#1900-01-01#|#1900-01-01#|#1988-08-28#|
|Time|#00:00:00#|#00:00:00#|#12:20:56#|
|Date Time|#1900-01-01 00:00:00#|#1900-01-01 00:00:00#|#1988-08-28 23:59:59#|
|Integer|0|-1999999991|2147483600|
|Long Integer|0|0|5645245584135987412|
|Decimal|0.0|<ib>NULL</ib>|-158121.025|4000.0|
|Email|"" (empty string)|<ib>NULL</ib>|"fran.wilson@company.com"|
|Phone Number|"" (empty string)|<ib>NULL</ib>|"+1 555 565 3730"|
|Text|"" (empty string)|<ib>NULL</ib>|"My name is Christina Sharp."|
|<Entity> Identifier|When an Entity is created, the <Entity> identifier data type is created for the identifier attribute.|---|---|

For more information about integrating with external databases, see [Integrating OutSystems with your ecosystem](https://success.outsystems.com/Support/Enterprise_Customers/Integrating_OutSystems_with_your_ecosystem).
