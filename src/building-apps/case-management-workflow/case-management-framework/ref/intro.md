---
tags: Case Management; Case Management framework;
summary: Explore the architecture and capabilities of the Case Management framework in OutSystems 11 (O11) for streamlined business process app development.
guid: 8149ad32-7c20-458b-92d4-2e2dac78f781
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=4376:1916
---

# Case Management framework reference

The Case Management framework accelerates the creation of custom-fit business process and case management apps, by extending the capabilities provided by [Business Process Technology (BPT)](../../../processes/intro.md).

## Framework architecture

![Diagram illustrating the architecture of the Case Management framework, including API modules, Business Logic modules, and Core Services modules](images/cmf-archi.png "Case Management Framework Architecture")

The **API modules** include the actions that you can use in your applications:

* The [Case Services API](auto/CaseServices_API.final.md) includes actions used to interact with cases related to a Process.
* The [Case Configurations API](auto/CaseConfigurations_API.final.md) includes actions used to configure a case in your app.
* The [Case Process Configurations API](auto/CaseProcessConfigurations_API.final.md) includes actions used to configure the underlying BPT process associated with a case.

The Business Logic, or **BL**, **modules** include the process logic to support Case Management framework.

The Core Services, or **CS**, **modules** include entities to support case management concepts and functionality.

Your app should interact with Case Management framework mostly through the API modules.
