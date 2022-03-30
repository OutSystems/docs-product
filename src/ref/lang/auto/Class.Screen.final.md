---
kinds: ServiceStudio.Model.NRNodes+WebScreen+Kind, ServiceStudio.Model.NewRuntime.ReferenceWebScreen+Kind
helpids: 4011, 0
---

# Screen

User interface with which end users interact.  

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
<td title="Title">Title</td>
<td>Text literal or expression displayed in the title bar of the browser.</td>
<td></td>
<td></td>
<td>When this property is empty, the title bar has the name of the element. Using expressions in titles, and like that having dynamic page titles, works in Platform Server 11.13.0 with Service Studio 11.12.0, and later.</td>
</tr>
<tr>
<td title="Public">Public</td>
<td>Set to Yes to allow the element to be added as dependency by other modules.</td>
<td>Yes</td>
<td>No</td>
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
<tr>
<td title="(Theme Editor)">(Theme Editor)</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr >
<th colspan="5">Events</th>
</tr>
<tr>
<td title="On Initialize">On Initialize</td>
<td>Action executed before rendering the screen or block and before fetching data.</td>
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
<tr >
<th colspan="5">Roles</th>
</tr>
<tr>
<td title="Roles">Roles</td>
<td>List of the Roles available in your module. Allows selection of the roles that have grants to display the screen.</td>
<td></td>
<td>Anonymous (unselected)<br/>Registered</td>
<td></td>
</tr>
</tbody>
</table>

