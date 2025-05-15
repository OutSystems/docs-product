---
summary: Explore solutions for the 'Invalid Public Structure' error in OutSystems 11 (O11) when dealing with public attributes and module references.
locale: en-us
guid: 6c059ca7-c68d-44de-9352-267cde943cff
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: error handling, outsystems development, data modeling, entities management, module dependencies
audience:
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Invalid Public Structure Error

The `Invalid Public Structure` error is issued in the following situations:

* `Public Structure <structure> contains an attribute of record type <type> that is not declared as Public`
  
    In a public structure, you have a compound attribute that is defined by an Entity/Structure that is not public.

    You must set as public the Entity/Structure that defines the attribute.

* `Public Structure <structure> contains an attribute of record type <type> that is a reference`
  
    In a public structure, you have an compound attribute, that is defined by an Entity/Structure that is a module reference. You can only expose elements defined in the current module.

    You must edit the public structure, select the attribute, and use Entities/Structures defined in the current module.

Double-click on the error line to take you directly to the attribute.
