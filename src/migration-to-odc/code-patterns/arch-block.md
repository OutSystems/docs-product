---
summary: 
locale: en-us
guid: 2ae09af8-26ba-452b-b757-e18d189b64d4
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/design/daglmSUESdKw9J3HdT87a8/O11-to-ODC-migration?node-id=2350-7042
helpids: 30521
---
# Asset consuming an ODC application Block

A dependency to a Block is a strong dependency, and in ODC, dependencies to other Apps must be weak dependencies.
This means that the Block must either be part of the consumer ODC asset, or the Block must be shared by an ODC Library.

## How to solve

You must solve this pattern in O11, before proceeding with the code migration to ODC.

### Solve in O11

To solve this pattern, review the O11 to ODC architecture mapping considering the following options:

* If only one ODC App or Library consumes the Block, move the O11 Module with the Block to a new O11 App, then map that O11 App to the ODC consumer.

    ![Diagram showing the architecture review process. Before the review, O11 Modules are part of ODC Apps. After the review, O11 Modules are moved to a new O11 App, which is then consumed by ODC Apps.](images/review-arch-consolidate-diag.png "Architecture Review Process for Single ODC App or Library")

* If several ODC Apps or Libraries consume the Block, convert the O11 Module with the Block to an O11 Library Module, move that O11 Module to a new O11 Ap, and then map that O11 App to an ODC Library.

    ![Diagram showing the architecture review process. Before the review, O11 Modules are part of ODC Apps. After the review, O11 Modules are moved to an O11 Library, which is then consumed by ODC Apps.](images/review-arch-move-to-lib-1-diag.png "Architecture Review Process for Multiple ODC Apps or Libraries")
