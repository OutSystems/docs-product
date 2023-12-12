---
summary: This article outlines steps for preparing O11 apps for migration to OutSystems Developer Cloud (ODC), focusing on adopting best practices in architecture and domain-driven design for a smooth transition.
locale: en-us
guid: ff542837-31ee-4773-a3b1-91f579fa73ba
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: 
---

# Prepare O11 application architecture

## Overview 

The preparation phase is a period of refactoring your O11 apps so that they're ready for migration to the ODC platform.This document is intended for O11 application architects who are planning and preparing the existing O11 application architecture to enable smooth migration to ODC in the future.

## Prepare existing O11 apps to migrate to ODC

Here are the steps to help you prepare and refactor your existing O11 apps to enable smooth and seamless migration to ODC at a later point.

Step 1:  Adopt the architecture canvas best practices

Application [architecture canvas](https://success.outsystems.com/documentation/best_practices/architecture/designing_the_architecture_of_your_outsystems_applications/the_architecture_canvas/#) is a framework to support application architecture design in OutSystems.

OutSystems recommends that you [design the architecture](https://success.outsystems.com/documentation/best_practices/architecture/designing_the_architecture_of_your_outsystems_applications/) of your O11 apps based on the architecture canvas best practices. This allows you to organize your architecture into concepts that facilitate the creation of domains.

Step 2: Adopt domain-driven architecture

[Domain-driven design](https://success.outsystems.com/documentation/best_practices/architecture/outsystems_domain_driven_architecture/domain_driven_design/) is a software engineering approach that aligns complex software applications with business problems they address.
OutSystems recommends that you adopt [domain-driven architecture](https://success.outsystems.com/documentation/best_practices/architecture/outsystems_domain_driven_architecture/) where you decouple large monolith software applications into small, serviceable pieces, providing team isolation and lifecycle independence.

By adopting domain-driven design principles, you can break down monolithic architecture into small, loosely-coupled apps. This helps to remove strong dependencies between apps and allows teams to work more independently.

Following the domain-driven architecture in O11 enables your business application architecture to get closer to the ODC architecture principles promoting application-independent lifecycles and strong ownership. This creates a smooth migration path into ODC cloud-native loosely coupled architecture composed of applications and libraries. For detailed information on ODC app architecture, refer to [app architecture](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/app_architecture/).

For detailed information on types of domains and domain architecture rules,  refer to [domain-driven design with OutSystems](https://success.outsystems.com/documentation/best_practices/architecture/outsystems_domain_driven_architecture/domain_driven_design_with_outsystems/).

Step 3: Validate your application architecture

While the Assessment tool is still under development, you can use the Discovery Tool in the  OutSystems[Forge](https://www.outsystems.com/forge/component-overview/409/discovery) to validate your [Architecture Canvas and Domain-driven design rules](https://success.outsystems.com/documentation/best_practices/architecture/designing_the_architecture_of_your_outsystems_applications/validating_your_application_architecture/).

Step 4: Map O11 domains to ODC apps and libraries 

Once you have designed your domain-driven architecture, you can map your O11 horizontal and vertical domains to ODC apps and libraries. This exercise helps you understand if your domain architecture is well designed, allowing you to iterate on the design before starting to refactor. 
For detailed information, refer to [map O11 domains to ODC apps and libraries](../preparation/o11architecture-to-odc-architecture.md).

Next, you must analyze your existing O11 application architecture and perform additional and modifications to map the existing O11 architecture to ODC architecture.
For detailed information, refer to [Convert O11 architecture blueprint to ODC architecture blueprint](../preparation/o11architecture-to-odc-architecture.md).

Step 5: Refactor your architecture to adhere to architecture best practices

As you assess your existing O11 domain architecture, you must refactor your O11 application to ensure that you follow the best practices of architecture canvas and domain-driven architecture. 

Here are some guidelines for refactoring your O11 app:

* [Refactor server actions to service action](../preparation/refactoring-o11-application/refactor-serveraction-to-serviceaction.md)

To learn more about fundamentals of ODC architecture and architecture design patterns in ODC, refer to [architecture fundamentals](https://learn.outsystems.com/training/journeys/architecture-fundamentals-559/apps/odc/1) and [architecture patterns](https://learn.outsystems.com/training/journeys/architecture-patterns-581/odc) under ODC training.

Step 6: Refactor your application to make it ODC-compatible

As you build your ODC application architecture, you must perform additional refactoring of your O11 app to make it ODC-compatible to enable a smooth migration to ODC.

Here are some procedures and guidelines for refactoring your O11 app:

* [Refactor anonymous and registered roles](../preparation/refactoring-o11-application/refactor-anonymous-registered-roles.md)
* [Refactor public roles](../preparation/refactoring-o11-application/refactor-public-roles.md)
* [Refactor public structures](../preparation/refactoring-o11-application/refactor-public-structures.md)
* [Refactor system entities](../preparation/refactoring-o11-application/refactor-systementities.md)
* [Refactor site properties](../preparation/refactoring-o11-application/refactor-siteproperties.md)
* [Refactor extensions](../preparation/refactoring-o11-application/refactor-extensions.md)

Step 7: Refactor code patterns

There are some features in O11 that are not supported in ODC. For example, ODC does not support SOAP and the O11 SOAP code cannot be automatically converted to ODC. 

Here are some code patterns that you must transform in O11 before migrating to ODC or modify the ODC code after the migration is complete:

* [Refactor SOAP](./refactoring-o11-application/refactor-soap.md)
* [Refactor BPT](./refactoring-o11-application/refactor-bpt.md)

## Additional resources

Here's some additional resources and training materials that can help you understand ODC architecture better:

* [O11 to ODC](https://learn.outsystems.com/training/journeys/from-o11-to-odc-569)
* [Architecture Fundamentals on ODC](https://learn.outsystems.com/training/journeys/architecture-fundamentals-559/apps/odc/1)
* [Architecture patterns in ODC training](https://learn.outsystems.com/training/journeys/architecture-patterns-581//odc/)
