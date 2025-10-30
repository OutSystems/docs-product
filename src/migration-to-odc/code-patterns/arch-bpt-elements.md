---
guid: 46402d14-c102-4977-86f1-ce3475df2910
locale: en-us
summary: This article provides guidelines for refactoring the usage of BPT entities and actions in O11 apps to ensure compatibility with OutSystems Developer Cloud (ODC).
figma: 
coverage-type:
  - unblock
  - understand
topic: 
app_type: reactive web apps,mobile apps
platform-version: o11
audience:
  - full stack developers
  - frontend developers
  - mobile developers
tags: cloud-native applications, system entities, api development, data integration, app conversion
outsystems-tools:
  - service studio
helpids: 30628
---

# Asset consuming O11 Business Process (BPT) elements

In ODC, business processes are available as [workflows](https://www.outsystems.com/tk/redirect?g=70b986e2-cd07-48a6-92c0-e57751112bb7), which have a different architecture and may still have yet limited support when compared to [O11 BPTs](../../building-apps/processes/intro.md).

## How to solve

<div class="info" markdown="1">

If you are only preparing your code for the conversion, at present, OutSystems recommends not making any changes to O11 BPTs. OutSystems is working on automating the conversion capabilities to map existing O11 BPTs functionality to ODC Workflows.

</div>

This pattern isn't supported yet.

You can only proceed with the conversion of ODC assets that don’t consume [O11 BPT elements](#bpt-elements).

In the meantime, rethink how you can comply with the ODC architecture using [ODC workflows](https://www.outsystems.com/tk/redirect?g=70b986e2-cd07-48a6-92c0-e57751112bb7) to implement your business processes.

## O11 BPT elements not yet supported by conversion {#bpt-elements}

This sections lists the O11 BPT elements that are currently not supported by the O11 to ODC conversion.

### Process management system actions

* ActivityOpen
* ActivityReset
* ActivityClose
* ActivityGetUrl
* ActivitySchedule
* ActivitySetGroup
* ActivitySkip
* ActivityStart
* ProcessTerminate

### Process management system entities

* Activity
* Activity_Definition
* Activity_Kind
* Activity_Status
* Process
* Process_Definition
* Process_Status

### BPT_API actions

* Activity_Discard
* Activity_IsValidId
* HumanActivity_AssignToUser
* HumanActivity_CheckRole
* HumanActivity_FlushPendingEvents
* HumanActivity_SetDueDate
* Process_BulkDelete
* Process_Delete
* Taskbox_Hide

### EPA_Taskbox API actions

* API_GetActivities
* API_GetActivityGuidanceHTML
* API_GetActivityPagination
* API_GetActivityVisualization
* API_GetDynamicHtml [DEPRECATED]
* API_GetNewOpenActivity
* API_GetStaticHtml [DEPRECATED]
* API_MarkActivitiesAsSeen
* API_SetActivityVisualization

### EPA_TaskboxExtension actions

* GetActivities
* GetActivityCount
* GetNewOpenActivity
* SetSessionUserId
