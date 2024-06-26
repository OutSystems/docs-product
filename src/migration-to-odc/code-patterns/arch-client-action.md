---
summary: 
locale: en-us
guid: ebd97f10-d965-4b69-9829-ccbabeee44d2
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
helpids: 30520
---
# Asset consuming an ODC application Client Action

A dependency to a Client Action is a strong dependency, and in ODC, dependencies to other Apps must be weak dependencies.
This means that the Client Action must either be part of the consumer ODC asset, or the Client Action must be shared by an ODC Library.

## How to solve

You must solve this pattern in O11, before proceeding with the code migration to ODC.

### Solve in O11

To solve this pattern, review the O11 to ODC architecture mapping considering the following options:

* If only one ODC App or Library consumes the Client Action, move the O11 Module with the Client Action to a new O11 App, then map that O11 App to the ODC consumer.

    ![Diagram showing the architecture review process. Before the review, O11 Module 1 is within ODC App 1. After the review, O11 Module 1 is moved to O11 App 4 and mapped to the ODC consumer.](images/review-arch-consolidate.png "Architecture Review Process for Single ODC App or Library")

* If several ODC Apps or Libraries consume the Client Action, convert the O11 Module with the Client Action to an O11 Library Module, move that O11 Module to a new O11 Ap, and then map that O11 App to an ODC Library.

    ![Diagram showing the architecture review process. Before the review, O11 Modules are within ODC Apps. After the review, O11 Module 1 is moved to O11 App 4 and shared as a library in ODC Library 1.](images/review-arch-move-to-lib.png "Architecture Review Process for Multiple ODC Apps or Libraries")
