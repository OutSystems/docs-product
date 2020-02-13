When designing the process flow of your process, you can add work to be carried out automatically in your process, that is, without the need for human intervention. This behavior is implemented through the **Automatic Activity** process activity which you can drag onto your canvas from the [Process Flow Toolbox](<../../../develop/processes/process-flow/process-flow-toolbox.md>).

An Automatic Activity can have output parameters and local variables.

Whenever you have side-effects, such as adding, changing, or deleting entity records in the database or in external systems, design them in an Automatic Activity.

## Flow of an Automatic Activity

Design the behavior of your Automatic Activity through an action flow. This means that, an Automatic Activity implements business logic in the same way as for an action through the action flow editor.

## Error Handling

When an error is raised in the Automatic Activity flow it causes the execution of the flow to stop. However, the Automatic Activity flow execution is retried again (from the beginning) after a while. This procedure is repeated until the Automatic Activity flow is successfully executed or the process is terminated.

Use Service Center to monitor which processes and process activities are raising errors.

## Automatic Activity Scope

Automatic Activities are executed in the scope of the process flow and you have access to the following elements:

* Output parameters from previously executed elements in the process flow path and local variables defined in the Automatic Activity.
* Process input and output parameters.
* Automatic Activity local variables.
* Actions output parameters invoked in the Automatic Activity.
* Queries invoked in the Automatic Activity.
* Automatic Activity output parameters.

When you're editing your automatic activity flow, all of the elements available in the scope are present in the Scope tree of the Expression Editor, in a case where you're editing an expression; or in the variables tree of the Select Variable window, in a case where you're trying to use a variable.
