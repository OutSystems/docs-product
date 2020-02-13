When designing the process flow of your process, you can put your process flow execution on hold. This behavior is implemented through the **Wait** process activity which you can drag onto your canvas from the [Process Flow Toolbox](<../../../develop/processes/process-flow/process-flow-toolbox.md>).

The Wait process activity allows you to put your process flow execution on hold until one of the following events occurs:

* **A timeout**: a specified timeout date is reached.
* **An entity action**: when an Entity Action that **creates** or **updates** an entity is executed and it matches the conditions to close the wait activity.

A Wait process activity can have input parameters, output parameters and [callback actions](<../../../develop/processes/actions-callback/actions-activities-callback.md>).

## End the Activity on Entity Events

If the execution of the wait is to be automatically ended after an event occurs over an entity, the kind of event must be set in the `Close On` property with one of the following entity actions: **Create&lt;Entity&gt;** or **Update&lt;Entity&gt;**.

Once you select the kind of event in the `On Close` property, a list of entity attributes is displayed for you to set the condition to automatically end the wait activity: a primary key for a specific record and/or reference attributes for a specific value on an attribute.

For example, if the wait activity is designed to wait until an entity is updated to a certain status, set its `On Close` property to the **Update&lt;Entity&gt;** entity action and the condition of the status to the expected status.

## Using Wait Activity References

Service Studio provides you with mechanisms to access Wait process activities among eSpaces. You can expose your Wait process activities to other eSpaces or use the Wait process activities defined in another eSpace.

## Remarks

Changing the `Close On` property to listen to events from another entity only has effect on Wait instances that are created after the change. All instances that were already executing will continue listening to events from the previous entity. Therefore, you should only make this change when there are no more Wait instances listening to the previous entity.
