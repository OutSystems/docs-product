---
summary: Learn how to resolve outdated producer warnings in OutSystems 11 (O11) by republishing modules to refresh references and prevent runtime errors.
locale: en-us
guid: 2d0f78ae-6d89-437a-ab38-cf89125d8036
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: dependency management, module versioning, error resolution, publishing process, runtime error prevention
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Outdated Producer Warning

Message
:   `Producer '<producer>' uses outdated references. Please republish '<producer>' to prevent runtime errors`

Cause
:   Your current module (e.g.: MyModule) has one or more references to another module (e.g.: Module1) which is referencing other producers that have changed since it (Module1) was last published.

Recommendation
:   Republish Module1 to refresh its references, and retry MyModule publishing, afterwards.
