---
summary: Explore the role-based permission model for IT users in OutSystems 11 (O11), detailing roles, permissions, and assignment methods.
locale: en-us
guid: 5a167254-3be6-44df-93ef-0d801e27efbb
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing%20the%20Applications%20Lifecycle?node-id=267:23
---

# Understand the Permission Model for IT Users

In OutSystems, the policies that grant or revoke permissions to IT users are managed using a role-based permission model. This means that **permissions** to perform operations are configured in **roles** that are then assigned to users.

![Diagram showing the overview of permission levels in OutSystems](images/lt-about-permission-levels-1.png "OutSystems Permission Levels Overview")

## Roles

In OutSystems, a role is a **set of permissions** that define which operations a user can perform over the environments and applications.

OutSystems has two built-in roles that allow you to implement a simple security policy:

* **Developer** - By default, this role allows deploying to the Development environment, open applications on Quality Assurance, and list applications on Production. You can change the permissions of the Developer role according to your case.

* **Administrator** - Has full control over all environments and applications. Allows deploying applications to all environments of the infrastructure and manage IT users, security, and environments. You can’t change the permissions of the Administrator role.

If these two built-in roles aren't enough to set up your security policies, you can [create additional roles](create-an-it-role.md#create-a-new-role) to define a more granular policy.

## Permissions

Each role is defined by a set of permissions that determine which operations the IT users assigned to that role can perform.

**Permission levels for an environment**
:   Each permission level is cumulative with the permissions of the levels below (except for the lowest one, “No Access to Environment”).

**Specific permissions for an environment**
:   Can be turned on/off for a specific environment.

**Infrastructure-wide permissions**
:   Control who can manage IT users, teams, and roles across the infrastructure. For self-managed infrastructures, allow managing the environments and its configurations.

![Illustration of environment-specific permissions in OutSystems](images/lt-about-permission-levels-5.png "OutSystems Environment-Specific Permissions")

Check the details for each permission in the [reference below](#outsystems-permissions-reference).

## Assigning Roles to IT Users

To achieve the security policy required for your IT users and teams, you might need to combine several roles with different levels of permissions and [assign those roles to the users](create-an-it-role.md#assign-roles-to-users) in a specific way.

The set of permissions that an IT user has over the environments and the applications in a factory is determined by the several roles that the user is assigned:

* The user’s default role.
* The role assigned to the user in the teams the user belongs to.
* The role assigned to the user for specific applications.

### Default role

While [creating an IT user](create-an-it-user.md), it's mandatory to define the **Default Role** for the user. This role defines the **base permissions** that the user has over the environments and all applications on the environments.

To follow the principle of security by default, the default role of users should grant them as little base permissions over applications as possible, so that all permissions necessary for the users to perform their work can be defined explicitly either through teams or directly for specific applications.

![Image depicting how a default role is assigned to an IT user in OutSystems](images/about-permission-levels-2.png "Default Role Assignment in OutSystems")

### Role assigned to users for a team { #role-assigned-to-users-for-a-team }

While [adding an IT user to a team](create-an-it-team.md#add-it-users-to-the-team), it's mandatory to define the role that will be applied to the user when dealing with **the applications that belong to that team**.

The role assigned to users for teams **overrides the default role** of the users, and is typically used to explicitly grant extra permissions that apply only to the applications that belong to the team.

![Image showing the role assignment to IT users for a team in OutSystems](images/about-permission-levels-3.png "Team-Based Role Assignment in OutSystems")

This allows granting permissions for all applications that the team manages, without having to grant permissions on each application individually.

For more information about team roles and permissions, see [Set Up the Permissions in a Team](setup-team-permissions.md)

### Role assigned to users for a specific application { #role-assigned-to-users-for-a-specific-application }

It's also possible to [assign a role directly to one user for a specific application](create-an-it-role.md#assign-a-role-to-a-user-for-a-specific-application). This provides flexibility for more exceptional situations where it may be useful to either **grant or revoke the permissions of users for particular applications** without using teams.

Roles assigned directly to a user on specific applications **override the default role** of the user and also **any role assigned through teams**.

![Image illustrating the assignment of roles to IT users for a specific application in OutSystems](images/about-permission-levels-4.png "Application-Specific Role Assignment in OutSystems")

## OutSystems Permissions Reference

This section describes which operations are available to a user when a specific permission is granted to that user through a role. Those operations depend on how the role is assigned to the user.

### Permission levels for an environment { #env-permission-levels }

Except for the lowest one, "No Access", each permission level is cumulative with the permissions of the levels below.

Full Control |  |
---------|----------
Assigned as **Default Role** | The user can manage the **environment settings**, such as the date format, and external database catalogs and connections. The user can also manage the front-end servers for this environment, zones, email and certificate settings, OutSystems licensing, and see auditing information of the changes made to the infrastructure.
Assigned for a **Team** | The user is set with **Change and Deploy** permission for the **team’s applications**, which is the highest permission that applies to applications.
Assigned for an **Application** | The user is set with **Change and Deploy** permission for the **application**, which is the highest permission that applies to applications.

Change and Deploy Applications | |
---------|----------
Assigned as **Default Role** | The user can see all the **environment’s applications** in Service Studio, LifeTime and Service Center, as well as change and deploy them. The user can also change in LifeTime and Service Center the settings of all the **environment’s applications** (such as Site Properties).
Assigned for a **Team** | The user can see the **team’s applications** in Service Studio,  LifeTime and Service Center, as well as change and deploy them. The user can also change in LifeTime and Service Center the settings of the **team’s applications** (such as Site Properties).
Assigned for an **Application** | The user can see the **application** in Service Studio, LifeTime and Service Center, as well as change and deploy it. The user can also change in LifeTime and Service Center the settings of the **application** (such as Site Properties).

Open and Debug Applications | |
---------|----------
Assigned as **Default Role** | The user can open and debug all the **modules of the environment’s applications** in Service Studio by using the **Environment > Open in Environment** menu.
Assigned for a **Team** |The user can open and debug the **modules of the team’s applications** in Service Studio by using the **Environment > Open in Environment** menu.
Assigned for an **Application** | The user can open and debug the **modules of the application** in Service Studio by using the **Environment > Open in Environment** menu.

Monitor and Add Dependencies * | |
---------|----------
Assigned as **Default Role** | From the applications for which the user has Change and Deploy permission, the user can add dependencies to the public elements of all the **environment’s applications**. The user can also monitor all the **environment’s applications** and the **environment’s performance**.
Assigned for a **Team** | From the applications for which the user has Change and Deploy permission, the user can add dependencies to the public elements of the **team’s applications**. The user can also monitor the **team’s applications**.
Assigned for an **Application** | From the applications for which the user has Change and Deploy permission, the user can add dependencies to the public elements of this **application**. The user can also monitor the **application**.

(*) **Monitor and Add Dependencies** permission level is available for environments with Platform Server Release Oct.2019 or later.

List Applications | |
---------|----------
Assigned as **Default Role** | The user can see all the **environment’s applications** listed in LifeTime and Service Center, but not in Service Studio.
Assigned for a **Team** | The user can see the **team’s applications** listed in LifeTime and Service Center, but not in Service Studio.
Assigned for an **Application** | The user can see the **application** listed in LifeTime and Service Center, but not in Service Studio.

Access * | |
---------|----------
Assigned as **Default Role** | The user can log in the **environment** but can’t see any of the environment’s applications listed in LifeTime, Service Center or Service Studio.
Assigned for a **Team** | Same behavior as **No Access** permission level for teams: The user can’t see the **team’s applications** listed in LifeTime, Service Center or Service Studio.
Assigned for an **Application** | Same behavior as **No Access** permission level for applications: The user can’t see the **application** listed in LifeTime, Service Center or Service Studio.

(*) **Access** permission level is available for environments with Platform Server Release Oct.2019 or later.

No Access | |
---------|----------
Assigned as **Default Role** | The user can’t log in the **environment**. You can't grant application-specific permissions to users that have this permission level in the default role.
Assigned for a **Team** | The user can’t see the **team’s applications** listed in LifeTime, Service Center or Service Studio, although the user can login in the environment.
Assigned for an **Application** | The user can’t see the **application** listed in LifeTime, Service Center or Service Studio, although the user can login in the environment.

### Specific permissions for an environment

Create Applications | |
---------|----------
Assigned as **Default Role** | The user can create new applications in the **environment** through Service Studio and Service Center (by uploading and publishing). The user can also create new applications in **any team** through LifeTime.
Assigned for a **Team** | The user can create new applications in the **team** through LifeTime.
Assigned for an **Application** | Not applicable.

Add System Dependencies | |
---------|----------
Assigned as **Default Role** | In the applications for which the user has Change and Deploy permission, the user can add new dependencies to the public elements of System module. Once these dependencies are added, any user, even without permission to add system dependencies, can use them.
Assigned for a **Team** | Not applicable.
Assigned for an **Application** | Not applicable.

### Infrastructure-wide permissions

Manage Users and Roles | (applies only to OutSystems Cloud)
---------|----------
Assigned as **Default Role** | The user can add, edit and remove IT users, roles and teams. The user can also turn on/off features in Technical Preview. Setting this permission ON also sets ON the permission "Manage Teams and Application Roles".
Assigned for a **Team** | Not applicable.
Assigned for an **Application** | Not applicable.

Manage Infrastructure and Users | (applies only to self-managed infrastructures)
---------|----------
Assigned as **Default Role** | The user can add, edit, remove and switch infrastructure environments, as well as turn on/off features in Technical Preview. The user can also add, edit and remove IT users, roles and teams. Setting this permission ON also sets ON the permission "Manage Teams and Application Roles".
Assigned for a **Team** | Not applicable.
Assigned for an **Application** | Not applicable.

Manage Teams and Application Roles | |
---------|----------
Assigned as **Default Role** |The user can add and remove IT users from all the **environment’s teams**, as well as grant and revoke roles to IT users for all the **environment’s applications** (the user's role must have higher permission levels for the environments than the role being granted). The user can also edit all the **environment’s teams** and access the audit logs.
Assigned for a **Team** | The user can add and remove IT users from the **team**, as well as grant and revoke roles to IT users for the **team’s applications** (the user's role must have higher permission levels for the environments than the role being granted). The user can also edit the **team** and access the team's audit logs.
Assigned for an **Application** | The user can grant and revoke roles to IT users for the **application** (the user's role must have higher permission levels for the environments than the role being granted). The user can also access the application's audit logs.
