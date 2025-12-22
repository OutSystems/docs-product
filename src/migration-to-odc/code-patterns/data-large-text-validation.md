---
guid: c488d2e0-29de-4728-a770-3a31006d7e59
locale: en-us
summary: This article provides guidelines for handling text data with length greater than 100 000 000 characters before converting O11 apps to OutSystems Developer Cloud (ODC).
figma: 
coverage-type:
  - unblock
topic: 
app_type: mobile apps,reactive web apps
platform-version: o11
audience: 
  - data engineers
  - full stack developers
tags: data migration, text attributes, outsystems 11, odc conversion, data validation
outsystems-tools:
  - conversion assessment tool
helpids: 30720
---

# Large text validation

This pattern identifies an entity in the assessed environment with a **Text** data type record exceeding 100 000 000 characters in length, which is the maximum allowed length for text data migration using the [O11 to ODC App Conversion Kit EAP](https://www.outsystems.com/o11-odc-migration/).

## How to solve

You must solve this pattern in the O11 source environment before proceeding with the data migration to ODC.

### Solve in O11

<div class="info" markdown="1">

If you are only preparing for the migration, at present, OutSystems recommends not making any changes to your data. OutSystems is working on automation capabilities to migrate text data with length greater than 100 000 000 characters.

</div>

To proceed with the migration of your OutSystems 11 apps, move the text data exceeding 100 000 000 characters to an external repository (for example, Amazon S3, or Azure Blob Storage). Otherwise, you can’t proceed with the data migration to ODC.
