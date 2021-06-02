---
kinds: ServiceStudio.Model.ProcessNodes+HumanActivity+Kind, ServiceStudio.Model.ReferenceHumanActivity+Kind
helpids: 0
---

# Human Activity

Activity to be executed by an end user.

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
<td title="Name">Name</td>
<td>Identifies an element in the scope where it is defined, like a screen, action, or module.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Description">Description</td>
<td>Text that documents the element.</td>
<td></td>
<td></td>
<td>Useful for documentation purpose.<br/>The maximum size of this property is 2000 characters.</td>
</tr>
<tr>
<td title="Label">Label</td>
<td>Text displayed to the end user in the Taskbox and in the back-office when an instance of this Human Activity is executed.</td>
<td></td>
<td></td>
<td>If not defined, the displayed text will be the Human Activity name.</td>
</tr>
<tr>
<td title="Public">Public</td>
<td>Indicates whether this process activity can be used by other modules.</td>
<td>Yes</td>
<td>No</td>
<td>This property is only available for process activities that were created in the current module. When a process activity is public its process must also be public.</td>
</tr>
<tr>
<td title="User">User</td>
<td>Defines the user that is going to complete the activity. Can be an expression.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Close On">Close On</td>
<td>Entity action that automatically ends the Human Activity execution.</td>
<td></td>
<td></td>
<td>The event that automatically closes (ends) the process activity execution:<br/><br/>
        <strong>Create &lt;entity&gt;:</strong> the Human Activity is closed when a record is created for the specified entity;<br/><br/>
        <strong>Update &lt;entity&gt;:</strong> the Human Activity is closed when a record is updated for the specified entity.</td>
</tr>
<tr>
<td title="Destination">Destination</td>
<td>Screen where the user will complete the Human Activity work after opening this activity in the Taskbox.</td>
<td></td>
<td></td>
<td>Available in Reactive Web and Traditional apps.</td>
</tr>
<tr>
<td title="Original Name">Original Name</td>
<td>Name of the element as defined in the module which implements it (producer module). This property is read-only.</td>
<td>Yes</td>
<td></td>
<td>This property is only visible for referenced elements.</td>
</tr>
<tr class="separator">
<th colspan="5">End-User Information</th>
</tr>
<tr>
<td title="Detail">Detail</td>
<td>Description of the Human Activity to be displayed to the end user in the Taskbox. Can be an expression. Overrides the Detail value defined on the Process. Changing this value will not affect existing Human Activity instances.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Instructions">Instructions</td>
<td>Instructions on how to complete the Human Activity work to be displayed to the end user in the Taskbox.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Due Date">Due Date</td>
<td>Optional date to inform the end user when is the due date of the activity. Can be an expression.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="separator">
<th colspan="5">Advanced</th>
</tr>
<tr>
<td title="Allow Skip">Allow Skip</td>
<td>If set to True, the execution of a failed activity may be skipped.</td>
<td>Yes</td>
<td>No</td>
<td>If skip is allowed, the end user's Taskbox displays an option to skip a failed activity. This option cannot skip a wait activity, use the system action ActivitySkip instead.</td>
</tr>
<tr>
<td title="Start Date">Start Date</td>
<td>Optional date that defines when the activity is scheduled to become available to be handled. Can be an expression.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="separator">
<th colspan="5">Roles</th>
</tr>
<tr>
<td title="Roles">Roles</td>
<td>List of the Roles available in your module. Allows selection of the roles that have grants to carry out the Human Activity work.</td>
<td></td>
<td>Registered<br/>ApplicationUser</td>
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
<td>ClosedBy</td>
<td>Identifier of the end user that closed the process activity instance.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td>ClosedInstant</td>
<td>Date and time when the process activity instance was closed.</td>
<td>Yes</td>
<td>Date Time</td>
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

