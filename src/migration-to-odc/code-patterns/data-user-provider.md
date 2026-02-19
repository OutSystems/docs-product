---
guid: a38b687f-5515-4cb5-a12d-85a7662a8c22
locale: en-us
summary: The data migration of O11 modules with user provider different than Users isn't supported.
figma: 
coverage-type:
  - unblock
topic: 
app_type: mobile apps,reactive web apps
platform-version: o11
audience: 
  - backend developers
  - frontend developers
  - full stack developers
  - mobile developers
  - architects
tags: outsystems 11, data migration, user provider, odc assets, module configuration
outsystems-tools:
  - conversion assessment tool
helpids: "30742"
---

# Module with a user provider different than Users

[User management](https://www.outsystems.com/tk/redirect?g=9e0fb9b7-d2b0-419f-a5d8-5b5ed730da5e) in OutSystems Developer Cloud (ODC) is different from [OutSystems 11 (O11)](../../user-management/intro.md):

* O11 includes two default user providers, Users (default) and Service Center, but you can also use other custom user providers. The Users provider handles app end-users and Service Center handles IT users.

* ODC uses a single unified user management system. App end-users and IT users exist in the same user provider.

This pattern identifies modules in the assessed environment with a user provider different from Users. The O11 to ODC App Conversion Kit EAP doesn't yet support data migration for this scenario.

## How to solve

<div class="info" markdown="1">

If you are only preparing your code for the conversion, at present, OutSystems recommends not making any changes to your data while ODC doesn't support segregated user providers.

</div>

This pattern isn't supported yet.

You can only proceed with data migration of ODC assets where all modules use **Users** as the user provider.
