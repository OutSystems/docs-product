---
summary: Learn how to allow developers in the team to create integrations with external databases.
locale: en-us
guid: 2bac9add-33d1-4240-8cc7-d23a897f0415
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing%20the%20Applications%20Lifecycle?node-id=267:84
---

# Allow Integrations With External Databases

In this example, we want to allow one developer in the team to [create integrations with external databases](../../integration-with-systems/external-database/connect-external-db.md). This developer must be able to publish extensions, through Integration Studio, that use specific database connections. However, the developer must not be able to change the settings of the database connections.

![Diagram illustrating the process of integrating with an external database](images/external-db-integration-diag.png "External Database Integration Diagram")

To do this:

1. [Create a new role](create-an-it-role.md#create-a-new-role) that has the permission level **Change and Deploy Applications**.  

    ![Screenshot showing the creation of a new IT role with Change and Deploy Applications permission](images/external-db-integration-new-role-lt.png "Creating a New IT Role")

1. [Set the developer's default role](create-an-it-role.md#set-the-user-default-role) to the new role. Make sure you edit the user and set the user's **Default Role**. Setting the **Change and Deploy** role to the user at the Application level can also be applied. Assigning the new role to the user in a team doesn't grant the necessary permissions.  

    ![Screenshot depicting how to set a developer's default role to a newly created IT role](images/external-db-integration-set-default-role-lt.png "Setting Developer's Default Role")

1. Go to the environment's Service Center console (`http://<your_environment>/ServiceCenter`) and select **Administration » Database Connections**.

1. Edit the database connection and grant the security level **Publish** to the role Integrator.  

    ![Screenshot of the Service Center console showing the security settings for a database connection](images/external-db-integration-connection-security-sc.png "Database Connection Security Settings")

Granting the security level **Publish** to the **Integrator** role on the database connection or setting the **Change and Deploy** role to the developer at the Application level and granting the security level **Publish** on the database connection, allows the developers assigned with these settings to publish extensions, through Integration Studio, that use this database connection. This security level doesn't allow the developers to change the settings of the database connection.

Other developers will then be able to use those extensions to access the data on the external database.

<div class="info" markdown="1">

Accessing the data on the external database through an extension requires that a user with the security level **Full Control** over the database connection [configures the extension in Service Center](../../integration-with-systems/external-database/connect-external-db.md#configure-the-extension-to-use-a-database-connection) to use the database connection.

</div>
