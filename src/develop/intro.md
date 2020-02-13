---
summary: Define and manage the user interface, data model, logic and security of your OutSystems applications.
tags: support-application_development; support-Mobile_Apps; support-webapps; support-webapps-overview
---

# Developing an Application

You can structure your [OutSystems application](../getting-started/right-app.md) into several modules, each of them implementing a specific purpose or concept.

Whether you start by a small application or a larger one, you should keep your application manageable and prepare it to scale. Check the [Reuse and Refactor](reuse-and-refactor/intro.md) section to learn how to achieve a modular design and avoid repeated logic.

## Reactive, Mobile and Traditional Web Modules

Reactive, Mobile and Traditional Web modules are the place to implement the UI interface that support a specific user process, such as UI flows, Screens and Blocks. You can also implement the logic directly related with that user process.

## Service Modules

[Service modules](reuse-and-refactor/services.md) enforce the separation of concerns and encapsulation of core services that can be reused by several applications, abstracting either business concepts or business-agnostic services that extend the framework.

## Library Modules

Use [Library modules](reuse-and-refactor/libraries.md) (or just Libraries) to encapsulate logic and UI patterns that are database independent, promoting the reuse of these elements within you factory.

## Extension Modules

Extension modules (or just Extensions) allow you to integrate with enterprise systems and to extend the existing functionality and data model of OutSystems. Learn more on how to [extend logic with your own code](../extensibility-and-integration/integration-studio/getting-started/intro.md).

