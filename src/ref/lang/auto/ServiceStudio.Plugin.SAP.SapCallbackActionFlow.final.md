---
kinds: ServiceStudio.Plugin.SAP.SapCallbackActionFlowDescriptor
helpids: 30068
---

# SAP Callback

Action that allows the customization of the calls to SAP remote functions. Once defined, they are executed on every call to any SAP remote functions under the connection. There are three available action flows for implementing these customizations: OnBeforeConnection, OnBeforeCall, OnAfterCall (defined in the SAP Connection element).  

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
</tbody>
</table>

