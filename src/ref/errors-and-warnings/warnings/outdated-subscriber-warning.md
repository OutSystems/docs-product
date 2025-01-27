---
summary: OutSystems 11 (O11) error occurs when a module set as a User Provider is incorrectly configured, requiring adjustment of the Is User Provider property.
locale: en-us
guid: 7fa65fdc-8d24-4c0b-afba-67d556a0bbf9
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: error handling, configuration management, user authentication, user management, authentication providers
audience:
  - full stack developers
  - frontend developers
  - backend developers
  - platform administrators
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Outdated Subscriber Warning

Message
:   `This module is no longer a User Provider. Subscriber module '<module>' is outdated.`

Cause
:   Your module is being used as User Provider of `<module>` and the Is User Provider property of your module is set to 'No'.

Recommendation
:   Do one of the following:

    * Set the Is User Provider property of your module to 'Yes'.
    * Change the User Provider module property of the `<module>`.
