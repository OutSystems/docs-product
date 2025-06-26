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

As you plan and prepare your existing O11 app architecture, there are code patterns that you should adapt or omit in your O11 apps to ensure a smooth migration to ODC.

<div class="info" markdown="1">

OutSystems is working on migration automation capabilities to support some of these patterns. Until then, you can use this information to help you [plan your migration](../migration-intro.md#stage-1-plan-for-the-o11-app-migration).

</div>

If you have access to the Migration Kit, the Migration Assessment Tool identifies some of the code patterns that you need to handle to achieve a successful migration of your apps.

You have to follow different approaches, depending on the pattern:

* [Fix in O11](#fix-in-o11) - Requires changes in the O11 app before proceeding with the migration to ODC.

* [Fix in ODC](#fix-in-odc) - Requires changes in the ODC app after the migration.

* [Optional](#optional) - Requires changes in the O11 app or in the ODC app, depending on the approach you choose.

* [Not yet supported](#not-supported) - ODC doesn't yet support the functionality, or the Migration Kit doesn't yet support the code pattern.

## Fix in O11

These are the patterns that require changes in the O11 apps:

* [Application consuming a non-read only Entity](arch-non-read-only-entity.md)
* [Asset consuming a Local Storage Entity](arch-local-storage.md)
* [Asset consuming a private Structure](arch-priv-struct.md)
* [Asset consuming a Process](arch-process.md)
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

## Fix in ODC

These are the patterns that require changes in the ODC apps:

* [Asset consuming O11 platform system elements](arch-system-element.md)
* [Asset consuming O11 user management elements](arch-user-mng-elements.md)
* [Asset consuming an extension](arch-extension.md)
* [Refactor site properties to be ODC-compatible](refactor-siteproperties.md)
* [Asset using unsupported O11 built-in function](elem-built-in-function.md)
* [Application with SQL Node](elem-sql-adapt.md)
* [Asset contains REST APIs using built-in OAuth 2.0 authentication flow](elem-rest-oauth2.md)
* [Asset with SAP BAPI connection](elem-sap.md)
* [Adapt login and logout flow of migrated apps](execute-adapt-login-flow.md)
* [Aggregate or SQL node referenced outside its scope](aggregate-sql-scope.md)

## Optional

These are the patterns that can be either solved in O11 or in ODC:

* [Asset consuming a Forge component](arch-forge.md)
* [Asset consuming an O11 app that is not mapped to any ODC asset](arch-not-mapped.md)

## Not yet supported

These are the patterns about elements that aren't supported in ODC, or that the Migration Kit doesn't yet support:

* [The Asset cannot contain BPTs](elem-bpt.md)
* [The Asset cannot contain SOAP](elem-soap.md)
* [The Asset cannot contain modules having a user provider different than Users](elem-user-provider.md)
* [Asset consuming O11 Business Process (BPT) elements](arch-bpt-elements.md)
* [The Asset cannot contain multi-tenant modules](elem-multi-tenant.md)
