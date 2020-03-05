---
summary: Ensure a strict security policy by checking the permissions IT users have over an application.
---

# Find Out the Permissions of IT Users

Understanding the permissions that IT users have over the applications is fundamental to ensure a strict security policy.

## Permissions over a specific application

In this example we want to understand who has access to the application Mobile Banking in the different environments and with which permissions:

1. In the LifeTime console (`https://<lifetime_env>/lifetime`), go to the **APPLICATIONS** area.

1. Find the Mobile Banking application and click the Name of the application to go to the details page.

1. Click the **Permissions** link.  

    ![](images/users-permissions-app-lt.png?width=950)

On this page, we can see:

* The users with **specific access to the application**, with which role and corresponding permissions. These specific permissions override any permission given to that user through a team or the default role.

* Which **teams** have access to this application. Clicking on the team, we will have the visibility of the different roles and permissions the members of that team have over the application. The permissions given through the team have precedence over the permissions given by the default role of a user.

## Permissions of a specific IT user 

In this example we want to understand the permissions that a specific user has, to ensure the company security policy is being enforced:

1. In the LifeTime console (`https://<lifetime_env>/lifetime`), go to the **USER MANAGEMENT** area.

1. In the **USERS** screen, find the user and click the Name of the user to go to the details page.  

    ![](images/users-permissions-user-lt.png?width=950)

On this page, we can see that:

* The **default role** of the user grants him access to the Development environment, but no access to any application. Also, it grants No Access to Quality and Production environments.

* The user has Architect **role in the team** Intranet, which grants him Change and Deploy permission in the Development environment over the applications that the team manages, Directory and Fleet Management. Over the same applications, the user has Monitor and Reference permission in the Quality environment and No Access in the Production environment.

* The user has been given **specific access** to Mobile Banking application with role Business Monitoring, which grants the user Monitor and Reference permission over this application in the Development and Quality environments, but No Access to the application in the Production environment.
