---
summary: 
locale: en-us
guid: bf0d4524-95c4-477b-9254-1e369a3f1f80
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
helpids: 30519
---
# Asset consuming an ODC application Server Action

A dependency to a Server Action is a strong dependency, and in ODC, dependencies to other Apps must be weak dependencies.
This means that it’s not possible to consume Server Actions from other Apps, only from Libraries.

## How to solve

You must solve this pattern in O11, before proceeding with the code migration to ODC.

### Solve in O11

Depending on your scenario, solve this pattern in one of the following ways:

* If the consumer is an ODC App and the Server Action isn't also consumed by an O11 Library Module, change the strong dependency to a weak dependency by [converting the server action to a service action](../../building-apps/reuse-and-refactor/services.md).

* Otherwise, review the O11 to ODC architecture mapping, considering the following options:

    * If only one ODC App or Library consumes the producer module, move the O11 Module with the Server Action to a new O11 app, than map that O11 App to the ODC consumer.

        ![Diagram showing the architecture review process. Before the review, O11 Modules are within ODC Apps. After the review, O11 Modules are moved to an O11 Library within an ODC Library.](images/review-arch-consolidate.png "Architecture Review Before and After")

    * If several ODC Apps or Libraries consume the producer module, convert the O11 Module with the Server Action to an O11 Library module, move that O11 Module to a new O11 App, then map that O11 App to an ODC Library.

        ![Diagram showing the architecture review process. Before the review, O11 Modules are within ODC Apps. After the review, O11 Modules are moved to an O11 Library within an ODC Library.](images/review-arch-move-to-lib.png "Architecture Review Before and After")
