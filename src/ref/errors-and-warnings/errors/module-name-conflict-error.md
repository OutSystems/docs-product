---
summary: Learn how to resolve the 'module Name Conflict' error in OutSystems 11 (O11) when encountering duplicate module or tenant names.
locale: en-us
guid: 8cac607a-6ba3-4392-825c-59d9eeaae525
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: error resolution, platform server, outsystems development, application deployment, tenant management
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# module Name Conflict Error

The `module Name Conflict` error is issued in the following situations:

* `module <name> already exists`
  
    There is another module with the same name in the Platform Server you are connected to.

    You must change the module name.

* `Tenant <name> already exists in module <name>`
  
    There is another tenant with the same name.

    You must change the tenant name.
