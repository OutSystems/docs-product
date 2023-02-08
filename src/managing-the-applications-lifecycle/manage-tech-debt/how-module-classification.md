---
tags: 
summary: You can change a module's classification in the AI Mentor Studio canvas.
en_title: 
locale: en-us
guid: 429d1c51-f248-425b-902e-2af8b6ec8a2e
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# How to change module classifications

<div class="info" markdown="1">

Architecture Dashboard is now AI Mentor Studio.

</div>

You can change a module's classification in the canvas. However, by changing the classification of a module, the classification of the app may be affected. OutSystems AI model receives this reclassification. 

## Prerequisites

Before changing a module’s classification in AI Mentor Studio, make sure that the following requirements are met:

* You have [enabled AI auto-classification](how-enable-autoclass.md).

* You have [full control permissions assigned as a default role](how-works.md#maintenance-and-operations-permissions)

## Change module classifications

To change a module’s classification, follow these steps:

1. In the AI Mentor Studio canvas, double-click the app that contains the module you want to reclassify.

    ![Double-click app](images/module-classification-ams.png)

1. Select the module you want to reclassify, and in the module details area, from the dropdown, select the new architecture layer. 

    ![Select new architecture layer](images/select-module-to-reclassifiy-ams.png)

    When you reclassify the module classification, the **Change module classification** popup is displayed letting you know that all auto-classification for the module will be overridden.

      ![Change module classification popup](images/change-module-classification-ams.png)

1. Click **Yes, change it**. 

When you reclassify a module, the technical debt score related to architecture code patterns is recalculated immediately.
