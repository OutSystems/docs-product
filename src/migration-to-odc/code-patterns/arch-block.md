---
summary: This article explains how to refactor an O11 Application Block dependency to be compatible with OutSystems Developer Cloud (ODC).
locale: en-us
guid: 2ae09af8-26ba-452b-b757-e18d189b64d4
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/design/daglmSUESdKw9J3HdT87a8/O11-to-ODC-migration?node-id=2350-7042
helpids: 30521
tags: app architecture conversion, dependency management, code conversion, app development, outsystems platform
audience:
  - frontend developers
  - full stack developers
  - architects
outsystems-tools:
  - architecture dashboard
  - service studio
coverage-type:
  - unblock
  - understand
---

# Asset consuming an ODC application Block

Your ODC asset consumes a Block from another asset. This creates a strong dependency between apps, which isn't supported in ODC.

In OutSystems 11 (O11), Blocks can be consumed across different apps. In ODC, however, dependencies between apps must be weak. This means that the Block must either be part of the consumer ODC asset, or the Block must be shared by an ODC library.

## How to solve

You must solve this pattern in O11, before proceeding with the code conversion to ODC.

### Solve in O11

To solve this pattern, review the O11 to ODC architecture mapping. Consider the following scenarios:

#### Single consumer

If only one ODC app or library consumes the Block, move the Block into the consumer ODC asset:

1. Create a new O11 app.
1. Move the O11 module that contains the Block to the new O11 app.
1. Map the new O11 app to the ODC asset that consumes the Block.

The Block is now part of the consumer ODC asset, thus there's no longer a strong dependency between apps.

![Diagram showing the architecture review process. Before the review, O11 Modules are part of ODC Apps. After the review, O11 Modules are moved to a new O11 App, which is then consumed by ODC Apps.](images/review-arch-consolidate-diag.png "Architecture Review Process for Single ODC App or Library")

#### Multiple consumers

If several ODC apps or libraries consume the Block, share the Block through an ODC library:

1. Convert the O11 module that contains the Block to an O11 library module.
1. Create a new O11 app.
1. Move the O11 library module to the new O11 app.
1. Map the new O11 app to an ODC library.

The Block is now shared by a library, which is deployed in the context of consumer apps only. Thus, there's no longer a strong dependency between apps.

![Diagram showing the architecture review process. Before the review, O11 Modules are part of ODC Apps. After the review, O11 Modules are moved to an O11 Library, which is then consumed by ODC Apps.](images/review-arch-move-to-lib-1-diag.png "Architecture Review Process for Multiple ODC Apps or Libraries")
