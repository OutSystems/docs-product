---
locale: en-us
guid: e1f2d221-fa69-4a47-bc46-5052d48ee60a
---

# Invalid Module Error

The `Invalid module` error is issued in the following situation:

* `Multi-tenant modules cannot be used as User Providers`
  
    The module is multi-tenant and cannot be a provider of end users to other modules.

    You must set the module to single-tenant or have another module that provides end users.
