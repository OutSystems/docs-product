---
summary: Use output parameters to your process activity to return information to the following process activities in the flow path.
locale: en-us
guid: 88f8d860-47a8-4529-b137-e3d7e832b5b7
app_type: traditional web apps, mobile apps, reactive web apps
---

# About Output Parameters in a Process Flow

When designing the process flow of your process, you may pass information among the process activities in the process flow. To accomplish this, add output parameters to your process activity to return information to the following process activities in the flow path. Each process activity has the privileges to read and write its own output parameters and read-only privileges over the output parameters of other process activities. Resuming, an output parameter is written by the process activity that owns it and read by the following process activities in the flow path.

The process for which you are designing the process flow may also have output parameters that should be set by the process activities present in the flow. The read and write privileges over the output parameters of a process are as follows:

* **Process Flow**: you have privileges to **read** and **write** the process output parameters while manipulating them in the process flow.

* **Execute Process**: in the case where you have an [Execute Process](<../../../ref/lang/auto/Class.Execute Process.final.md>) activity in the process flow, the output parameters of this process activity are those of the executed process for which you have **read-only** privileges.

## Output Parameters Default Value

If an output parameter was never set, you'll get its default value when you read it. This default value is the one **defined in the currently published process**. However, if a new process version is published while your process is being executed all of the changes to the default values are immediately applied.

When the process execution ends, any process output parameter that has never been written is set to its default value. The same default value rules are applied to **input parameters**.
