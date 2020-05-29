---
summary: Learn how to allow developers in the team to create integrations with external databases.
---

# Allow Integrations With External Databases

In this example, we want to allow one developer in the team to [create integrations with external databases](../../extensibility-and-integration/connect-external-db.md). This developer must be able to publish extensions, through Integration Studio, that use specific database connections. However, the developer must not be able to change the settings of the database connections.

![](images/external-db-integration-diag.png?width=400)

To do this:

1. [Create a new role](create-an-it-role.md#create-a-new-role) that has the permission level **Change and Deploy Applications**.  

    ![](images/external-db-integration-new-role-lt.png?width=500)

1. [Set the developer's default role](create-an-it-role.md#set-the-user-default-role) to the new role.  

    ![](images/external-db-integration-set-default-role-lt.png?width=500)

1. Go to the environment's Service Center console (`http://<your_environment>/ServiceCenter`) and select **Administration » Database Connections**.

1. Edit the database connection and grant the security level **Publish** to the role Integrator.  

    ![](images/external-db-integration-connection-security-sc.png?width=600)

This way, the developers assigned with the Integrator role as Default Role will be able to publish extensions, through Integration Studio, that use this database connection. However, other developers will only be able to use those extensions to access data on the external database after a user with the security level **Full Control** over the database connection [configures the extensions in Service Center](../../extensibility-and-integration/connect-external-db.md#configure-the-extension-to-use-a-database-connection) to use the database connection.
