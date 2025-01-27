---
summary: Explore role creation and assignment features in OutSystems 11 (O11) for enhanced IT user management and security policy customization.
locale: en-us
guid: 23c1ff9e-cfa0-4efc-9406-f7bec7187f24
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing%20the%20Applications%20Lifecycle?node-id=267:29
tags: user management, security policy, it user permissions, roles and permissions, environment configuration
audience:
  - platform administrators
  - full stack developers
outsystems-tools:
  - lifetime
coverage-type:
  - apply
---

# Create and Assign Roles

OutSystems has two built-in roles that allow you to implement a simple security policy - **Developer** and **Administrator**.

However, if you need a more granular policy, you can [create additional roles](#create-a-new-role) to [assign to your IT users](#assign-roles-to-users).

Check the [permission model for IT users](about-permission-levels.md) to better understand how the different roles assigned to a user define the user’s permissions over the environments and the applications.

## Create a new role

To create a new role, do the following:

1. In your LifeTime console (`https://<lifetime_env>/lifetime`), go to the **USER MANAGEMENT** area.

1. Choose **ROLES** and click the **New Role** link.  

    ![Screenshot of the LifeTime console showing the process of creating a new role in the USER MANAGEMENT area.](images/roles-create-new-lt.png "Creating a New Role in LifeTime Console")

1. Fill in the Role Name.

1. Define the permissions that the new role will have over each environment:

    * Move the slider to choose the permission level over the environment and applications.

    ![Image depicting the slider interface for setting permission levels for a new role in the LifeTime console.](images/roles-permission-levels-lt.png "Setting Permission Levels for a New Role")

    * Set the toggle to define the specific permissions for the environment’s applications.

    ![Screenshot showing the toggle switches for defining specific permissions for applications within an environment in the LifeTime console.](images/roles-specific-permissions-lt.png "Defining Specific Permissions for a New Role")

    * Set the toggle to define the infrastructure-wide permissions.

    ![Image displaying the toggle switches for setting infrastructure-wide permissions for a new role in the LifeTime console.](images/roles-infra-wide-permissions-lt.png "Setting Infrastructure-wide Permissions")

1. Click the **SAVE** button to create the role.

When you change the permissions of an existing role, LifeTime will propagate those changes asynchronously to the registered environments.

## Assign roles to users

You can assign **roles** to **users** in three different ways:

* [Set the user’s default role](#set-the-user-default-role)
* [Assign a role to a user in a team](#assign-a-role-to-a-user-in-a-team)
* [Assign a role to a user for specific applications](#assign-a-role-to-a-user-for-a-specific-application)

### Set the user default role

You set the Default Role of a user when [creating the user](create-an-it-user.md):

![Screenshot of the LifeTime console interface for creating a new user and setting their default role.](images/roles-create-user-lt.png "Creating a User and Setting Default Role")

At any time, you can change the default role of the user in the user’s details page:

1. In the **USER MANAGEMENT** area, choose **USERS**.

1. Find the user you want to change from the list of users and click the Name of the user to go to the details page.

1. Change the user's Default Role in the Role dropdown.  

    ![Image showing the dropdown menu for changing a user's default role in the LifeTime console.](images/roles-default-role-lt.png "Changing a User's Default Role")

The change will be immediately saved.

### Assign a role to a user in a team

You specify the role of users in a team when you [add the users to the team](create-an-it-team.md#add-it-users-to-the-team):

![Screenshot illustrating the process of granting a role to a user within a team in the LifeTime console.](images/roles-grant-in-team-lt.png "Granting a Role to a User in a Team")

You can change the role of a user in the team either in the team’s screen or in the user's detail screen:

![Image showing the interface for updating a user's role in a team in the LifeTime console.](images/roles-update-in-team-lt.png "Updating a User's Role in a Team")

The change will be immediately saved.

### Assign a role to a user for a specific application

To assign a role to a user for a specific application, do the following:

1. In the **USER MANAGEMENT** area, choose **USERS**.

1. Find the user you want from the list of users and click the Name of the user to go to the details page.

1. Click the **Grant Role in Applications** link.  

    ![Screenshot highlighting the 'Grant Role in Applications' link in the LifeTime console's USER MANAGEMENT area.](images/roles-grant-in-app-link-lt.png "Granting Role in Applications Link")

1. Choose the Role and the applications you want the user to have that role.  

    ![Image showing the interface for assigning a role to a user for specific applications in the LifeTime console.](images/roles-grant-in-app-lt.png "Assigning a Role to a User for Specific Applications")

1. Click the **Grant Role in Applications** button.

To change the role that a user has over a specific application, change the role directly in the user’s screen. The change will be immediately saved:

![Screenshot of the LifeTime console where a user's role for a specific application can be changed.](images/roles-update-in-app-lt.png "Changing a User's Role for a Specific Application")

To revoke the role that a user has over a specific application, click the remove icon for that application in the user’s screen:

![Image displaying the option to revoke a user's role for a specific application in the LifeTime console.](images/roles-revoke-in-app-lt.png "Revoking a User's Role for a Specific Application")
