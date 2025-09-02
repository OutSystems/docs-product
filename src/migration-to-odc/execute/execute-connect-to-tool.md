---
summary: Learn how to connect to the Migration Assessment Tool before migrating yourr O11 apps and data to ODC
tags: migration, migration assessment tool, application deployment, configuration, authentication
guid: a4a2aea6-eee3-4224-8f6f-8f84da3057b2
locale: en-us
app_type: mobile apps, reactive web apps, traditional web apps
platform-version: o11
figma: https://www.figma.com/design/daglmSUESdKw9J3HdT87a8/O11-to-ODC-migration?node-id=2114-1320
audience:
  - platform administrators
  - full stack developers
  - tech leads
outsystems-tools:
  - lifetime
  - service studio
coverage-type:
  - apply
---

# Connect to Migration Assessment Tool

<div class="info" markdown="1">

This article only applies to customers with access to the Migration Kit.

</div>

Before you can start migrating your O11 apps and data to ODC, you must connect to the Migration Assessment Tool. By doing this, the [migration plans](../plan/plan-define-migration-plans.md) you've defined in the Migration Assessment Tool are available in the ODC migration console.

## Prerequisites

* You must have the **O11 Migrations** > **Manage configurations** permission in your ODC tenant.

* The [Migration Assessment Tool has been set up in O11](../setup-assessement-tool.md).

## Connect to Migration Assessment Tool

![Diagram showing the current connect to migration assessment tool step in the migration process](images/execute-connect-to-tool-diag.png "Connect to Migration Assessment Tool")

To connect to the Migration Assessment Tool, follow these steps:

1. Log in to the ODC Portal.

1. Under **MIGRATE O11**, click **Configurations**.

1. Click **Edit**.

1. Enter the following values for **O11 LifeTime**:

    * **URL**: The URL of the LifeTime environment where you installed the Migration Assessment Tool engine.

    * **Authentication Token**: The authentication token of the service account used to access the LifeTime environment.

    For more information about the Migration Assessment Tool and these values, refer to [Set up the Migration Assessment Tool](../setup-assessement-tool.md).

1. Click **Save**.

## Next steps

* Ensure the IT users migrating the code have the **O11 Migrations** > **Migrate O11 code** permission in the ODC tenant.

* [Migrate code](execute-about-migrate-code.md).
