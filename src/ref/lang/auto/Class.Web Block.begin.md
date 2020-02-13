---
tags: runtime-traditionalweb
---

Reusable screen part that can implement its own logic.

## Exposed Web Block

A Web Block cannot be exposed when:

* It has a parameter that is defined using an Entity/Structure that is not exposed.
* It has a parameter that is defined using an Entity/Structure that is reused from another module.
* It contains a Link widget, Button widget, or a consumed Web Screen with arguments of Binary Data, Record, or List data types.

In case the execution of the Producer and Consumer modules are under different User Providers, the modules have different sessions. In this case, variables associated to the session can hold different values between modules.
