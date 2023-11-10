---
summary: Learn how to manage User Groups by modifying the System reference or accessing OutSystems database directly.
tags: support-Mobile_Apps; support-webapps
locale: en-us
guid: f2dc6e55-9db1-48b6-9e06-796a42618b8d
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Customize Groups

The Users application does not support Group hierarchies by default so it's not possible to make one group part of another. However, OutSystems was designed to support this by either using the OutSystems platform or an external system.

## Using custom Group management in OutSystems

1. Create a new Application.
1. In the references window find the **Group** entity under **(System)**.
1. Model and create entities that reference the Group entity using foreign keys.
1. Design screens to manage these groups.
1. Use a database management tool to connect to the OutSystems database.
1. Edit the records in the `OSSYS_Group` table and, for each group that has these customizations, set its `HasCustomManagement` attribute to `True`. These groups will no longer be visible in the Users application.


## Using external custom Group management

1. Use a database management tool to connect to the OutSystems database.
1. Edit the records in the `OSSYS_Group` table and set the `HasCustomManagement` field to `True` for the groups you want to manage yourself. These groups will no longer be visible in the Users application.
1. Model and create tables that reference the `OSSYS_Group` using the foreign keys.
1. Design your external systems to manage the tables you created.
