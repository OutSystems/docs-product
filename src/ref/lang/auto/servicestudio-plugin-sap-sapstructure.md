---
kinds: ServiceStudio.Plugin.SAP.SapStructureDescriptor
helpids: 30072
locale: en-us
guid: 895732c3-42f6-4e78-87f8-efef7a1de2ef
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Structure - SAP Remote Function

Structure used in input and output arguments of SAP remote functions.  

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
<tr >
<th colspan="5">Advanced</th>
</tr>
<tr>
<td title="OriginalABAPStructureType">Original ABAP DataType</td>
<td>Original ABAP structure data type in the SAP system.</td>
<td>Yes</td>
<td>Table</td>
<td></td>
</tr>
</tbody>
</table>

