---
summary: 
locale: en-us
guid: f74beda0-279a-499c-932d-5ad57587c8f3
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/design/daglmSUESdKw9J3HdT87a8/O11-to-ODC-migration?node-id=2350-7805
helpids: 30529
---
# Asset consuming a Screen in mobile app

A dependency to a Screen is a strong dependency, and in ODC, dependencies to other Apps must be weak dependencies.
This means that it's not possible to consume Screens from other Apps.
Libraries can't share Screens, nor consume Screens from Apps.

## How to solve

You must solve this pattern in O11, before proceeding with the code migration to ODC.

### Solve in O11

To solve this pattern, review the O11 to ODC architecture mapping considering the following options:

* If only one ODC App consumes the Screen, move the O11 Module to a new O11 App, than map that O11 app to the ODC consumer.

    ![Diagram showing the architecture review process. Before: O11 Module 1 in O11 App 1 has a strong dependency on ODC App 1. After: O11 Module 1 is consolidated within O11 App 1, eliminating the strong dependency.](images/review-arch-consolidate-diag.png "Architecture Review Before and After")

* If several ODC Apps consume the Screen, ensure all consumers O11 Apps are mapped to the same consumer ODC App, and that the Screen is part of an O11 Module that belongs to an O11 App mapped to the consumer ODC App.

* If one or more ODC Libraries consume the Screen, ensure that the consumption of the Screen is moved to an O11 Module belonging to an O11 app mapped to an ODC App instead of to an ODC Library.
