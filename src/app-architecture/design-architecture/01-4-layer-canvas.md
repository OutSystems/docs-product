---
summary: OutSystems 11 (O11) features the Architecture Canvas tool for streamlined Service-Oriented Architecture (SOA) design.
guid: 2b38e6ed-2c22-4d06-87b7-88d1db436ea4
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/design/rdSCF3WV51agwVCcEFkx2I/App-architecture?node-id=1-489&t=WkNS4cBkPZHvTban-1
tags: soa design, architecture canvas, reusable services, module dependency, cost-effective architecture
audience:
  - full stack developers
  - architects
outsystems-tools:
  - service studio
  - architecture canvas
coverage-type:
  - understand
  - evaluate
topic:
  - architecture-canvas
---

# The Architecture Canvas

The Architecture Canvas is an OutSystems architecture tool to make the design of Service-Oriented Architectures (SOA) simple. It promotes the correct abstraction of reusable (micro)services and the correct isolation of distinct functional modules, in cases where you are developing and maintaining multiple applications that reuse common modules. A typical medium to large OutSystems installation will support 20+ mission critical applications and 200+ interdependent modules.

These applications/modules have different change life cycles and are maintained and sponsored by different teams. New applications tend to evolve fast while highly reused services will change much slower. The most important benefit you get out of a well designed architecture is that applications and the modules that compose them will preserve independent lifecycles and decrease to a minimum dependencies and overall change impact. The result is a cost-effective OutSystems architecture design, easier to maintain and evolve.

## The layers and sub layers

Each layer and sub layer sets a different nature of the functionality to be captured in a module:

![Diagram of the OutSystems Architecture Canvas showing different layers including Orchestration Modules, End-user Modules, Core Modules, and Foundation Modules.](images/architecture-canvas-layers-diag.png "OutSystems Architecture Canvas Layers")

<div class="info" markdown="1">

The orchestration layer is used in OutSystems 10 for hyperlinks between screens of two different applications. Such links are considered strong dependencies, which compromise each application's lifecycle independence. In OutSystems 11 screen destinations are considered weak references, so an orchestration layer is no longer required, and as such has been removed from the architecture canvas.

</div>

Sub layers are shown in detail below:

![Detailed diagram of the OutSystems Architecture Canvas sub layers, including Orchestration, Enduser, Core, and Foundation with their respective external modules.](images/architecture-canvas-sublayers-diag.png "OutSystems Architecture Canvas Sub Layers")

## Architecture design with the Architecture Canvas

The Architecture Canvas is used in two different stages of the architecture design:

1. **Identifying concepts (functional, non-functional and integration needs)**
The canvas helps collecting architecture requirements in a structured and systematic way.
![Illustration of the Architecture Canvas used for identifying concepts such as User Processes, Business Concepts, and Utilities and Integration.](images/architecture-identify-concepts-diag.png "Identifying Concepts on the Architecture Canvas")

1. **Define modules**
Design the modules that implement the identified concepts, following [recommended patterns](05-integration-patterns.md).

Designing an architecture is not a one-time event. It is a continuous process. The architecture must be iterated, cycling these two stages, as a solution evolves and new concepts and needs emerge from your business.

![Graphic representing the iterative process of architecture design, with two steps: 1. Identify Concepts and 2. Define Modules.](images/architecture-iteration-diag.png "Architecture Iteration Process")

## Using the Architecture Canvas

To start using the Architecture Canvas check the following articles:

* [Translating business concepts into application modules](02-translating-business-app-modules.md)

* [Validating your application architecture](03-validating-app-architecture.md)

## More information

Check out the [Electronic Canvas tool](http://www.outsystems.com/forge/component/706/electronic-canvas/), available in the OutSystems Forge. It assists you in the design of a new architecture by allowing you to place and move around your concepts in a digital Architecture Canvas. It enables you to identify and organize all the architectural elements that need to be implemented in a new project.

To learn more about how to design your application architecture check the [Designing the architecture of your OutSystems applications](intro.md) guide.
