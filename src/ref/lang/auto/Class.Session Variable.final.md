---
kinds: ServiceStudio.Model.Variables+SessionVariable+Kind
helpids: 15001
locale: en-us
guid: ee806cae-33e4-4751-b49f-ddbd4aa5164c
---

# Session Variable


Use Session Variables to store data server-side in a key-value format. Use it to cache, for example, for configurations and app context data. Session Variables clear when users log out of the app or close all the browser windows.

<div class="info" markdown="1">

The Session Variables feature is only available for Traditional Web Apps.

</div>

Session Variables are available only in Traditional Web Apps. Avoid referencing elements with Session Variables in Reactive Web or Mobile Apps, as the platform can't keep the values of Session Variables in this scenario between requests. This is due to the runtime differences in the Reactive Web Apps / Mobile Apps on one side, which run in the client-side context, and Traditional Web Apps that run in the server-side context.

You can use the variables with many data types, but avoid using them for [compound data types](<../../data/data-types/available-data-types.md>) due to performance considerations.

To add a Session Variable, click **Data** tab > **Session Variables** > **Add Session Variable**.


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
<td title="Data Type">Data Type</td>
<td>The variable data type.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Default Value">Default Value</td>
<td>Initial value of this element. If undefined, the default value of the data type is used.</td>
<td></td>
<td></td>
<td>The default value of a session variable must be a literal.</td>
</tr>
</tbody>
</table>

