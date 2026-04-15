---
guid: 10a12023-68a5-44db-bc0d-c13a8fc2b05a
locale: en-us
summary: The data migration of O11 modules with multiple tenants isn't yet supported.
figma:
coverage-type:
  - unblock
topic:
app_type: reactive web apps,mobile apps
platform-version: o11
audience:
  - backend developers
  - frontend developers
  - full stack developers
  - mobile developers
  - architects
tags: multi-tenancy,outsystems developer cloud,o11 modules,non-supported patterns,data migration
outsystems-tools:
  - conversion assessment tool
helpids: "30737"
isautopublish: true
---

# Module with data in multiple tenants

[Multi-tenancy](https://www.outsystems.com/tk/redirect?g=6e1bb224-5f33-4233-adc5-57dc98793113) allows a single application server and database server to provide different customers with their own isolated set of computing resources. Currently, OutSystems Developer Cloud (ODC) doesn’t support multi-tenancy.

In OutSystems 11, tenants are associated with a user provider. By default, the user provider is **Users** module, but you can [use other custom user providers](../../user-management/end-user-manage/end-user-authentication/single-sign-on.md#different-user-provider).

Initially, the effective user provider only has its default tenant. Then additional tenants can be created to enable multi-tenancy.

This pattern identifies modules in the database of the assessed environment with data in those additional tenants, besides the default tenant. The O11 to ODC App Conversion Kit EAP doesn't yet support data migration for this scenario.

## How to solve

<div class="info" markdown="1">

If you are only preparing for the conversion, at present, OutSystems recommends not making any changes to your data while ODC lacks built-in multi-tenancy support.

</div>

This pattern isn't supported yet.

You can only proceed with data migration of ODC assets that only contain modules where the only active tenant is the default tenant.
