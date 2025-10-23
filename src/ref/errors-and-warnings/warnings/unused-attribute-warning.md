---
summary: Learn how to address the Unused Attribute Warning in OutSystems 11 (O11) by deleting unnecessary value entries and verifying attribute deletions.
locale: en-us
guid: 54c78d12-b3c9-428a-bc6f-cc0d7a8c5546
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: error handling, entity management, application development, ide usage, outsystems platform
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Unused Attribute Warning

Message
:   `Consider deleting the value <value>. It’s never used because it refers to the missing attribute <attribute>.`

Cause
:   A value is set for an attribute that no longer exists for the given Entity.

Recommendation
:   Delete the value entry from the inline record properties. Additionally, verify that the deletion of the attribute is intended, and not accidental.
