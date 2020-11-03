---
summary: Learn about adding, disabling and deleting end users in the Users application.
tags: support-Mobile_Apps; support-webapps
---

# Add and Delete End Users

<div class="info" markdown="1">

We've been working on this article. Please let us know how useful this new version is by voting.

</div>

In the Users application, click the **Users** tab to view the list of all the end users currently active in your environment.

## Create a new end user { #create }

<div class="info" markdown="1">

If you use an external authentication method (for example, Active Directory or SAML 2.0) to authenticate end users, you don't need to create the users manually. Instead, they're created automatically in the OutSystems database on the first login.

Check [End Users Authentication](end-user-authentication/intro.md) for more information on external authentication methods.

</div>

To create a new end user for your applications do the following:

1. Click **Create a new User** under the "Users" page heading.

1. Fill in the details and press **Save**.  

    The Users app redirects you to the user detail page after creating the user.

1. Assign groups and roles to the user.

![Demo of creating a user in the Users app](images/add-delete-users-gif1.gif?width=550)

## Activate and deactivate an existing end user { #activate-deactivate }

A deactivated end user can't log in to any application and has all the granted permissions suspended.  
To deactivate an end user, access the user detail page and then click **Set as Inactive**.

In the **Users** tab, click **Inactive Users** to view the list of deactivated users.  
To activate an end user again, enter the user details and click **Set as Active**.

## Delete an existing end user { #delete }

To permanently delete an end user, click **Edit this User** on the user detail screen and select **Delete this User**.

![Demo of deleting an end user in the Users app](images/add-delete-users-gif2.gif?width=550)
