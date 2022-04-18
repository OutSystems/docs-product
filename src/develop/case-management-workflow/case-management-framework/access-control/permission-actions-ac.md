---
tags: Case Management; Case Management framework;
summary: Learn about permissions for access control and which Case Management framework actions check for these permissions.
guid: 7748225f-8e88-43ea-bed6-29d510530176
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
---

# Permissions and Case Management framework actions

Access control in the Case Management framework works by preventing access to a case unless a user has been granted permission to do so.

## Permissions

The following access rights, or permissions, exist in the Case Management framework:

Read-only
:   Allows access to read case information.

Write
:   Allows access to read and to modify case information.

## Access control in API actions

If a user attempts to access a case they don't have permission to read or write to, an exception is raised indicating that access to that resource is restricted and that the user doesn't have the permission to access the resource.
 
For **Service actions**, some return a single case and others a list of cases. If the user does not have read permissions for all cases in a list of cases, only the ones they do have access to are returned. The cases they don't have access to are ignored and no exception is raised.

| Action Type | Action | Required Permission | Return Type |
|---|---|---|---|
| Case | [Case_AddComments](../ref/auto/CaseServices_API.final.md#Case_AddComments) | Write | Single |
| Case | [Case_AddTags](../ref/auto/CaseServices_API.final.md#Case_AddTags) | Write | Single |
| Case | [Case_RemoveTag](../ref/auto/CaseServices_API.final.md#Case_RemoveTag) | Write | Single | 
| Case | [Case_Complete](../ref/auto/CaseServices_API.final.md#Case_Complete) | Write | Single |
| Case | [Case_Delete](../ref/auto/CaseServices_API.final.md#Case_Delete) | Write | Single |
| Case | [Case_UpdatePriority](../ref/auto/CaseServices_API.final.md#Case_UpdatePriority) | Write | Single |
| Case | [Case_UpdateStatus](../ref/auto/CaseServices_API.final.md#Case_UpdateStatus) | Write | Single |
| Activity | [Case_BlockActivity](../ref/auto/CaseServices_API.final.md#Case_BlockActivity) | Write | Single |
| Activity | [Case_UnblockActivity](../ref/auto/CaseServices_API.final.md#Case_UnblockActivity) | Write | Single |
| Activity | [Case_CloseActivity](../ref/auto/CaseServices_API.final.md#Case_CloseActivity) | Write | Single |
| Activity | [Case_CloseActivityAsync](../ref/auto/CaseServices_API.final.md#Case_CloseActivityAsync) | Write | Single |
| Activity | [Case_OpenActivity](../ref/auto/CaseServices_API.final.md#Case_OpenActivity) | Write | Single |
| Activity | [Case_PickupActivity](../ref/auto/CaseServices_API.final.md#Case_PickupActivity) | Write | Single |
| Activity | [Case_ReleaseActivity](../ref/auto/CaseServices_API.final.md#Case_ReleaseActivity) | Write | Single |
| Activity | [Case_SkipActivity](../ref/auto/CaseServices_API.final.md#Case_SkipActivity) | Write | Single |
| Activity | [Case_TakeoverActivity](../ref/auto/CaseServices_API.final.md#Case_TakeoverActivity) | Write | Single |
| Activity | [Case_PerformActionActivity](../ref/auto/CaseServices_API.final.md#Case_PerformActionActivity) | Write | Single |
| Service | [Case_GetActivitiesTimeline](../ref/auto/CaseServices_API.final.md#Case_GetActivitiesTimeline) | Read-only | Single |
| Service | [Case_GetAllHistoryByIdAndDate](../ref/auto/CaseServices_API.final.md#Case_GetAllHistoryByIdAndDate) | Read-only | Single |
| Service | [Case_GetAllTags](../ref/auto/CaseServices_API.final.md#Case_GetAllTags) | Read-only | Single |
| Service | [Case_GetDetailsByCaseId](../ref/auto/CaseServices_API.final.md#Case_GetDetailsByCaseId) | Read-only | Single |
| Service | [Case_GetHistory](../ref/auto/CaseServices_API.final.md#Case_GetHistory) | Read-only | Single |
| Service | [Case_GetAllSubcases](../ref/auto/CaseServices_API.final.md#Case_GetAllSubcases) | Read-only | Single |
| Service | [Case_GetActivities](../ref/auto/CaseServices_API.final.md#Case_GetActivities) | Read-only | List |
| Service | [Case_GetActivitiesByCaseId](../ref/auto/CaseServices_API.final.md#Case_GetActivitiesByCaseId) | Read-only | List |
| Service | [Case_GetAllByUserWithAccess](../ref/auto/CaseServices_API.final.md#Case_GetAllByUserWithAccess) | Read-only | List |
| Service | [Case_GetByTagId](../ref/auto/CaseServices_API.final.md#Case_GetByTagId) | Read-only | List |
| Service | [Case_GetByTagLabel](../ref/auto/CaseServices_API.final.md#Case_GetByTagLabel) | Read-only | List |
| Service | [Case_GetAllByExternalRequester](../ref/auto/CaseServices_API.final.md#Case_GetAllByExternalRequester) | Read-only | List |
| Service | [Case_GetAllByGroupWithAccess](../ref/auto/CaseServices_API.final.md#Case_GetAllByGroupWithAccess) | Read-only | List |
| Service | [Case_GetAllByUserId](../ref/auto/CaseServices_API.final.md#Case_GetAllByUserId) | Read-only | List |
