---
summary: Reuse functionality from other modules to avoid repeated code and to achieve a modular design.
locale: en-us
guid: 33e63dcb-e047-49d9-ad6b-e14efd20ed46
---

# Reuse and Refactor

As your apps grow, keep them maintainable and scalable by centralizing the logic in a reusable, modular way. In OutSystems you can use different types of modules and **reference** them as **producer modules**. Similarly, the **consumer modules** use the elements of logic that the producers expose.

Here is an overview of module types.

Module type | Description
--- | ---
Reactive | Module for building Reactive Web Apps. Supports UI and logic.
Mobile | Module for building Mobile Apps. Supports UI and logic.
Traditional Web | Module for building Traditional Web Apps. Supports UI and logic.
Service | Enforces the encapsulation of core services by abstracting either business concepts or business-agnostic services. See more at [Service modules](services.md).
Library | Encapsulates logic and UI patterns that are database independent, promoting the reuse of these elements within your factory. See more at [Library modules](libraries.md)
Extension | Lets you integrate with enterprise systems and to extend the existing functionality and data model of OutSystems. You can learn more in the document about [extending logic with your code](../../extensibility-and-integration/integration-studio/getting-started/intro.md).

You can also create **blank modules**, which are modules that don't contain user interface. For example, if you're creating a Reactive Web App, you can add a **blank module** to avoid referencing OutSystems UI.