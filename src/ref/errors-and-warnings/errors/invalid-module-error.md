---
summary: Explore how OutSystems 11 (O11) handles the 'Invalid module' error when multi-tenant modules are used as User Providers.
locale: en-us
guid: e1f2d221-fa69-4a47-bc46-5052d48ee60a
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: error handling, multi-tenancy, security, traditional web apps, user management
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Invalid Module Error

The `Invalid module` error is issued in the following situation:

* `Multi-tenant modules cannot be used as User Providers`
  
    The module is multi-tenant and cannot be a provider of end users to other modules.

    You must set the module to single-tenant or have another module that provides end users.
