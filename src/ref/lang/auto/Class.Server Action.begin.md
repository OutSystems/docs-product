Action that runs logic on the server side.  

## Exposed Server Action

An Action cannot be exposed when:

* It has a parameter that is defined using an Entity/Structure that is not exposed.
* It has a parameter that is defined using an Entity/Structure that is reused from another module.

In case the execution of the Producer and Consumer modules are under different User Providers, the modules have different sessions. In this case, variables associated to the session can hold different values between modules.
