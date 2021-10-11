---
summary: Learn about basic end user management, such as creating, deleting, deactivating registered user accounts or placing them into User Groups with specific permissions.
tags: support-Mobile_Apps; support-webapps
---

# End User management

Applications user management is created around the following core concepts:

 - [Users](#Users)
 - [Groups](#Groups)
 - [User Providers](#user-providers)
 - [Tenants](#tenants)

Through the combination of these concepts you can define all the user management needs required to provide access to your applications to the end users. This section guides you in everything that you need to know about end user management.

## Users

The end users of your OutSystems applications are considered either **Anonymous Users** or **Named Users** (also called Registered Users) according to the following definitions:

Anonymous Users
:   Users that, cumulatively, (i) access an OutSystems application but do not log in, (ii) only access public sections of an OutSystems application, and (iii) whose identity is not known by the OutSystems application. An Anonymous User becomes a Named User when an OutSystems application establishes the identity of that user.

Named Users or Registered Users
:   Users that are registered and can log in to an OutSystems application.  

You can manage the Registered Users of your OutSystems applications through the **Users** application, available at `http://<environment address>/Users`. Check [Access the Users application](accessing-users.md) for more information on creating and managing Registered Users.

OutSystems also offers the [Users API](<../../../ref/apis/auto/users-api.final.md>) to perform end user management programmatically. Use the API to write your own applications for managing Registered Users or for exposing APIs to external systems through Web Services.

<div class="info" markdown="1">

If you use an external authentication method (for example, Active Directory or SAML 2.0) to authenticate end users, you don't need to create these users manually. Instead, these users are created automatically in the OutSystems database on their first login.  
Check [End Users Authentication](end-user-authentication/intro.md) for more information on external authentication methods.

</div>

### Internal Users vs. External Users { #internal-external }

<div class="info" markdown="1">

Applies to OutSystems licenses purchased after January 2020.

</div>

Registered Users (or Named Users) are classified in **Internal Users** or **External Users**, for licensing purposes, according to the following definition:

Internal Users
:   Named users with an email domain belonging to the customer, one of its affiliates or parent company. Any named user with no email associated is also qualified as an Internal User.

External Users
:   Any Named Users who are not considered Internal Users.

You can classify all Registered Users whose email address contains a specific domain (for example, `mycompany.com`) as Internal Users, while all other Registered Users are considered External Users. Check [Classify Users as Internal Users](classify-internal-users.md) for more information on configuring these domains.

By default, Registered Users are considered **Internal Users**.

<div class="info" markdown="1">

The distinction between Internal Users and External Users is only applicable to the **end users** of your OutSystems applications. [IT users](../../../managing-the-applications-lifecycle/manage-it-teams/intro.md) (for example, OutSystems developers or Administrators) are a separate set of users that don't have this kind of classification.

</div>

## Groups

[Groups](groups.md) help you to group users that have same type of permissions in your applications. With groups you can easily attribute the [same role at a group level](../user-roles/intro.md) instead in doing it per user. For example you can have departmental groups (HR, Marketing, Sales, etc.) for applications used by the entire company.

## User providers

User providers are applications that enable you to manage the end-users that access your applications. OutSystems provides the [Users application](accessing-users.md) out of the box, but other User providers can be developed by your teams.

## Tenants

User providers always have a Default Tenant, but in a scenario, for example of an application accessed by different customers, you can create different tenants for different types of users. [Read this article](https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/How_to_Build_a_Multi-tenant_Application#Managing_Tenants_and_End-Users), if you want to learn more about multi-tenancy in OutSystems. 
