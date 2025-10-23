---
summary: Learn how to apply the Architecture Canvas principles to applications in OutSystems 11 (O11) for effective architecture analysis and management.
guid: f3394f79-117e-4550-9556-16b76d0d9269
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/design/rdSCF3WV51agwVCcEFkx2I/App-architecture?node-id=1-1728&t=WkNS4cBkPZHvTban-1
tags: application architecture, architecture canvas, layer classification, dependency rules
audience:
  - full stack developers
  - architects
outsystems-tools:
  - service studio
  - architecture dashboard
coverage-type:
  - evaluate
  - understand
topic:
  - application-composition
---

# Applying the Architecture Canvas to applications

To analyze the application architecture, the [Architecture Canvas](../01-4-layer-canvas.md) principles play a major role, just like with module architecture.

The same way individual modules are classified in an Architecture Canvas, each application is also placed in one of the layers.

Applications should be placed in the same layer as the top-most module layer in it. The following representation displays the nature of the modules that compose each application, as well as the application adopting the nature of its top-most module.

![Diagram showing the classification of applications into Orchestration, End-User, Core, and Library layers according to the Architecture Canvas principles.](images/applying-4-layer-canvas-apps_0.png "Architecture Canvas Layer Classification")

Applications are subject to the same validation rules, respecting the relations between them:

1. No upward references

1. No side references among **End-User** applications or **Orchestration** applications

1. No cyclic references between two applications

The same rationale applies for modules and for applications. **Orchestration** and **End-user** applications should not provide reusable services to ensure their life cycle independence. For example, an **End-User** application can contain reusable **Core** and **Library** modules, as long as they are consumed only by other modules of the same application.

## Evolving your architecture along with your applications

To better understand the dependencies among applications, consider the following typical scenario.

### First project

Commonly, people don’t start thinking about defining several applications, starting with one application per project.

In the first project, a new application is created to hold all the modules that were conceived at the architecture design stage. This application results from the blending of components that will eventually be versioned and deployed to a Quality Assurance environment.

![Diagram of the first project showing an End-User Application composed of End-User, Core, and Library modules.](images/applying-4-layer-canvas-apps_1.png "First Project Application Composition")

### Second project

On a second similar project, another application for a different business process is created, adding a few more **Core** and **Library** modules.

![Diagram of the second project illustrating an additional End-User Application with its own set of Core and Library modules.](images/applying-4-layer-canvas-apps_2.png "Second Project Application Composition")

### Third project

Soon, in a third evolution project, **End-user #1** starts reusing **Core C** and **End-user #2** starts reusing **Core B**. Although there is no violation in terms of module architecture, the two **End-user** applications have side references to each other - a cycle in fact.

![Diagram of the third project highlighting the cyclic dependencies between two End-User Applications through Core modules.](images/applying-4-layer-canvas-apps_3.png "Third Project Application Dependencies")

This clearly implies that the two applications are strongly coupled. Deploying a new version of the first to Production may require to take the second along, and vice-versa.

### Solving the issues

The commonly reused resources must be isolated in a new application, as displayed in the following diagram - the **Core Application**.

![Diagram showing the isolation of commonly reused Core and Library modules into a separate Core Application to avoid coupling between End-User Applications.](images/applying-4-layer-canvas-apps_4.png "Isolated Core Application")

Not only **Core B** and **Core C**, that are directly referenced, must be moved to this application, but also all their dependencies (**Library B** and **Library C**) to avoid upward references to the **End-user** applications.

With this configuration, the **End-user** applications can evolve independently at different paces. In addition, the **Core** application isolates the critical resources that must be carefully evolved to manage impacts.

Validation of the application architecture can also be done with the [Discovery tool](http://www.outsystems.com/forge/component/409/discovery/).

## Correctly composing applications

There are [four rules](rules-correct-app-composition.md)that will help you make sure that you address the critical points when composing your applications.

Another common aspect you need to take into account is [isolating an application Theme](isolating-app-theme.md)to share the same look & feel among your applications.

## More information

To learn more about how to design your application architecture check the [Designing the architecture of your OutSystems applications](../intro.md) guide.

You can also check for further recommendations on how you should [compose your application landscape](https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Designing_the_architecture_of_your_OutSystems_applications/Application_composition).
