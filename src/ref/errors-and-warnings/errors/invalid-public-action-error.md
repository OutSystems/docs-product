---
summary: OutSystems 11 (O11) issues the "Invalid Public Action" error for non-public or referenced record parameters in public actions.
locale: en-us
guid: f55fcb70-f968-4223-9b1c-8f9136349e41
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: outsystems, error handling, public actions, module references, entity/structure accessibility
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Invalid Public Action Error

The `Invalid Public Action` error is issued in the following situations:

* `Public Action <action> contains a parameter of record type <type> that is not declared as public`
  
    In a public action, you have a Record (Entity/Structure) parameter that is not declared as public.

    You must set as public the Entity/Structure that belongs to the definition of the Record parameter.

* `Public Action <action> contains a parameter of record type <type> that is a reference`
  
    In a public action, you have a Record parameter defined by an Entity/Structure that is a module reference. You can only expose elements that are defined in the current module.

    You must edit the public action and define the parameter using Entities/Structures defined in the current module.

Double-click on the error line to take you directly to the public action property.
