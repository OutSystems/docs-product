---
summary: OutSystems 11 (O11) enhances IT team permission management by enabling infrastructure managers to delegate role assignments to team managers.
locale: en-us
guid: e666aa10-a5dd-41c4-856d-52a7b2ff5474
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing%20the%20Applications%20Lifecycle?node-id=267:79
---

# Allow Managers to Handle Permissions of IT Teams

As an infrastructure manager, when someone joins your company you need to create a new IT user and assign the corresponding roles. This is tedious work but cannot be easily delegated, otherwise, the security of your infrastructure might be compromised.

To help you with this, OutSystems allows you to keep control of the users and teams that are created while delegating the permissions management to the team manager.

To do this:

1. [Create a new role](create-an-it-role.md#create-a-new-role) for the team manager that has the infrastructure-wide permission **Manage Teams and Application Roles**. The team manager will only be able to assign roles that have the same or lower permissions than his/her own. Therefore, you must set the permission levels for each environment to the maximum level that the team manager needs to assign to the team.  

    ![Screenshot of the process to create a new role for team managers in OutSystems](images/managers-handle-teams-new-role-lt.png "Creating a New Role for Team Managers")

1. [Add the team manager to the team](create-an-it-team.md#add-it-users-to-the-team) with the new role.  

    ![Interface showing how to add a team manager to an IT team in OutSystems](images/managers-handle-teams-add-to-team-lt.png "Adding a Team Manager to the Team")

When a new user joins the company, the infrastructure manager still needs to [create the user](create-an-it-user.md) and set the default role. Then, the team manager can add the user to the team.

![Step-by-step guide for an infrastructure manager to add a new IT user in OutSystems](images/managers-handle-teams-add-users-lt.png "Infrastructure Manager Adding a New User")

When adding the user to the team, the team manager can only assign a role that has the same or lower permissions than his/her own.

![Procedure for a team manager to assign roles to a new user within their permission level in OutSystems](images/managers-handle-teams-add-user-role-lt.png "Team Manager Assigning a Role to a New User")