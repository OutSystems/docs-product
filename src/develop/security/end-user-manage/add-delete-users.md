---
summary: Learn about adding, disabling and deleting end users in the Users application.
tags: support-Mobile_Apps; support-webapps
locale: en-us
guid: 8b17c8d9-939a-486c-bec9-fe1309df7aed
app_type: traditional web apps, mobile apps, reactive web apps
---

# Add and Delete End Users


In the Users application, click the **Users** tab to view the list of all the end users currently active in your environment.

## Create a new end user { #create }

<div class="info" markdown="1">

If you use an external authentication method (for example, Active Directory or SAML 2.0) to authenticate end users, you don't need to create the users manually. Instead, they're created automatically in the OutSystems database on the first login.

Check [End Users Authentication](end-user-authentication/intro.md) for more information on external authentication methods.

</div>

Before you can add users, you must have access to the Users application. To learn more about access to the Users application, see [Access the Users application](accessing-users.md).

To create a new end user for your applications do the following:

1. From the Users tab click **Create a new User**.

1. Complete the form entering all required fields, and press **Save**. The Users app redirects you to the user detail page.

1. Assign groups and roles to the user.

![Demo of creating a user in the Users app](images/add-delete-users-gif1.gif?width=550)

## Activate and deactivate an existing end user { #activate-deactivate }

A deactivated end user can't log in to any application and has all permissions suspended.
  
1. To deactivate an end user, from the user detail page, click **Set as Inactive**.

1. To view the list of deactivated users, from the **Users** tab, click **Inactive Users**. To re-activate an end user, enter the user details and click **Set as Active**.

## Delete an existing end user { #delete }

To permanently delete an end user, from the user detail screen, click **Edit this User** and select **Delete this User**.

![Demo of deleting an end user in the Users app](images/add-delete-users-gif2.gif?width=550)
