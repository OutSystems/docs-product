---
summary: OutSystems 11 (O11) to OutSystems Developer Cloud (ODC) app conversion planning covers app mapping, testing, downtime, and data migration.
locale: en-us
guid: 788a3d99-a2fe-4fa2-b868-d2851cd2ffb8
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: app conversion, o11 to odc conversion, application portfolio management, conversion strategies, conversion planning
audience:
  - Developer
  - Architect
  - Tech lead
  - Platform administrator
outsystems-tools:
  - service studio
  - app conversion kit
coverage-type:
  - understand
  - apply
isautopublish: true
---

# Plan app conversion

In the planning phase of the [app conversion process](../migration-intro.md), you get an understanding of the future ODC architecture for the O11 apps you want to convert, and assess their ODC-readiness.

When you start planning the conversion of your first set of O11 apps to ODC, you need to [set up the Conversion Assessment Tool](../setup-assessement-tool.md).

## Account for the conversion effort { #account-for-effort }

The following aspects significantly affect your conversion effort. Account for them when you plan your conversion timeline.

**Key recommendations:** allocate sufficient time for testing, account for downtime, freeze development on apps you're converting, and plan extra time for components without an ODC equivalent.

### Manual intervention and testing { #effort-testing }

Manual intervention and testing affect your conversion effort in the following ways:

* Converted apps need manual intervention and development effort beyond the automated conversion process. Refer to [Adjust converted code](https://www.outsystems.com/tk/redirect?g=007740bc-589f-4f26-8b65-3dc1d7991785) for details.
* Some O11 constructs, extensions, and Forge components don't have an ODC equivalent. Identify these gaps early, and plan for alternative solutions or custom development to replace any missing functionality. Refer to the [code patterns](../code-patterns/intro.md) for common constructs that require adjustments.
* Test all converted assets thoroughly before you deploy them to production.

### Development freeze for converted apps { #effort-freeze }

After you convert an O11 app's code to ODC, avoid further changes to that app in O11. Changing a converted app in O11 may require reconverting it, to ensure the data migration and code conversion for dependent apps run as expected. Refer to [Convert code](https://www.outsystems.com/tk/redirect?g=4e0c455a-c243-4daa-aa69-16982558893b) for details on the code conversion process.

### Entity and data schema changes { #effort-entities }

If you change entities in O11 after an initial code conversion, including adding new ones, run a new code conversion before migrating data. Creating entities manually on both sides doesn't work because this approach doesn't preserve the internal keys that data migration relies on. Refer to [Troubleshooting O11 to ODC conversion issues](https://www.outsystems.com/tk/redirect?g=f684fea5-c98e-488e-8003-458f874b4704) for more details.

### Data migration downtime and results { #effort-data-migration }

Data migration affects your O11 and ODC apps in the following ways:

* Data migration temporarily stops the ODC apps on the target stage, and a **Production Final** data migration also stops the app in the O11 production environment, so account for downtime.
* When you don't use **Production Final**, running data migration while apps are actively in use in O11 risks producing invalid data (for example, foreign keys referencing non-existent records) or row count discrepancies between O11 and ODC.
* The migration also truncates the migrated apps' ODC database tables at the start of the process, and the data migration then repopulates them to mirror the O11 database, so ODC loses any data that existed only there before the migration.

Refer to [Migrate data](https://www.outsystems.com/tk/redirect?g=8073a9f1-f82c-4c11-991f-248ae59b09a9) for details on the data migration process.

### Application size and complexity { #effort-complexity }

The more O11 modules you merge into a single ODC asset, the larger and more complex the resulting app becomes, which can slow down ODC Studio and the publish process, and make the app harder to manage.

When you [map your O11 apps to ODC assets](plan-map-in-tool.md) and [define your conversion plans](plan-define-migration-plans.md), consider breaking very large apps into smaller, manageable apps whenever possible.

## Main planning steps { #planning-steps }

Follow these steps to plan your O11 to ODC conversion:

1. [Map O11 to ODC architecture](plan-map-apps.md).

    In this step, you [design the to-be ODC architecture blueprint](plan-design-odc-arch.md) for the O11 apps you want to convert, and [map the O11 apps to ODC assets](plan-map-in-tool.md) in the Conversion Assessment Tool.

1. [Define conversion plans](plan-define-migration-plans.md) to group sets of apps that you want to  convert independently.

1. [Assess the ODC-readiness](plan-assess-refactor.md) of your O11 apps.
