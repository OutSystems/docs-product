---
summary: OutSystems 11 (O11) supports maintaining UI in dedicated modules to enhance reuse and reduce merge conflicts.
tags: ui module management, screen reuse, block reuse, merge conflict reduction, theme compatibility
locale: en-us
guid: 04f7cedb-d02b-42e9-b9f4-f7cbf2cb8506
app_type: reactive web apps
platform-version: o11
figma:
audience:
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - evaluate
topic:
  - front-end-architecture
  - reuse-ui
---

# Maintain UI in dedicated modules

Your team can benefit from having Screens and Blocks in separate UI Modules and then reusing those UI elements in other Modules. This is not only a good development practice, but also improves team collaboration, because there are less merge conflicts when working on different Modules simultaneously.

To reuse Screens and Blocks between Modules, you need to meet the following requirements in your App.

* The Themes need to be the same. This guarantees that UI looks the same. If the Themes are different, you get the Theme compatibility warning.
* The UI elements (Screens, Blocks) need to be public. By setting these elements as public you make them available for referencing in other Modules. 

## Current limitations

Because of the architectural differences between Apps, there are some limitations when reusing Screens and Blocks between Modules and Apps. When you move Screens between Apps, Service Studio checks for these limitations.

* Reusing Screens and Blocks is not available in Mobile Apps.
* System Event **On Application Ready** runs every time you navigate between Screens in different Modules.

