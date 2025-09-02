---
summary: Learn more about migrating O11 code to ODC
tags: code migration, migration kit, migration assessment tool, version tagging, environment management
guid: 4e0c455a-c243-4daa-aa69-16982558893b
locale: en-us
app_type: mobile apps, reactive web apps, traditional web apps
platform-version: o11
figma: https://www.figma.com/design/daglmSUESdKw9J3HdT87a8/O11-to-ODC-migration?node-id=2119-4
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
  - migration assessment tool
coverage-type:
  - apply
---

# Migrate code

<div class="info" markdown="1">

This article only applies to customers with access to the Migration Kit.

</div>

![Diagram showing the current migrate code step in the migration process](images/execute-migrate-code-diag.png "Migrate code")

Once the O11 apps in your [migration plan](../plan/plan-define-migration-plans.md) are [prepared for ODC](../prepare/prep-intro.md), you are ready to migrate their O11 code using the migration console in ODC Portal.

The migration console enables you to:

* Automatically convert and merge your O11 modules into ODC apps and libraries based on the [mapping defined in the Migration Assessment tool](../plan/plan-map-apps.md).

* Download the migrated ODC apps so you can edit them in ODC Studio to fix the identified issues and get them ready to publish.

For detailed information about how to migrate code using the tool, refer to [Code migration using the tool](execute-how-to-migrate-code.md).

## Tagging your apps

When migrating apps from O11 to ODC, the latest tagged version of the app is fetched from the source environment. This is the version that's migrated to ODC.

After you've made all the changes to your app and before you start the code migration process, ensure that you have tagged your app in the environment from where you want to migrate the app.

For more information about tagging your apps, refer to [Tag a Version](../../deploying-apps/tag-a-version.md).
