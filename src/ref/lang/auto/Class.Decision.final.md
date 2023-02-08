---
kinds: ServiceStudio.Model.ProcessNodes+Decision+Kind
helpids: 0
locale: en-us
guid: 87b4ecb6-b6c3-4c7b-b2ab-603bd95f36e2
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Decision

When designing the process flow of your process, you can split it into multiple paths, only one of which is followed, depending on the behavior implemented through the **Decision** process activity which you can drag onto your canvas from the [Process Flow Toolbox](<../../../develop/processes/process-flow/process-flow-toolbox.md>).

By default, the first two connectors for the Decision are labeled with Yes and No because these are the most frequent ones. However, you may change these names and also add more connectors with other names.

A Decision can have local variables.

Design your Decision so that it can be called many times, that is, design it without any "side-effects," such as adding, changing, or deleting entity records in the database or in external systems. This means that you must design your Decision to be reentrant.

## Flow of a Decision

The logic of the decision is implemented through a decision flow which is identical to an action flow except that all flows must end with an **Outcome** decision element. The Outcome defines the result returned by your decision flow to the process flow. Design your decision flow using the action flow editor.

You may have more than one Outcome decision element in your decision flow but only one result is returned from your decision.

To quickly launch the editor, simply double-click on the Decision process activity, in the process flow.

In the Process flow, each connector that flows from the Decision must be labeled with a name. Then, use these names in the Outcome decision elements when designing your decision flow.

All of the connectors flowing from the Decision in the process flow must have a corresponding Outcome decision element in the decision flow.

## Error Handling

When an error is raised in the Decision flow it causes the execution of the flow to stop. However, the Decision flow execution is retried again (from the beginning) after a while. This procedure is repeated until the Decision flow is successfully executed or the process is terminated.

Use Service Center to monitor which processes and process activities are raising errors.

## Decision Scope

Decisions are executed in the scope of the process flow and you have access to the following elements:

* Output parameters from previously executed elements in the process flow path
* Process input and output parameters
* Decision local variables
* Actions output parameters invoked in the Decision
* Queries invoked in the Decision

When you're editing your decision flow, all of the elements available in the scope are present in the Scope tree of the Expression Editor, in a case where you're editing an expression, or in the variables tree of the Select Variable window, in a case where you're trying to use a variable.

## Properties

<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
<th>Mandatory</th>
<th>Default value</th>
<th>Observations</th>
</tr>
</thead>
<tbody>
<tr>
<td title="Description">Description</td>
<td>Text that documents the element.</td>
<td></td>
<td></td>
<td>Useful for documentation purpose.<br/>The maximum size of this property is 2000 characters.</td>
</tr>
<tr>
<td title="Label">Label</td>
<td>Text displayed in the back-office when an instance of this Decision activity is executed.</td>
<td></td>
<td></td>
<td>If not defined, the displayed text will be the Decision activity name.</td>
</tr>
<tr>
<td title="Name">Name</td>
<td>Identifies an element in the scope where it is defined, like a screen, action, or module.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

## Runtime Properties

<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
<th>Read Only</th>
<th>Type</th>
<th>Observations</th>
</tr>
</thead>
<tbody>
<tr>
<td>ClosedInstant</td>
<td>Date and time when the process activity instance was closed.</td>
<td>Yes</td>
<td>Date Time</td>
<td></td>
</tr>
<tr>
<td>ActivityId</td>
<td>Identifier of the process activity instance at runtime.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

