---
summary: OutSystems 11 (O11) feature for converting Record Lists to Excel files, including mandatory properties and attributes for file export.
helpids: 10002
locale: en-us
guid: d1e3abef-bbf3-4455-87b2-3c19acc594bb
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: data export, excel integration, data management, application development, outsystems best practices
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Record List To Excel

Converts a Record List to an Excel file. You can use the output file for download or you can send it as an email attachment, for example. The Record List to Excel action executes exclusively on the server-side and must be used within a Server Action.

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
<td title="Record List">Record List</td>
<td>Holds the list of records to be exported to an Excel file.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr >
<th colspan="5">Attributes</th>
</tr>
<tr>
<td title="Attribute">Attribute</td>
<td>Record attribute(s) to include in the export.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

