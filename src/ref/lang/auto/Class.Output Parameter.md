---
kinds: ServiceStudio.Model.Variables+ActivityOutput+Kind, ServiceStudio.Model.Variables+GenericOutputParameter+Kind, ServiceStudio.Model.Variables+JSOutputParameter+Kind, ServiceStudio.Model.Variables+ProcessOutput+Kind, ServiceStudio.Model.Variables+SerializableOutputParameter+Kind, ServiceStudio.Model.Variables+WebReferenceGenericOutputParameter+Kind, ServiceStudio.Model.Variables+ReferenceActivityOutput+Kind, ServiceStudio.Model.Variables+ReferenceGenericOutputParameter+Kind, ServiceStudio.Model.Variables+ReferenceProcessOutput+Kind, ServiceStudio.Model.Variables+ReferenceSerializableOutputParameter+Kind
helpids: 7012, 30101
---

# Output Parameter

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
<td title="Default Value">Default Value</td>
<td>Initial value of this element. If undefined, the default value of the data type is used.</td>
<td></td>
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
<td title="Data Type">Data Type</td>
<td>The data type of the output parameter.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Is Start Activity Input/ Is Close Activity Input">Is Start Activity Input/ Is Close Activity Input</td>
<td>Indicates if the output parameter is also used as an input parameter of the process activity's extended action.</td>
<td>Yes</td>
<td>Yes, Mandatory</td>
<td>The possible values are:<br/>
        – "Yes, Mandatory": The output parameter is a mandatory input parameter of the Start&lt;Activity&gt;/Close&lt;Activity&gt; extended action;<br/>
        – "Yes, Optional": The output parameter is an optional input parameter of the Start&lt;Activity&gt;/Close&lt;Activity&gt; extended action;<br/>
        – "No": The output parameter is not an input parameter of the Start&lt;Activity&gt;/Close&lt;Activity&gt; extended action.<br/>
        The property "Is Start Activity Input" is only available when specifying an output parameter for a Conditional Start process activity.<br/>
        The property "Is Close Activity Input" is only available when specifying an output parameter for a Human Activity or a Wait process activities.</td>
</tr>
</tbody>
</table>

