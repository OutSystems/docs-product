---
kinds: ServiceStudio.Model.Flows+Process+Kind, ServiceStudio.Model.ReferenceProcess+Kind
helpids: 17016
locale: en-us
guid: 27d0d6c8-85f1-45aa-adf1-a6333b01c3b9
---

# Process

A process is an element that allows you to integrate your business processes into your applications. It's designed in a process flow, which usually represents the activities that have to be carried out during an entity life cycle. 

Check how to [use processes](<../../../develop/processes/intro.md>) in OutSystems.

## Exposed Process Activity

A Process Activity **cannot be exposed** if their Process is not exposed or the module is Multi-tenant. 

Process activities that can be exposed are:

* Human Activity
* Wait
* Conditional Start

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
<td title="Public">Public</td>
<td>Set to Yes to allow the element to be added as dependency by other modules.</td>
<td>Yes</td>
<td>No</td>
<td>This property is only available for processes that were created in the current module. When a process is set to public its process entity is also made public.</td>
</tr>
<tr>
<td title="Launch On">Launch On</td>
<td>Entity action that automatically starts the execution of a new process instance.</td>
<td></td>
<td></td>
<td>When an entity action is chosen, the primary key of the entity is automatically added as an input parameter of the process. This way, each process instance has a reference indicating the entity record it is related to.</td>
</tr>
<tr>
<td title="Original Name">Original Name</td>
<td>Name of the element as defined in the module which implements it (producer module). This property is read-only.</td>
<td>Yes</td>
<td></td>
<td>This property is only visible for referenced elements.</td>
</tr>
<tr >
<th colspan="5">End-User Information</th>
</tr>
<tr>
<td title="Label">Label</td>
<td>Name of the Process to be displayed to the end user.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Detail">Detail</td>
<td>Description to be used as the default Detail property of Human Activities in the process flow. This description will be displayed to the end user in the Taskbox for all Human Activities inside this process. Changing this value will not affect existing Human Activity instances.</td>
<td></td>
<td></td>
<td>This property should be defined when the Launch On property is not defined or, if defined, when the Entity referred in it does not have any Text attribute. These properties are used to calculate a default value for the Detail property of Human Activities that don't have that property specified.<br/>
        You can use expressions to build dynamic descriptions, giving more contextual information to the end user.</td>
</tr>
<tr >
<th colspan="5">Advanced</th>
</tr>
<tr>
<td title="Expose Process Entity">Expose Process Entity</td>
<td>Set to Yes to make the corresponding Process Entity become available in the Entities folder.</td>
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
<td>ProcessId</td>
<td>Identifier of the process instance at runtime.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

