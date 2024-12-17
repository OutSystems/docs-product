---
summary: Explore troubleshooting steps for missing module warnings in OutSystems 11 (O11) when a producer module is not found.
tags: troubleshooting, platform server, runtime errors, producer module, module references
locale: en-us
guid: f6effa12-876e-460a-a0a2-7e366645038e
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - frontend developers
  - full stack developers
  - platform administrators
outsystems-tools:
  - service studio
  - platform server
coverage-type:
  - unblock
---

# Missing Module Warning

## Module &lt;module name> uses module &lt;producer name> that was not found. Runtime errors may occur.

**Cause**

Your module has a reference to a producer module that was not found.

**Recommended action**

Do one of the following:

* Check with the producer module's owner to determine what the cause might be for the missing [module](../../../ref/lang/auto/class-module.md).
* Check with the Platform Server administrator.
