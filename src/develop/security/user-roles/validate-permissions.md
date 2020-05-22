---
summary: If you need to restrict end user access to specific areas or operations in an application, you must validate their permissions.
tags: support-Security; support-Security-featured
---

# Validate End User Permissions in the Application

If you need to restrict end user access to specific areas or operations of a web application, you must validate their permissions using Roles to control access to screens, screen elements or actions.

To restrict end user access to a screen of an app, in the **Roles** property of the screen select the end user Roles that can view the screen.

![Restrict access to a screen using Roles](images/valdiate-screen-ss.png)

To validate the permissions of end users to screen elements or actions of an app, use the CheckRole built-in function to determine if the end user has the necessary roles.

## In Traditional Web

In the screen **Preparation** add the **Check&lt;Role_name&gt;Role** action.

![Roles_prep](images/validate-preparation-role-ss.png)

The following examples show how you can use **Check&lt;Role_name&gt;Role** actions to hide interface elements and access to actions depending on a Role:

* Hide or display interface elements using an **If** widget with a `Check<Role_name>Role` **Condition**.

![Restrict access to an interface element by using check roles action](images/validate-ui-element-ss.png)

* Block or allow executing actions by hiding the Buttons or Links that call the actions, using an **If** widget with a `Check<Role_name>Role` **Condition**.

![Restrict access to a button that calls an action by using check roles](images/validate-button-ss.png)

< div class="info" markdown="1">
If you only need to check for a Role **once** in your screen, you can use a `Check<Role_name>Role` function directly in the **Condition** of an **If** widget.

![Restrict access to a button that calls an action by using check roles function](images/validate-one-ui-element-ss.png)
</div>
