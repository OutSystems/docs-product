---
summary: Explore how OutSystems 11 (O11) identifies and recommends the deletion of unused actions in a module to optimize application performance.
locale: en-us
guid: 7316b94a-14c9-4e46-85bf-c1105c44030e
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: performance optimization, code maintenance, application development, outsystems ide, code cleanup
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Unused User Action Warning

Message
:   `<Action> action is never used in this module. Consider deleting it.`

Cause
:   You have an action that is not being used in the module.

Recommendation
:   Check whether the action is really necessary and if not, delete it from the module.
