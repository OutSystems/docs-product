---
summary: Learn how to configure the Administrator user of the Users app.
tags: support-Mobile_Apps; support-webapps
locale: en-us
guid: 319FF915-A2E9-4A0B-AC8A-93E0A511E997
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Configure the Administrator user of the Users app

Before [accessing the Users app](accessing-users.md) for the first time, you have to configure the Administrator user. Configuring the Administrator user of the Users app sets the user password and grants the Administrator user ("admin") with all the available roles.

## Prerequisites

To perform this operation ensure the following:

* Your environments use **OutSystems 11 Platform Server Release Jul.2019** or later.

* If your environments are managed by LifeTime, you must have the [Change and Deploy Applications permission](../../../managing-the-applications-lifecycle/manage-it-teams/about-permission-levels.md#env-permission-levels). This means you must have one of the following:

    * A role assigned to your user with the **Change and Deploy Applications** permission level (or higher) as default role.
    * A role assigned to your user with the **Change and Deploy Applications** permission level (or higher) for the Users app.

* If your environments aren't managed by LifeTime, you must have one of the following:

    * A role assigned to your user has **Full Control** over the Users module.
    * A role assigned to your user has  **Full Control** directly over the Users module.

<div class="info" markdown="1">

To find out your permissions, see [Find Out the Permissions of IT Users](../../../managing-the-applications-lifecycle/manage-it-teams/find-out-the-permissions-of-it-users.md).

</div>

## Configure the Administrator user

To configure the Administrator user for the Users app, do the following:

1. Log in to Service Center (`http://<environment_address>/ServiceCenter`). Make sure your user meets the [prerequisites](#prerequisites) to perform the operation.

1. Go to **Factory** > **Modules**.

1. Search for **Users** and click the module name to open the details page.

1. Click the **Single Sign-On** tab.

1. Click the **Configure Administrator user** button.

    ![Configure the Administrator user of the Users application](images/users-configure-admin-sc.png)

1. Set the password for the Administrator user.

1. Click **Apply**.

OutSystems saves the password you entered for the Administrator user ("admin") of the Users application, and grants the Administrator user with all the available Roles.

To reset the password of the Administrator of User, repeat the previous procedure.
