---
guid: 61073980-baa9-4391-93f5-921d5ca0517a
locale: en-us
summary: This article provides guidelines for handling binary data bigger than 20 MB before converting O11 apps to OutSystems Developer Cloud (ODC).
figma:
coverage-type:
  - unblock
topic:
app_type: reactive web apps,mobile apps
platform-version: o11
audience:
  - data engineers
  - full stack developers
tags: data migration, binary attributes, outsystems 11, odc conversion, data validation
outsystems-tools:
  - service studio
helpids: 30660
---

# Large binaries validation

This pattern identifies an entity in the assessed environment with a **binary data** record exceeding 20 MB, which is the maximum allowed size for data migration using the App Conversion Kit.

## How to solve

You must solve this pattern in the O11 source environment before proceeding with the data migration to ODC.

### Solve in O11

<div class="info" markdown="1">

If you are only preparing for the conversion, at present, OutSystems recommends not making any changes to your data. OutSystems is working on automation capabilities to convert binary data bigger than 20 MB.

</div>

To proceed with the conversion of your OutSystems 11 applications, move the binary data exceeding 20 MB to an external repository (for example, Amazon S3, or Azure Blob Storage). Otherwise, you can’t proceed with the data migration to ODC.
