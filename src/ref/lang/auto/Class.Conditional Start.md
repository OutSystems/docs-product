---
kinds: ServiceStudio.Model.ProcessNodes+ConditionalStart+Kind, ServiceStudio.Model.ReferenceConditionalStart+Kind
helpids: 0
---

# Conditional Start

Starts an alternative flow in the process flow.  

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
<td>Text displayed in the back-office when an instance of this Conditional Start activity is executed.</td>
<td></td>
<td></td>
<td>If not defined, the displayed text will be the Conditional Start activity name.</td>
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
<td title="Start On">Start On</td>
<td>Entity action that automatically starts the execution of the Conditional Start flow.</td>
<td></td>
<td></td>
<td>When an entity event is chosen, the primary key of the entity is automatically added as an input parameter of the process. In this way each process instance has a reference indicating which entity record it is related to.<br/><br/>
        Entity actions that start the exectution:<br/>
        <strong>Create &lt;entity&gt;:</strong>
        the Conditional Start begins the execution of the flow when a record is created for the specified entity;<br/><br/>
        <strong>Update &lt;entity&gt;:</strong>
        the Conditional Start begins the execution of the flow when a record is updated for the specified entity.<br/><br/></td>
</tr>
<tr>
<td title="Original Name">Original Name</td>
<td>Name of the element as defined in the module which implements it (producer module). This property is read-only.</td>
<td>Yes</td>
<td></td>
<td>This property is only visible for referenced elements.</td>
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
<td>StartedBy</td>
<td>Identifier of the user who started the process activity instance.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td>StartedInstant</td>
<td>Date and time when the process activity instance was started.</td>
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

