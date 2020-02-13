---
summary: Learn how to access the Users application.
tags: support-Mobile_Apps; support-webapps
---

# Access the Users application

The **Users** application of a specific OutSystems environment is available at `https://<environment_address>/Users`.

You need an account with administrator privileges to log in the Users application. This account **is not** the same you use to connect to Service Center, LifeTime or Service Studio, as those are IT users, although you can create accounts with the same credentials for both purposes.

Before accessing the Users application for the first time, you must [configure the Administrator user](#configure-users-administrator).

![users first login](images/users-first-login-usr.png)

## Configure Users administrator

Configuring the Administrator user for Users application sets the password and also grants the Administrator user with all the available Roles.

To configure the Administrator user, do the following:

1. Log in to Service Center using the administrator credentials (`http://<environment_address>/ServiceCenter`).

1. Go to **Factory -> Modules**.

1. Search for **Users** and click the module name to open the details page.

1. Click the **Single Sign-On** tab.

1. Click the **Configure Administrator user** button.

    ![configure administrator user](images/users-configure-admin-sc.png)

1. Set the password for the Administrator user.

1. Click **Apply**.
