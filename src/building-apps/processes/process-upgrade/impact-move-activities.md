---
summary: Explore how moving activities in process flows impacts executing instances in OutSystems 11 (O11).
locale: en-us
guid: 64eb9856-d396-4d2b-8df4-a0b23f520787
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=266:38
---
# Impact of Moving Activities in Process Flows

When you publish a module containing modified [process flows](../process-flow/process-flow-editor.md), all the executing process instances that were based on the former process flows are automatically upgraded by OutSystems. This topic lists some examples of the impact of moved activities on executing process instances.

## Process Instance is Executing Before the Moved Activity

In this case the execution of the process instance has not executed the moved activity and should have executed it: **the execution is suspended**.

In case the process instance is suspended it has to be analyzed in Service Center to decide whether it can continue or should be stopped.

![Diagram showing the impact of moving an activity from a future to a past position in process flows, resulting in suspended execution.](images/process-upgrade-move-future-to-past.png "Process Upgrade: Moving Activity from Future to Past")

## Process Instance is Executing After the Moved Activity (Case 1)

In this case the execution of the process instance has already executed the moved activity and it is going to execute it again: **the execution is suspended**.

In case the process instance is suspended it has to be analyzed in Service Center to decide whether it can continue or should be stopped.

![Illustration of a process instance suspended due to an activity being moved from a past to a future position in the process flow.](images/process-upgrade-move-past-to-future.png "Process Upgrade: Moving Activity from Past to Future (Case 1)")

## Process Instance is Executing After the Moved Activity (Case 2)

In this case the execution of the process instance has already executed the moved activity in a [Conditional Start](<../../../ref/lang/auto/class-conditional-start.md>) and it is going to execute it again: **the execution is suspended**.

In case the process instance is suspended it has to be analyzed in Service Center to decide whether it can continue or should be stopped.

![Flowchart depicting a suspended process instance after moving an activity post-Conditional Start in a process flow.](images/process-upgrade-move-past-to-future-2.png "Process Upgrade: Moving Activity from Past to Future (Case 2)")
