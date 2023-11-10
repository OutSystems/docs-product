---
summary: Learn about creating groups, assigning roles to them and managing group members in the Users application.
tags: support-Mobile_Apps; support-webapps
locale: en-us
guid: 17e0082a-7169-482d-a383-89eeab15b9df
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Manage End Users and Organize Roles using Groups

When managing large sets of end users, it can be difficult to manage their roles individually. Instead of manually assigning roles to each end user, you can create groups of end users and assign the roles to the group. 

## Create a new group

To create a new group:

1. In the Groups tab, click on **Create a new Group**.
1. Name the group and add a description.
1. Click Save to create the group. 

When the group is created, you’ll be redirected to the group's detail page, where you can add end users as members and assign roles to the group.

## Assign roles to a group

To assign a role to the group:

1. In the group's detail page, in the Roles section, enter the required role in the input box.
1. Click on Add to assign the role to the group.

You can assign as many roles as needed to the group.

When you add an end user to the group, all the roles that are granted to the group are granted to the user. These roles will appear in the user detail page with the group name under the column `Inherited from` and cannot be removed individually. 

## Add members to a group

To add an end user as a member to the group:

1. In the group's detail page, under the list of end users in the Members section, enter the required username in the input box.
1. Click on Add to add the end user as a member to the group.

You can add as many end users as required to the group.

![](images/groups-gif1.gif?width=500)
 
An end user's groups can also be managed in the user details page, where you can see a list of all the groups the user belongs to and add new groups or remove existing ones.

## Remove users from a group

To remove an user from a group:

1. In the group's detail page, in the Members section, enter the required username in the search box.
1. Hover over the entry for the end user in the list and click **Remove** to remove the end user from the group.

When you remove a user from a group, all the roles granted to the user by inheritance from that group will be revoked. You can still manually add a role that was granted to the user by inheritance from a group. This overrides the group inheritance, i.e., if you assign a role to an end user both through a group and individually, the role will not be revoked if the end user is removed from the group. In this scenario, the column `Inherited from` in the Roles section of the user detail page is empty.

![](images/groups-gif2.gif?width=500)
