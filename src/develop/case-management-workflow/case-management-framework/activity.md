---
tags: Case Management; Case Management framework;
summary: Learn about the expanded functionality for human activities that the Case Management framework provides.
guid: 3dd527f3-1678-47ac-bf40-c86b8116b5b3
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
---

# Activities

When you need the end user to make a decision or to act before a case advances, you use [Human Activities](../../../ref/lang/auto/Class.Human_Activity.final.md) . In the context of the Case Management framework,  Human Activities are referred to as **activities**.

The Case Management framework includes a set of API actions in the [Case Services API](./ref/auto/CaseServices_API.final.md) module that expand the functionality of activities.

## Assign an activity

Use the [Activity_AssignToGroup](./ref/auto/CaseServices_API.final.md#Activity_AssignToGroup), [Activity_AssignToGroupAndUser](./ref/auto/CaseServices_API.final.md#Activity_AssignToGroupAndUser), and [Activity_AssignToUser](./ref/auto/CaseServices_API.final.md#Activity_AssignToUser) actions to assign an activity to a group, a group and a user, or to single a user.%%
Assigning an activity means that a user, or a group of users, are responsible for solving the activity.

## Pick up an activity

Enable end users to pick up an activity for completion using [Case_PickupActivity](./ref/auto/CaseServices_API.final.md#Case_PickupActivity).

If an activity isn't assigned to a specific user, any user can pick up the activity.%%
If an activity is assigned to a group, the user must belong to that group or be under a valid delegation from a user who belongs to the group to pick up the activity.%%
If an activity is assigned to a specific user, other users can't pick it up.

## Block and unblock an activity

Enable end users to block an activity using [Case_BlockActivity](./ref/auto/CaseServices_API.final.md#Case_BlockActivity).

Blocking an activity prevents other users from opening, closing, and skipping the activity.

An activity associated with a case can be blocked by the user to which it is assigned to or by a user under a valid delegation from the assigned user.  

Check if an activity is blocked using the [Activity_CheckIsBlocked](./ref/auto/CaseServices_API.final.md#Activity_CheckIsBlocked) action.

Enable end users to unblock an activity using the [Case_UnblockActivity](./ref/auto/CaseServices_API.final.md#Case_UnblockActivity) action.

## Take over an activity

Enable end users to pick up an activity for completion using [Case_TakeoverActivity](./ref/auto/CaseServices_API.final.md#Case_TakeoverActivity).

Taking over an activity removes the existing assignment and assigns the activity to another user.

An activity must already be assigned before being taken over.

To take over an activity the user needs to belong to the assigned group (if any group is assigned) or be under the delegation of a user of the same group and the activity can't be blocked.

## Release an activity

Enable end users to release an activity using [Case_ReleaseActivity](./ref/auto/CaseServices_API.final.md#Case_ReleaseActivity).

Release an activity to remove the assignment and unblock the activity.

The only user that can release an activity is the user assigned to that activity.

## Open an activity

Before opening an activity can be opened with the [Case_OpenActivity](./ref/auto/CaseServices_API.final.md#Case_OpenActivity) action, but not without checking first if the user has access to it, either by himself or under a valid delegation. This action returns the activity's URL.

## Close an activity

Enable the closing of an activity using the following actions:

[Case_CloseActivity](./ref/auto/CaseServices_API.final.md#Case_CloseActivity)
:   This action works synchronously and follows the default BPT behavior, committing the current transaction.

[Case_CloseActivityAsync](./ref/auto/CaseServices_API.final.md#Case_CloseActivityAsync)
:    This action works asynchronously and launches a process to close the current process, not committing within the action and closing the activity only when the execution of the closing process occurs.

The Activity_CalculateExecutionTime action allows you to calculate the execution time of an activity, based on the configured SLA and record that time in the activity's ExecutionTime property.

## Validate user access to an activity

Validate a user's access to an activity using the following actions:

[Activity_CheckUserAccess](./ref/auto/CaseServices_API.final.md#Activity_CheckUserAccess)
:   Checks if a user has access to an activity or if the activity is delegated to the user.

[Activity_ValidateUserAccess](./ref/auto/CaseServices_API.final.md#Activity_ValidateUserAccess)
:   Checks if a user has access to an activity or if the activity is delegated to the user. Raises an exception if the user doesn't have access to the activity.

## Assign multiple users to an activity

Assigning multiple users to an activity enables you to launch the same activity multiple times to different assigned users. You can select if all or a selection of those assigned users tasks are completed before the process can advance. The process of assigning multiple users is described in the [Executing multiple instance activities](../../processes/design-patterns/multiple-instance-activities.md) article.
