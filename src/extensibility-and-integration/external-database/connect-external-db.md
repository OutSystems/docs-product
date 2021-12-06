---
summary: OutSystems allows you to define connections to your existing SQL Server, Azure Server, Oracle or MySQL databases and use data in those databases using visual objects in Service Studio.
tags: support-application_development; support-Database; support-Integrations_Extensions; support-database-overview; support-Integrations_Extensions-featured
---

# Integrate with an External Database using Integration Studio

OutSystems integrates with your existing databases. This allows you to develop applications that access data on external databases using OutSystems entities in Service Studio and without having to worry about data migration. For a list of supported external database engines and their supported versions check the [System Requirements](../../getting-started/system-requirements.md#integration-with-external-systems).

<div class="info" markdown="1">
 
When you are done developing your integration with an external database and you want to deploy the application to another Environment (e.g. quality assurance environment) check out [this step by step guide](../../managing-the-applications-lifecycle/deploy-applications/deploy-an-app-externaldb.md).

</div>


The creation of an integration with an external database involves the following general steps:

1. In Service Center, define a connection to the external database.
1. In Integration Studio, create an extension module to map tables or views in the external database to OutSystems entities.
1. In Service Center, configure the extension to use a database connection.
1. In Service Studio, reference and use the extension in your application.

The following sections go throught each one of these general steps in detail.

## Define a Connection to the External Database

To use tables and views from external databases, create a database connection: 

1. Open the **Service Center** management console of your OutSystems environment.

    ![](images/connect-external-db-0.png?width=800)

    Tip: Open Service Center directly from Service Studio by clicking **Environment Management...**.

1. On the **Administration** tab, select **Database Connections**.

    ![](images/connect-external-db-new-connection-sc.png?width=1000)

1. Click **New Database Connection** and fill in the fields to set up the connection to the external database.

    ![](images/connect-external-db-create-connection-sc.png?width=1000)

    If you need to fine-tune the database connection, choose the option **Advanced configuration**. This allows you to define your own connection string.

1. Click **Test Connection** to check if the connection is working correctly.

    <div class="info" markdown="1">

    The database user must have permissions to:

    * List the necessary tables and views on the external database.
    * Perform the operations Create, Read, Update, and Delete on those tables and views.

    </div>

1. Click **Create** to create the Database Connection.

## Map Tables or Views to Entities in an Extension Module

After configuring a database connection in Service Center, use Integration Studio to create an extension that maps the tables or views in the external database to OutSystems entities:

1. Go back to **Service Studio**, open your Application, select **New Module** and create a new **Extension** Module.

    ![](images/connect-external-db-03.png?width=800)

1. In **Integration Studio**, **Connect** to your environment.

    ![](images/connect-external-db-003.png?width=400)

1. Right-click the **Entities** folder in the Extension Tree and select **Connect to External Table or View...**.

    ![](images/connect-external-db-3.png?width=1000)

1. Follow the steps of the wizard.

    ![](images/connect-external-db-4.png?width=600)
    
    <div class="info" markdown="1">

    Make sure that you: 
    
    * Select the database connection configured previously.
    * Select the necessary tables and views.
    * Define a logical database name that you will use to connect the extension to a physical database connection in the next section.

    </div>

1. After closing the wizard, review the imported entity names, descriptions and data types for each attribute.

1. Select **1-Click Publish** to publish the Extension Module.

    After publishing the extension, OutSystems warns you that you still need to configure which database connection the extension will use.

1. In the **1-Click Publish** summary window, select the **Missing Configuration** warning and then select **Configure**.

    ![](images/connect-external-db-5.png?width=600)  

## Configure the Extension to Use a Database Connection

After mapping the tables or views, use Service Center to configure which database connection the extension will use:

1. In **Service Center**, make sure you are in the **Operation** tab of **Factory** > **Extensions** > **&lt;your extension name&gt;**.

1. Associate the logical database name of the extension to the database connection that the extension will use in runtime.

    ![](images/connect-external-db-configure-extension-sc.png?width=1000)

In some cases you need to select the database based on runtime data. Typically, the applicable databases share the same schema but they contain different data.

In these scenarios, you can use the action [DatabaseConnection_SetConnectionStringForSession](<../../ref/apis/auto/platformruntime-api.final.md#DatabaseConnection_SetConnectionStringForSession>) of the [PlatformRuntime API](<../../ref/apis/auto/platformruntime-api.final.md>).


## Use the Extension in your application

The Extension is now ready to be used in OutSystems applications:

1. In your application, click **Manage Dependencies...**.

1. Add a dependency to the Extension and select the Entities that you will use in your application.  

    ![](images/connect-external-db-7.png?width=600)

You can now use the entities of the extension to manipulate data on the external databases just like you do with the standard OutSystems entities.
