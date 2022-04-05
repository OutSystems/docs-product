---
kinds: ServiceStudio.Model.Nodes+End+Kind, ServiceStudio.Model.Nodes+UpdateScreen+Kind
helpids: 0
---

# End

When designing the process flow of your process, you must end flow paths with the **End** process activity which you can drag onto your canvas from the [Process Flow Toolbox](<../../../develop/processes/process-flow/process-flow-toolbox.md>).

<div class="info" markdown="1">

The process execution terminates when all of the flow paths in the main process flow (the process flow that begins with the Start process activity) reach their End process activity.

</div>

## Terminating the Process Execution

You may force the process execution to be terminated by setting to 'Yes' the `Terminate Process` property of the End activity. Once one of these End elements is reached, the process execution is stopped and all its activities instances have their execution stopped in the life cycle state that they were executing.

<div class="info" markdown="1">

The execution of a terminated process might be restarted in the Service Center.

</div>



