---
kinds: ServiceStudio.Model.Nodes+WebBlock+Kind, ServiceStudio.Model.ReferenceWebBlock+Kind
helpids: 1006
tags: runtime-traditionalweb
locale: en-us
guid: 5d03bd37-8e91-4c60-8d7f-b550ab56994d
---

# Web Block


Reusable screen part that can implement its own logic.

## Exposed Web Block

A Web Block cannot be exposed when:

* It has a parameter that is defined using an Entity/Structure that is not exposed.
* It has a parameter that is defined using an Entity/Structure that is reused from another module.
* It contains a Link widget, Button widget, or a consumed Web Screen with arguments of Binary Data, Record, or List data types.

In case the execution of the Producer and Consumer modules are under different User Providers, the modules have different sessions. In this case, variables associated to the session can hold different values between modules.

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
<td></td>
</tr>
<tr>
<td title="Icon">Icon</td>
<td>Picture to be displayed to help identify this element.</td>
<td>Yes</td>
<td></td>
<td></td>
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
<td title="Cache in Minutes">Cache in Minutes</td>
<td>Maximum time content or results are stored in memory. When undefined, nothing is cached.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Style Sheet">Style Sheet</td>
<td>Style sheet associated with this element.</td>
<td></td>
<td></td>
<td>Click on "..." to edit the property value.</td>
</tr>
<tr>
<td title="JavaScript">JavaScript</td>
<td>JavaScript associated with this element.</td>
<td></td>
<td></td>
<td>Click on "..." to edit the property value.</td>
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
<td>RuntimeId</td>
<td>The identifier of the Web Block instance at runtime.</td>
<td>Yes</td>
<td>Text</td>
<td></td>
</tr>
</tbody>
</table>

