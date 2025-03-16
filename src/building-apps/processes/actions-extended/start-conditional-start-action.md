---
summary: Explore how to initiate a Conditional Start in OutSystems 11 (O11) using the Start Conditional Start Action with specific input parameters.
locale: en-us
guid: 143a03ee-a51c-4c5b-b28c-45266ccd9926
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: process automation, conditional start, process flows, outsystems processes, event handling
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
  - understand
topic:
  - event-driven-processes
---

# Start Conditional Start Action

Use the **Start&lt;Conditional Start Name&gt;** [process activity extended action](intro.md) in an action flow to start a **Conditional Start**. Once started, an instance of the Conditional Start flow is created and executed while the Conditional Start continues to listen for more incoming events.

## Input parameters

* **ProcessId**: id of the process instance where the Conditional Start instance is executed. (Type: Process Identifier; Mandatory)

Use [Process Entities](../process-entities/intro.md) to obtain the process identifier.

* **Conditional Start Input Parameters**: one parameter for each input parameter in the Conditional Start definition.

<div class="warning" markdown="1">

The input parameters must be in the same order and of the same type as what is defined in the Conditional Start.

</div>
