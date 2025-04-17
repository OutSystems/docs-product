---
summary: Explore application composition in OutSystems 11 (O11), focusing on module assembly and deployment dependencies essential for architectural design.
tags: application deployment, dependency management, architectural design, application life cycle management
guid: dd85b743-88c8-4cba-8214-de594cffeefa
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - architects
  - full stack developers
outsystems-tools:
  - service studio
  - lifetime
coverage-type:
  - understand
  - evaluate
topic:
  - application-composition
---

# Application composition

An OutSystems application is an assembly of Modules and Extensions defined in Service Studio. An application constitutes the minimum deployment unit among environments in [LifeTime](https://success.outsystems.com/Documentation/11/Managing_the_Applications_Lifecycle).

Understanding the dependencies among applications is also key to design a correct architecture. Even if you have a correct module architecture, the wrong application composition can result in:

* Applications not being able to evolve independently (different life cycles).

* Applications that impact each other unnecessarily. Deploying one application may result in having to take all other applications with it to Production.

Check the complete guide on how to design your application architecture in [Designing the architecture of your OutSystems applications](../intro.md).
