---
summary: Resolve asset issues in OutSystems 11 (O11) by managing modules with different user providers and ensuring findings are not mapped to ODC Assets.
locale: en-us
guid: 7ac9c1fe-c4b3-4213-8c15-187e38d3ba29
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
helpids: 30627
coverage-type:
  - unblock
  - understand
tags: outsystems 11, migration, user provider, odc assets, module configuration
audience:
  - none
outsystems-tools:
  - none
---
# The Asset cannot contain modules having a user provider different than Users

This pattern identifies OutSystems 11 (O11) modules configured with a User Provider other than the default **Users** provider. Migrating these modules directly to OutSystems Developer Cloud (ODC) is currently not supported because ODC uses a single, unified user management system:

* In O11, the **User Provider module** property specifies the source for the user records to be used by the module.
O11 includes two default user providers, Users (default) and Service Center, but you can also use other custom user providers. The Users provider handles app end-users and Service Center handles IT users.

* In ODC, the **User Provider module** property doesn't exist. App end-users and IT users exist in the same user provider.

## How to solve

<div class="info" markdown="1">

If you are only preparing your code for the migration, at present, OutSystems recommends not making any changes to modules with findings for this code pattern, while ODC doesn't support segregated user providers.

</div>

This pattern isn't supported yet.

You can only proceed with the migration of apps with Users set as the user provider.
