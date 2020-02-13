---
summary: Learn how to define Roles to set the security of your applications.
tags: 
---

# User Roles

Roles are used to restrict or allow end-users to access specific screens and
operations of your application.

Roles are set at design time. You can use them when designing the logic of
your application and you can associate them with the following elements:

* Screen
* Human Activity

## System Roles and Custom Roles

When you create a new module in Service Studio, OutSystems provides you with a
default set of **System Roles** but you are allowed to define your own
**custom Roles**.

OutSystems provides the following System Roles:

* **Anonymous:** Allows any end-user to access the element, including users that are not logged in (non-authenticated users). Anonymous is the most general Role and when you associate this Role, for example with a screen, all of the existing Roles are automatically associated with it. 

* **Registered:** Allows any end-user who has logged into an Application running in the same platform server (authenticated users) to access the element. This is possible due to the Single Sign-On mechanism of OutSystems, which allows sharing end-user sessions among applications/modules. When you associate this Role with an element all of the existing Roles are automatically associated with it, except the Anonymous role. 

Besides the System Roles already provided, you can define your own custom Roles to manage the access of end-users to the screens and operation of your application.

## Persistency in Roles

Granting and revoking Roles during runtime (using the Grant&lt;Role name&gt;Role
and Revoke&lt;Role name&gt;Role actions) can be persistent across multiple sessions
or only be active for a single session. This setting can only be changed for
Traditional Web Apps.

![Roles-persitency.png](images/Roles-persitency.png)

* **Persistent:** The runtime granting or revoking of Roles is stored in the database and is kept in between login sessions. Set the `Is Persistent` property of the Role to `Yes`. 

* **Not persistent:** The runtime granting or revoking of Roles is not stored in the database, lasting only for a single session. When the end-user is logged out, the runtime granting or revoking of Roles is lost. Set the `Is Persistent` property of the Role to `No`. 

<div class="info" markdown="1">

When end-user authentication and authorization is performed using an external system, non-persistent Roles should be used. This makes it easier to map permissions defined in an external system, such as Active Directory, to OutSystems Roles. Using non-persistent Roles ensures that changes to end-user permissions made in the external system are reflected in OutSystems.

</div>
