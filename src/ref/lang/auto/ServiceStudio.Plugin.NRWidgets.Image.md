---
kinds: ServiceStudio.Plugin.NRWidgets.ImageDescriptor
helpids: 30043
---

# Image

Displays an image from a defined source.  

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
<td title="Type">Type</td>
<td>Specifies the source of the image: Local Image, External URL or Binary Data.</td>
<td>Yes</td>
<td>Local Image</td>
<td></td>
</tr>
<tr>
<td title="Image">Image</td>
<td>Defines the image to display when Type is set to Local Image.</td>
<td></td>
<td></td>
<td>Only available when Type is set as Local.</td>
</tr>
<tr>
<td title="Url">URL</td>
<td>Defines the URL of the image to display when Type is set to External URL.</td>
<td></td>
<td></td>
<td>Only available when Type is set as External URL.</td>
</tr>
<tr>
<td title="ImageContent">Image Content</td>
<td>Defines the image to display when Type is set to Binary Data.</td>
<td>Yes</td>
<td></td>
<td>Only available when Type is set as Binary Data.</td>
</tr>
<tr>
<td title="DefaultImage">Default Image</td>
<td>Image to display when the Binary Data image cannot be fetched.</td>
<td></td>
<td></td>
<td>Only available when Type is set as Binary Data.</td>
</tr>
<tr>
<td title="Style">Style Classes</td>
<td>Specifies one or more style classes to apply to the widget. Separate multiple values with spaces.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="separator">
<th colspan="5">Attributes</th>
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

## Events

<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
<th>Mandatory</th>
<th>Observations</th>
</tr>
</thead>
<tbody>
<tr>
<td title="EventName">Event</td>
<td>JavaScript or custom event to be handled.</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Handler">Handler</td>
<td>JavaScript event handler.</td>
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
<td>Id</td>
<td>Identifies the widget instance at runtime (HTML 'id' attribute). You can use it in JavaScript and Extended Properties.</td>
<td>Yes</td>
<td>Text</td>
<td></td>
</tr>
</tbody>
</table>

