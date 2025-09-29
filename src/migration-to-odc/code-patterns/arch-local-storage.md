---
summary: This article provides guidance on refactoring dependencies to Local Storage Entities in O11 apps to ensure compatibility with ODC.
locale: en-us
guid: 8639ad48-cd26-4273-8175-65db6a3f241d
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/design/daglmSUESdKw9J3HdT87a8/O11-to-ODC-migration?node-id=2350-7558
helpids: 30525
tags: local storage entities, app architecture conversion, outsystems development, code conversion, app development best practices
audience:
  - full stack developers
  - architects
outsystems-tools:
  - service studio
coverage-type:
  - unblock
  - understand
---

# Asset consuming a Local Storage Entity

In ODC, Assets can't have dependencies to Local Storage Entities from other Assets. Furthermore, Libraries can't consume Entities. This means that each App must define its own Local Storage Entities and can't share them with other Apps.

## How to solve

You must solve this pattern in O11, before proceeding with the code conversion to ODC.

### Solve in O11

To solve this pattern, review the O11 to ODC architecture mapping and move the O11 module with the Local Storage Entity to an O11 App, then map that O11 app to the ODC consumer.

![Diagram showing the architecture review before and after. Before: ODC App 1 has O11 App 1 with O11 Module 1, ODC App 2 has O11 App 2 with O11 Module 2, and ODC App 3 has O11 App 3 with O11 Module 3. Strong dependencies to an ODC App aren't allowed. After: Each ODC App has its corresponding O11 App and Module without dependencies.](images/review-arch-consolidate-diag.png "Architecture Review Before and After")
