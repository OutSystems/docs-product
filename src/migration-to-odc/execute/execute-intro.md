---
summary: "OutSystems 11 (O11) to ODC app conversion: prerequisites, limitations, and the three-step process to migrate code, data, and end users."
guid: 903fe9c6-5b0c-4c22-929a-abd06a3763e7
locale: en-us
app_type: mobile apps, reactive web apps, traditional web apps
platform-version: o11
figma:
tags:
  - Data
  - End-users
  - Infrastructure
  - Lifecycle
audience:
  - Developer
  - Platform administrator
outsystems-tools:
  - service studio
  - conversion assessment tool
coverage-type:
  - apply
topic:
  - conversion-prerequisites
isautopublish: true
---

# Execute app conversion

<div class="info" markdown="1">

App conversion (code conversion and data migration) is in Beta. For more information about Beta features, refer to [OutSystems product releases](https://success.outsystems.com/support/release_notes/outsystems_product_releases/#beta). If you want to try this new capability, [sign up for the beta](https://www.outsystems.com/o11-odc-migration).

</div>

Once the O11 apps in a [conversion plan](https://www.outsystems.com/tk/redirect?g=ab447daa-dffc-4374-8ae6-986c8f3d63c4) are [prepared for ODC](https://www.outsystems.com/tk/redirect?g=14a67d54-aa12-45bc-8262-48c9f2a2780c), you can start executing its conversion. After completing the conversion process for those apps, you should have:

* The O11 app's code converted, and its data and end users migrated to ODC.

* The O11 entities mapped to their ODC counterparts.

## Limitations

Consider the following limitations:

* App conversion **isn't supported** for O11 Personal environments

* OutSystems Partners can execute [code conversion](execute-how-to-migrate-code.md) from O11 Cloud demo environments, but [data migration](execute-how-to-migrate-data.md) isn't supported.

### Temporary limitations

OutSystems is working to improve the app conversion capability. Meanwhile, consider these additional limitations:

* App conversion **isn't yet supported** for the following infrastructure setup:

    * O11 self-managed infrastructures
    * Hybrid O11 infrastructures
    * O11 infrastructures with additional pipelines

* When executing app conversion to [ODC self-hosted](https://www.outsystems.com/tk/redirect?g=2433ca96-db20-493f-b04b-0e82e33c424e) organizations, [data migration](execute-how-to-migrate-data.md) isn't yet supported to self-hosted stages. Data migration can only be executed to the Development stage, managed in the OutSystems Cloud.

## Prerequisites

Before you start converting your O11 apps to ODC, make sure the following requirements are met:

* You have an enterprise [O11 cloud infrastructure](https://www.outsystems.com/tk/redirect?g=079418c8-7a3d-4b5e-9c13-c1ae7a1f122e). Take into account the [limitations](#limitations) for the O11 infrastructure setup.

* Your O11 infrastructure has **LifeTime 11.29.0 or later**. Refer to [O11-ODC connectivity](https://www.outsystems.com/tk/redirect?g=b6c0c043-0b0a-4825-9271-afaa60bd2ee9) for further details.

    <div class="info" markdown="1">

    If you are already executing O11 to ODC app conversion using a previous version of LifeTime, your existing LifeTime service account access token continues to work until it expires. Creating or regenerating a service account access token specifically for O11 to ODC conversions or interoperability requires **LifeTime 11.29.0** or later.

    </div>

* The [O11 to ODC architecture mapping](https://www.outsystems.com/tk/redirect?g=6901e523-4fa3-42bd-b37e-880e06d5cb62) has been defined in the [Conversion Assessment Tool](https://www.outsystems.com/tk/redirect?g=29920fad-9efd-45ae-a4e4-212705fceb65).

* The [O11 to ODC architecture has been validated](https://www.outsystems.com/tk/redirect?g=0b89d709-a914-4f96-8869-3c653149576d).

* Your O11 apps were [adjusted to be ODC-compatible](https://www.outsystems.com/tk/redirect?g=99ad22b2-8292-4f3a-8d71-0d8ddc11402a).

* The adjusted O11 apps were tested and work as expected.

## App conversion process

Before you start converting the apps from an O11 infrastructure to ODC, you need to [configure the conversion settings](execute-connect-to-tool.md).

Then, these are the main steps to convert the apps in a [conversion plan](https://www.outsystems.com/tk/redirect?g=ab447daa-dffc-4374-8ae6-986c8f3d63c4) to ODC:

1. [Convert the apps' code](execute-about-migrate-code.md).

1. [Configure the converted apps](execute-configure-migrated-apps.md).

1. [Migrate the apps' data](execute-about-migrate-data.md).
