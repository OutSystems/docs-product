---
summary: Learn more about converting O11 code to ODC
tags: code conversion, app conversion kit, conversion assessment tool, version tagging, environment management
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
  - conversion assessment tool
coverage-type:
  - apply
---

# Convert code

<div class="info" markdown="1">

This article only applies to customers with access to the App Conversion Kit.

</div>

![Diagram showing the current convert code step in the conversion process](images/execute-migrate-code-diag.png "Convert code")

Once the O11 apps in your [conversion plan](../plan/plan-define-migration-plans.md) are [prepared for ODC](../prepare/prep-intro.md), you are ready to convert their O11 code using the app conversion console in ODC Portal.

The app conversion console enables you to:

* Automatically convert and merge your O11 modules into ODC apps and libraries based on the [mapping defined in the Conversion Assessment tool](../plan/plan-map-apps.md).

* Download the converted ODC apps so you can edit them in ODC Studio to fix the identified issues and get them ready to publish.

For detailed information about how to convert code using the tool, refer to [Code conversion using the tool](execute-how-to-migrate-code.md).

## Tagging your apps

When converting apps from O11 to ODC, the latest tagged version of the app is fetched from the source environment. This is the version that will be converted to ODC.

After you've made all the changes to your app and before you start the code conversion process, ensure that you have tagged your app in the environment from where you want to convert the app.

For more information about tagging your apps, refer to [Tag a Version](../../deploying-apps/tag-a-version.md).
