---
kinds: ServiceStudio.Model.Entity+Kind, ServiceStudio.Model.SyntheticEntity+Kind, ServiceStudio.Model.ReferenceEntity+Kind
helpids: 15005
---

# Entity

An Entity represents a table in a database.  

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
<td title="Expose Read Only">Expose Read Only</td>
<td>Set to Yes to expose the entity while protecting its data records from being written in a consumer module.</td>
<td>Yes</td>
<td>No</td>
<td>Note: Consumer modules can update data records using SQL even when this property is set to Yes.</td>
</tr>
<tr>
<td title="Identifier Attribute">Identifier Attribute</td>
<td>Attribute that uniquely identifies the entity.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Label Attribute">Label Attribute</td>
<td>Attribute used to describe each record of the entity.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Order By Attribute">Order By Attribute</td>
<td>Attribute used for the default ordering of the records of the entity.</td>
<td></td>
<td>(None)</td>
<td></td>
</tr>
<tr>
<td title="Is Active Attribute">Is Active Attribute</td>
<td>Specifies a Boolean attribute of the entity which defines if the record is to be fetched in a query.</td>
<td></td>
<td>(None)</td>
<td></td>
</tr>
<tr>
<td title="Original Name">Original Name</td>
<td>Name of the element as defined in the module which implements it (producer module). This property is read-only.</td>
<td>Yes</td>
<td></td>
<td>This property is only visible for referenced elements.</td>
</tr>
<tr class="separator">
<th colspan="5">Advanced</th>
</tr>
<tr>
<td title="Update Behavior">Update Behavior</td>
<td>Set which is the way the update of entity records is performed:<br/> - <b>All Attributes</b>: all the attributes are always updated in the database.<br/> - <b>Changed Attributes</b>: only the attributes that were changed are updated in the database thus, improving efficiency.</td>
<td>Yes</td>
<td>Changed Attributes</td>
<td></td>
</tr>
<tr>
<td title="Expose Process Events">Expose Process Events</td>
<td>If set to True, creating or updating entity records issues events to processes.</td>
<td>Yes</td>
<td>No</td>
<td></td>
</tr>
<tr>
<td title="Is Multi-tenant">Is Multi-tenant</td>
<td>Set to Yes to isolate data per tenant or No to share data among tenants. If not set, it inherits the module setting.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Show Tenant Identifier">Show Tenant Identifier</td>
<td>Set to Yes to show the <code>TenantId</code> entity attribute and disable automatic data isolation for this entity.</td>
<td>Yes</td>
<td>No</td>
<td></td>
</tr>
<tr>
<td title="Original Show Tenant Identifier">Original Show Tenant Identifier</td>
<td>Indicates the <code>TenantId</code> property value originally set in the referenced module.</td>
<td>Yes</td>
<td>No</td>
<td></td>
</tr>
<tr>
<td title="Logical Database">Logical Database</td>
<td>The Platform's logical name for the external database where the entity is stored.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Supports Nulls">Supports Nulls</td>
<td>If set to Yes, mandatory attributes that are set with the default value are converted to/from null when storing/retrieving data from the external database. Otherwise no conversion is done.</td>
<td>Yes</td>
<td>No</td>
<td>This property is only visible for reference entities from extension modules.<br/>The value conversion only applies to mandatory attributes.</td>
</tr>
</tbody>
</table>

