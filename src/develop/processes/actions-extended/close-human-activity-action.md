---
locale: en-us
guid: 249a28f9-965b-47b7-bbe1-6ba5d20032d5
app_type: traditional web apps, mobile apps, reactive web apps
---

# Close Human Activity Action

Use the **Close&lt;Human Activity Name&gt;** [process activity extended action](intro.md) in an action flow to close a **Human Activity**. Once closed, the Human Activity ends its execution.

To close a Human Activity in a screen action proceed as follows:

1. Edit the web screen that is set as the `Destination` in the human activity, and add a new input parameter of `Activity Identifier` type.

2. In the process flow, edit the human activity properties and below the `Destination` web screen set the newly added input parameter with the human activity identifier runtime property: `ActivityId`.

3. Finally, in the screen action flow, add the `Close<Human Activity Name>` extended action and set its `ActivityId` input parameter with the activity identifier input parameter of the web screen and fill all the human activity input parameters.

## Input parameters

* **ActivityId:** id of the activity instance. (Type: Activity Identifier; Mandatory)

* **Human Activity Input Parameters**: one parameter for each input parameter in the human activity definition.

<div class="warning" markdown="1">

The input parameters must be in the same order and of the same type as what is defined in the human activity.

</div>
