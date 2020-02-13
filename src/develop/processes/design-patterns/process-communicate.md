# Communicating with a Process

Use this patterns to communicate with a process, from another process or from the application.

There are two ways of doing this:

* **Explicitly**: the communication is made through explicit call to process-specific actions.
* **Implicitly**: the communication is made through actions over records in the database.


## Explicit Communication

The communication to a process is made through [process extended actions](../actions-extended/intro.md) or process system actions/functions.

### Launch a Process

Use the [Launch&lt;Process&gt;](../actions-extended/launch-process-action.md) process extended action to launch the execution of another process.

### Start a Flow within a Process

Design the flow in a [Conditional Start](<../../../ref/lang/auto/Class.Conditional Start.final.md>) and use the [Start&lt;Conditional Start&gt;](../actions-extended/start-conditional-start-action.md) action to start executing new instances of the flow. This is useful when the number of executed instances of a flow is only known at runtime.

### Terminate a Process

A process may be terminated with the **ProcessTerminate** system action or with the [Terminate](<../../../ref/lang/auto/Class.Process End.final.md>) tool in the process flow. If the process has launched child processes, make sure you design logic to also terminate them.

### Close an Activity

One way of ending the execution of an activity in a process is through the **ActivityClose** system action.

The other way is to use extended actions, which are directly bound to the activity:

* [Close&lt;Human Activity&gt;](../actions-extended/close-human-activity-action.md): Ends the execution of a [Human Activity](<../../../ref/lang/auto/Class.Human Activity.final.md>) in a process. You may use it for, for example, explicitly end the execution of a human activity that is no longer necessary.

* [Close&lt;Wait&gt;](../actions-extended/close-wait-action.md): Ends the execution of a [Wait](<../../../ref/lang/auto/Class.Wait.final.md>) in a process. You may use it for, for example, to explicitly end a wait activity in a process when another process reaches a certain point in its flow.

Once the activity is closed, the process follows on to the next activity in the flow.

You may use the **On Close** callback action to add specific logic to validate whether to close the activity or not.


## Implicit Communication

The communication to the process is made through events that occur in the database, such as the creation and update of entity records.

### Implicitly Launch a Process

To implicitly launch a process, set that process `Launched On` property to **Create&lt;Entity&gt;**. For each newly created entity record a process instance is launched.

### Implicitly Start a Flow within a Process

Design the flow in a [Conditional Start](<../../../ref/lang/auto/Class.Conditional Start.final.md>) and set its `Start On` property to **Create&lt;Entity&gt;** / **Update&lt;Entity&gt;**.  After that, the execution of a new instance of the flow is started every time a record of the entity is created/updated. This is useful when the number of executed instances of a flow is only known at runtime.

### Implicitly Close an Activity

Use the `Close On` property of activities to implicitly end their execution when an entity is either created or updated:

* [Human Activity](<../../../ref/lang/auto/Class.Human Activity.final.md>): for example, end the execution of a human activity when an entity is updated with a specific value;

* [Wait](<../../../ref/lang/auto/Class.Wait.final.md>): for example, implement a waiting activity in a process that waits until another process updates an entity with a specific value.

Once the activity is closed, the process follows on to the next activity in the flow.

You may use the **On Close** callback action to add specific logic to validate whether to close the activity or not.
