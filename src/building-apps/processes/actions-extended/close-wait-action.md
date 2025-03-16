---
summary: Learn how to use the Close Wait Action in OutSystems 11 (O11) to effectively end a Wait activity in an action flow.
locale: en-us
guid: 9b85a078-cdb8-467d-8fca-001f5f88b4a0
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: outsystems 11, workflow processes, process automation, action flow control, wait activity management
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
  - remember
topic:
  - event-driven-processes
---

# Close Wait Action

Use the **Close&lt;Wait Name&gt;** [process activity extended action](intro.md) in an action flow to close a **Wait** activity. Once closed, the Wait activity ends its execution.

<div class="warning" markdown="1">

Closing [Wait](<../../../ref/lang/auto/class-wait.md>) activities demands advanced knowledge about the Platform to either obtain the Wait activity identifier or supply the activity identifier to the Screen Actions.

</div>

## Input parameters

* **ActivityId**: id of the activity instance. (Type: Activity Identifier; Mandatory)

* **Wait Output Parameters**: one input parameter for each output parameter in the Wait activity definition, if any.

<div class="warning" markdown="1">

The input parameters must be in the same order and of the same type as what is defined in the Wait activity.

</div>
