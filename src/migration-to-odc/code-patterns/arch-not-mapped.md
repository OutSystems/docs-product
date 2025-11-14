---
summary: Learn how to handle dependencies that are not mapped to any ODC asset during the assessment of your O11 to ODC conversion.
locale: en-us
guid: 0cd0a808-f2c4-4c00-ac10-f25e5efecb71
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
helpids: 30535
tags: application upgrade, dependency mapping, odc conversion, architecture mapping, outsystems platform
audience:
  - full stack developers
  - architects
  - platform administrators
outsystems-tools:
  - service studio
coverage-type:
  - unblock
  - understand
---

# Asset consuming an O11 app that is not mapped to any ODC asset

The ODC asset consumes a dependency that belongs to an O11 app that isn't mapped to any ODC asset. This means that the ODC asset will have broken references once you convert it to ODC.

## How to solve

This pattern can be solved in O11 or in ODC. Start by checking if the functionality provided by the O11 app that the asset consumes is already available in ODC.

If the functionality is **already available in ODC**, for example, because it was manually converted to ODC or it's provided by an ODC Forge component, you can choose to [solve this pattern in ODC](#solve-odc). Otherwise, you should [solve this pattern in O11](#solve-o11).

### Solve in ODC { #solve-odc }

To solve this pattern in ODC:

1. In the Conversion Assessment Tool, set the **Where To Fix** for this finding as **ODC**.

1. Once the consumer asset is converted to ODC, update it in ODC Studio to consume the ODC app or component that offers the same functionality as the O11 app your asset was consuming.

### Solve in O11 { #solve-o11 }

Review the O11 to ODC architecture mapping, and map the O11 producer app to an ODC asset.
