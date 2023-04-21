---
summary: Create IT users for new developers and operators that will operate the platform.
locale: en-us
guid: 67304326-4018-4f4c-88c7-8e5034fe9ce5
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Create an IT User

OutSystems allows you to manage IT users like developers, testers, and operators.

When adding a new user they must be given a username to log into the platform. This username is their own unique identifier. 

For example, a new developer just joined the company. To create the new IT user, follow these steps:

1. In your LifeTime console (`https://<lifetime_env>/lifetime`), go to the **USER MANAGEMENT** area.

1. Choose **USERS** and click the **New User** link.

1. Complete the form with the user’s information. 

    You must set the **Default Role** of the user. Afterward, you can grant the user with additional permissions through teams or for specific applications. While selecting the user's **Default Role**, you get a preview of the default permissions that will be granted to the user by assigning that role.  

    **Note**: The password must meet the password complexity rules. It must have at least 12 characters including at least one number, one lowercase letter, and one uppercase letter. The password complexity rule is applicable only when a new password is created or an existing password is updated.

    ![](images/user-create-lt.png)

1. Click the **Create** button to create the user.

The user is now created. You can grant the user with **additional permissions** by assigning roles to the user [in teams](about-permission-levels.md#role-assigned-to-users-for-a-team) or [for specific applications](about-permission-levels.md#role-assigned-to-users-for-a-specific-application):

![](images/user-grant-additional-permissions.png)

Check the OutSystems [permission model for IT users](about-permission-levels.md) to better understand which should be the user’s default role and how can you grant the user with additional permissions.

## Centralized user management

LifeTime console (`https://<lifetime_env>/lifetime`) is the master of data for IT users and ensures that every user has the same credentials in all environments that are registered in LifeTime. When you register an environment in LifeTime, from that moment on you will not be able to change the accounts of IT users in the Service Center of that environment.

When you create or update an IT user account in LifeTime, the user's credentials will be updated in LifeTime's database and that change is also propagated to all registered environments. This behavior is also enforced by LifeTime's synchronization process.
