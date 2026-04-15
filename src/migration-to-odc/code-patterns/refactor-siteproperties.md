---
summary: This article outlines how to refactor site properties in your O11 apps for compatibility with ODC.
locale: en-us
guid: 19d82c11-dc9a-43e8-bce1-1767e48e58fd
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: configuration management, site properties, application settings, runtime settings, api key management
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
  - understand
isautopublish: true
---

# Asset programmatically changing a site property

[Site properties](../../building-apps/data/site/site.md) are global variables with configurable values. They are used in O11 apps to:

* Store configurable variables by environment, such as API Key, Client ID, and Client Secret values.

* Implement configuration values for an application that can be set at runtime.

In ODC, site properties are replaced by **settings**. While they serve a similar purpose for configuration, [ODC settings](https://www.outsystems.com/tk/redirect?g=0624bc73-64c2-45bb-a740-c4cef83989fc) are **read-only at runtime** and cannot be modified through application logic as O11 site properties.

## How to solve

You must adjust the logic of your app to avoid changing the value of site properties programmatically. If you need to keep configurations that can be changed at runtime, use an [entity](https://www.outsystems.com/tk/redirect?g=7bf1d47d-7310-4ec8-a5db-a41b983bdb5b) to store and manage those values.

OutSystems recommendation is to solve this pattern in O11. However, you can opt to proceed with the code conversion and solve it in ODC.

### Solve in O11 (recommended)

To ensure a smoother conversion to ODC, solve this pattern in O11 by adjusting your logic as follows:

1. Create an entity to store the site properties that you need to change at runtime.

1. Replace the logic that assigns values to site properties using the created entity to manage those values. Also, consider creating logic to bootstrap those values.

### Solve in ODC

To solve this pattern in ODC:

1. In the Conversion Assessment Tool, set the **Where To Fix** for this finding as **ODC**.

1. Once your asset is converted to ODC, adjust the logic of your converted app as described above for O11.
