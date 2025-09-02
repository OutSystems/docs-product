---
summary: Learn more about the step-by-step process when migrating your o11 apps and data to ODC.
guid: 903fe9c6-5b0c-4c22-929a-abd06a3763e7
locale: en-us
app_type: mobile apps, reactive web apps, traditional web apps
platform-version: o11
figma: https://www.figma.com/design/daglmSUESdKw9J3HdT87a8/O11-to-ODC-migration?node-id=2139-92
tags: data migration, app migration, low-code platforms, migration process, migration tools
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - platform administrators
  - architects
outsystems-tools:
  - service studio
  - migration assessment tool
coverage-type:
  - apply
---

# Execute the migration

<div class="info" markdown="1">

This article only applies to customers with access to the Migration Kit. 

</div>

Once the O11 apps in a [migration plan](../plan/plan-define-migration-plans.md) are [prepared for ODC](../prepare/prep-intro.md), you can start executing its migration. After completing the migration process for those apps, you should have:

* The O11 app's code, data, and end users migrated to ODC. 

* The O11 entities mapped to their ODC counterparts.

## Prerequisites

Before you start migrating your apps, ensure the following:

* [The O11 to ODC architecture mapping has been defined in the tool](../plan/plan-map-apps.md).

* [The O11 to ODC architecture has been validated](../plan/plan-assess-refactor.md).

* [The compatibility of your O11 apps with ODC](../prepare/prep-refactor-o11-apps.md).

* The adjusted O11 apps were tested and work as expected.

## Step-by-step migration process

The following diagram shows the steps involved in the migration process.

![Diagram showing the steps involved in the migration process](images/execute-one-shot-migration-diag.png "Migration process")

To migrate your apps, follow these steps:

1. [Connect to the Migration Assessment Tool](execute-connect-to-tool.md).

1. [Migrate the apps' code](execute-about-migrate-code.md).

1. [Configure the migrated apps](execute-configure-migrated-apps.md).

1. [Migrate the apps' data](execute-about-migrate-data.md).
