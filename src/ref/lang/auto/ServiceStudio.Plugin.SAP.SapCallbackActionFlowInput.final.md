---
kinds: ServiceStudio.Plugin.SAP.SapCallbackActionFlowInputDescriptor
helpids: 30069
locale: en-us
guid: 03cdc256-d569-4d64-b280-eea6b54e24bb
app_type: traditional web apps, mobile apps, reactive web apps
---

# Input Parameter (SAP Callback)

<div class="info" markdown="1">

Only applies to Windows-only Service Studio.

</div>

Input parameter of a SAP Callback action (named FunctionName). Added automatically by Service Studio to the OnAfterCall and OnBeforeCall SAP Callback actions.  

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
<td title="Type">Data Type</td>
<td>The data type of the input parameter.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="IsMandatory">Is Mandatory</td>
<td>Set to Yes to require for a value to be set.</td>
<td>Yes</td>
<td>Yes</td>
<td></td>
</tr>
<tr>
<td title="DefaultValue">Default Value</td>
<td>Initial value of this element. If undefined, the default value of the data type is used.</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

