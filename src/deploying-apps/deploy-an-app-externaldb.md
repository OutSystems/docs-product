---
summary: Learn how to deploy your integration with an external database from your Development environment to another environment.
tags: 
locale: en-us
guid: 33c27796-6e3d-4507-bdd3-27cc71036ee5
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing%20the%20Applications%20Lifecycle?node-id=257:74
---

# Deploy an Integration With an External Database

Follow the steps in this guide to deploy an application with a connection to an external database from an OutSystems environment (in this case, the Development environment) to the next environment (in this case, the Quality environment).

Use this guide after you [created the integration with the external database](../../extensibility-and-integration/external-database/connect-external-db.md) in your Development environment and if your application needs to connect to a different external database in each environment.

<div class="info" markdown="1">

**Before you begin following this step by step guide, make sure that:**

* Your infrastructure uses **LifeTime 11.4.2** or later.
* Both the source and target environments use **Platform Server 11 Release Jul.2019 CP1** or later.
* You have **Change & Deploy Applications** permission for the applications that you want to deploy.
* You created the **Extension** that integrates with an external database while connected to an environment running **Platform Server 11 Release Jul.2019 CP1** or later.  
Otherwise, republish the Extension in Integration Studio while connected to an environment running **Platform Server 11 Release Jul.2019 CP1** or later.

</div>

## Define a Database Connection in the Quality environment

In the Quality environment, define a Database Connection:

1. Open the **Service Center** management console of your **Quality environment**.

1. On the **Administration** tab, select **Database Connections**.

    ![Screenshot of the Service Center Administration tab with Database Connections selected](images/ext-db-05.png "Service Center Administration Tab")

1. Click **New Database Connection** and fill in the fields to set up the connection to the external database.

    ![Form for creating a new database connection in the Service Center](images/ext-db-06.png "New Database Connection Form")

    If you need to fine-tune the database connection, choose the option **Advanced configuration**. This allows you to define your own connection string.

    <div class="info" markdown="1">

    If you are defining a connection to an external Oracle database which NLS_LANGUAGE parameter is different from `AMERICAN`, make sure you set the **NLS_LANGUAGE** field to the same value set in the database. This will prevent runtime issues related to date and number formats.

    To get the value of the NLS_LANGUAGE parameter set in your external Oracle database you can run the following script:
        `select value from nls_database_parameters where parameter = 'NLS_LANGUAGE';`

    </div>

1. Click **Test** to check if the connection is working correctly.

    <div class="info" markdown="1">

    The database user must have permissions to:

    * List the necessary tables and views in the external database.
    * Perform the operations Create, Read, Update, and Delete on those tables and views.

    </div>

1. Click **Create** to create the Database Connection.

## Deploy the application to the Quality environment

To deploy the application to the Quality environment follow these steps:

1. Open LifeTime for your Infrastructure.

    ![LifeTime management console interface showing the option to manage all environments](images/ext-db-07.png "LifeTime Management Console")

    Tip: Open LifeTime directly from Service Center by clicking **Manage all environments**.

1. Select the **Applications** tab and select the **DEPLOY...** button between the Development environment and the Quality environment.

    ![DEPLOY button highlighted between Development and Quality environments in LifeTime](images/ext-db-08.png "Deploy Button in LifeTime")

1. Select **Add Applications** and, in the **Choose one or more Applications** dialog, select your application and select **Add to Deployment Plan**.

    ![Dialog for adding applications to the deployment plan in LifeTime](images/ext-db-09.png "Add Applications to Deployment Plan")

1. Select the **VALIDATE NOW** button between the Development environment and the Quality environment.

    ![VALIDATE NOW button highlighted between Development and Quality environments in LifeTime](images/ext-db-10-ea.png "Validate Deployment in LifeTime")

1. Select the **CONTINUE** button between the Development environment and the Quality environment.

    ![CONTINUE button highlighted between Development and Quality environments in LifeTime](images/ext-db-11-ea.png "Continue Deployment in LifeTime")

1. Verify the deployment plan, select **Deploy Now** and then in the **Deploy applications as planned** dialog select **Deploy Now** to start the deployment.

    ![Deploy Now dialog in LifeTime with the Deploy Now button to start the deployment](images/ext-db-12.png "Deploy Now Dialog in LifeTime")

1. In the **Configure applications settings** step, enter the three-part **Physical Table Name** of each external database Entity. Make sure you enter the correct **Physical Table Name** for the target environment.

    ![Configure applications settings step showing fields for entering the Physical Table Name](images/ext-db-16-ea.png "Configure Application Settings")

    <div class="info" markdown="1">

    If your application connects to the same external database/schema for both your environments, select **Copy from Source** to copy the **Physical Table Name** from the source environment.

    </div>

1. After the deployment stops, click the **configuration or confirmation** link in the warning banner to open Service Center and map the database name of the extension to the database connection.

    ![Warning banner with a configuration or confirmation link after deployment in LifeTime](images/ext-db-13-ea.png "Post-Deployment Configuration Link")

1. Associate the logical database name of the extension to the Database Connection that you created previously.

    ![Service Center interface for associating the logical database name of the extension to the Database Connection](images/ext-db-14.png "Associate Logical Database Name")

After the Deployment finishes your Extension is ready to be used by other applications in the Quality environment.

![Confirmation that the extension is ready to be used in the Quality environment](images/ext-db-15.png "Extension Ready in Quality Environment")
