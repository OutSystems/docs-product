---
kinds: ServiceStudio.Model.Entity+Kind, ServiceStudio.Model.SyntheticEntity+Kind, ServiceStudio.Model.ReferenceEntity+Kind
helpids: 15005
locale: en-us
guid: 1c756124-6173-4742-a20d-52bb7e0833fc
app_type: traditional web apps, mobile apps, reactive web apps
---

# Static Entity

A static entity is an entity that has static data associated to it. This static data is managed at design time and can be used directly in the business logic design of the application, benefiting from strong typing.  

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
<td>Identifies the entity in the module.</td>
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
<td>Label used to describe the entity in the user interface of the application.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Label (plural)">Label (plural)</td>
<td>Label used to described the plural of the entity in the user interface of the application.</td>
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
<td title="Identifier Attribute">Identifier Attribute</td>
<td>Attribute that uniquely identifies the entity.</td>
<td></td>
<td>Id</td>
<td></td>
</tr>
<tr>
<td title="Label Attribute">Label Attribute</td>
<td>Label used to describe the attribute.</td>
<td></td>
<td>Label</td>
<td></td>
</tr>
<tr>
<td title="Order By Attribute">Order By Attribute</td>
<td>Attribute used for the default ordering of the records of the entity.</td>
<td></td>
<td>Order</td>
<td></td>
</tr>
<tr>
<td title="Is Active Attribute">Is Active Attribute</td>
<td>Specifies a Boolean attribute of the entity which defines if the record is to be fetched in a query.</td>
<td></td>
<td>Is_Active</td>
<td></td>
</tr>
<tr>
<td title="Original Name">Original Name</td>
<td>Name of the element as defined in the module which implements it (producer module). This property is read-only.</td>
<td>Yes</td>
<td></td>
<td>This property is only visible for referenced elements.</td>
</tr>
<tr >
<th colspan="5">Advanced</th>
</tr>
<tr>
<td title="Use Translations">Use Translations</td>
<td>Indicates whether to use existing translation for the records of the static entity or not.</td>
<td>Yes</td>
<td>Yes</td>
<td></td>
</tr>
</tbody>
</table>

