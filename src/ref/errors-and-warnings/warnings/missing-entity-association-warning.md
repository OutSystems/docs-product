---
summary: Learn how to resolve missing entity association warnings in OutSystems 11 (O11) by managing module references and permissions.
locale: en-us
guid: 590a02ff-3c8a-442a-a6af-a18205dbe1d8
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: module management, entity references, permissions, environment management, troubleshooting
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
  - service center
coverage-type:
  - unblock
---

# Missing Entity Association Warning

Message
:   `Referenced Entity <entity> is not associated with this module`

Cause
:   You are using an entity from a Producer module that is no longer associated with your module. For example, your access to this producer changed and you cannot use its public entities.

Recommendation
:   Do one of the following:

    * Open the Add/Remove References window and add the necessary entity identifiers; check in the environment management console if you have access to the Producer module.
    * Contact the Producer's owner to check what has changed.

---

Message
:   `Foreign Entity <entity> is not associated with this module`

Cause
:   You are using an entity from a Producer extension that is not associated with your module.

Recommendation
:   Do one of the following:

    * Open the Add/Remove References window and add the necessary entity references.
    * Check in Service Center if you have access to the Producer extension.
    * Contact the Producer's owner to check what has changed.
  