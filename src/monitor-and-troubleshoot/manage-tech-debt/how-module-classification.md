---
summary: Learn to reclassify modules in OutSystems 11 (O11) using Code Quality, impacting app classifications and technical debt scores.
locale: en-us
guid: 429d1c51-f248-425b-902e-2af8b6ec8a2e
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing%20the%20Applications%20Lifecycle?node-id=929:728
tags:
  - Architecture
  - Technical Debt
audience:
  - Developer
  - Platform administrator
  - Architect
outsystems-tools:
  - code quality
coverage-type:
  - apply
isautopublish: true
---

# How to change module classifications

<div class="info" markdown="1">

AI Mentor Studio is now Code Quality.

</div>

You can change a module's classification in the canvas. However, by changing the classification of a module, the classification of the app may be affected. OutSystems AI model receives this reclassification.

## Prerequisites

Before changing a module’s classification in Code Quality, make sure that the following requirements are met:

* You have [enabled AI auto-classification](how-enable-autoclass.md).

* You have [full control permissions assigned as a default role](how-works.md#maintenance-and-operations-permissions)

## Change module classifications

To change a module’s classification, follow these steps:

1. In the Code Quality canvas, double-click the app that contains the module you want to reclassify.

    ![Screenshot of Code Quality canvas showing module classification options](images/module-classification-ams.png "Code Quality Canvas")

1. Select the module, then in the module details area, choose the new architecture layer from the dropdown.

    ![Screenshot of a module selected in Code Quality with the architecture layer dropdown open in the module details area](images/select-module-to-reclassifiy-ams.png "Module Architecture Layer Dropdown")

1. Click **Yes, change it** in the **Change module classification** popup to confirm the override.

When you reclassify a module, the technical debt score related to architecture code patterns is recalculated immediately.
