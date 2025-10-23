---
summary: Explore how OutSystems 11 (O11) addresses the complexities of microservices architecture, enhancing security, debugging, and data integration.
tags: microservices, application scaling, independent deployment, software modularization, network communication
guid: b161ae4a-7e15-4b76-93d8-f3096d4948c6
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/design/rdSCF3WV51agwVCcEFkx2I/App-architecture?node-id=5-46&t=bB3MvYj2DPjavxZe-1
audience:
  - full stack developers
  - architects
outsystems-tools:
  - none
coverage-type:
  - evaluate
  - understand
topic:
  - soa-and-microservices
  - domain-driven-design
---

# Understanding microservices

Microservices (also known as the microservices architecture), according to James Lewis and Martin Fowler:

_is an approach to developing a single application as a suite of small services, each running in its own process and communicating with lightweight mechanisms, often an HTTP resource API. These services are built around business capabilities and independently deployable by fully automated deployment machinery. There is a bare minimum of centralized management of these services, which may be written in different programming languages and use different data storage technologies_.

With the hype of microservices and the fall of monoliths, it became clear that as the constituent services are small, they can be built by one or more small teams from the beginning, separated by service boundaries. All in all, this makes it easier to scale up the development effort.

|Microservices have many benefits...|...but come with additional burdens|
|-----|-----|
| **Strong Module Boundaries**<br/>Microservices reinforce modular structure, which is particularly important for larger teams. The structure of a software system mirrors the communication structure of the organization that built it.| **Inter-process communication**<br/>Dealing with network latency and hiccups, data marshalling<br/>**Multiple transactions**<br/>Handling and coordinating multiple independent commits|
|**Independent Deployment**<br/>Simple services are easier to deploy, and since they're autonomous, are less likely to cause system failures when they go wrong. Continuous delivery becomes a must, as the organizations that do this can respond quickly to market changes and introduce new features faster than their competition.|**Fault tolerance**<br/>Recovering from and handling communication errors and service consistency<br/>**Limited data mashup**<br/>Executed in memory and limited to APIs<br/>**Security**<br/>Access management and authentication|
|**Technology Diversity**<br/>With microservices, you can mix multiple languages, development frameworks and data-storage technologies.|**Debugging & troubleshooting**<br/>Drilldown to the root cause, because it may be inside of the chain of services<br/>**Monitor & logging**<br/>Need to centralize effective monitoring & logging|

As you can see, all the initial benefits create additional burdens. What was promised to speed up the process has now become a huge complexity problem.

Monoliths and microservices aren't a simple binary choice, and you must not forget that there are systems out there that don't quite fit into either category.

That said, the normal assumption is that, because of the cost of microservices on productivity, they can only be made up for in more complex systems, but this isn't absolutely true.

OutSystems already solves some of these burdens by:

|1. Adopting a single stack||
|--|--|
|<br/><br/><br/>OutSystems provides you with built-in capabilities that handle:<br/>* Security<br/>* Debugging and troubleshooting<br/>* Monitor and logging|![Illustration of OutSystems domain-driven architecture with multiple hexagons representing different services.](images/outsystems_domain_driven_architecture_6.png "OutSystems Domain-Driven Architecture Capabilities")|

|2. Exposing a query model||
|--|--|
|<br/><br/><br/>By exposing a query model, data mashup is now possible, as you can query entities directly to read data and use APIs to write data.<br/>* Limited data mashup|![Diagram showing OutSystems domain-driven architecture with hexagons and icons representing data queries and API interactions.](images/outsystems_domain_driven_architecture_7.png "OutSystems Query Model in Domain-Driven Architecture")|

With this initial context in mind, it's now time to ask the question: when should you adopt a domain architecture (and therefore a microservices architecture) in OutSystems? Let’s dig into it!
