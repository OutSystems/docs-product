---
summary: This article provides guidelines for refactoring O11 apps to ensure compatibility with OutSystems Developer Cloud (ODC), highlighting various specific areas for manual refactoring in preparation for future automated migration support.
locale: en-us
guid: 469bbfc7-8121-4cd8-8e4f-22b882f8e821
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: 
---

# O11 to ODC migration code patterns

As you plan and prepare your existing O11 app architecture to smoothly migrate to ODC at a later point, you must refactor and adjust your O11 implementation to ease the migration process.

<div class="info" markdown="1">

The OutSystems Migration Toolkit will provide automation in the future to support some of the following refactorings. Until then, you’ll have to manually refactor the app so that the migration is not blocked.

</div>

Here's some guidelines to refactor your O11 app:

* [Asset consuming an Application Theme](arch-app-theme.md)
* [Asset consuming an ODC application Block](arch-block.md)
* [Asset consuming an ODC application Client Action](arch-client-action.md)
* [Asset consuming an extension](arch-extension.md)
* [Asset consuming an Image from an Application](arch-image.md)
* [Asset consuming a Local Storage Entity](arch-local-storage.md)
* [Asset consuming a Screen in mobile app](arch-mobile-screen.md)
* [Application consuming a non-read only Entity](arch-non-read-only-entity.md)
* [Asset consuming a reference that is not defined in any mapped ODC asset](arch-not-mapped.md)
* [Asset consuming a private Structure](arch-priv-struct.md)
* [Asset consuming a Process](arch-process.md)
* [Asset consuming a Resource](arch-resource.md)
* [Asset consuming a Role](arch-role.md)
* [Asset consuming a Script](arch-script.md)
* [Asset consuming an ODC application Server Action](arch-server-action.md)
* [Asset consuming O11 system elements](arch-system-element.md)
* [The Asset cannot contain BPTs](elem-bpt.md)
* [The Asset cannot contain SOAP](elem-soap.md)
* [End users with no email](end-user-no-email.md)
* [Refactor anonymous and registered roles](refactor-anonymous-registered-roles.md)
* [Refactor site properties](refactor-siteproperties.md)
