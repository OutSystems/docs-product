---
summary: Learn how to resolve the Inconsistent Dependency Warning in OutSystems 11 (O11) by republishing the producer module to prevent runtime errors.
locale: en-us
guid: 7a05fa08-e986-451f-8636-5cdc78aa5a10
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: error resolution, runtime errors, module deployment, platform server, service center
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - platform administrators
outsystems-tools:
  - service studio
  - service center
coverage-type:
  - unblock
---

# Inconsistent Dependency Warning

Message
:   `Producer '<producer>' is inconsistent. Please republish '<producer>' in order to prevent runtime errors`

Cause
:   Your module has references to a Producer (module or Extension) that is not consistent in the Platform Server where it was deployed. This inconsistency might arise when, for example, the database indicates that the producer exists but the corresponding files could not be found in the file system.

Recommendation
:   This problem can be solved by 1-Click publishing the producer. Due to the potential severity of this problem, you should notify the Service Center administrator.
