When designing the process flow of your process, you can add work to be carried out by the end user. This behavior is implemented through the **Human Activity** process activity, which you can drag onto your canvas from the [Process Flow Toolbox](<../../../develop/processes/process-flow/process-flow-toolbox.md>).

The Human Activity allows you to specify and assign a work to be carried out by the end users in your application. Once the process flow execution reaches a Human Activity the end user or end users are informed (in their [Taskbox](<../../../develop/processes/intro.md#using-the-taskbox>)) of the work that has to be carried out. Then, one of them executes the activity and signals in the Taskbox that the activity has been done, and the Human Activity execution finishes. The process flow execution continues to the next process activity in the flow path.

A Human Activity can have input parameters, output parameters and [callback actions](<../../../develop/processes/actions-callback/actions-activities-callback.md>).

Human Activity is not available in Service Modules because this activity requires user interface.

## Assigning a Human Activity to end users

If no configuration is done, the Human Activity is assigned to all end users, that is, it is displayed in the [Taskbox](<../../../develop/processes/intro.md#using-the-taskbox>) of each end user until it's executed by one of them. However, to force the assignment of a Human Activity to a specific end user, set the `User` property to the desired end user. For advanced cases, you may set an expression that returns the user that handles the activity, using the expression editor.

To improve the end users experience while executing these activities, you can provide the details of the Human Activity and the instructions on how to execute it. For this, select the Human Activity instance in the flow path, and set the `Detail` and `Instructions` properties under **End-User Information**:

![Human Activity properties](images/process-human-activity-properties-ss.png)

This information will be available in the activities list and the activity details of the end users' Taskbox:

![Human Activity Taskbox](images/process-human-activity-taskbox.png)

## End the Activity on Entity Events

If the execution of the human activity is to be automatically ended after an event occurs over an entity, the kind of event must be set in the `Close On` property with one of the following entity actions: **Create&lt;Entity&gt;** or **Update&lt;Entity&gt;**.

Once you select the kind of event in the On Close property, a list of entity attributes is displayed for you to set the condition to automatically end the human activity: a primary key for a specific record and/or reference attributes for a specific value on an attribute.

For example, if the human activity is designed for a user to carry on an interview but interviews can be canceled, then the `Close On` property must be set with the **UpdateInterview** entity action and the interview status attribute with the canceled code.

## Adding security

You may add security to your Human Activities to be sure that only authorized end users can execute the activity, which is especially useful for critical or high responsibility activities. For this, simply check the roles allowed to execute the Human Activity.

## Using Human Activity references

Service Studio provides you with mechanisms to access Human Activity process activities among modules. You can expose your Human Activity process activities to other modules or use Human Activity process activities defined in another module. This activity cannot be exposed if its Process is not exposed or the module is Multi-tenant.

## Remarks

Changing the `Close On` property to listen to events from another entity only has effect on Human Activity instances that are created after the change. All instances that were already executing will continue listening to events from the previous entity. Therefore, you should only make this change when there are no more Human Activity instances listening to the previous entity.
