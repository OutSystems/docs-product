---
summary: Explore how OutSystems 11 (O11) handles and resolves corrupted widget issues by recreating them automatically.
locale: en-us
guid: 04f0e0bf-0ef7-4abe-b596-bfb4a48393a2
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: error handling, widget management, outsystems service studio, ui development, debugging
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Invalid Widget Warning

Message
:   `Screen '<screen name>' contained a corrupted <widget kind> Widget that was re-created. Please check its properties`

Cause
:   Service Studio has detected a widget that got corrupted but was able to re-create it for you.

Recommendation
:   Check if the Widget Properties are set with the correct values.
