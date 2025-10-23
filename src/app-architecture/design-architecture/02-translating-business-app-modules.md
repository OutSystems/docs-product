---
summary: Learn how to translate business concepts into manageable application modules using OutSystems 11 (O11) and the Architecture Canvas method.
guid: 24fbf144-fff4-426c-917f-d30f2b1eb523
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/design/rdSCF3WV51agwVCcEFkx2I/App-architecture?node-id=1-835&t=WkNS4cBkPZHvTban-1
tags: software architecture, module management, application design, enterprise applications
audience:
  - full stack developers
  - architects
  - business analysts
outsystems-tools:
  - service studio
  - architecture dashboard
coverage-type:
  - understand
  - evaluate
topic:
  - map-os-to-global-concepts
---

# Translating business concepts into application modules

Once you identify your concepts, you must translate them into application modules. To do so correctly, it is key you find the correct balance between:

1. Not having to handle too many modules and;

1. Having a manageable complexity and life cycle independence for each module.

## Finding the right concept granularity

Consider the following example of concepts identified with the [Architecture Canvas](01-4-layer-canvas.md) method.

![Diagram illustrating the Architecture Canvas method with concepts categorized into User processes, Business concepts, and Utilities and integration.](images/architecture-canvas-concepts-diag.png "Architecture Canvas Concept Diagram")

The number of modules that need to be defined to implement these concepts depends on the concept granularity. To define an architecture, concepts don’t need to be captured at very low level (like in this example). However, the correct granularity is influenced by the following criteria:

Complexity
:   A concept may be too vast to be implemented in a single module. For example, user process **Customer management** may include several sub-processes: provisioning a new customer, analyzing customer trends, adding a service to a customer, among others.

    Split it into several modules to keep the complexity of each module manageable.

Independent life cycles
:   Even if you predict that all the sub-concepts together don’t result in a complex module, splitting a module in smaller concepts is also required if you need to manage functionality independently.

    This allows you to parallelize development among different developers or keep different evolution paces for different business sponsors.

Service isolation
:   There are several [integration patterns to correctly abstract services](05-integration-patterns.md), requiring you to split a concept in several technical components according to the scenario.

## Validating your architecture

To make sure the way you organized your concepts comply with Architecture Canvas recommendations, check the following article to learn how you can [validate your application architecture](03-validating-app-architecture.md).

## More information

Check the complete guide on how to design your application architecture in [Designing the architecture of your OutSystems applications](intro.md).
