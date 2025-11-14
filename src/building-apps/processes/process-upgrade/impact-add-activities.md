---
summary: Explore how OutSystems 11 (O11) automatically upgrades executing process instances when activities are added to process flows.
locale: en-us
guid: b51a153e-2fe4-4721-ac98-8de123fdf804
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=266:29
tags: process flows, process instance upgrade, outsystems platform, application lifecycle management, continuous deployment
audience:
  - full stack developers
  - backend developers
  - frontend developers
  - platform administrators
  - architects
outsystems-tools:
  - service studio
coverage-type:
  - understand
---

# Impact of Adding Activities to Process Flows

When you publish a module containing modified [process flows](../process-flow/process-flow-editor.md), all of the executing process instances that were based on the former process flows are automatically upgraded by OutSystems. This topic lists some examples of the impact of newly added activities on executing process instances.

## Process Instance is Executing After the Added Activity

In this case the execution of the process instance has already passed the added activity and **continues executing**.

![Diagram showing a process instance execution after an activity has been added to the process flow](images/process-upgrade-adding-past.png "Process Instance Executing After Added Activity")

## Process Instance is Executing Before the Added Activity

In this case the execution of the process instance has not passed the added activity and **continues executing**.

![Illustration of a process instance executing before reaching a newly added activity in the process flow](images/process-upgrade-adding-future.png "Process Instance Executing Before Added Activity")

## Process Instance is Executing in a New Branch

In this case the execution of the process instance has already passed the new branch and **continues executing**.

![Flowchart depicting a process instance execution that has bypassed a new branch in the process flow](images/process-upgrade-adding-branch.png "Process Instance in a New Branch")
