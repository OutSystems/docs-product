---
summary: Learn more about the step-by-step process when converting your o11 apps and data to ODC.
guid: 903fe9c6-5b0c-4c22-929a-abd06a3763e7
locale: en-us
app_type: mobile apps, reactive web apps, traditional web apps
platform-version: o11
figma: https://www.figma.com/design/daglmSUESdKw9J3HdT87a8/O11-to-ODC-migration?node-id=2139-92
tags: data migration, app conversion, low-code platforms, conversion process, conversion tools
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - platform administrators
  - architects
outsystems-tools:
  - service studio
  - conversion assessment tool
coverage-type:
  - apply
---

# Execute app conversion

<div class="info" markdown="1">

This article only applies to customers with access to the App Conversion Kit. 

</div>

Once the O11 apps in a [conversion plan](../plan/plan-define-migration-plans.md) are [prepared for ODC](../prepare/prep-intro.md), you can start executing its conversion. After completing the conversion process for those apps, you should have:

* The O11 app's code converted, and its data and end users migrated to ODC.

* The O11 entities mapped to their ODC counterparts.

## Prerequisites

Before you start converting your apps, ensure the following:

* [The O11 to ODC architecture mapping has been defined in the tool](../plan/plan-map-apps.md).

* [The O11 to ODC architecture has been validated](../plan/plan-assess-refactor.md).

* [The compatibility of your O11 apps with ODC](../prepare/prep-refactor-o11-apps.md).

* The adjusted O11 apps were tested and work as expected.

## Step-by-step conversion process

The following diagram shows the steps involved in the conversion process.

![Diagram showing the steps involved in the conversion process](images/execute-conversion-diag.png "Conversion process")

To convert your apps, follow these steps:

1. [Connect to the Conversion Assessment Tool](execute-connect-to-tool.md).

1. [Convert the apps' code](execute-about-migrate-code.md).

1. [Configure the converted apps](execute-configure-migrated-apps.md).

1. [Migrate the apps' data](execute-about-migrate-data.md).
