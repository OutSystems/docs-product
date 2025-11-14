---
summary: Explore the encapsulation and exposure rules of Structures in OutSystems 11 (O11), including their properties and limitations.
helpids: 15007, 30102
locale: en-us
guid: fe544d88-12d3-4de4-95b1-687bc64c34bc
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: data structures, api integration, data management, data modeling, consistency management
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Structure

A Structure is a compound data type used to encapsulate groups of related attributes. Structures can be used in scenarios such as defining complex data types for REST API methods, integrating with external systems, or managing compound data in your app.

For example, in an app, you can create a UserInfo structure to store data like the user's ID, name, and profile picture. You can reuse this structure in different actions throughout the app, ensuring consistency and efficiency.

For more information, refer to [Use structures to create compound data types](../../../building-apps/data/structure-create-use.md#example-using-a-structure).

## Exposed Structure

A Structure cannot be exposed when:

* It has an attribute that is defined using an Entity/Structure that is not exposed.
* It has an attribute that is defined using an Entity/Structure that is reused from another module.

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
</tbody>
</table>
