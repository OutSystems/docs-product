---
kinds: ServiceStudio.Model.NRFlows+ClientActionFlow+Kind, ServiceStudio.Model.NRFlows+ClientScreenActionFlow+Kind, ServiceStudio.Model.ReferenceClientAction+Kind
helpids: 30098
---

# Client Action

Action that runs logic on the client side.  

## Exposed Client Action

An Action cannot be exposed when:

* It has a parameter that is defined using an Entity/Structure that is not exposed.
* It has a parameter that is defined using an Entity/Structure that is reused from another module.

In case the execution of the Producer and Consumer modules are under different User Providers, the modules have different sessions. In this case, variables associated to the session can hold different values between modules.

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
<tr>
<td title="Function">Function</td>
<td>Set to Yes to define the action as a function. Functions must return a value and can be used in expressions.</td>
<td>Yes</td>
<td>No</td>
<td>This property is only available in global scope actions. Client actions set as functions can only be used in client action expressions.</td>
</tr>
<tr>
<td title="Icon">Icon</td>
<td>Picture to be displayed to help identify this element.</td>
<td>Yes</td>
<td></td>
<td>The recommended dimensions for the icon are 32 &#215; 32 pixels.</td>
</tr>
<tr>
<td title="Original Name">Original Name</td>
<td>Name of the element as defined in the module which implements it (producer module). This property is read-only.</td>
<td>Yes</td>
<td></td>
<td>This property is only visible for referenced elements.</td>
</tr>
</tbody>
</table>

