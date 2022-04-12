---
kinds: ServiceStudio.Model.EntityAttribute+Kind, ServiceStudio.Model.ReferenceEntityAttribute+Kind
helpids: 0
locale: en-us
guid: a5293dd0-7718-4b6e-a560-a807edb69083
---

# Entity Attribute

An Entity Attribute represents a column in a database table.  

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
<td title="Label">Label</td>
<td>Text used when the attribute is displayed in widgets.</td>
<td></td>
<td></td>
<td>This property is also used as the column header when exporting entity data to Excel.</td>
</tr>
<tr>
<td title="Data Type">Data Type</td>
<td>The attribute data type.</td>
<td>Yes</td>
<td></td>
<td>The attribute data type must be a basic data type or an Entity Identifier.</td>
</tr>
<tr>
<td title="Length">Length</td>
<td>Maximum size of the attribute in characters.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Decimals">Decimals</td>
<td>Number of decimal places.</td>
<td></td>
<td></td>
<td>Only available when data type is Decimal (mandatory).</td>
</tr>
<tr>
<td title="Is AutoNumber">Is AutoNumber</td>
<td>Set to Yes to generate and set Number values automatically at runtime.</td>
<td>Yes</td>
<td>No</td>
<td></td>
</tr>
<tr>
<td title="Is Mandatory">Is Mandatory</td>
<td>Set to Yes to require for a value to be set when using Form validations.</td>
<td>Yes</td>
<td>No</td>
<td></td>
</tr>
<tr>
<td title="Delete Rule">Delete Rule</td>
<td>Specifies the action to take when the record that the foreign key references is deleted.</td>
<td>Yes</td>
<td>Protect</td>
<td>Only available when data type is an Entity Identifier (the attribute is a foreign key).<br/>
        Possible values are <strong>Protect</strong>, <strong>Delete</strong> and <strong>Ignore</strong>.<br/>
        If the foreign key references an external Entity exposed by an Extension, the only possible value is <strong>Ignore</strong>, as the referential integrity can't be guaranteed.</td>
</tr>
<tr>
<td title="Default Value">Default Value</td>
<td>Initial value of this element. If undefined, the default value of the data type is used.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr >
<th colspan="5">Advanced</th>
</tr>
<tr>
<td title="Original Name">Original Name</td>
<td>The attribute column name as defined in the external database.</td>
<td></td>
<td></td>
<td>This property is only available in external entities' attributes.</td>
</tr>
<tr>
<td title="Original Type">Original Type</td>
<td>The attribute column data type as defined in the external database.</td>
<td></td>
<td></td>
<td>This property is only available in external entities' attributes.</td>
</tr>
</tbody>
</table>

