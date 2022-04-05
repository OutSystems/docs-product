---
kinds: ServiceStudio.Model.Image+Kind, ServiceStudio.Model.ReferenceImage+Kind
helpids: 0
---

# Image

An image resource. The supported image formats are GIF, JPEG, and PNG.  

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
<td title="Width">Width</td>
<td>Width of the image in pixels.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Height">Height</td>
<td>Height of the image in pixels.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Runtime Path">Runtime Path</td>
<td>Path to the image.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Original Filename">Original Filename</td>
<td>Name of the file from which the image was imported.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Original Format">Original Format</td>
<td>File format of the imported image.</td>
<td></td>
<td></td>
<td></td>
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
<td>URL</td>
<td>The runtime URL of the image.</td>
<td>Yes</td>
<td>Text</td>
<td>Only available in mobile apps.</td>
</tr>
</tbody>
</table>

