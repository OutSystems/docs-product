---
kinds: ServiceStudio.Model.NRNodes+WebBlock+Kind, ServiceStudio.Model.NewRuntime.ReferenceWebBlock+Kind
helpids: 1006
locale: en-us
guid: fc28dd21-c51c-429f-a88d-61824267676a
---

# Block

Reusable screen part that can implement its own logic.  

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
<td title="Style Sheet">Style Sheet</td>
<td>Style sheet associated with this element.</td>
<td></td>
<td></td>
<td>Click on "..." to edit the property value.</td>
</tr>
<tr >
<th colspan="5">Events</th>
</tr>
<tr>
<td title="On Initialize">On Initialize</td>
<td>Action to be executed before the block is rendered.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="On Ready">On Ready</td>
<td>Action to be executed after the static content of this element is rendered. The data may not be available at this moment.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="On Render">On Render</td>
<td>Action to be executed when this screen/element is completely rendered and after a change in a variable, aggregate or data action of the screen/element.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="On Destroy">On Destroy</td>
<td>Action to be executed when this element will be removed from the DOM.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="On Parameters Changed">On Parameters Changed</td>
<td>Action to be executed when the value of an input parameter of this element changes.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr >
<th colspan="5">Required Scripts</th>
</tr>
<tr>
<td title="Required Script">Required Script</td>
<td>Script(s) required by the element.</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

