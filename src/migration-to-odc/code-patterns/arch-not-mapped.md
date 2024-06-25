---
summary: 
locale: en-us
guid: 0cd0a808-f2c4-4c00-ac10-f25e5efecb71
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
helpids: 30535
---
# Asset consuming a reference that is not defined in any mapped ODC asset

The ODC Asset consumes a dependency that belongs to an app mapped that isn't mapped to an ODC Asset.
This means that the ODC Asset will have broken references once you migrate it to ODC.

## How to solve

You can decide to solve this pattern in O11, before migrating code, or in ODC, after migrating the code.

### Solve in O11

Review the review the O11 to ODC architecture mapping by mapping the O11 producer App to an ODC App or Library.

### Solve in ODC

After migrating the asset to ODC, fix the broken dependency.
