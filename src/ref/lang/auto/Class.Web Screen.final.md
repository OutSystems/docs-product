---
kinds: ServiceStudio.Model.Nodes+WebScreen+Kind, ServiceStudio.Model.ReferenceWebScreen+Kind
helpids: 4011
---

# Web Screen

User interface that end users interact with.  

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
<td title="Title">Title</td>
<td>Text literal or expression displayed in the title bar of the browser.</td>
<td></td>
<td></td>
<td>When this property is empty, the title bar has the name of the element.</td>
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
<td title="HTTP Security">HTTP Security</td>
<td>Security level required for HTTP requests. Can be overridden by application security settings in Service Center or LifeTime.</td>
<td>Yes</td>
<td></td>
<td>The possible values are: "" (empty), None, SSL/TLS, SSL/TLS with client certificates.</td>
</tr>
<tr>
<td title="Integrated Authentication">Integrated Authentication</td>
<td>Set to Yes to use Integrated Authentication to validate user access.</td>
<td>Yes</td>
<td></td>
<td>An empty value means that the element inherits the integrated authentication specified at flow level.</td>
</tr>
<tr>
<td title="Cache in Minutes">Cache in Minutes</td>
<td>Maximum time content or results are stored in memory. When undefined, nothing is cached.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Is Frequent Destination">Is Frequent Destination</td>
<td>Set to Yes to make this element visible as a quick option in Destination lists.</td>
<td>Yes</td>
<td>No</td>
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
<tr >
<th colspan="5">Roles</th>
</tr>
<tr>
<td title="Roles">Roles</td>
<td>List of the Roles available in your module. Allows selection of the roles that have grants to display the web screen.</td>
<td></td>
<td>Anonymous (unselected)<br/>Registered<br/>ApplicationUser</td>
<td></td>
</tr>
<tr >
<th colspan="5">Extended Properties</th>
</tr>
<tr>
<td title="Property">Property</td>
<td>Name of an attribute to add to the HTML translation for this element.</td>
<td></td>
<td></td>
<td>You can pick a property from the drop-down list or type a free text. The name of the property will not be validated by the platform.<br/><br/>Duplicated properties are not allowed. Spaces, " or ' are also not allowed.</td>
</tr>
<tr>
<td title="Value">Value</td>
<td>Value of the attribute.</td>
<td></td>
<td></td>
<td>You can type the value directly or write expressions using the Expression Editor.<br/><br/>If the Value is empty, the corresponding HTML tag is created as property="property". For example, the nowrap property does not require a value, therefore nowrap="nowrap" is added.</td>
</tr>
</tbody>
</table>

