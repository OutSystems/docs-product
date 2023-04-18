---
kinds: ServiceStudio.Model.Nodes+SendEmail+Kind, ServiceStudio.Model.ProcessNodes+SendEmailActivity+Kind
helpids: 0
tags: runtime-traditionalweb
locale: en-us
guid: 73d29c1b-5be0-4ebc-9828-0c0aaaff142b
app_type: traditional web apps
platform-version: o11
---

# Send Email

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

Use the Send Email Tool within the web flow to send an email. The content of the email is based on your predefined Email screens, which you can specify in the **Email** field of the Properties Pane. The email is sent asynchronously, after OutSystems Scheduler Service checks the sending queue.

Send Email is not available in Service Modules because this tool requires user interface.

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
<td title="From">From</td>
<td>Email address of the sender.</td>
<td></td>
<td></td>
<td>Use the EmailAddressCreate built-in function to create an encoded value for the 'From' property.<br/><br/>The default sender is configured in the Email Configuration in Service Center.<br/><br/>The maximum size of this property is 200 characters.</td>
</tr>
<tr>
<td title="To">To</td>
<td>One or more email addresses to send the email. Separate email addresses with a comma (,).</td>
<td>Yes</td>
<td></td>
<td>To handle Email addresses use the Email data type and Email built-in functions.<br/><br/>The maximum size of this property is 2000 characters.</td>
</tr>
<tr>
<td title="CC">CC</td>
<td>One or more email addresses to send a carbon copy of the email. Separate email addresses with a comma (,).</td>
<td></td>
<td></td>
<td>To handle Email addresses use the Email data type and Email built-in functions.<br/><br/>The maximum size of this property is 2000 characters.</td>
</tr>
<tr>
<td title="BCC">BCC</td>
<td>One or more email addresses to send a blind carbon copy of the email. Separate email addresses with a comma (,).</td>
<td></td>
<td></td>
<td>To handle Email addresses use the Email data type and Email built-in functions.<br/><br/>The maximum size of this property is 2000 characters.</td>
</tr>
<tr>
<td title="Log Content">Log Content</td>
<td>Set to Yes to store the email content in the email logs of the Platform Server. Check the email logs in Service Center.</td>
<td>Yes</td>
<td>No</td>
<td></td>
</tr>
<tr>
<td title="Email">Email</td>
<td>Email screen to be used as the body of the email to send.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Description">Description</td>
<td>Text that documents the element.</td>
<td></td>
<td></td>
<td>This property is only available in process flows.</td>
</tr>
<tr>
<td title="Label">Label</td>
<td>Text displayed in the back-office when an instance of this Send Email activity is executed.</td>
<td></td>
<td></td>
<td>This property is only available in process flows.</td>
</tr>
</tbody>
</table>

## Runtime Properties

<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
<th>Read Only</th>
<th>Type</th>
<th>Observations</th>
</tr>
</thead>
<tbody>
<tr>
<td>EmailId</td>
<td>Identifier of the sent email.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>ActivityId</td>
<td>Identifier of the process activity instance at runtime.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

