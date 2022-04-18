---
locale: en-us
guid: b41e47d0-4d8d-4c37-84fb-b49af5783548
app_type: traditional web apps, mobile apps, reactive web apps
---

# Impact of Changing Parameters

When you publish a module containing modified [process flows](../process-flow/process-flow-editor.md), all of the executing process instances that were based on the former process flows are automatically upgraded by OutSystems. This topic describes which changes to input and output parameters may suspend process instances.


## Impact of Modified Output Parameters of an Activity

Modifying output parameters of process activities **suspends** the execution of process instances which are in the following conditions:

* There's a process activity in the flow that is using the modified output parameters.

* The process instance has already executed the process activity with modified output parameters but not the process activity that is using them.

However, the execution **is not suspended** if modifications were only made to the type of the output parameters and types can be automatically converted.


## Impact of Modified Input/Output Parameters of a Process

The modification of input/output parameters of a process suspends other process instances that are executing it through a [Execute Process](<../../../ref/lang/auto/Class.Execute Process.final.md>) activity.

However, the execution **is not suspended** if modifications were only made to the type of the input/output parameters and types can be automatically converted.


## Additional Changes with Impact on the Execution of Process Instances

Modifying the flow of a process may also have impact on executing process instances.

The following topics contain examples of these changes and their impact:

* [Impact of Adding Activities to Process Flows](impact-add-activities.md)
* [Impact of Removing Activities from Process Flows](impact-delete-activities.md)
* [Impact of Moving Activities in Process Flows](impact-move-activities.md)
