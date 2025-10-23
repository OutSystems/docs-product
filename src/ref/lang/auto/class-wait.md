---
summary: OutSystems 11 (O11) features a Wait process activity that pauses process flows until specified events or timeouts occur.
locale: en-us
guid: f8be65b0-6cde-4d57-ad19-0f473f662fa0
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: process management, workflow automation, event-driven processes, entity events
audience:
  - full stack developers
  - frontend developers
  - mobile developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Wait

When designing the process flow of your process, you can put your process flow execution on hold. This behavior is implemented through the **Wait** process activity which you can drag onto your canvas from the [Process Flow Toolbox](<../../../building-apps/processes/process-flow/process-flow-toolbox.md>).

The Wait process activity allows you to put your process flow execution on hold until one of the following events occurs:

* **A timeout**: a specified timeout date is reached.
* **An entity action**: when an Entity Action that **creates** or **updates** an entity is executed and it matches the conditions to close the wait activity.

    <div class="info" markdown="1">

    When the timeout occurs, the Wait activity is tentatively ended by executing the **OnClose** callback action. If the entity action has not been executed, waiting continues until the next timeout.

    </div>

A Wait process activity can have input parameters, output parameters and [callback actions](<../../../building-apps/processes/actions-callback/actions-activities-callback.md>).

## End the Activity on Entity Events

If the execution of the wait is to be automatically ended after an event occurs over an entity, the kind of event must be set in the `Close On` property with one of the following entity actions: **Create&lt;Entity&gt;** or **Update&lt;Entity&gt;**.

Once you select the kind of event in the `On Close` property, a list of entity attributes is displayed for you to set the condition to automatically end the wait activity: a primary key for a specific record and/or reference attributes for a specific value on an attribute.

For example, if the wait activity is designed to wait until an entity is updated to a certain status, set its `On Close` property to the **Update&lt;Entity&gt;** entity action and the condition of the status to the expected status.

## Using Wait Activity References

Service Studio provides you with mechanisms to access Wait process activities among eSpaces. You can expose your Wait process activities to other eSpaces or use the Wait process activities defined in another eSpace.

## Remarks

Changing the `Close On` property to listen to events from another entity only has effect on Wait instances that are created after the change. All instances that were already executing will continue listening to events from the previous entity. Therefore, you should only make this change when there are no more Wait instances listening to the previous entity.

## Properties

| Name | Description | Mandatory | Observations |
|---|---|---|---|
| Description | Text that documents the element. | | Useful for documentation purposes.The maximum size of this property is 2000 characters. |
| Label | Text displayed in the back-office when an instance of this Wait activity is executed. | | If not defined, the displayed text will be the Wait process activity name. |
| Name | Identifies an element in the scope where it is defined, like a screen, action, or module. | Yes | |
| Public | Indicates whether this process activity can be used by other modules. | Yes | This property is only available for process activities that were created in the current module. When a process activity is public its process must also be public. |
| Close On | Entity action that automatically ends the Wait Activity execution. | | The event that automatically closes (ends) the process activity execution: <br/><br/> `Create <entity>`: the Wait is ended when a record is created for the specified entity. <br/><br/> `Update <entity>`: the Wait is ended when a record is updated for the specified entity. |
| Original Name | Name of the element as defined in the module which implements it (producer module). This property is read-only. | Yes | This property is only visible for referenced elements. |
| Timeout | Date and time until the Wait activity pauses the process flow execution. | | You may set the timeout date in two ways: <br/><br/> **Absolute**: the timeout date is fixed. For example: `#2015-01-01 00:00:00#` <br/><br/> **Relative**: the timeout date depends on the current moment. For example, if you want to wait a day then define your timeout date as: `AddDays(CurrDateTime(),1)`. This value is defined as a Date Time. |
| Allow Skip | If set to True, the activity execution may be skipped. | Yes | When allowed, skip can be triggered programmatically using the **ActivitySkip** system action under the **(System)** reference. |

## Runtime Properties

| Name | Description | Read Only | Type |
|---|---|---|---|
| ClosedInstant | Date and time when the process activity instance was closed. | Yes | Date Time |
| Expired | True if the process activity instance ended because of a timeout. | Yes | Boolean |
| Skipped | True if the process activity instance ended because it was skipped. | Yes | Boolean |
| ActivityId | Identifier of the process activity instance at runtime. | Yes | |
