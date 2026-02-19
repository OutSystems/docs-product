---
summary: This article provides guidelines for refactoring O11 apps to ensure compatibility with OutSystems Developer Cloud (ODC), highlighting various specific areas for manual refactoring in preparation for future automated conversion to ODC.
locale: en-us
guid: 469bbfc7-8121-4cd8-8e4f-22b882f8e821
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: app conversion, outsystems developer cloud, code refactoring, application lifecycle management, outsystems platform
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - backend developers
  - architects
outsystems-tools:
  - app conversion kit
  - service studio
coverage-type:
  - none
---

# O11 to ODC conversion patterns

This page describes the app patterns you need to consider to ensure a smooth conversion of your O11 apps to ODC.

<div class="info" markdown="1">

OutSystems is working on conversion automation capabilities to support some of these patterns. Until then, you can use this information to help you [plan your conversion](../migration-intro.md#stage-1-plan-for-the-o11-app-migration).

The Conversion Assessment Tool identifies some of the code patterns that you need to handle to achieve a successful conversion of your apps.

</div>

You must handle different patterns during the several conversion phases:

* [Before the conversion](#handle-o11), you must prepare your O11 apps to be ODC compatible and ready to convert.  

* [After the conversion](#handle-odc), you must make some adjustments to ensure your new ODC apps can be published.

## Patterns to handle in O11 {#handle-o11}

These are the patterns that require changes in the O11 apps before proceeding with the conversion to ODC.

### Code

* [Application consuming a non-read only Entity](arch-non-read-only-entity.md)
* [Asset consuming a Local Storage Entity](arch-local-storage.md)
* [Asset consuming a private Structure](arch-priv-struct.md)
* [Asset consuming a Process](arch-process.md)
* [Asset consuming a Resource](arch-resource.md)
* [Asset consuming a Script](arch-script.md)
* [Asset consuming an Application Theme](arch-app-theme.md)
* [Asset consuming an Image from an Application](arch-image.md)
* [Asset consuming an ODC application Block](arch-block.md)
* [Asset consuming an ODC application Client Action](arch-client-action.md)
* [Asset consuming an ODC application Server Action](arch-server-action.md)
* [Asset consuming a reference to the Common Plugin](arch-common-plugin.md)
* [Asset consuming a Traditional Web module](convert-trad-web.md) - Optionally, you can choose to solve this pattern in ODC after the conversion.
* [Asset consuming a Forge component](arch-forge.md) - Optionally, you can choose to solve this pattern in ODC after the conversion.
* [Asset consuming an O11 app that is not mapped to any ODC asset](arch-not-mapped.md) - Optionally, you can choose to solve this pattern in ODC after the conversion.
* [Asset consuming its own service action](arch-internal-service-action.md) - Optionally, you can choose to solve this pattern in ODC after the conversion.
* [Unsupported Delete Rule to an entity from another app](elem-unsupported-delete-rule.md) - Optionally, you can choose to solve this pattern in ODC after the conversion.
* [Library with cyclic dependency to another ODC library](arch-lib-cyclic.md)
* [Asset cannot contain Traditional Web modules](elem-trad-web.md)
* [Asset consuming REST API with multipart request](elem-rest-consume-multipart.md)
* [Refactor anonymous and registered roles](refactor-anonymous-registered-roles.md)

### Data {#data-patterns}

* [Large binaries validation](data-large-binaries-validation.md)
* [Large text validation](data-large-text-validation.md)
* [User email validation](data-user-email-validation.md)

### App configuration

* [Align persistent login timeout](persistent-login-timeout.md)

## Patterns to handle in ODC {#handle-odc}

These are the patterns that require changes in the converted ODC apps before you publish them.

### Code

* [Asset consuming O11 platform system elements](arch-system-element.md)
* [Asset consuming O11 user management elements](arch-user-mng-elements.md)
* [Asset consuming an extension](arch-extension.md)
* [Asset using unsupported O11 built-in function](elem-built-in-function.md)
* [Application with SQL Node](elem-sql-adapt.md)
* [Asset contains REST APIs using built-in OAuth 2.0 authentication flow](elem-rest-oauth2.md)
* [Asset with SAP BAPI connection](elem-sap.md)
* [Adapt login and logout flow of converted apps](execute-adapt-login-flow.md)
* [Aggregate or SQL node referenced outside its scope](aggregate-sql-scope.md)

### App configuration

* [Refactor site properties to be ODC-compatible](refactor-siteproperties.md)
* [Update the URLs of consumed REST API endpoints](update-url-consumed-rest-endpoint.md)

## Limitations

Conversion to ODC isn't yet supported for the following patterns.

### Code

* [SOAP](elem-soap.md)
* [Apps containing BPT elements](elem-bpt.md) or [consuming BPT elements](arch-bpt-elements.md)
* [Modules configured with a user provider different than Users](elem-user-provider.md)
* [Multi-tenant modules](elem-multi-tenant.md)

### Data

* [Modules with multiple active tenants](data-multiple-tenants.md)
* [Modules with a user provider different than Users](data-user-provider.md)

### Infrastructure

* [Self-managed infrastructures](infra-self-managed.md)
* [Additional pipelines](infra-additional-pipelines.md)
