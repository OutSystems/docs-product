---
summary: Learn how to resolve the invalid shared configuration issue in OutSystems 11 (O11) by consulting the Service Center Factory Configuration solution.
locale: en-us
guid: 7f61abb9-ec5a-47ae-9e7e-d98dc926e78f
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: error handling, application management, outsystems service center, shared configuration issues, runtime errors
audience:
  - platform administrators
  - full stack developers
outsystems-tools:
  - service center
coverage-type:
  - unblock
---

# Application Configuration Warning

Message
:   `Shared Configuration '<Shared Configuration>' is invalid and will be ignored.`

Cause
:   Your module is using a Shared Configuration with an invalid definition, so it won't be used in runtime.

Recommendation
:   Ask the application manager or the Service Center administrator to correct it with the Service Center Factory Configuration solution, available in the [OutSystems Community](<http://www.outsystems.com/community>), and republish the module, afterwards.
