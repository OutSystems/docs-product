---
summary: OutSystems 11 (O11) enables control over end-user access to app screens, data, and actions based on user IDs or roles.
tags: access control, security best practices, role-based access control, user permissions, security warnings
locale: en-us
guid: 68463867-fb0c-4e54-9fe5-d0e117dbf9bb
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=280:120
audience:
  - frontend developers
  - full stack developers
  - platform administrators
outsystems-tools:
  - service studio
coverage-type:
  - understand
  - apply
topic:
  - secure-screen
  - secure-ui-element
---

# Validate End User Permissions in the Application

You can restrict end-user access to specific areas, operations or data of an app.

By validating their user ID or Roles you can control access to screens, screen elements or actions. It's also possible to restrict access to data depending on the logged in user or their role.

## Restricting access to screens, processes, and actions

To restrict access to a screen of an app, in the **Roles** property of the screen select the end user Roles that can view the screen.

**Note**: **Anonymous screens** generate public endpoints which is a  security risk as it can lead to cross-site request forgery attacks. For more information, see [Security Warning](../../ref/errors-and-warnings/warnings/security-warning.md). 

![Screenshot showing how to validate end user permissions for a screen in an application](images/valdiate-screen-ss.png "Screen Roles Validation")

To restrict access to screen elements or actions of a screen, use the **Check&lt;Role_name&gt;Role** action or function to determine if the end user has the necessary Role.

## Restricting access to data

You can also restrict access to data based on the user ID or the user Role.

In this next example, `GetUserId()` was used so that account owners can only see the opportunities of their own accounts:

![Example of restricting data access based on user ID using GetUserId function](images/validate-user-ss.png "User Data Access Validation")

To restrict the displayed data by Role, use **Check&lt;Role_name&gt;Role** in an expression on an aggregate filter.

In this next example, we're checking for the OrderManagerRole to restrict visibility over inactive opportunities. When the **Check&lt;Role_name&gt;Role** evaluates to false, only active opportunities are shown:

![Example of restricting data visibility by user role using Check<Role_name>Role function](images/validate-role-ss.png "Role-based Data Access Validation")

## In Traditional Web

If you only need to check for a Role **once** in a screen, you can use a `Check<Role_name>Role` function directly in the **Condition** of an **If** widget.

![Screenshot demonstrating how to check for a user role once using a Check<Role_name>Role function in a Traditional Web app](images/validate-one-ui-element-ss.png "Single Role Check in Traditional Web")

If you need to check for the same Role **more than once** in the same screen, follow these steps:

1. In the **Preparation** of the screen, add the **Check&lt;Role_name&gt;Role** action, and set the **UserId** to `GetUserId()`.

    ![Image showing the preparation steps for checking a user role multiple times on a screen](images/validate-preparation-role-ss.png "Preparation for Role Check")

1. Use the **Check&lt;Role_name&gt;Role\.HasRole** output, to hide interface elements and restrict access to actions, for example:

    * Hide or display interface elements using an **If** widget with a `Check<Role_name>Role.HasRole` **Condition**.

        ![Screenshot illustrating how to restrict access to an interface element using the Check<Role_name>Role action](images/validate-ui-element-ss.png "Interface Element Access Restriction")

    * Block or allow executing actions by hiding the Buttons or Links that call the actions, using an **If** widget with a `Check<Role_name>Role.HasRole` **Condition**.

        ![Screenshot showing how to restrict access to a button that calls an action based on user roles](images/validate-button-ss.png "Action Access Restriction")
