# Invalid Module Error

The `Invalid module` error is issued in the following situation:

* `Multi-tenant modules cannot be used as User Providers`
  
    The module is multi-tenant and cannot be a provider of end users to other modules.

    You must set the module to single-tenant or have another module that provides end users.
