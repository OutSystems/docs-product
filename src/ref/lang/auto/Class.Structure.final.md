---
kinds: ServiceStudio.Model.Structure+Kind, ServiceStudio.Model.SystemActionStructure+Kind, ServiceStudio.Model.WebReferenceStructure+Kind, ServiceStudio.Model.ReferenceStructure+Kind
helpids: 15007, 30102
locale: en-us
guid: fe544d88-12d3-4de4-95b1-687bc64c34bc
---

# Structure

A Structure is a compound data type used to encapsulate groups of related attributes.  

## Exposed Structure

A Structure cannot be exposed when:

* It has an attribute that is defined using an Entity/Structure that is not exposed.
* It has an attribute that is defined using an Entity/Structure that is reused from another module.

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
</tbody>
</table>

