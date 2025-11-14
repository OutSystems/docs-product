---
summary: This article provides guidance on refactoring strong dependencies on Images in O11 apps to ensure compatibility with ODC.
locale: en-us
guid: 4732cbaa-a548-4c28-b2fb-081be0f1ecc3
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/design/daglmSUESdKw9J3HdT87a8/O11-to-ODC-migration?node-id=2350-7347
helpids: 30524
tags: odc, code conversion, application development, dependency management, architecture
audience:
  - frontend developers
  - full stack developers
  - architects
outsystems-tools:
  - service studio
coverage-type:
  - unblock
  - understand
---

# Asset consuming an Image from an Application

A dependency to an Image is a strong dependency, and in ODC, dependencies to other Apps must be weak dependencies. This means that the Image must either be part of the consumer ODC asset, or the Image must be shared by an ODC Library.

## How to solve

You must solve this pattern in O11, before proceeding with the code conversion to ODC.

### Solve in O11

Depending on your scenario, review the O11 to ODC architecture mapping considering the following options:

* If only one ODC App or Library consumes the Image, move the O11 Module with the Image to a new O11 App, then map that O11 App to the ODC consumer.

    ![Diagram showing the architecture review process for ODC and O11 modules, illustrating the movement of an O11 module to a new O11 app.](images/review-arch-consolidate-diag.png "Architecture Review for ODC and O11 Modules")

* If several ODC Apps or Libraries consume the Image, convert the O11 Module with the Image to an O11 Library Module, move that O11 Module to a new O11 Ap, and then map that O11 App to an ODC Library.

    ![Diagram showing the architecture review process for ODC and O11 modules, illustrating the movement of an O11 module to an ODC library.](images/review-arch-move-to-lib-1-diag.png "Architecture Review for ODC and O11 Modules")
