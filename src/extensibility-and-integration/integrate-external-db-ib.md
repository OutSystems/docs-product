---
summary: 
tags: 
---

# Integrate with an external database using Integration Builder (Technical Review)

You can integrate your applications  with external databases including DB2 iSeries, MySQL, Oracle, Azure SQL, and SQL Server using Integration Builder. Once you establish a database connection, you can develop apps in Service Studio that query and aggregate data that resides in the external database. Your app can extract, load, transform, and update data from the external database.

For more information about the supported databases and the systems that are certified to integrate with OutSystems, see [Integration with external systems.](../setup/system-requirements.md)

To integrate with an external database using Integration Builder:

1. Log into Integration Builder with your development environment URL and your username and password.

1. Create a new integration for an external system and configure its settings.

1. Select a connection or create a new one to allow your integration to access the data in your external database.

1. Select a database and the tables you want the integration to consume.

1. Publish the integration to your environment.

1. Use the integration in your application.

## How to integrate with an external database

### Log into Integration Builder

1. Open Integration Builder, available at https://integrationbuilder.outsystems.com.

1. In the **Environment** field, enter the address of your OutSystems development environment and click **Next**.

For security and governance reasons, you can only connect to a development environment. Once Integration Builder publishes the integration, it is available for you to use in the environment you enter on the login page.

1. Enter your username and password and click **Log in**.

### Create a new integration

1. On the **My integrations** screen, click **Create integration**.

1. Choose a provider.

1. Validate your credentials and click **Confirm**. 

    Note: This step only occurs if you are using a personal environment. 

1. Follow the wizard steps to configure the integration. 

    <ul><li>Connect integration</li>
    <li>Select database</li>
    <li>Add tables</li>
    <li>Review integration</li>
    <li>Publish</li></ul>

The following steps are an example of an  integration with MySQL:

### Connect integration

1. Select a connection and click **Next**.

    **Note**: The list of connections only displays  the connections you have permissions to view.

    Alternatively, you can create a new connection. To do this:

    a. Click **+ Create a connection**.

    b. Click **Create connection in Service Center**.

    c. In Service Center, enter the mandatory details and click **Create**.

    d. Go back to Integration Builder and continue with step 1.

### Select database

1. Select the database to consume with the integration and click **Next**.

### Add tables

1. Select the tables to consume with the integration and click Next.
When you publish the integration, these tables are represented as entities in Service Studio.

   **Note:** You can select more tables later on by editing the published integration in Integration Builder.

    To view the attributes of a table, select the relevant table. 

### Review integration and publish

1. Review the integration information, update if necessary, and click **Publish**.

    The published integration is now available in your environment and ready to be used in your OutSystems applications. 

### Use the integration in your application

1. In your application, go to **Module** -> **Manage Dependencies**.

1. Add a dependency to the integration and select the entities you want to use in your application.

    You can now use the entities of the integration to manipulate data on the external databases just like you do with the standard OutSystems entities.

For more information about integrating with external databases, see [Integrating OutSystems with your ecosystem](https://success.outsystems.com/Support/Enterprise_Customers/Integrating_OutSystems_with_your_ecosystem).
