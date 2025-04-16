---
summary: OutSystems 11 (O11) offers tools to ensure application architecture compliance with essential design rules.
guid: f0975aa9-dd78-42c9-9c69-536e6a3e57a3
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/design/rdSCF3WV51agwVCcEFkx2I/App-architecture?node-id=1-865&t=WkNS4cBkPZHvTban-1
tags: application architecture, dependency management, software design principles
audience:
  - backend developers
  - full stack developers
  - architects
outsystems-tools:
  - discovery
coverage-type:
  - evaluate
  - understand
topic:
  - validate-app-architecture
---

# Validating your application architecture

There are 3 rules you **must always** comply with in order to achieve a well-designed application architecture.

![Diagram illustrating the three main rules for application architecture compliance: no upward references, no side references, and no circular references.](images/validating-app-architecture-rules-diag.png "Application Architecture Compliance Rules Diagram")

The compliance of the implemented modules with these architecture rules can be automatically verified using the [Discovery tool](http://www.outsystems.com/forge/component/409/discovery/). It analyzes the actual dependencies among modules, identifying violations and pinpointing the elements (actions, screens, entities) that are assembled in the wrong place. 

## Rule #1 - No upward references

An upward reference tends to create a cluster where any 2 modules, directly or indirectly, have a circular dependency.

In this example, since **Library E** consumes **End-user A**, any pair of elements inside the identified cluster is in a circular relation. Take **C** and **D** for example: **C** > E > A > **D** and reverse **D** > E > A > **C**.

![Diagram showing an example of upward references in application architecture, highlighting the problematic dependencies between modules A, C, D, and E.](images/validating-app-architecture-no-upward-references-diag.png "No Upward References Diagram")

Another unexpected effect is that **End-user B** is legitimately consuming **Core D**, and becomes dependent of the entire cluster. Not only its runtime will get an unnecessarily large footprint, but it will also be constantly impacted (outdated) with changes made in modules that it should not even be aware of.

### What is wrong?

An upward violation clearly identifies that services are not properly isolated.

### How to fix it?

Find the elements that are being consumed and move them to a lower layer. In this case, move the reusable service in **A** to a **Library**, eventually to **E** itself, if it fits in the same concept.

## Rule #2 - No side references among End-users or Orchestrations

In this example, **End-user A** is consuming some element of **End-user B** (maybe something as simple as a formatting function). Not only it got coupled to module **B**, but it unnecessarily inherited **D**, **E** and **G**.

![Diagram depicting an example of side references among End-user modules A and B, and the resulting inherited dependencies from Core and Foundation modules.](images/validating-app-architecture-no-side-references-diag.png "No Side References Among End-users or Orchestrations Diagram")

### What is wrong?

**End-user** or **Orchestration** modules should not provide reusable services. This ensures that they are correctly isolated, allowing them to have different lifecycles - different versioning paces due to different sponsors or project teams.

This isolation is critical since **End-users** and **Orchestrations** are at the top of the hierarchy. A reference to suchs modules tends to bring along a huge set of indirect dependencies from lower layers.

### How to fix it?

Find out which are the elements of **B** being consumed by **A** and move them to a new (or an existing, if there is a conceptual fit) lower layer module:

* To a **Core** module if it is business related.

* To a **Library** if it is business-agnostic.

## Rule #3 - No cycles among Cores or Libraries

Respecting rules #1 and #2, **End-users** and **Orchestrations** cannot be involved in any cyclic references.

The third rule is about avoiding cycles among **Cores** or **Libraries**, since those are allowed to have side references.

![Diagram illustrating the rule against cycles among Core or Library modules, with an example of a circular reference between modules A and B.](images/validating-app-architecture-no-circular-references-diag.png "No Cycles Among Cores or Libraries Diagram")

A cycle is always undesirable, since it brings unexpected impacts and hard-to-manage code.

### What is wrong?

A cycle between modules indicates that the concepts are not correctly abstracted.

A cycle between **A** and **B** either indicates that:

* They are strongly coupled, or;

* One of the directions is undesirable. For instance, **A** should be conceptually consuming **B** because the concept in **A** extends **B**.

### How to fix it?

Most of the times, if there is clearly an undesirable direction in the relation concepts must be moved to another module.

For example, if it is **B** that should not be consuming **A**, then the elements of **A** consumed by **B** should be:

* Moved to a new module, if they represent another reusable concept, or;

* Moved to **B** itself, if they were misplaced elements of the same concept.

However, If **A** and **B** are too strongly coupled, they should be merged together.

If that merge results in a too large module, it may be necessary to create a third module on top of the two. The original two modules represent base concepts and the new module normally supply business rules, to support some end-user process, that need to handle both base concepts. This composition logic is the one causing the cycle.

## More information

To learn more about how to design your application architecture check the [Designing the architecture of your OutSystems applications](intro.md) guide.

