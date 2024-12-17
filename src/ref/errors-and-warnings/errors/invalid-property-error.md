---
summary: Explore solutions for the 'Invalid Property' error in OutSystems 11 (O11) when a property is defined multiple times for the same element.
locale: en-us
guid: b13b8d21-4c7b-4c3d-a928-00112c210227
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: error handling, property management, debugging, ide usage, traditional web apps
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Invalid Property Error

The `Invalid Property` error is issued in the following situations:

* `{0} '{1}' can't be defined multiple times for the same element.`
  
    You are declaring the same entry, for example the 'title' extended property, in the same element.

    Edit the element and remove the entry that is duplicated.

Double-click on the error line to take you directly to the invalid property.
