---
locale: en-us
guid: 143a03ee-a51c-4c5b-b28c-45266ccd9926
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
