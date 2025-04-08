---
summary: This article provides guidelines for refactoring O11 apps to ensure compatibility with OutSystems Developer Cloud (ODC), highlighting various specific areas for manual refactoring in preparation for future automated migration support.
locale: en-us
guid: 469bbfc7-8121-4cd8-8e4f-22b882f8e821
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: migration, outsystems developer cloud, code refactoring, application lifecycle management, outsystems platform
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - backend developers
  - architects
outsystems-tools:
  - migration toolkit
  - service studio
coverage-type:
  - none
---

# O11 to ODC migration code patterns

<!--

Index of the files in the patterns dir. Updated manually.

A arch-app-theme.md - Asset consuming an Application Theme
A arch-block.md - Asset consuming an ODC application Block
A arch-client-action.md - Asset consuming an ODC application Client Action
A arch-extension.md - Asset consuming an extension
A arch-image.md - Asset consuming an Image from an Application
A arch-local-storage.md - Asset consuming a Local Storage Entity
A arch-mobile-screen.md - Asset consuming a Screen in mobile app
A arch-non-read-only-entity.md - Application consuming a non-read only Entity
A arch-not-mapped.md - Asset consuming a reference that is not defined in any mapped ODC asset
A arch-priv-struct.md - Asset consuming a private Structure
A arch-process.md - Asset consuming a Process
A arch-resource.md - Asset consuming a Resource
A arch-script.md - Asset consuming a Script
A arch-server-action.md - Asset consuming an ODC application Server Action
A arch-system-element.md - Asset consuming O11 system elements
A cannot-open-module.md - Cannot open module
A convert-trad-web.md - Asset consuming a reference to a Traditional Web element
A elem-bpt.md - The Asset cannot contain BPTs
A elem-soap.md - The Asset cannot contain SOAP
A end-user-no-email.md - End users with no email
A outdated-or-broken-dependencies.md - Asset with outdated or broken dependencies
A refactor-anonymous-registered-roles.md - Refactor anonymous and registered roles
A refactor-siteproperties.md - Refactor site properties to be ODC-compatible

-->

As you plan and prepare your existing O11 app architecture to migrate late to ODC, you must refactor and adjust your O11 implementation for an efficient migration process.

<div class="info" markdown="1">

The OutSystems Migration Toolkit will provide automation in the future to support some of the following patterns. Until then, manually refactor the apps to proceed with the migration.

</div>

Here are some guidelines to refactor your O11 app.

## General

General information about the language elements and architecture in O11 and ODC.

* [Asset consuming O11 system elements](arch-system-element.md)

## Fix in O11

These are the patterns that require modification in the O11 apps.

* [Application consuming a non-read only Entity](arch-non-read-only-entity.md)
* [Asset consuming a Local Storage Entity](arch-local-storage.md)
* [Asset consuming a private Structure](arch-priv-struct.md)
* [Asset consuming a Process](arch-process.md)
* [Asset consuming a reference that is not defined in any mapped ODC asset](arch-not-mapped.md)
* [Asset consuming a reference to a Traditional Web element](convert-trad-web.md)
* [Asset consuming a Resource](arch-resource.md)
* [Asset consuming a Script](arch-script.md)
* [Asset consuming an Application Theme](arch-app-theme.md)
* [Asset consuming an Image from an Application](arch-image.md)
* [Asset consuming an ODC application Block](arch-block.md)
* [Asset consuming an ODC application Client Action](arch-client-action.md)
* [Asset consuming an ODC application Server Action](arch-server-action.md)
* [Asset with outdated or broken dependencies](outdated-or-broken-dependencies.md)
* [Asset consuming a reference to the Common Plugin](arch-common-plugin.md)
* [Cannot open module](cannot-open-module.md)
* [End users with no email](end-user-no-email.md)
* [Refactor anonymous and registered roles](refactor-anonymous-registered-roles.md)

## Not supported

These are the patterns about elements that are not supported in ODC when compared to O11.

* [The Asset cannot contain BPTs](elem-bpt.md)
* [The Asset cannot contain SOAP](elem-soap.md)

## Fix in ODC

These are the patterns that require modification in the ODC apps.

* [Asset consuming an extension](arch-extension.md)
* [Refactor site properties to be ODC-compatible](refactor-siteproperties.md)
