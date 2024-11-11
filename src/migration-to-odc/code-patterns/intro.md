---
summary: This article provides guidelines for refactoring O11 apps to ensure compatibility with OutSystems Developer Cloud (ODC), highlighting various specific areas for manual refactoring in preparation for future automated migration support.
locale: en-us
guid: 469bbfc7-8121-4cd8-8e4f-22b882f8e821
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: 
---

# O11 to ODC migration code patterns

As you plan and prepare your existing O11 app architecture to migrate late to ODC, you must refactor and adjust your O11 implementation for an efficient migration process.

<div class="info" markdown="1">

The OutSystems Migration Toolkit will provide automation in the future to support some of the following patterns. Until then,manually refactor the apps so to unblock the migration.

</div>

Here are some guidelines to refactor your O11 app.

## General

General information about the language elements and architecture in O11 and ODC.

* [Asset consuming O11 system elements](arch-system-element.md)

## Fix in O11

These are the patterns that require modification in the O11 apps.

* [App theme](arch-app-theme.md)
* [Entity, local storage](arch-local-storage.md)
* [Entity, non-read only ](arch-non-read-only-entity.md)
* [Image from an app](arch-image.md)
* [ODC application Block](arch-block.md)
* [ODC application Client Action](arch-client-action.md)
* [ODC application server action](arch-server-action.md)
* [Private structure](arch-priv-struct.md)
* [Process](arch-process.md)
* [Reference not defined in any mapped ODC asset](arch-not-mapped.md)
* [Resource](arch-resource.md)
* [Roles, anonymous and registered ](refactor-anonymous-registered-roles.md)
* [Roles, public](arch-role.md)
* [Screen in mobile app](arch-mobile-screen.md)
* [Script](arch-script.md)
* [Traditional web elements](convert-trad-web.md)

## Not supported

These are the patterns about elements that are not supported in ODC when compared to O11.

* [The Asset cannot contain BPTs](elem-bpt.md)
* [The Asset cannot contain SOAP](elem-soap.md)

## Fix in ODC

These are the patterns that require modification in the ODC apps.

* [Extension](arch-extension.md)
* [Site properties](refactor-siteproperties.md)

