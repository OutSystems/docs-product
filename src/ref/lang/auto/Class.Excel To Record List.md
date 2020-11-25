---
kinds: ServiceStudio.Model.Nodes+ExcelToRecordList+Kind
helpids: 10001
---

# Excel To Record List

Imports the contents of an MS Excel sheet into a list.  

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
<td title="Record Definition">Record Definition</td>
<td>Entity or structure that defines the structure of the data that you want to load.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="File Content">File Content</td>
<td>Holds the Excel file.</td>
<td>Yes</td>
<td></td>
<td>The expected data type is Binary Data.</td>
</tr>
<tr>
<td title="Sheet Name">Sheet Name</td>
<td>Name of the Excel sheet to import. By default, the first sheet is imported, unless a sheet named 'Sheet1' exists in the file.</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

