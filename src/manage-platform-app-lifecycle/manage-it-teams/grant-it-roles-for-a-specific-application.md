---
summary: Learn how to grant specific application permissions in OutSystems 11 (O11) for enhanced monitoring without module access.
locale: en-us
guid: 00796575-6a6e-40dc-a4a8-88ff5d4a549a
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing%20the%20Applications%20Lifecycle?node-id=267:68
tags: permissions management, application lifecycle management, user roles, business user enablement, monitoring applications
audience:
  - platform administrators
  - business analysts
  - full stack developers
outsystems-tools:
  - lifetime
  - service studio
coverage-type:
  - understand
  - apply
topic:
  - assign-a-role-for-an-app
---

# Grant Permissions for Specific Applications

In enterprise scenarios, there is often the need to grant more granular permissions over specific applications.

In this example we want to allow a business user to **monitor** the applications Mobile Banking and Fleet Management in LifeTime Analytics, but **without granting permissions to open** the modules in those applications.

![Diagram showing how to grant role permissions for specific application teams](images/grant-role-for-app-teams-diag.png "Team Permissions Diagram")

To do this, configure the business user:

1. [Create a new role](create-an-it-role.md#create-a-new-role) called Business Monitoring that has the permission level **Monitor and Add Dependencies**. This permission level allows users to monitor applications without granting access to opening the modules of those applications.  

    ![Screenshot of creating a new role called Business Monitoring in LifeTime](images/grant-role-for-app-new-role-lt.png "Creating a New Role in LifeTime")

1. Go to the user detail screen of the business user and [assign the role](create-an-it-role.md#assign-a-role-to-a-user-for-a-specific-application) Business Monitoring to the applications Mobile Banking and Fleet Management.  

    ![Screenshot of assigning the Business Monitoring role to a user for Mobile Banking and Fleet Management applications](images/grant-role-for-app-assign-role-lt.png "Assigning a Role to a User")

Checking the [permissions of the business user](find-out-the-permissions-of-it-users.md#permissions-of-a-specific-IT-user), you can see that the user has **Monitor and Add Dependencies** permission over Fleet Management and Mobile Banking applications, but no access over any other application in the environment.

![Screenshot showing the permissions of a business user with Monitor and Add Dependencies permission over Fleet Management and Mobile Banking applications](images/grant-role-for-app-check-permission-lt.png "Checking User Permissions")
