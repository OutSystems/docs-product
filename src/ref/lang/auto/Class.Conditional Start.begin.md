When designing the process flow of your process, you can start a flow when an event occurs in an entity record. This behavior is implemented through the **Conditional Start** process activity which you can drag onto your canvas from the [Process Flow Toolbox](<../../../develop/processes/process-flow/process-flow-toolbox.md>).

The Conditional Start process activity starts the execution of its flow either when a **record creation** or a **record update** event occurs. However, to ensure that all new incoming events are handled, the Conditional Start does not end its execution after handling an event. For that, every time an event occurs it starts a new execution of the flow and returns itself to listen for the new incoming events.

All Conditional Start activities in the process flow end their execution when the process execution ends.

A Conditional Start process activity can have input parameters, output parameters and [callback actions](<../../../develop/processes/actions-callback/actions-activities-callback.md>).

## Start Executing on Entity Events

If the flow of the conditional start is to start executing automatically after an event occurs over an entity, the kind of event must be set in the `Start On` property with one of the following entity actions: **Create&lt;Entity&gt;** or **Update&lt;Entity&gt;**.

Once you select the kind of event in the `Start On` property, a list of entity attributes is displayed for you to set the condition to automatically start the flow of the conditional start: a primary key for a specific record and/or reference attributes for a specific value on an attribute.

For example, if the conditional start flow is designed to handle new scheduled interview then the `Start On` property must be set with the **CreateInterview** entity action.

## Adding Dependency Connectors

In some cases you may want the Conditional Start to be executed only after one or more process activities have finished their execution, that is, the Conditional Start execution is dependent on the execution of other process activities. To implement this behavior simply add a connector from each of the process activities on which the Conditional Start depends to the Conditional Start itself.

This kind of connector is represented as the green dotted connector shown in the image below:

![](images/dependency-connector.jpg)

## Using Conditional Start Activity References

Service Studio provides you with mechanisms to access Conditional Start process activities among eSpaces. You can expose your Conditional Start process activities to other eSpaces or use Conditional Start process activities defined in another eSpace.

## Remarks

Changing the `Start On` property to listen to events from another entity only has effect on Conditional Start instances that are created after the change. All instances that were already executing will continue listening to events from the previous entity. Therefore, you should only make this change when there are no more Conditional Start instances listening to the previous entity.

As a best practice, remember to [limit the number of Conditional Starts in a Process](<../../../develop/processes/best-practices/limit-conditional-starts.md>).
