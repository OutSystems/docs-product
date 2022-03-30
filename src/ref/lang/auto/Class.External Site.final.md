---
kinds: ServiceStudio.Model.Nodes+WebExternalSite+Kind, ServiceStudio.Model.NRNodes+WebExternalSite+Kind
helpids: 1003
---

# External Site

Navigates to a given URL, which can be defined during development time or runtime. During the development time the URL is entered in the **URL** property of the External Site Tool. To supply the URL dynamically you need the URL input parameter which you can create by right-clicking the External Site in the tree and selecting **Add Input Parameter**. The name `URL` of the input parameter must not change.

Encode the URL by using the [EncodeURL()](<builtinfunction.Text.final.md#EncodeUrl>) built-in function.

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
<td title="URL">URL</td>
<td>Site address to which to navigate.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr >
<th colspan="5">Advanced</th>
</tr>
<tr>
<td title="Is Frequent Destination">Is Frequent Destination</td>
<td>Set to Yes to make this element visible as a quick option in Destination lists.</td>
<td>Yes</td>
<td>No</td>
<td>This property is only available in web apps.</td>
</tr>
</tbody>
</table>

