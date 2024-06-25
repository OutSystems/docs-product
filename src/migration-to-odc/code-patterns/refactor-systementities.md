---
summary: This article outlines how to refactor system entities in your O11 apps for compatibility with ODC.
locale: en-us
guid: 3e9df6e0-0883-4c03-8cbd-f2259c689768
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: 
---

# Refactor System entities to be ODC-compatible

[System entities](https://success.outsystems.com/documentation/how_to_guides/data/data_migration_from_production_to_non_production_environment/outsystems_platform_metamodel/) are pure system tables used in the metamodel of the OutSystems platform. There are no system entities in ODC. Therefore, any reference to the metamodel must be removed except for the User entity that exists as a cache but with a simpler field structure.
