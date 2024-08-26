---
summary: Learn more about the step-by-step one shot process when migrating your o11 apps and data to ODC
tags: 
guid: f3102151-e4fb-415a-91da-9c16dc56fe2e
locale: en-us
app_type: mobile apps, reactive web apps, traditional web apps
platform-version: o11
figma: https://www.figma.com/design/daglmSUESdKw9J3HdT87a8/O11-to-ODC-migration?node-id=2139-92
---

# Execute one shot migration

<div class="info" markdown="1">

This article only applies to customers with access to the Migration Kit. 

</div>

One-shot migration is ideal for smaller, low-code projects with two or fewer business apps and up to 300 application objects. After completing the one-shot migration, you should have your:

* O11 app code, data, and end users migrated to ODC.

* O11 entities mapped to their ODC counterparts.

* Migrated, tested, and published ODC apps.

## Prerequisites

Before you start migrating apps, ensure the following:

* [The Migration Assessment Tool is set up](../setup-assessement-tool.md).

* [The O11 to ODC architecture mapping has been defined in the tool](../plan/plan-map-apps.md).

* [The O11 to ODC architecture has been validated](../plan/plan-assess-refactor.md).

* [The compatibility of your O11 apps with ODC ](../prepare/prep-refactor-o11-apps.md)

## Step-by-step migration process

The following diagram shows the steps involved in the one-shot migration process.

![Diagram showing the steps involved in the one-shot migration process](images/execute-one-shot-migration-diag.png "One-shot migration process")

To migrate your apps, follow these steps:

1. [Connect to the Migration Assessment Tool](execute-connect-to-tool.md).

1. [Migrate code](execute-how-to-migrate-code.md).

1. [Configure migrated apps](execute-configure-migrated-apps.md).

1. [Migrate data](execute-about-migrate-data.md).
