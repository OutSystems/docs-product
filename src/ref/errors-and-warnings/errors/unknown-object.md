---
summary: Learn how to resolve the 'Unknown Object' error in OutSystems 11 (O11) when using images or resources in Style Sheets.
locale: en-us
guid: c6d53c58-5032-4598-b03f-a5b8e4f3d6c1
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: ide usage, reactive web apps, resource management, deployment issues, error handling
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Unknown Object

The `Unknown Object` error is issued in the following situations:

* `Unknown object '<Image or Resource>' used in '<Theme or Block>' Style Sheet.`

    The Style Sheet of the Theme or Block contains a reference to an unknown image or resource.

    Open the Theme or Block Style Sheet and fix the reference to the image or resource, or add the necessary image and resource to your module.

* `Object '<Resource>' used in '<Theme or Block>' Style Sheet is not being deployed.`

    The Style Sheet of the Theme or Block contains a reference to a resource that has the property Deploy Action set to `Do Nothing`.

    Set the property Deploy Action of the resource to `Deploy to Target Directory`.

Double-click on the error line to take you directly to the source of the error.
