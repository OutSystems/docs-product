---
tags: Case Management; Case Management framework;
summary: Learn about delegating cases and activities using the Case Management framework.
guid: 29292c65-0d1c-489c-b7f8-622d282dc021
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---
# Delegate activities

You can enable the delegation of cases and activities from the assigned user to another user. You can limit a delegation to a specific time or delegate indefinitely.

After a case or activity is delegated, the delegate user can perform tasks on the case or activity.

## Create, update or delete a delegation

Enable users to create, update, or delete a delegation using the [Delegation_Create](ref/auto/CaseConfigurations_API.final.md#Delegation_Create), [Delegation_CreateOrUpdate](ref/auto/CaseConfigurations_API.final.md#Delegation_CreateOrUpdate), [Delegation_Update](ref/auto/CaseConfigurations_API.final.md#Delegation_Update), [Delegation_Delete](ref/auto/CaseConfigurations_API.final.md#Delegation_Delete) actions located in the **CaseConfigurations_API** module.

<div class="info" markdown="1">

The **FromGroupId** and **FromGroupExtendeId** attributes aren't implemented in the current version of Case Management framework.

</div>

To delegate the work for a set amount of time, use the **From** and **To** attributes.

## Validate a delegation

Validate a delegation using the [Delegation_IsValid](ref/auto/CaseServices_API.final.md#Delegation_IsValid) action from the **CaseServices_API** module.

## Fetch current delegations

The following actions from the **CaseServices_API** module allow you to check delegations:

* [Delegation_GetAll](ref/auto/CaseServices_API.final.md#Delegation_GetAll)

* [Delegation_GetById](ref/auto/CaseServices_API.final.md#Delegation_GetById)

* [Delegation_GetByUser](ref/auto/CaseServices_API.final.md#Delegation_GetByUser)


## Case and Activity actions that check delegations

The following actions from the CaseServices_API module check active delegations:

* [Case_OpenActivity](ref/auto/CaseServices_API.final.md#Case_OpenActivity)

* [Case_CloseActivity](ref/auto/CaseServices_API.final.md#Case_CloseActivity)

* [Case_CloseActivityAsync](ref/auto/CaseServices_API.final.md#Case_CloseActivityAsync)

* [Case_BlockActivity](ref/auto/CaseServices_API.final.md#Case_BlockActivity)

* [Case_UnblockActivity](ref/auto/CaseServices_API.final.md#Case_UnblockActivity)

* [Case_PickupActivity](ref/auto/CaseServices_API.final.md#Case_PickupActivity)

* [Case_TakeoverActivity](ref/auto/CaseServices_API.final.md#Case_TakeoverActivity)

* [Case_UpdatePriority](ref/auto/CaseServices_API.final.md#Case_UpdatePriority)

* [Case_UpdateStatus](ref/auto/CaseServices_API.final.md#Case_UpdateStatus)

* [Case_UpdateStatusByActivityId](ref/auto/CaseServices_API.final.md#Case_UpdateStatusByActivityId)

* [Case_AddComments](ref/auto/CaseServices_API.final.md#Case_AddComments)

* [Activity_AddComments](ref/auto/CaseServices_API.final.md#Activity_AddComments)

When using these actions keep the following in mind:

* Set the **DelegatedBy** attribute as the **UserId** of the user originally assinged to the case or activity.

* If you use the action for a case used under delegation, the information regarding the user that performed the action and by who delegated it, is logged in the case’s history.
