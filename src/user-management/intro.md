---
summary: Learn how to create users, user roles and permissions management to restrict access to application screens, interface elements and operations by its end users.
tags: support-Security-featured
locale: en-us
guid: b84f5da2-64c0-4efe-a51e-0990d3279bc5
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
coverage-type:
  - none
audience:
  - none
outsystems-tools:
  - user management app
---
# User management

## User providers

The **Users** module serves as the default user provider that enables single sign-on for end-users. It is possible to create and use other modules as user providers. In doing so, all modules using that user provider will share a source of user records and active sessions.

A user provider has a default tenant, which hosts the users that are created and managed by it. However, new tenants can be created to build multi-tenant applications. To learn more about multi-tenancy, refer to [How to build a multi-tenant application](https://success.outsystems.com/documentation/how_to_guides/development/how_to_build_a_multi_tenant_application/).
