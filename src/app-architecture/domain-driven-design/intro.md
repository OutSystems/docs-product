---
summary: Explore Domain Driven Architecture in OutSystems 11 (O11) for managing complex software development and deployment.
tags: domain-driven design, software architecture, monolithic architecture, services decoupling, complex software systems
guid: 744dbbef-0e48-47e1-9b5e-09ad8ae610a8
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/design/rdSCF3WV51agwVCcEFkx2I/App-architecture?node-id=5-39&t=bB3MvYj2DPjavxZe-1
audience:
  - full stack developers
  - architects
  - tech leads
  - backend developers
outsystems-tools:
  - none
coverage-type:
  - evaluate
  - understand
topic:
  - domain-driven-design
  - good-architecture-value
---

# OutSystems Domain Driven Architecture

In this section you can find information on all aspects of using a Domain Driven Architecture in OutSystems. The when and how to leverage and validate such solution is discussed, along with the existing methods and tools that you can use to validate your architecture.

## The architectural challenge

With the **growth of a software factory**, it becomes more and more difficult to isolate development and deployment. Both become more complex and slow. Small change requests become harder to implement. Planning becomes hard. This all means that the teams are at odds with each other. 

![Illustration of the complexity and interdependency in software development.](images/outsystems_domain_driven_architecture_0.png "Complexity in Software Development")

The teams start facing growing pains to cope with the interests of the business because everything starts to become interdependent. It becomes hard to avoid ripple effects where changes impact other businesses. Decisions are harder to make as more decision-makers are involved. 

The need to decouple the large monolith into small, serviceable pieces becomes imperative, providing team isolation and lifecycle independence.

![Diagram showing the transition from a monolithic architecture to decoupled services.](images/outsystems_domain_driven_architecture_1.png "Decoupling Monolithic Architecture")

As the software complexity increases, it also increases the need to split and organize the software into smaller serviceable pieces that can be independently managed by teams.

## The strategic and technical approaches

The strategic approach is to align software development and teams with the interests of the business. This approach is required to guide the teams on what to focus on and which specific area of business is related with business needs. It also helps keep major efforts devoted to what’s most important to the business now.

The technical approach is to guide development with the goal of preventing the software development model from becoming corrupted. The balance between both approaches it's covered next.

Is this always true? Does it apply to any software factory? Let’s look into both approaches.

|Simple logic and faster centralized development?|Continuous integration, continuous delivery and scalability?|
|--|--|
|![Graphic representing a centralized development model with simple logic and faster development.](images/outsystems_domain_driven_architecture_2.png "Centralized Development Model")|![Graphic representing a model with continuous integration, continuous delivery, and scalability.](images/outsystems_domain_driven_architecture_3.png "Continuous Integration and Delivery Model")|

   
Each option has advantages and disadvantages. Let’s look into the main ones:

![Comparative diagrams showing the evolution of software complexity from small apps to large monoliths and decoupled services.](images/outsystems_domain_driven_architecture_4.png "Software Complexity and Architecture")

