---
locale: en-us
guid: 2e8ca3cb-cfae-41a3-bbd0-c6b14ca14258
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
summary: An event in OutSystems allows a block to notify its parent element of an occurrence, with the option to pass input parameters and a mandatory setting
---
# Event

An event is an element that allows a block to interact with its parent element by notifying it that a particular event has occurred. Essentially, the block triggers an event and then the parent element handles it.

Events can only be defined inside blocks.

![Screenshot showing how to define an event inside a block in OutSystems Service Studio](images/add-event-block-ss.png "Defining an Event Inside a Block")

Input parameters can be added to events. This allows data to pass from the scope of a block to the outer scope of the parent element. This is necessary since the block and parent element have different scopes.

If the **Is Mandatory** property of an event is set to **Yes**, you must define an event handler in the parent element where the block with the event is used. 

![Screenshot illustrating the IsMandatory property set to True, indicating the need to define an event handler in OutSystems Service Studio](images/mandatory-event-ss.png "Mandatory Event Property Set to True")


## Trigger event

A trigger event defines what action in a block can trigger an event. To learn more about how trigger events work, refer to the [Demo: How To Trigger Block Events](https://learn.outsystems.com/training/journeys/blocks-and-events-635/demo-how-to-trigger-block-events/o11/90). 

## Related information
[Block events](https://learn.outsystems.com/training/journeys/blocks-and-events-635/block-events/o11/78)

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
<td title="Is Mandatory">Is Mandatory</td>
<td>Set to Yes to require this event to be triggered in the logic of the element.</td>
<td>Yes</td>
<td>Yes</td>
<td></td>
</tr>
</tbody>
</table>

