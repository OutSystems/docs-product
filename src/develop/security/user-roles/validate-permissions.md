---
summary: If you need to restrict end user access to specific areas or operations in an application, you must validate their permissions.
tags: support-Security; support-Security-featured
---

# Validate End User Permissions in the Application

If you need to restrict end user access to specific areas or operations of an app, you must validate their permissions using Roles to control access to screens, screen elements or actions.

To restrict access to a screen of an app, in the **Roles** property of the screen select the end user Roles that can view the screen.

![Restrict access to a screen using Roles](images/valdiate-screen-ss.png)

To restrict access to screen elements or actions of a screen, use the **Check&lt;Role_name&gt;Role** action or function to determine if the end user has the necessary Role.

## In Traditional Web

If you only need to check for a Role **once** in a screen, you can use a `Check<Role_name>Role` function directly in the **Condition** of an **If** widget.

![Restrict access to a button that calls an action by using check roles function](images/validate-one-ui-element-ss.png)

If you need to check for the same Role **more than once** in the same screen, follow these steps:

1. In the **Preparation** of the screen, add the **Check&lt;Role_name&gt;Role** action, and set the **UserId** to `GetUserId()`.

    ![Roles_prep](images/validate-preparation-role-ss.png)

1. Use the **Check&lt;Role_name&gt;Role\.HasRole** output, to hide interface elements and restrict access to actions, for example:

    * Hide or display interface elements using an **If** widget with a `Check<Role_name>Role.HasRole` **Condition**.

        ![Restrict access to an interface element by using check roles action](images/validate-ui-element-ss.png)

    * Block or allow executing actions by hiding the Buttons or Links that call the actions, using an **If** widget with a `Check<Role_name>Role.HasRole` **Condition**.

        ![Restrict access to a button that calls an action by using check roles](images/validate-button-ss.png)
