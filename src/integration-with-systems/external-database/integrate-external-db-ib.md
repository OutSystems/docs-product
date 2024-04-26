---
summary: Integrating your applications with external databases using Integration Builder
tags:
locale: en-us
guid: fcc67384-67da-41a3-b52b-e2491db85b0c
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/jSgZ0l0unYdVymLxKZasno/Extensibility%20and%20Integration?node-id=1208:5983
---

# Integrate with an external database using Integration Builder

You can use Integration Builder to integrate your apps with the following external databases:

* Relational databases:

    * DB2 iSeries
    * PostgreSQL, Aurora PostgreSQL and Azure PostgreSQL
    * MySQL
    * Oracle
    * Azure SQL and SQL Server

* Non-relational databases:

    * MongoDB

<div class="info" markdown="1">

For more information about the supported databases and the systems that are certified to integrate with OutSystems, see [Integration with external systems in the system requirements article](../../setup-infra-platform/setup/system-requirements.md).

</div>

Once you establish a database connection, you can develop apps in Service Studio that query and aggregate data that resides in the external database. Your app can create, read, update, and delete data from the external database.

## Prerequisites

* Depending on the external database you want to integrate with, your environments must use the following Platform Server versions:

    * For integrations with MongoDB your environments must use Platform Server 11.7.2 or later.
    * For integrations with DB2 iSeries, MySQL, Oracle, Azure SQL, and SQL Server, you need Platform Server 11.14.0 or later.
    * For integrations with PostgreSQL, Aurora PostgreSQL and Azure PostgreSQL you need Platform Server 11.15.0 or later.

* All infrastructure servers must be able to connect to the external database.

* If you use the [Internal Network configuration](../../security/configure-internal-network.md), you must add the [Integration Builder IPs](../../setup-infra-platform/setup/network-requirements.md#integration-builder).

## Known limitations

* Previous external database extensions created in Integration Studio cannot be edited in Integration Builder.

* External database extensions created in Integration Builder cannot be edited in Integration Studio.

* An external database integration created in Integration Builder only supports one database, catalog, or schema at a time. If you require various tables or collections from different databases, catalogs, or schemas, you must create several integrations.

* It's not possible to define the following fields at attribute level: data types, length, mandatory, autonumber, delete rule, and description.

* It's not possible to manually define identifiers.

## Process overview

To integrate with an external database using Integration Builder, follow these steps:

1. Log into Integration Builder using your development environment URL and your IT user credentials (username and password).

1. Create a new integration for an external system and configure its settings.

1. Select a connection or create a new one to allow your integration to access the data in your external database.

1. Select tables or collections you want the integration to consume.

1. Publish the integration to your environment.

1. Use the integration in your application.

    ![Flowchart illustrating the process of integrating with an external database using Integration Builder](images/integrate-external-db-process-diag.png "Integration Builder Process Overview")

Previous integrations created in Integration Studio must be maintained and evolved in Integration Studio. Integration Builder cannot maintain those integrations. For new integrations, use Integration Builder.

## How to integrate with an external database

### Log into Integration Builder

1. Open Integration Builder, available at [https://integrationbuilder.outsystems.com](https://integrationbuilder.outsystems.com).

1. In the **Environment** field, enter the address of your OutSystems development environment and click **Next**.

    ![Screenshot of the Integration Builder login page with fields for environment URL and user credentials](images/login-ib.png "Login to Integration Builder")

    **Note**: For security and governance reasons, you can only connect to a **development** environment. Once Integration Builder publishes the integration, it is available for you to use in the environment you enter on the login page.

1. Enter your username and password and click **Log in**.

### Create a new integration

1. On the **My integrations** screen, click **Create integration**.

    ![Screenshot highlighting the 'Create integration' button in Integration Builder](images/create-integration-ib.png "Create Integration Button")

1. Choose a provider.

    ![Screenshot displaying the step of choosing a provider in Integration Builder](images/choose-provider-ib.png "Choose a Provider")

1. If you are creating an integration with a relational database and using a Personal Environment, validate your credentials and click **Confirm**.

    ![Screenshot showing the credentials validation step in Integration Builder for relational database integration](images/validate-credentials-ib.png "Validate Credentials")

1. If you are creating a MongoDB integration, and don't have Integration Manager MongoDB plugin installed, Integration Builder let's you know. Install the plugin by selecting **Install MongoDB plugin**, and after the plugin is installed, click **Next**.

1. Follow the wizard steps to configure the integration.

### Connect integration

You can connect an integration in the following ways:

* [**Use an existing connection**](#option-1): If you already have a database connection, you can **select a connection** from the list of available connections.

* [**Create a new connection**](#option-2): If you need a new database connection and you meet one of the following scenarios, you can **create a connection**:

    * You're integrating with a relational database and you have the required [permissions](../../manage-platform-app-lifecycle/manage-it-teams/about-permission-levels.md).

    * You're integrating with MongoDB.

* [**Request a new connection 3**](#option-3): If you need a new connection to a relational database but don't have the required permissions, you can **request a new connection**. This option is only available for integrations with relational databases.

#### Use an existing connection { #option-1 }

If the database connection you want to use already exists, do the following:

1. Select a connection, click **Next**, and then continue with [selecting a database](#select-database).

    **Note**: The list of connections only displays connections that you have permissions to view. To select a connection from the list, you must have **Full Control** permissions.

    ![Screenshot depicting the selection of a database connection in Integration Builder](images/select-connection-ib.png "Select a Connection")

#### Create a new connection { #option-2 }

If you meet one of the following scenarios, you can **create a connection**:

* You're integrating with a relational database and you have the required [permissions](../../manage-platform-app-lifecycle/manage-it-teams/about-permission-levels.md).

* You're integrating with MongoDB.

Create a new connection by following these steps:

1. Click **+ Create a connection**.

    ![Screenshot illustrating the option to create a new database connection in Service Studio via Integration Builder](images/create-ss-connection-ib.png "Create a Connection in Service Studio")

1. Enter the mandatory details, test your connection, and finally click **Create connection**.

    <div class="info" markdown="1">

    If you are creating a connection to an external Oracle database which NLS_LANGUAGE parameter is different from `AMERICAN`, make sure you set the **NLS_LANGUAGE** field to the same value set in the database. This will prevent runtime issues related to date and number formats.

    To get the value of the NLS_LANGUAGE parameter set in your external Oracle database you can run the following script:
        `select value from nls_database_parameters where parameter = 'NLS_LANGUAGE';`

    </div>

    <div class="info" markdown="1">

    For integrations with relational databases and if your environment uses Platform Server version 11.14.0 or earlier, click **Create in Service Center** and follow [this procedure](connect-external-db.md#define-connection) to create the database connection in Service Center.

    **Note:** By default, SQL Server/Azure SQL is selected in the DBMS dropdown. Don’t forget to select the correct database.

    After you create the database connection, return to Integration Builder.

    </div>

1. Select the new integration, click **Next**, and continue with [selecting tables or collections](#select-database).

#### Request a new connection { #option-3 }

<div class="info" markdown="1">

This options is only available for integrations with relational databases.

</div>

1. If your credentials don't allow you to create a connection, you can request your OutSystems Administrator to create it by clicking **Send request by email**.

    ![Screenshot showing the option to send a request for a new database connection via email in Integration Builder](images/send-request-ib.png "Request a New Connection")

1. Enter all connection details to allow an OutSystem Administrator to create the connection and click **Send email**.

    ![Screenshot of the interface for sending an email request for a new database connection in Integration Builder](images/send-request-email-ib.png "Send Request Email")

    When your request is approved it will appear in your connection list in Integration Builder.

1. Go back to Integration Builder, select a connection, click **Next**, and then continue with [selecting a database](#select-database).

### Select tables or collections

Depending on the database type, follow the steps for [relational databases](#rel-db) or the steps for [MongoDB](#non-rel-db).

#### Integration with a relational database { #rel-db }

If you are integrating with DB2 iSeries, PostgreSQL, Aurora PostgreSQL, MySQL, Oracle, Azure SQL, or SQL Server, follow these steps:

1. Select the database, catalog, or schema, to consume with the integration and click **Next**.

    ![Screenshot showing the step of selecting a database, catalog, or schema in Integration Builder](images/select-database-ib.png "Select Database")

1. Select the tables to consume with the integration and click **Next**.

    To view the attributes of a table, select the relevant table.

    ![Screenshot displaying the interface for adding tables to an integration in Integration Builder](images/add-tables-ib.png "Add Tables to Integration")

When you publish the integration, the selected tables are represented as entities in Service Studio.
You can select more tables later on by editing the published integration in Integration Builder.

After these steps, [review and publish your integration](#review).

#### Integration with MongoDB { #non-rel-db }

If you are integrating with MongoDB, follow these steps:

1. Select the collections to consume with the integration.

1. For each collection to consume, set the following fields:

    * In the **Access Type**, to only allow reading data and prevent writing data for that collection, set the **Read-only** checkbox for the given collection.

    * In **Format**, set the output format of the collection to one of the following:

        * **Structure** - The content of the documents in that collection are represented as Structures. OutSystems generate each Structure based on the document's structure. This means that in Service Studio, the data type of Input and Output Parameters of the generated Server Actions are set to the relevant Structures. Furthemore, you don't need to serialize and deserialize JSON data.

        * **JSON** - The content of the documents in that collection are represented in JSON format. This means that in Service Studio, the Input and Output Parameters of the generated Server Action will be in JSON format (text type). You can serialize and deserialize the JSON from and to OutSystems Structures. Those Structures are not generated by Integration Builder, and you must created them.

1. For collections with **Format** set as **Structure**, de-select the fields you don't want to use in your integration.

    <div class="info" markdown="1">

    After selecting Structure, you see the structure of the selected collection. Fields are displayed in the right side of the screen and are presented with the same hierarchy as in the database.

    By default, Integration Builder generates the structure by looking at the five most recent documents available in the collection. You can change the sample selecting **Most recent** or **Evenly spread**, changing the number of documents to be analyzed, and then selecting **Update structure**.

    When a field has different data types in different documents, Integration Builder can’t determine the final data type to show in the structure. In this case, the field is unselectable. If you need that field in your integration, you must use the JSON format for that collection.

    Structure format isn't available for empty collections.

    </div>



1. Click **Next**.

<div class="info" markdown="1">

Once you select a collection, the **Access Type** option appears. To only allow reading data and prevent writing data for that collection, select the **Read-only** checkbox for the given collection.

</div>

After this step, [review and publish your integration](#review).

### Review integration and publish { #review }

1. Review the integration information, update it if necessary.

1. If you are creating an integration with a relational database, ensure you have selected the correct **Default value behavior** (by default **Overwrite database NULLs** is selected).

    The following are the options for null and default values:

    * Overwrite database NULLs - Always writes platform default values to the database. Database NULLs are read as platform default values.

    * Preserve database NULLs - Always write Integration Builder default values as database NULL. Database NULLs are read as Integration Builder default values.

    ![Screenshot showing the default value behavior options during the review of an integration in Integration Builder](images/review-default-values-ib.png "Review Default Value Behavior Option")

    For more information about default values, see [Platform and Integration Builder default values](#platform-and-integration-builder-default-values).

1. Click **Publish**.

After the integration is published in your environment, you can [use it in your OutSystems applications](#use).

#### Platform and Integration Builder default values

To help you decide which default behavior is best for your new integration with a relational database, the following table outlines the differences between the default values for the platform and Integration Builder.

|Type | Platform default value | Integration Builder default value |
|---|---|---|
|Binary Data|Byte array with no elements|Byte array with no elements|N/A|
|Boolean|False|False|
|Currency|0.0|N/A|
|Date|#1900-01-01#|#1900-01-01#|
|Time|#00:00:00#|#00:00:00#|#12:20:56#|
|Date Time|#1900-01-01 00:00:00#|#1900-01-01 00:00:00#|
|Integer|0|-1999999991|
|Long Integer|0|-8999999999999998|
|Decimal|0.0|99999993.14159356|
|Email|"" (empty string)|`"<ib>NULL</ib>"`|
|Phone Number|"" (empty string)|`"<ib>NULL</ib>"`|
|Text|"" (empty string)|`"<ib>NULL</ib>"`|

### Structure of generated integrations

For integrations with external databases, Integration Builder generates and publishes integrations, which are OutSystems applications composed of two modules:

* An extension that exposes Entities with Entity actions to interact with external databases. By default, the extension name has a "_DRV" suffix, meaning "Driver".
* One service module that's used to register the integration in Integration Manager. It's an internal module that is required for Integration Builder to work. It's protected to prevent changes. By default, the module name has a "_IS" suffix, meaning "Integration Service".

### Use the integration in your application { #use }

Depending on the type of database you integrated with, follow the steps on one of the following sections.

#### Integration with a relational database

1. In your application, go to **Module** -> **Manage Dependencies**.

1. Add a dependency to the integration, select the entities you want to use in your application, and click **Apply**.

    ![Screenshot demonstrating how to add a dependency to an integration in OutSystems Service Studio](images/add-dependency-ss.png "Add Dependency in Service Studio")

    You can now use the entities of the integration to manipulate data on the external databases just like you do with the standard OutSystems entities.

#### Integration with MongoDB

1. In your application, go to **Module** -> **Manage Dependencies**.

1. Select the integration, then select the server actions you want to use in your application, and finally select **Apply**.

You can now use the Server Actions of the integration to show and manipulate data from the MongoDB database.
To learn more about how to use MongoDB integration in your apps, check the [this article](mongo-db.md).
