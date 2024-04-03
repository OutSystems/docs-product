---
summary: Blocks use events to communicate changes to the parent screen/block or to another block.
tags:
locale: en-us
guid: 77d2313f-f484-4581-825e-c198e4756a11
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=201:12
---

# Pass Data Between Blocks

In a screen or block with child blocks, it can happen that an event in a child block requires updating another block. For example, a block containing a date picker that, when changed, requires updating a chart plotted by another block. To learn more about creating reusable blocks, check [Create and Reuse Screen Blocks](block-create-reuse.md). There you can learn how can you create a reusable block. It's useful before creating an use case that will use events to pass data or communicate between blocks.

For example, suppose there is a screen that is the parent of two blocks:

* The **Source** block that implements a date picker.
* The **Target** block that plots a chart based on a date.

When the date changes in the Source block the Target block needs to be refreshed.

![Diagram showing communication between Source block with date picker and Target block with chart](images/block-communicate-1.png "Source and Target Block Communication")

The following is an overview of the communication between blocks:

1. On the **Source** block, create and trigger an Event to notify the Parent screen or block and pass the necessary data;
1. On the **Parent** screen or block, handle the event triggered by the Source block and update the input parameters of the Target block;
1. Finally, in Reactive Web and Mobile apps, execute logic in the OnParametersChanged event handler on the **Target** block, if necessary. In Traditional Web apps, explicitly refresh the **Target** block.

Follow the steps below to implement this communication mechanism.

On the **Source** block:

1. Right-click the Source block on the Elements tree and add an Event. If necessary, add input parameters to the Event to pass values to the parent;

1. Create an action where you trigger the Event using the Trigger Event tool. If necessary, pass the necessary data as the input parameters of the Event;

    ![Screenshot of adding an event to the Source block in the Elements tree](images/block-communicate-2.png "Creating an Event in Source Block")

1. Call the action to trigger the Event.

On the **Parent** screen or block:

1. In the interface editor, select the widget of the Source block instance.

1. In the Properties Pane, edit the Event and Handler properties under the Events section to add a new event handler action for the Event triggered by the Source block.

    ![Screenshot showing the editing of Event and Handler properties in the Properties Pane](images/block-communicate-3.png "Editing Event and Handler Properties")

1. In the newly created action, implement the logic to set new values for the input parameters of the Target block. When this happens, the Target block is automatically updated.

In **Reactive Web** and **Mobile** apps, if the **Target** block needs to execute logic in response to the updated input parameter values:

1. In the Elements tree, select the Target block.

1. In the Properties Pane, edit the On Parameters Changed property under the Events section and select **(New Client Action)** to create a Client Action that runs when the values of the input parameters change.

1. In the newly created Client Action, implement the logic to refresh the queries or deal with the new values of the input parameters.

    ![Screenshot of creating a new Client Action for the Target block in response to parameter changes](images/block-communicate-5.png "Creating a Client Action for Target Block")

In **Traditional Web** apps, if the **Target** block needs to execute logic in response to the updated input parameter values:

1. Go to the event handler action.

1. Update the **Target** block with the Ajax Refresh tool.
