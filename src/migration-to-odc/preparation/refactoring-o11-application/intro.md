---
summary: This article provides guidelines for refactoring O11 apps to ensure compatibility with OutSystems Developer Cloud (ODC), highlighting various specific areas for manual refactoring in preparation for future automated migration support.
locale: en-us
guid: 469bbfc7-8121-4cd8-8e4f-22b882f8e821
app_type: traditional web apps, mobile apps, reactive web appsc
platform-version: o11
figma: 
---

# About refactoring O11 apps to be ODC compatible

As you plan and prepare your existing O11 app architecture to smoothly migrate to ODC at a later point, you must refactor and adjust your O11 implementation to ease the migration process. 

<div class="info" markdown="1">

The OutSystems Migration Toolkit will provide automation in the future to support some of the following refactorings. Until then, you’ll have to manually refactor the app so that the migration is not blocked.

</div>

Here's some guidelines to refactor your O11 app:

* [Refactor anonymous and registered roles](refactor-anonymous-registered-roles.md)
* [Refactor BPT](refactor-bpt.md)
* [Refactor SOAP](refactor-soap.md)
* [Refactor public roles](refactor-public-roles.md)
* [Refactor public structures](refactor-public-structures.md)
* [Refactor system entities](refactor-systementities.md)
* [Refactor site properties](refactor-siteproperties.md)
* [Refactor extensions](refactor-extensions.md)

