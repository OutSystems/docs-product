---
summary: Learn how to access the Users application, where you can create, update, and delete end users (users of your applications) and their roles.
tags: support-Mobile_Apps; support-webapps
---

# Access the Users application

<div class="info" markdown="1">

We've been working on this article. Please let us know how useful this new version is by voting.

</div>

OutSystems provides the **Users** application for you to create, update, and delete end users (the users of your applications) and their roles. It also allows you to manage roles individually or in bulk using groups.

The Users application of a specific OutSystems environment is available at:

`https://<environment_address>/Users`

You need an account with administrator privileges to log in the Users application. This account is **not** the same you use to connect to Service Center, LifeTime or Service Studio, as those are [IT Users](../../../managing-the-applications-lifecycle/manage-it-teams/intro.md), although you can create accounts with the same credentials for both purposes.

Before accessing the Users application for the first time, you must [configure the Administrator user](#configure-users-admin).

![Users app login screen before configuring the Administrator user](images/users-first-login-usr.png)

## Configuring the Administrator user of the Users app { #configure-users-admin }

Configuring the Administrator user of the Users application sets the user password and grants the Administrator user ("admin") with all the available Roles.

### Prerequisites

To perform this operation, your user must have [Change and Deploy Applications permission](../../../managing-the-applications-lifecycle/manage-it-teams/about-permission-levels.md#env-permission-levels) over the Users application, which means one of the following:

* There's a role assigned to your user with the **Change and Deploy Applications** permission level (or higher) as default role.
* There's a role assigned to your user with the **Change and Deploy Applications** permission level (or higher) for Users application.

For environments that aren't managed by LifeTime, the user accessing Service Center requires one of the following:

* The role assigned to the user has **Full Control** over the Users module.
* The user has **Full Control** directly over the Users module.

### Configure the Administrator user

To configure the Administrator user of the Users application, do the following:

1. Log in to Service Center (`http://<environment_address>/ServiceCenter`). Make sure your user meets the prerequisites to perform the operation.

1. Go to **Factory** > **Modules**.

1. Search for **Users** and click the module name to open the details page.

1. Click the **Single Sign-On** tab.

1. Click the **Configure Administrator user** button.

    ![Configure the Administrator user of the Users application](images/users-configure-admin-sc.png)

1. Set the password for the Administrator user.

1. Click **Apply**.

OutSystems saves the password you entered for the Administrator user ("admin") of the Users application, and grants the Administrator user with all the available Roles.
