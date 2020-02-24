# Using Process Activities Callback Actions

When designing the process flow of your process, you can add business rules to validate the execution of your process activities at some stage of their life cycle. This allows you to block or quit the activity instance execution if a specified condition is not verified. This behavior is implemented through **Activity Callback actions**.


## Add an Activity Callback Action

1. In the **eSpace tree**, under the **Process** layer, right-click on the **Process Activity** element and select the callback action.

1. Design the behavior of the action.

The business rules can be designed for the following available activity callback actions:

* **On Ready**: this action is executed before a **Conditional Start**, **Human Activity**, or **Wait** activity instance begins its work.

* **On Open**: this action is executed when the end user tries to open a task in the [Taskbox](../intro.md#using-the-taskbox), that is, when a **Human Activity** instance is being opened.

* **On Start**: this action is executed when a **Conditional Start** activity instance is about to **start executing its outgoing flow**.

* **On Close**: this action is executed when a **Human Activity** or **Wait** activity instance is about to **end its execution**.

* **On Skip**: this action is executed when a **Human Activity** or **Wait** activity instance is about to **be skipped**.

Below is a table containing a summary of which callback actions are executed by the activities:

|Tool   |![](../../../shared/icons-tools/action.png) On Ready   |![](../../../shared/icons-tools/action.png) On Open   |![](../../../shared/icons-tools/action.png) On Start   |![](../../../shared/icons-tools/action.png) On Close   |![](../../../shared/icons-tools/action.png) On Skip   |
|----------|----------|----------|----------|----------|----------|
|![](../../../shared/icons-tools/start-process.png) Start|-|-|-|-|-|
|![](../../../shared/icons-tools/conditional-start.png) Conditional Start|Yes|-|Yes|-|-|
|![](../../../shared/icons-tools/human-activity.png) Human Activity|Yes|Yes|-|Yes|Yes|
|![](../../../shared/icons-tools/email-send.png) Send Email|-|-|-|-|-|
|![](../../../shared/icons-tools/automatic-activity.png) Automatic Activity|-|-|-|-|-|
|![](../../../shared/icons-tools/process.png) Execute Process|-|-|-|-|-|
|![](../../../shared/icons-tools/wait-activity.png) Wait|Yes|-|-|Yes|Yes|
|![](../../../shared/icons-tools/decision.png) Decision|-|-|-|-|-|
|![](../../../shared/icons-tools/end-process.png) End|-|-|-|-|-|


## Designing Activities Callback Actions at Process Level

If you have the same business rules being executed by the callbacks of several process activities (in your process flow), you may move all of the common business rules to a single place: a common callback action at the process level. For that, add the corresponding activity callback action to your process and design the common business rules there.

<div class="info" markdown="1">

The activities callback actions at the process level are identified by the activity callback action name infixed with the `Activity` word. For example, `On Start` and `On Close` activity callback actions have corresponding common callback actions at the process level: `On Activity Start` and `On Activity Close`.

</div>


## Add an Activity Callback Action at Process Level

1. In the **eSpace tree**, under the **Process** layer, right-click on the **Process** element and select the available `On Activity ...` action.
1. Design the behavior of the action.

When the process is being executed, the activity callback actions are executed as follows:

1. Executes the activity callback action defined in the process (if any).
1. Executes the callback action defined in the activity (if any).

<div class="warning" markdown="1">

Sub-processes executed in your process flow do not inherit the callback actions. This means that each process level has its own independent callback actions.

</div>
