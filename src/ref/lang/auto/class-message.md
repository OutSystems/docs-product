---
kinds: ServiceStudio.Model.NRNodes+FeedbackMessage+Kind
helpids: 0
summary: Provides a feedback message to the end user.
tags: runtime-mobileandreactiveweb;
locale: en-us
guid: 70ed4ea2-9f23-4c19-b322-11255785072c
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=845:1547
---

# Message

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

You can provide a feedback message to the end user by using the Message logic tool within a Client Action flow.

## Using the Message logic tool

1. Drag the Message logic tool onto the Client Action flow.
1. Set the message **Label**, **Message**, and **Type** properties.

    In this example, we enter ``Invalid password`` in the **Message** property (the message displayed to the user) and select **Error** as the message type.  

    ![Screenshot showing the configuration of the Message logic tool with 'Invalid password' as the message and 'Error' as the type](images/message-class-1-ss.png "Message Logic Tool Configuration")

    ![Screenshot of the Message logic tool placed within a Client Action flow in Service Studio](images/message-class-6-ss.png "Message Logic Tool on Client Action Flow")

The available predefined message types are as follows:

* Info

    ![Example of an 'Info' type feedback message in Service Studio](images/message-class-2-ss.png "Info Message Type")

* Success

    ![Example of a 'Success' type feedback message in Service Studio](images/message-class-3-ss.png "Success Message Type")

* Warning

    ![Example of a 'Warning' type feedback message in Service Studio](images/message-class-4-ss.png "Warning Message Type")

* Error

    ![Example of an 'Error' type feedback message in Service Studio](images/message-class-5-ss.png "Error Message Type")


## Properties

<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Data Type</th>
<th>Description</th>
<th>Mandatory</th>
<th>Default value</th>
<th>Observations</th>
</tr>
</thead>
<tbody>
<tr>
<td title="Label">Label</td>
<td>Text</td>
<td>Identifies an element in the flow.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Message">Message</td>
<td>Text</td>
<td>Message displayed to the user.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Type">Type</td>
<td>Message type identifier</td>
<td>Specifies the UI look and feel of the displayed message.</td>
<td>Yes</td>
<td>Info</td>
<td>The possible values are: Info, Success, Warning, and Error.</td>
</tr>
</tbody>
</table>

