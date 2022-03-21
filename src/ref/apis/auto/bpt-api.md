# BPT API

For Platform Version 9.0.99.11. Low-level API to create custom inboxes for process activities.

## Summary

Action | Description
---|---
[Activity_Discard](<#Activity_Discard>) | Discards an Activity and the execution of the current Process flow stops, that is, none of the following activities in the flow is executed.%%Remarks:%%This action commits the current transaction.
[Activity_IsValidId](<#Activity_IsValidId>) | Checks whether an Activity Identifier is valid for a Kind of activity.
[HumanActivity_AssignToUser](<#HumanActivity_AssignToUser>) | Assigns a Human Activity to a User and sets the activity status to Ready. The human activity is only shown in that user's Taskbox.%%Remarks:%%This action commits the current transaction.
[HumanActivity_CheckRole](<#HumanActivity_CheckRole>) | Checks whether a User has the role for executing a Human Activity.
[HumanActivity_FlushPendingEvents](<#HumanActivity_FlushPendingEvents>) | Forces a Human Activity to handle immediately all its pending events.%%Remarks:%%This action commits the current transaction.
[HumanActivity_SetDueDate](<#HumanActivity_SetDueDate>) | Sets the due date for a Human Activity.%%Remarks:%%This action commits the current transaction.
[Process_BulkDelete](<#Process_BulkDelete>) | Deletes all the logged information of instances of top level Processes that have terminated or closed before the given date.%%The information that is deleted is all the logging of: process instances, activities instances, input parameters values, output parameters values, process instances executed within other process instances, etc.%%This action finds all top level process instances and recursively deletes all its subprocess instances, ensuring the meta-model remains consistent.%%In the meta-model, a top level process instance is identified in the Process entity by the condition: Top_Process_Id = Id.%%Remarks:%%This action does NOT commit the current transaction.
[Process_Delete](<#Process_Delete>) | Deletes all the logged information of an instance of a top level Process, which must be either terminated or closed.%%The information that is deleted is all the logging of: process instance, activities instances, input parameters values, output parameters values, processes instances executed within other process instance, etc.%%This action finds the specified top level process instance and recursively deletes all its subprocess instances, ensuring the meta-model remains consistent.%%In the meta-model, a top level process instance is identified in the Process entity by the condition: Top_Process_Id = Id.%%This action will raise an exception in the following situations:%%\- The process instance does not exist;%%\- The process instance is not a top level process instance;%%\- The process instance is not terminated or closed.%%Remarks:%%This action does NOT commit the current transaction.
[Taskbox_Hide](<#Taskbox_Hide>) | Add this action to a Preparation to disable the TaskBox on a screen.

## Actions

### Activity_Discard { #Activity_Discard }

Discards an Activity and the execution of the current Process flow stops, that is, none of the following activities in the flow is executed.  
  
Remarks:  
This action commits the current transaction.

*Inputs*

ActivityId
:   Type: EntityReference. Mandatory.  
    The identifier of the Activity.

### Activity_IsValidId { #Activity_IsValidId }

Checks whether an Activity Identifier is valid for a Kind of activity.

*Inputs*

ActivityId
:   Type: EntityReference. Mandatory.  
    The identifier of the Activity.

Kind
:   Type: EntityReference. Mandatory.  
    The kind of the Activity.

*Outputs*

IsValid
:   Type: Boolean.  
    Returns True if it is a valid identifier of an Activity.

### HumanActivity_AssignToUser { #HumanActivity_AssignToUser }

Assigns a Human Activity to a User and sets the activity status to Ready. The human activity is only shown in that user's Taskbox.  
  
Remarks:  
This action commits the current transaction.

*Inputs*

HumanActivityId
:   Type: EntityReference. Mandatory.  
    The identifier of the Human Activity.

UserId
:   Type: EntityReference. Mandatory.  
    The identifier of the User.

### HumanActivity_CheckRole { #HumanActivity_CheckRole }

Checks whether a User has the role for executing a Human Activity.

*Inputs*

HumanActivityId
:   Type: EntityReference. Mandatory.  
    The identifier of the Human Activity.

UserId
:   Type: EntityReference. Mandatory.  
    The identifier of the User.

*Outputs*

HasPermission
:   Type: Boolean.  
    Returns True if the user has the role to execute the activity.

### HumanActivity_FlushPendingEvents { #HumanActivity_FlushPendingEvents }

Forces a Human Activity to handle immediately all its pending events.  
  
Remarks:  
This action commits the current transaction.

*Inputs*

HumanActivityId
:   Type: EntityReference. Mandatory.  
    The identifier of the Human Activity.

*Outputs*

ProcessedEvents
:   Type: Integer.  
    Returns the number of pending events handled in the flush.

### HumanActivity_SetDueDate { #HumanActivity_SetDueDate }

Sets the due date for a Human Activity.  
  
Remarks:  
This action commits the current transaction.

*Inputs*

HumanActivityId
:   Type: EntityReference. Mandatory.  
    The identifier of the Human Activity.

DueDate
:   Type: DateTime. Mandatory.  
    The date and time limit for the human activity to be finished.

### Process_BulkDelete { #Process_BulkDelete }

Deletes all the logged information of instances of top level Processes that have terminated or closed before the given date.  
The information that is deleted is all the logging of: process instances, activities instances, input parameters values, output parameters values, process instances executed within other process instances, etc.  
  
This action finds all top level process instances and recursively deletes all its subprocess instances, ensuring the meta-model remains consistent.  
In the meta-model, a top level process instance is identified in the Process entity by the condition: Top_Process_Id = Id.  
  
Remarks:  
This action does NOT commit the current transaction.

*Inputs*

ProcessesOlderThan
:   Type: DateTime. Mandatory.  
    The date and time before which processes are to be deleted.

ProcessDefinitionId
:   Type: EntityReference.  
    The identifier of the process definition.

MaxDeletedProcesses
:   Type: Integer. Default: 1000.  
    The maximum number of processes to be deleted. The default is 1000. Set to 0 (zero) for unlimited deletes.

*Outputs*

HasMoreToDelete
:   Type: Boolean.  
    Returns True if there are still process instances left to be deleted.

### Process_Delete { #Process_Delete }

Deletes all the logged information of an instance of a top level Process, which must be either terminated or closed.  
The information that is deleted is all the logging of: process instance, activities instances, input parameters values, output parameters values, processes instances executed within other process instance, etc.  
  
This action finds the specified top level process instance and recursively deletes all its subprocess instances, ensuring the meta-model remains consistent.  
In the meta-model, a top level process instance is identified in the Process entity by the condition: Top_Process_Id = Id.  
  
This action will raise an exception in the following situations:  
\- The process instance does not exist;  
\- The process instance is not a top level process instance;  
\- The process instance is not terminated or closed.  
  
Remarks:  
This action does NOT commit the current transaction.

*Inputs*

ProcessId
:   Type: EntityReference. Mandatory.  
    The identifier of the process instance.

### Taskbox_Hide { #Taskbox_Hide }

Add this action to a Preparation to disable the TaskBox on a screen.


