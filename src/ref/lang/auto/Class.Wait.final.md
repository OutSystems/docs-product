---
kinds: ServiceStudio.Model.ProcessNodes+WaitActivity+Kind, ServiceStudio.Model.ReferenceWaitActivity+Kind
helpids: 0
locale: en-us
guid: f8be65b0-6cde-4d57-ad19-0f473f662fa0
---

# Wait

When designing the process flow of your process, you can put your process flow execution on hold. This behavior is implemented through the **Wait** process activity which you can drag onto your canvas from the [Process Flow Toolbox](<../../../develop/processes/process-flow/process-flow-toolbox.md>).

The Wait process activity allows you to put your process flow execution on hold until one of the following events occurs:

* **A timeout**: a specified timeout date is reached.
* **An entity action**: when an Entity Action that **creates** or **updates** an entity is executed and it matches the conditions to close the wait activity.

A Wait process activity can have input parameters, output parameters and [callback actions](<../../../develop/processes/actions-callback/actions-activities-callback.md>).

## End the Activity on Entity Events

If the execution of the wait is to be automatically ended after an event occurs over an entity, the kind of event must be set in the `Close On` property with one of the following entity actions: **Create&lt;Entity&gt;** or **Update&lt;Entity&gt;**.

Once you select the kind of event in the `On Close` property, a list of entity attributes is displayed for you to set the condition to automatically end the wait activity: a primary key for a specific record and/or reference attributes for a specific value on an attribute.

For example, if the wait activity is designed to wait until an entity is updated to a certain status, set its `On Close` property to the **Update&lt;Entity&gt;** entity action and the condition of the status to the expected status.

## Using Wait Activity References

Service Studio provides you with mechanisms to access Wait process activities among eSpaces. You can expose your Wait process activities to other eSpaces or use the Wait process activities defined in another eSpace.

## Remarks

Changing the `Close On` property to listen to events from another entity only has effect on Wait instances that are created after the change. All instances that were already executing will continue listening to events from the previous entity. Therefore, you should only make this change when there are no more Wait instances listening to the previous entity.

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
<td>Text displayed in the back-office when an instance of this Wait activity is executed.</td>
<td></td>
<td></td>
<td>If not defined, the displayed text will be the Wait process activity name.</td>
</tr>
<tr>
<td title="Name">Name</td>
<td>Identifies an element in the scope where it is defined, like a screen, action, or module.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Public">Public</td>
<td>Indicates whether this process activity can be used by other modules.</td>
<td>Yes</td>
<td>No</td>
<td>This property is only available for process activities that were created in the current module. When a process activity is public its process must also be public.</td>
</tr>
<tr>
<td title="Close On">Close On</td>
<td>Entity action that automatically ends the Wait Activity execution.</td>
<td></td>
<td></td>
<td>The event that automatically closes (ends) the process activity execution:<br/><br/>
        <strong>Create &lt;entity&gt;:</strong> the Wait is ended when a record is created for the specified entity;<br/><br/>
        <strong>Update &lt;entity&gt;:</strong> the Wait is ended when a record is updated for the specified entity.</td>
</tr>
<tr>
<td title="Original Name">Original Name</td>
<td>Name of the element as defined in the module which implements it (producer module). This property is read-only.</td>
<td>Yes</td>
<td></td>
<td>This property is only visible for referenced elements.</td>
</tr>
<tr >
<th colspan="5">Advanced</th>
</tr>
<tr>
<td title="Timeout">Timeout</td>
<td>Date and time until the Wait activity pauses the process flow execution.</td>
<td></td>
<td></td>
<td>You may set the timeout date in two ways:<br/><br/>
        <strong>Absolute:</strong> the timeout date is fixed.<br/>
        For example: <code>#2015-01-01 00:00:00#</code><br/><br/>
        <strong>Relative:</strong> the timeout date depends on the current moment.
        For example, if you want to wait a day then define your timeout date as: <code>AddDays(CurrDateTime(),1)</code><br/>
        This value is defined as a Date Time.</td>
</tr>
<tr>
<td title="Allow Skip">Allow Skip</td>
<td>If set to True, the activity execution may be skipped.</td>
<td>Yes</td>
<td>No</td>
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
<td>Expired</td>
<td>True if the process activity instance ended because of a timeout.</td>
<td>Yes</td>
<td>Boolean</td>
<td></td>
</tr>
<tr>
<td>Skipped</td>
<td>True if the process activity instance ended because it was skipped.</td>
<td>Yes</td>
<td>Boolean</td>
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

