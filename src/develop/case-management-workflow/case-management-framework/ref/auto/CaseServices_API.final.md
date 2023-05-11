---
guid: f5983291-ad80-4f87-955a-aae1180139a8
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Case Services API

The Case Services API includes actions used to interact with cases related to a Process.

Use this API to modify a case, for example:

* Pick up, release, block, unblock, or close an Activity.
* Initialize, update the status, or complete a case.
* Execute a rule.

You can also use this API to check information for a case, for example:

* Check the workdays.
* Check the history of a case.
* Check available Statuses.
* Check Activity Counters.

## Summary

Action | Description
---|---
[Activity_AddComments](<#Activity_AddComments>) | Adds a comment to an existing acitivity
[Activity_AssignToGroup](<#Activity_AssignToGroup>) | Assigns an Activity to an existing group.%%If access control is switched on, automatically grants write access to the group for the case the activity is associated with.%%It performs a COMMIT on the transaction.
[Activity_AssignToGroupAndUser](<#Activity_AssignToGroupAndUser>) | Assigns an Activity to an existing group and user.%%If access control is switched on, automatically grants write access to the group and user for the case the activity is associated with.
[Activity_AssignToUser](<#Activity_AssignToUser>) | Assigns an Activity to an existing user.%%If access control is switched on, automatically grants write access to the user for the case the activity is associated with.
[Activity_CalculateAndSetDueDate](<#Activity_CalculateAndSetDueDate>) | Calculate and set the due DateTime for an Activity, based on the Activity configured SLA and Calendar (if set). Creates an event if SetEvent field is set to True, that can be captured and execute some logic.
[Activity_CalculateExecutionTime](<#Activity_CalculateExecutionTime>) | Calculate and set the execution time for an Activity based on the Activity configured SLA
[Activity_CheckIsBlocked](<#Activity_CheckIsBlocked>) | Check if an activity is blocked
[Activity_CheckUserAccess](<#Activity_CheckUserAccess>) | Checks if the user is assigned to the activity, or has access to it under delegation.
[Activity_SetDueDate](<#Activity_SetDueDate>) | Set the due date for an Activity
[Activity_SetStartDate](<#Activity_SetStartDate>) | Schedules a start date for the Activity to be available.
[Activity_ValidateUserAccess](<#Activity_ValidateUserAccess>) | Validate user authorization to access the activity (directly assigned to the activity, or under delegation). If the user is not authorized an exception is raised.
[ActivityEvent_Set](<#ActivityEvent_Set>) | Creates an activity event
[Calendar_CheckWorkingDay](<#Calendar_CheckWorkingDay>) | Checks if the date is a working day (for a specific calendar)
[Calendar_GetAll](<#Calendar_GetAll>) | Gets the list of calendars
[Calendar_GetById](<#Calendar_GetById>) | Gets the details for a specific calendar
[Calendar_GetEndDate](<#Calendar_GetEndDate>) | Calculate the end date based on the working hours and holidays/non working days. Also perform the calculation based on the TimeZone associated to the Calendar.
[Case_AddComments](<#Case_AddComments>) | Add comments to an existing case.
[Case_AddTags](<#Case_AddTags>) | Enables to add an existing tag (or tags) to a particular case instance
[Case_AssociateProcess](<#Case_AssociateProcess>) | Enables to associate an existing case instance with a proccess, based on an existing process identifier
[Case_BlockActivity](<#Case_BlockActivity>) | Enables to block an existing activity associated to an existing case.
[Case_CheckActiveActivity](<#Case_CheckActiveActivity>) | For a given case and activity definition returns the activity instance, if it exists and the user has permissions on it
[Case_CheckActivityAccess](<#Case_CheckActivityAccess>) | Check if a user has access (directly assigned) to an activity (open or closed)
[Case_CheckActivityIsActive](<#Case_CheckActivityIsActive>) | Checks if the given activity belongs to the current OutSystems BPT process that is active for this Case, and if the activity itself is also active.
[Case_CheckProcessIsActive](<#Case_CheckProcessIsActive>) | Checks if the current associated bpt process  is active for this Case
[Case_CloseActivity](<#Case_CloseActivity>) | Close an activity and validates that only the correct user can close it. Will try to close it in a synchronous way (bpt default behavior) so it performs a COMMIT in the current transition.
[Case_CloseActivityAsync](<#Case_CloseActivityAsync>) | Close an activity and validates that only the correct user can close it (will try to close the activity in an asynchronous way). Enhanced activity close funtionality in opposing the default syncronous bpt close behavior).
[Case_Complete](<#Case_Complete>) | Enables to close an existing case instance based on an existing process identifier
[Case_Delete](<#Case_Delete>) | Deletes a case instance
[Case_Discard](<#Case_Discard>) | Discard a case instance%%%%Note: All associated running processes/activities will be terminated.
[Case_DiscardActivity](<#Case_DiscardActivity>) | Discards an activity (discarded status), stopping the execution of the current process flow. Calls the Activity_Discard action from the BPT API which commits the current transaction.
[Case_GetIdByProcessId](<#Case_GetIdByProcessId>) | Gets the case identifier based on the process identifier
[Case_GrantAccessToGroup](<#Case_GrantAccessToGroup>) | Grants a given group access to a given Case
[Case_GrantAccessToUser](<#Case_GrantAccessToUser>) | Grants a given user access to a given Case
[Case_Initialize](<#Case_Initialize>) | Enables to initialize a new case instance based on an existing case definition identifier
[Case_IsMilestoneAchieved](<#Case_IsMilestoneAchieved>) | Checks whether a given Milestone has been achieved or not for a given Case
[Case_OpenActivity](<#Case_OpenActivity>) | Opens an acitivity and validates that only the correct user can open it
[Case_PerformActionActivity](<#Case_PerformActionActivity>) | Perform an action to an existing activity associated to a case, taking into account the action specifc validations.
[Case_PickupActivity](<#Case_PickupActivity>) | Assigns the activity to the user, if it is not assigned. The user needs to belong to the group assigned to the activity (if the group activity is set), or have an active delegation.
[Case_ReleaseActivity](<#Case_ReleaseActivity>) | Releases the activity assigned to a specific user. Can only be released by the user that has the activity assigned.
[Case_RemoveTag](<#Case_RemoveTag>) | Removes a Tag from a Case
[Case_RevokeAccessFromGroup](<#Case_RevokeAccessFromGroup>) | Revokes access to a given Case for a given group
[Case_RevokeAccessFromUser](<#Case_RevokeAccessFromUser>) | Revokes access to a given Case for a given user
[Case_SkipActivity](<#Case_SkipActivity>) | Skips the current activity assigned to a specific user. Can only be skipped by the user that has the activity assigned (or under a valid delegation).
[Case_TakeoverActivity](<#Case_TakeoverActivity>) | Reassigns the case activity to the user. The user needs to belong to the group assigned to the activity (if the activity group is set)
[Case_UnblockActivity](<#Case_UnblockActivity>) | Enables to unblock an existing blocked activity associated to an existing case
[Case_UpdateGroupAccess](<#Case_UpdateGroupAccess>) | Updates Group access to a given Case
[Case_UpdatePriority](<#Case_UpdatePriority>) | Updates the priority for an existing case
[Case_UpdateStatus](<#Case_UpdateStatus>) | Updates the status for an existing case
[Case_UpdateStatusByActivityId](<#Case_UpdateStatusByActivityId>) | Updates the Status for an existing case from an exisiting activity
[Case_UpdateUserAccess](<#Case_UpdateUserAccess>) | Updates User access to a given Case
[Case_ValidateAccess](<#Case_ValidateAccess>) | Validates if a User has access to a given Case (either by himself or under an active delegation)
[CaseActivityAction_Get](<#CaseActivityAction_Get>) | Get the Action chosen by the user for a specified activity
[CaseDefinition_GrantAccessToGroup](<#CaseDefinition_GrantAccessToGroup>) | Grants a given group access to all cases from a given Case Definition
[CaseDefinition_GrantAccessToUser](<#CaseDefinition_GrantAccessToUser>) | Grants a given user access to all cases from a given Case Definition
[CaseDefinition_RevokeAccessFromGroup](<#CaseDefinition_RevokeAccessFromGroup>) | Revokes access to cases from a given Case Definition (from a group)
[CaseDefinition_RevokeAccessFromUser](<#CaseDefinition_RevokeAccessFromUser>) | Revokes access to cases fom a given CaseDefinition (from a user)
[CaseDefinition_UpdateGroupAccess](<#CaseDefinition_UpdateGroupAccess>) | Updates Group access permissions to a given Case definition
[CaseDefinition_UpdateUserAccess](<#CaseDefinition_UpdateUserAccess>) | Updates User access permissions to a given Case definition
[Delegation_GetAll](<#Delegation_GetAll>) | Get all delegations which current user has access to.
[Delegation_GetById](<#Delegation_GetById>) | Get a delegation by Identifier, if the user has access to it
[Delegation_GetByUser](<#Delegation_GetByUser>) | Gets the active delegations for the specified user in which the Timestamp is between the Delegation's From and To Dates
[Delegation_IsValid](<#Delegation_IsValid>) | Checks if there is an active delegation from user (optional group) for destination user
[DEPRECATED_Case_AddAccessToGroup](<#DEPRECATED_Case_AddAccessToGroup>) | Give access control to a group associated to an exisitng case instance
[DEPRECATED_Case_AddAccessToUser](<#DEPRECATED_Case_AddAccessToUser>) | Give access control to a user associated to an exisitng case instance
[DEPRECATED_Case_CheckUserPermission](<#DEPRECATED_Case_CheckUserPermission>) | Checks if the currently logged in user has access to the specified case
[DEPRECATED_Case_RemoveAccessFromGroup](<#DEPRECATED_Case_RemoveAccessFromGroup>) | Remove access control from a group to an existing case instance
[DEPRECATED_Case_RemoveAccessFromUser](<#DEPRECATED_Case_RemoveAccessFromUser>) | Remove access control from a user to an existing case instance
[DEPRECATED_Case_SetAccessControlToActivity](<#DEPRECATED_Case_SetAccessControlToActivity>) | Will check and assign/unassign access control to a case instance
[Email_Send](<#Email_Send>) | Sends an email in the context of a case. DO NOT call this action to send test emails or preview emails.
[Group_GetUsersById](<#Group_GetUsersById>) | Gets the list of users for an existing group. The role is an optional search criteria.
[Group_GetUsersToAssociate](<#Group_GetUsersToAssociate>) | Gets the list of users that can be assoicated to an existing group
[GroupExtended_CheckUserAssociation](<#GroupExtended_CheckUserAssociation>) | Checks if the group contains the user association
[GroupExtended_GetAll](<#GroupExtended_GetAll>) | Gets all Group Matrix
[GroupExtended_GetByGroupId](<#GroupExtended_GetByGroupId>) | Gets sepecific group details
[GroupExtended_GetByGroupName](<#GroupExtended_GetByGroupName>) | Gets sepecific group details by group name (exact match)
[GroupExtended_GetById](<#GroupExtended_GetById>) | Gets sepecific group details
[GroupExtended_GetGroupIdById](<#GroupExtended_GetGroupIdById>) | Gets the Group Identifier by the Group extended  Identifier
[GroupExtended_GetGroupsByUser](<#GroupExtended_GetGroupsByUser>) | Gets the list of groups that the user belongs to
[GroupExtended_GetGroupsToAssociate](<#GroupExtended_GetGroupsToAssociate>) | Returns the list of possible groups to be associated
[Holiday_GetById](<#Holiday_GetById>) | Get a Holiday record
[Milestone_SetAchieved](<#Milestone_SetAchieved>) | Updates the IsAchieved field to True and the AchievedOn date and AchievedBy user from a given Milestone Definition of a Case
[Milestone_SetUnachieved](<#Milestone_SetUnachieved>) | Updates the IsAchieved field to False and resets the AchievedOn and AchievedBy fields from a given Milestone Definition of a Case
[NonWorkingDay_GetById](<#NonWorkingDay_GetById>) | Get a NonWorkingDay record
[Process_CalculateAndSetDueDate](<#Process_CalculateAndSetDueDate>) | Calculate and set the due date time for an existing process.
[Process_CalculateExecutionTime](<#Process_CalculateExecutionTime>) | Calculate and set the execution time for a process based on the Process.
[Process_CheckIsPriorityValid](<#Process_CheckIsPriorityValid>) | Checks if the priority has a valid value for an existing process
[Process_GetIdByActivityId](<#Process_GetIdByActivityId>) | Gets the process identifier for an existing activity
[Process_ResumeSuspendedFromImpactAnalysis](<#Process_ResumeSuspendedFromImpactAnalysis>) | Will try to resume the processes that were suspended due Impact Analysis after a deployment
[Process_SetCalendar](<#Process_SetCalendar>) | Enables to modify the calendar of an existing process
[Process_SetDueDate](<#Process_SetDueDate>) | Sets the due date and time for an existing process
[ProcessEvent_Set](<#ProcessEvent_Set>) | Creates a process event
[Purge_AllCases](<#Purge_AllCases>) | Will purge all cases that are closed and meet the conditions to be purged.%%The purge will be asynchronous.
[Purge_CaseId](<#Purge_CaseId>) | Purges a specific case Id, if already closed.
[Rule_ExecuteActivityConditon](<#Rule_ExecuteActivityConditon>) | Exceutes a rule associated to an activity to return a customized output  (as Text)%%To identify the rule, use RuleId or RuleName/CaseDefinitionId.
[Rule_ExecuteCustom](<#Rule_ExecuteCustom>) | Exceutes a rule associated to an object/activity to return a customized output  (as Text)%%To identify the rule, use RuleId or RuleName/CaseDefinitionId.
[Rule_ExecuteGroup](<#Rule_ExecuteGroup>) | Exceutes a rule associated to an object/activity to return a specific group identifier.%%To identify the rule, use RuleId or RuleName/CaseDefinitionId.
[Rule_ExecuteLogic](<#Rule_ExecuteLogic>) | Exceutes a rule associated to an object/activity to return true if the rule is applicable and valid, false otherwise.%%To identify the rule, use RuleId or RuleName/CaseDefinitionId.
[Rule_ExecuteStatus](<#Rule_ExecuteStatus>) | Exceutes a rule associated to an object/activity to return a list of existing status (one or more).%%To identify the rule, use RuleId or RuleName/CaseDefinitionId.
[Rule_ExecuteUser](<#Rule_ExecuteUser>) | Exceutes a rule associated to an object/activity to return a specific user identifier.%%To identify the rule, use RuleId or RuleName/CaseDefinitionId.
[SampleUser_GetList](<#SampleUser_GetList>) | Retrieves the list of sample users
[SampleUser_Login](<#SampleUser_Login>) | Login for sample users
[Timezone_ConvertFromServerTime](<#Timezone_ConvertFromServerTime>) | Converts a server's timezone DateTime to a specific timezone.
[Timezone_ConvertToServerTime](<#Timezone_ConvertToServerTime>) | Converts a specific timezone DateTime to the server's timezone.
[User_GetIdByUsername](<#User_GetIdByUsername>) | Gets the user identifier from the username.
[UserExtended_GetById](<#UserExtended_GetById>) | Gets an user extended details

Service Action | Description
---|---
[Activity_GetActionList](<#Service_Activity_GetActionList>) | Returns the list of available actions for an existing activity based on its current details
[Activity_GetExtraFieldValue](<#Service_Activity_GetExtraFieldValue>) | Gets the actual value of an extra field for a specific activity
[Case_GetActivities](<#Service_Case_GetActivities>) | Gets all activities that match the provided scope and search criteria
[Case_GetActivitiesTimeline](<#Service_Case_GetActivitiesTimeline>) | Gets the list of completed and ongoing activities for a given case
[Case_GetActivityCounters](<#Service_Case_GetActivityCounters>) | Gets the counters for each activity progress status that match the provided scope and search criteria
[Case_GetAllByExternalRequester](<#Service_Case_GetAllByExternalRequester>) | Gets all the Case instances requested by the specified external requester details
[Case_GetAllHistoryByIdAndDate](<#Service_Case_GetAllHistoryByIdAndDate>) | Get the list of all case operations associated to an existing case instance
[Case_GetAllPossibleStatus](<#Service_Case_GetAllPossibleStatus>) | Gets the list of valid status for a given case, based on the current case status and on the defined state machine (otherwise no status will be returned)
[Case_GetAllStatus](<#Service_Case_GetAllStatus>) | Gets the list of all active status for a given case
[Case_GetAllSubcases](<#Service_Case_GetAllSubcases>) | Gets the list of all child cases for a given parent case
[Case_GetAllTags](<#Service_Case_GetAllTags>) | Gets all the tags associated to a specific case instance
[Case_GetByTagId](<#Service_Case_GetByTagId>) | Gets the list of case details that have matching tags with the input tag id list (exact match)
[Case_GetByTagLabel](<#Service_Case_GetByTagLabel>) | Gets the list of case details that have matching tags with the input tag label (partial match)
[Case_GetCases](<#Service_Case_GetCases>) | Gets all cases that meet the filter criteria
[Case_GetCasesByActivity](<#Service_Case_GetCasesByActivity>) | Gets all cases that meet the filter criteria based on their activities
[Case_GetCasesByActivityCounters](<#Service_Case_GetCasesByActivityCounters>) | Gets the Case state counters (Active, Closed, All) for the selected filters
[Case_GetCounters](<#Service_Case_GetCounters>) | Gets the Case state counters (Active, Closed, All) for the selected filters
[Case_GetDefinitionDetails](<#Service_Case_GetDefinitionDetails>) | Gets information about activity statistics for a Case Definition
[Case_GetDetailsByCaseId](<#Service_Case_GetDetailsByCaseId>) | Gets details for an exisiting case identifier
[Case_GetExtraFieldValue](<#Service_Case_GetExtraFieldValue>) | Gets the actual value of an extra field for a specific case
[Case_GetGroupsUsersWithAccess](<#Service_Case_GetGroupsUsersWithAccess>) | Gets all Users and Groups that have access to this Case instance
[Case_GetHistory](<#Service_Case_GetHistory>) | Get the list of all case operations associated to an existing case instance
[Case_GetMilestones](<#Service_Case_GetMilestones>) | Gets the details of the Milestones associated with a given Case
[Case_GetStatusTimeline](<#Service_Case_GetStatusTimeline>) | Gets the status timeline (past and current) for a given case
[DEPRECATED_Case_GetActivities](<#Service_DEPRECATED_Case_GetActivities>) | Gets all activities associated with cases
[DEPRECATED_Case_GetActivitiesByCaseId](<#Service_DEPRECATED_Case_GetActivitiesByCaseId>) | Gets all activities associated with specific cases
[DEPRECATED_Case_GetActivityCounters](<#Service_DEPRECATED_Case_GetActivityCounters>) | Get activities count by each activity filter type
[DEPRECATED_Case_GetCases](<#Service_DEPRECATED_Case_GetCases>) | Gets all cases that meets the filter criterias
[DEPRECATED_Case_GetCasesCounters](<#Service_DEPRECATED_Case_GetCasesCounters>) | Get requests (Case) count by each case filter type
[Tag_GetAllByLabel](<#Service_Tag_GetAllByLabel>) | Gets all Tags for a given Case Definition that match the specified label. If no label is specified all tags are returned up to the MaxResults input parameter value

Structure | Description
---|---
[Activity_AssignDetails](<#Structure_Activity_AssignDetails>) | Details about activity assignment details
[Activity_CaseView](<#Structure_Activity_CaseView>) | For specific case, holds the activity view details
[Activity_Details](<#Structure_Activity_Details>) | Activity details
[Activity_Details2](<#Structure_Activity_Details2>) | Holds information for a case activity details
[ActivityAction_Details](<#Structure_ActivityAction_Details>) | Activity Action Detail
[ActivityActionOutput_View](<#Structure_ActivityActionOutput_View>) | Structure that a represents output action condition from a condition activity from the builder
[ActivityCounter](<#Structure_ActivityCounter>) | Counter for a specific activity progress status
[ActivityDetails](<#Structure_ActivityDetails>) | 
[ActivityDueDate](<#Structure_ActivityDueDate>) | Structure that defines the considered time range of an Activity due date
[ActivityEvent_Create](<#Structure_ActivityEvent_Create>) | Public structure to create a new activity event
[ActivityHistory](<#Structure_ActivityHistory>) | 
[ActivityResult](<#Structure_ActivityResult>) | 
[ActivityScope](<#Structure_ActivityScope>) | 
[ActivityScopeCounters](<#Structure_ActivityScopeCounters>) | 
[ActivitySearchCriteria](<#Structure_ActivitySearchCriteria>) | Input parameter with Activity filters. When values for different filter criteria types are sent, returned activities will match all filters (&quot;AND&quot; condition). Inside each criteria attribute list, the returned cases will match at least one of those values (&quot;OR&quot; condition).
[ActivitySort](<#Structure_ActivitySort>) | Activity fields to sort for
[Calendar_Detail](<#Structure_Calendar_Detail>) | Public structure with the calendar deailts
[Calendar_FilterResults](<#Structure_Calendar_FilterResults>) | Generic Filter Serch Structure
[Case_ActivityCount](<#Structure_Case_ActivityCount>) | Count of each activity filter type
[Case_DefinitionDetails](<#Structure_Case_DefinitionDetails>) | Holds activities statistics about a case definition
[Case_Details](<#Structure_Case_Details>) | Details for an existing case
[Case_Details2](<#Structure_Case_Details2>) | Holds information for a case details
[Case_ExecutionDetails](<#Structure_Case_ExecutionDetails>) | Holds information for case sla details
[Case_FilterResults](<#Structure_Case_FilterResults>) | Case Filter Search Structure
[Case_Identifier](<#Structure_Case_Identifier>) | Case Identifier
[Case_Information](<#Structure_Case_Information>) | Case Information Details
[Case_RequestCount](<#Structure_Case_RequestCount>) | Count of each case filter type
[CaseAccess](<#Structure_CaseAccess>) | Information about the read/write access of a Case
[CaseAccessControl_GroupDetails](<#Structure_CaseAccessControl_GroupDetails>) | Public  structure with Group Details
[CaseActivities_FilterResults](<#Structure_CaseActivities_FilterResults>) | Case Activities Filter Search Structure
[CaseActivity_Details](<#Structure_CaseActivity_Details>) | Holds details for a case definition activities statistics
[CaseActivity_View](<#Structure_CaseActivity_View>) | Represents an Activity Detail associated with a Case
[CaseActivityScope](<#Structure_CaseActivityScope>) | Structure that defines how Cases are filtered by Activities
[CaseActivitySearchField](<#Structure_CaseActivitySearchField>) | Holds a field to search for
[CaseActivitySortField](<#Structure_CaseActivitySortField>) | Holds a field to sort for
[CaseCounter](<#Structure_CaseCounter>) | Count of each case filter type
[CaseDetails](<#Structure_CaseDetails>) | Case intance details
[CaseDetails_Lite](<#Structure_CaseDetails_Lite>) | Details for an existing case (Case identifier and Case number)
[CaseExternalRequest_Create](<#Structure_CaseExternalRequest_Create>) | Public structure that enables to create case external request instances
[CaseExternalRequest_Details](<#Structure_CaseExternalRequest_Details>) | Public structure with CaseExternalRequest details
[CaseRequest_View](<#Structure_CaseRequest_View>) | Represents a Case Detail
[CaseScope](<#Structure_CaseScope>) | Structure that defines how Cases are filtered by Requester Scope and Case State Filter
[CaseSearchCriteria](<#Structure_CaseSearchCriteria>) | Possible Case filters. Note: the result of mixing values for filters of different types works as an &quot;AND&quot; and inside filters of the same type as an &quot;OR&quot;, for the list of cases to return.
[CaseSearchField](<#Structure_CaseSearchField>) | Holds a field to search for
[CaseSort](<#Structure_CaseSort>) | Case fields to sort for
[CaseSortField](<#Structure_CaseSortField>) | Holds a field to sort for
[CaseStatus_Details](<#Structure_CaseStatus_Details>) | Case Status Detail
[Delegation_Details](<#Structure_Delegation_Details>) | Structure that contains the Delegation Details
[Delegation_User](<#Structure_Delegation_User>) | Delegation User Details
[Delegation_UserDetails](<#Structure_Delegation_UserDetails>) | User Information
[Delegation_View](<#Structure_Delegation_View>) | Holds a Delegation&#180;
[ExtraFieldValue](<#Structure_ExtraFieldValue>) | Public structure with that holds the value for a setting
[FilterHistoryResults](<#Structure_FilterHistoryResults>) | Filter for case history list
[FilterResults](<#Structure_FilterResults>) | Filter Search Structure
[FilterResults2](<#Structure_FilterResults2>) | Filter Serch Structure
[Group_Details](<#Structure_Group_Details>) | Group Information
[Group_Details2](<#Structure_Group_Details2>) | Public structure with system entity group details
[GroupExtended_Detail](<#Structure_GroupExtended_Detail>) | Public structure to create a new Group Extended
[Holiday_Detail](<#Structure_Holiday_Detail>) | Public structure with the calendar holiday details
[HumanActivityTimelineDetails](<#Structure_HumanActivityTimelineDetails>) | 
[InformationGroupAccess](<#Structure_InformationGroupAccess>) | Holds the flags for each group type access
[MilestoneDetails](<#Structure_MilestoneDetails>) | Holds the details of a Milestone
[NonWorkingDay_Detail](<#Structure_NonWorkingDay_Detail>) | Public structure with the non working details
[Notification_Details](<#Structure_Notification_Details>) | Holds information for a notification case details
[NotificationEmail_Details](<#Structure_NotificationEmail_Details>) | Holds information for an email notification
[OrderHistoryResult](<#Structure_OrderHistoryResult>) | Order history results
[Process_Details](<#Structure_Process_Details>) | Process details
[Process_Details2](<#Structure_Process_Details2>) | Holds information for a case process details
[ProcessEvent_Create](<#Structure_ProcessEvent_Create>) | Public structure to create a new process event
[RuleExecution_Details](<#Structure_RuleExecution_Details>) | Holds information for a rule execution case details
[SampleUser](<#Structure_SampleUser>) | SampleUser
[Search_CaseDetails](<#Structure_Search_CaseDetails>) | Represents the details of a Case instance
[SearchCriteria](<#Structure_SearchCriteria>) | Result set filter criteria
[SLA_Details](<#Structure_SLA_Details>) | Holds information for sla details
[StatusDetails](<#Structure_StatusDetails>) | Case Status Details
[TagDetails](<#Structure_TagDetails>) | Public structure with Tag details
[TagIdentifier](<#Structure_TagIdentifier>) | Tag Identifier
[User_Details](<#Structure_User_Details>) | Generic structure with user details
[User_SearchResults](<#Structure_User_SearchResults>) | Public structure to return the search results for Group extended
[UserExtended_Details](<#Structure_UserExtended_Details>) | Details about user

## Actions

### Activity_AddComments { #Activity_AddComments }

Adds a comment to an existing acitivity

*Inputs*

ActivityId
:   Type: mandatory, Activity Identifier.  
    Activity Identifier

DelegatedBy
:   Type: optional, User Identifier.  
    User that is delegating the task (when it's a delegation)

Comments
:   Type: mandatory, Text.  
    Text containing comments to add

### Activity_AssignToGroup { #Activity_AssignToGroup }

Assigns an Activity to an existing group.  
If access control is switched on, automatically grants write access to the group for the case the activity is associated with.  
It performs a COMMIT on the transaction.

*Inputs*

ActivityId
:   Type: mandatory, Activity Identifier.  
    Activity Identifier

GroupId
:   Type: mandatory, Group Identifier.  
    Group Identifier

### Activity_AssignToGroupAndUser { #Activity_AssignToGroupAndUser }

Assigns an Activity to an existing group and user.  
If access control is switched on, automatically grants write access to the group and user for the case the activity is associated with.

*Inputs*

ActivityId
:   Type: mandatory, Activity Identifier.  
    Activity Identifier

GroupId
:   Type: mandatory, Group Identifier.  
    Group Identifier

UserId
:   Type: mandatory, User Identifier.  
    User Identifier

### Activity_AssignToUser { #Activity_AssignToUser }

Assigns an Activity to an existing user.  
If access control is switched on, automatically grants write access to the user for the case the activity is associated with.

*Inputs*

ActivityId
:   Type: mandatory, Activity Identifier.  
    Activity Identifier

UserId
:   Type: mandatory, User Identifier.  
    User Identifier

### Activity_CalculateAndSetDueDate { #Activity_CalculateAndSetDueDate }

Calculate and set the due DateTime for an Activity, based on the Activity configured SLA and Calendar (if set). Creates an event if SetEvent field is set to True, that can be captured and execute some logic.

*Inputs*

ActivityId
:   Type: mandatory, Activity Identifier.  
    Activity Identifier

CalendarId
:   Type: optional, Calendar Identifier.  
    (Optional) Calendar considered for the SLA time calculations. If no calendar is filled in, and there is a calendar already associated with the activity the last one will be used, otherwise it will consider a full day time.

StartDate
:   Type: optional, Date Time.  
    (Optional) Start date for the SLA calculations. If nof filled in, it will use the current DateTime

MinutesForCompletion
:   Type: mandatory, Integer.  
    Time for completion (minutes). To use the configured response time send value 0. If this value is filled in, any configured value will be overriden

SetEvent
:   Type: optional, Boolean.  
    If True, an event will be triggered when the activity exceeds the SLA time. It can be used to perform specific tasks (ex: send an email)

*Outputs*

DueDate
:   Type: Date Time.  
    Activity due Date and Time

### Activity_CalculateExecutionTime { #Activity_CalculateExecutionTime }

Calculate and set the execution time for an Activity based on the Activity configured SLA

*Inputs*

ActivityId
:   Type: mandatory, Activity Identifier.  
    Activity Identifier

### Activity_CheckIsBlocked { #Activity_CheckIsBlocked }

Check if an activity is blocked

*Inputs*

ActivityId
:   Type: mandatory, Activity Identifier.  
    Activity Identifier

*Outputs*

IsBlocked
:   Type: Boolean.  
    If the activity is blocked

### Activity_CheckUserAccess { #Activity_CheckUserAccess }

Checks if the user is assigned to the activity, or has access to it under delegation.

*Inputs*

ActivityId
:   Type: mandatory, Activity Identifier.  
    Activity Identifier

UserId
:   Type: mandatory, User Identifier.  
    User Identifier

*Outputs*

IsValid
:   Type: Boolean.  
    If the user has access to the activity.

ActivityAssignmentDetails
:   Type: [Activity_AssignDetails](<#Structure_Activity_AssignDetails>).  
    Activity Assignment Details (user and group assigned to the activity, status and opening date)

### Activity_SetDueDate { #Activity_SetDueDate }

Set the due date for an Activity

*Inputs*

ActivityId
:   Type: mandatory, Activity Identifier.  
    Activity Identifier

DueDatetime
:   Type: mandatory, Date Time.  
    The date and time limit for the human activity to be finished.

SetEvent
:   Type: optional, Boolean.  
    If True, an event will be triggered when the activity exceeds the SLA to perform specific tasks (ex: send an email).

### Activity_SetStartDate { #Activity_SetStartDate }

Schedules a start date for the Activity to be available.

*Inputs*

ActivityId
:   Type: mandatory, Activity Identifier.  
    Activity Identifier

StartDate
:   Type: mandatory, Date Time.  
    Optional date that defines when the activity is scheduled to become available to be handled

### Activity_ValidateUserAccess { #Activity_ValidateUserAccess }

Validate user authorization to access the activity (directly assigned to the activity, or under delegation). If the user is not authorized an exception is raised.

*Inputs*

ActivityId
:   Type: mandatory, Activity Identifier.  
    Activity Identifier

UserId
:   Type: mandatory, User Identifier.  
    User Identifier

*Outputs*

ActivityAssignmentDetails
:   Type: [Activity_AssignDetails](<#Structure_Activity_AssignDetails>).  
    Activity Assignment Details (user and group assigned to the activity, status and opening date)

### ActivityEvent_Set { #ActivityEvent_Set }

Creates an activity event

*Inputs*

ActivityEventCreateRec
:   Type: mandatory, [ActivityEvent_Create](<#Structure_ActivityEvent_Create>).  
    ActivityEvent Record

### Calendar_CheckWorkingDay { #Calendar_CheckWorkingDay }

Checks if the date is a working day (for a specific calendar)

*Inputs*

CalendarId
:   Type: mandatory, Calendar Identifier.  
    Calendar Identifier

Date
:   Type: mandatory, Date.  
    Date to check

*Outputs*

IsWorkingDay
:   Type: Boolean.  
    True if the date is a working day in the given calendar, false otherwise.

### Calendar_GetAll { #Calendar_GetAll }

Gets the list of calendars

*Inputs*

Filter
:   Type: mandatory, [Calendar_FilterResults](<#Structure_Calendar_FilterResults>).  
    Filter conditions

*Outputs*

CalendarDetailList
:   Type: [Calendar_Detail](<#Structure_Calendar_Detail>) List.  
    Calendar Detail List

TotalResults
:   Type: Long Integer.  
    Number of total results that match the criteiria

### Calendar_GetById { #Calendar_GetById }

Gets the details for a specific calendar

*Inputs*

CalendarId
:   Type: mandatory, Calendar Identifier.  
    Calendar Identifier

Date
:   Type: optional, Date.  
    Date to filter for the calendar holidays (by defaut the current date is used)

OnlyActive
:   Type: optional, Boolean.  
    Filter only active holidays and non working days?

*Outputs*

CalendarDetail
:   Type: [Calendar_Detail](<#Structure_Calendar_Detail>).  
    Calendar details

### Calendar_GetEndDate { #Calendar_GetEndDate }

Calculate the end date based on the working hours and holidays/non working days. Also perform the calculation based on the TimeZone associated to the Calendar.

*Inputs*

CalendarId
:   Type: mandatory, Calendar Identifier.  
    Calendar Identifier

StartDate
:   Type: mandatory, Date Time.  
    Start date for the calculation (server timezone). If your StartDate is not on the server timezone you need to convert it first.

Minutes
:   Type: mandatory, Integer.  
    Number of minutes (it must be always a positive value)

*Outputs*

EndDate
:   Type: Date Time.  
    End date based on the working days (server time)

### Case_AddComments { #Case_AddComments }

Add comments to an existing case.

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

DelegatedBy
:   Type: optional, User Identifier.  
    User that is delegating the task (when it's a delegation)

Comments
:   Type: mandatory, Text.  
    The comment to be added to the case

IsVisibleToRequester
:   Type: optional, Boolean.  
    If True, the comment will be visible for the requester as well as the operator. Otherwise the comment will be available only to Operators

### Case_AddTags { #Case_AddTags }

Enables to add an existing tag (or tags) to a particular case instance

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

TagsList
:   Type: mandatory, Text.  
    List of comma separated tag labels, to add to the Case instance

### Case_AssociateProcess { #Case_AssociateProcess }

Enables to associate an existing case instance with a proccess, based on an existing process identifier

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

ProcessId
:   Type: mandatory, Process Identifier.  
    Process Identifier

CalendarId
:   Type: optional, Calendar Identifier.  
    (Optional) Calendar associated for SLA Calculation. If the calendar is not filled in and there is a calendar associated with the process it will be used, otherwise it will consider 24/7.

OverrideMinutesForCompletion
:   Type: optional, Integer.  
    Response time in minutes (SLA) - to use the configured response time fill in with 0. If this value is filled in this will override any configured value.

GenerateEvent
:   Type: optional, Boolean.  
    If True, an event will be triggered when the case/process exceeds the defined SLA - minutes for completion

Comments
:   Type: optional, Text.  
    Additional comments for case initialization

### Case_BlockActivity { #Case_BlockActivity }

Enables to block an existing activity associated to an existing case.

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

ActivityId
:   Type: mandatory, Activity Identifier.  
    Activity Identifier

DelegatedBy
:   Type: optional, User Identifier.  
    User that is delegating the task (when it's a delegation)

Comments
:   Type: optional, Text.  
    Additional comments on the blocking action (optional)

### Case_CheckActiveActivity { #Case_CheckActiveActivity }

For a given case and activity definition returns the activity instance, if it exists and the user has permissions on it

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

ActivityDefinitionId
:   Type: mandatory, Activity_Definition Identifier.  
    Activity Definition Identifier  
    (use ActivityDefinitionId or ActivityDefinitionSSKey to identify the activity defintion in the system)

ActivityDefinitionSSKey
:   Type: mandatory, Text.  
    Activity Definition SS Key  
    ActivityDefinitionSSKey to identify the activity defintion in the system)

IncludeGroupCheck
:   Type: optional, Boolean.  
    If true, the user must belong to the group assigned to the activity or the activity is assigned to the user.  
    If false then the activity must be assigned to the user.

*Outputs*

ActivityId
:   Type: Activity Identifier.  
    Activity Identifier

### Case_CheckActivityAccess { #Case_CheckActivityAccess }

Check if a user has access (directly assigned) to an activity (open or closed)

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

ActivityId
:   Type: mandatory, Activity Identifier.  
    Activity Identifier

UserId
:   Type: optional, User Identifier.  
    User Identifier (if empty, current user will be assumed)

*Outputs*

HasAccessToActivity
:   Type: Boolean.  
    Returns True, if the given activity exists (open or closed) and the user has access to it

IsActive
:   Type: Boolean.  
    Returns True if the activity is ready/open, False if is already Closed (or an assync close request was already submited)

IsBlocked
:   Type: Boolean.  
    Returns true, if the activity is blocked (when the user has access to it)

### Case_CheckActivityIsActive { #Case_CheckActivityIsActive }

Checks if the given activity belongs to the current OutSystems BPT process that is active for this Case, and if the activity itself is also active.

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Id

ActivityId
:   Type: mandatory, Activity Identifier.  
    Activity Id

*Outputs*

IsActive
:   Type: Boolean.  
    if the activity and current process are still active

### Case_CheckProcessIsActive { #Case_CheckProcessIsActive }

Checks if the current associated bpt process  is active for this Case

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

*Outputs*

IsActive
:   Type: Boolean.  
    if the current process is still active

### Case_CloseActivity { #Case_CloseActivity }

Close an activity and validates that only the correct user can close it. Will try to close it in a synchronous way (bpt default behavior) so it performs a COMMIT in the current transition.

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

ActivityId
:   Type: mandatory, Activity Identifier.  
    Activity Identifier

ActionId
:   Type: optional, CaseAction Identifier.  
    Action performed by the user (mandatory when more than one is available to the user)

CaseStatusId
:   Type: optional, CaseStatus Identifier.  
    Status Identifier (optional)

DelegatedBy
:   Type: optional, User Identifier.  
    User that is delegating the task (when it's a delegation)

Comments
:   Type: optional, Text.  
    Additional description for close action (optional)

IsVisibleToRequester
:   Type: optional, Boolean.  
    If true, this action will be visible to the requester in the case history

### Case_CloseActivityAsync { #Case_CloseActivityAsync }

Close an activity and validates that only the correct user can close it (will try to close the activity in an asynchronous way). Enhanced activity close funtionality in opposing the default syncronous bpt close behavior).

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

ActivityId
:   Type: mandatory, Activity Identifier.  
    Activity Identifier

ActionId
:   Type: optional, CaseAction Identifier.  
    Action performed by the user (mandatory when more than one is available to the user)

CaseStatusId
:   Type: optional, CaseStatus Identifier.  
    Status Identifier (optional)

DelegatedBy
:   Type: optional, User Identifier.  
    User that is delegating the task (when it's a delegation)

Comments
:   Type: optional, Text.  
    Additional description for close action (optional)

IsVisibleToRequester
:   Type: optional, Boolean.  
    If true, this action will be visible to the requester in the case history

### Case_Complete { #Case_Complete }

Enables to close an existing case instance based on an existing process identifier

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

CaseStatusId
:   Type: optional, CaseStatus Identifier.  
    End Status (Optional)

Comments
:   Type: optional, Text.  
    Additional comments for case completion

UserId
:   Type: optional, User Identifier.  
    User who completed the Case instance (Optional - if the parameter is not filled in, the currently logged in user will be used)

### Case_Delete { #Case_Delete }

Deletes a case instance

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    

### Case_Discard { #Case_Discard }

Discard a case instance  
  
Note: All associated running processes/activities will be terminated.

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

### Case_DiscardActivity { #Case_DiscardActivity }

Discards an activity (discarded status), stopping the execution of the current process flow. Calls the Activity_Discard action from the BPT API which commits the current transaction.

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

ActivityId
:   Type: mandatory, Activity Identifier.  
    Activity Identifier

DelegatedBy
:   Type: optional, User Identifier.  
    User that is delegating the task (when it's a delegation)

Comments
:   Type: optional, Text.  
    Additional comments for the Discard action (optional)

*Outputs*

IsSuccess
:   Type: Boolean.  
    If the action was done successfully

### Case_GetIdByProcessId { #Case_GetIdByProcessId }

Gets the case identifier based on the process identifier

*Inputs*

ProcessId
:   Type: mandatory, Process Identifier.  
    Process Identifier

*Outputs*

CaseId
:   Type: Case Identifier.  
    Gets the Case Identifier and Definition

### Case_GrantAccessToGroup { #Case_GrantAccessToGroup }

Grants a given group access to a given Case

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

GroupId
:   Type: mandatory, Group Identifier.  
    Group Identifier

HasWritePermission
:   Type: mandatory, Boolean.  
    If True the Group is granted read/write permissions to the case. If False only read permission is granted.

### Case_GrantAccessToUser { #Case_GrantAccessToUser }

Grants a given user access to a given Case

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

UserId
:   Type: mandatory, User Identifier.  
    User Identifier

HasWritePermission
:   Type: mandatory, Boolean.  
    If True the User is granted read/write permissions to the case. If False only read permission is granted.

### Case_Initialize { #Case_Initialize }

Enables to initialize a new case instance based on an existing case definition identifier

*Inputs*

CaseDefinitionId
:   Type: mandatory, CaseDefinition Identifier.  
    Case Definition Identifier

CaseStatusId
:   Type: optional, CaseStatus Identifier.  
    Initial Status (Optional)

PriorityId
:   Type: optional, ProcessDefinitionPriority Identifier.  
    Initial Priority (Optional)

ParentCaseId
:   Type: optional, Case Identifier.  
    Parent Case Identifier (Optional)

Comments
:   Type: optional, Text.  
    Additional comments for case initialization

UserId
:   Type: optional, User Identifier.  
    User who initialized the Case instance (Optional - if the parameter is not filled in, the currently logged in user will be used)

CaseRequesterUserId
:   Type: optional, User Identifier.  
    Requester of the Case (internal). The requester is the OutSystems user who requested the case, in case it was submitted by other person (UserId field) or system

ExternalRequesterDetails
:   Type: optional, [CaseExternalRequest_Create](<#Structure_CaseExternalRequest_Create>).  
    Details about the Requester of the Case (external). The external requester is the person who requested the case, in case it was submitted by other person (UserId field) or system

Tags
:   Type: optional, Text.  
    List of comma separated tags to add to the Case instance

*Outputs*

CaseId
:   Type: Case Identifier.  
    Case Identifier

### Case_IsMilestoneAchieved { #Case_IsMilestoneAchieved }

Checks whether a given Milestone has been achieved or not for a given Case

*Inputs*

MilestoneDefinitionId
:   Type: mandatory, MilestoneDefinition Identifier.  
    Milestone Definition Identifier

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

*Outputs*

IsAchieved
:   Type: Boolean.  
    True if the Milestone has been achieved, false otherwise

### Case_OpenActivity { #Case_OpenActivity }

Opens an acitivity and validates that only the correct user can open it

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

ActivityId
:   Type: mandatory, Activity Identifier.  
    Activity Identifier

DelegatedBy
:   Type: optional, User Identifier.  
    User that is delegating the task (when it's a delegation)

Comments
:   Type: optional, Text.  
    Additional description for open action (optional)

*Outputs*

HandlingURL
:   Type: Text.  
    URL that enables to redirect the user to the activity page (if applicable)

### Case_PerformActionActivity { #Case_PerformActionActivity }

Perform an action to an existing activity associated to a case, taking into account the action specifc validations.

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

ActivityId
:   Type: mandatory, Activity Identifier.  
    Activity Identifier

ActivityActionId
:   Type: mandatory, ActivityAction Identifier.  
    Activity Action Identifier

DelegatedBy
:   Type: optional, User Identifier.  
    User that is delegating the task (when it's a delegation)

Comments
:   Type: optional, Text.  
    Additional description (optional)

*Outputs*

IsSuccess
:   Type: Boolean.  
    If the action was done successfully

HandlingURL
:   Type: Text.  
    URL that enables to redirect the user to the activity page (if applicable). Only for open and pickup actions.

### Case_PickupActivity { #Case_PickupActivity }

Assigns the activity to the user, if it is not assigned. The user needs to belong to the group assigned to the activity (if the group activity is set), or have an active delegation.

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

ActivityId
:   Type: mandatory, Activity Identifier.  
    Id

DelegatedBy
:   Type: optional, User Identifier.  
    User that is delegating the task (when it's a delegation)

Comments
:   Type: optional, Text.  
    Additional description for pickup action (optional)

*Outputs*

IsSuccess
:   Type: Boolean.  
    If the action was done successfully

HandlingURL
:   Type: Text.  
    URL that enables to redirect the user to the activity page (if applicable).

### Case_ReleaseActivity { #Case_ReleaseActivity }

Releases the activity assigned to a specific user. Can only be released by the user that has the activity assigned.

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

ActivityId
:   Type: mandatory, Activity Identifier.  
    Activity Identifier

DelegatedBy
:   Type: optional, User Identifier.  
    User that is delegating the task (when it's a delegation)

Comments
:   Type: optional, Text.  
    Additional description for release action (optional)

*Outputs*

IsSuccess
:   Type: Boolean.  
    If the action was done successfully

### Case_RemoveTag { #Case_RemoveTag }

Removes a Tag from a Case

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

TagId
:   Type: mandatory, Tag Identifier.  
    Tag Identifier

### Case_RevokeAccessFromGroup { #Case_RevokeAccessFromGroup }

Revokes access to a given Case for a given group

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

GroupId
:   Type: mandatory, Group Identifier.  
    Group Identifier

### Case_RevokeAccessFromUser { #Case_RevokeAccessFromUser }

Revokes access to a given Case for a given user

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

UserId
:   Type: mandatory, User Identifier.  
    User Identifier

### Case_SkipActivity { #Case_SkipActivity }

Skips the current activity assigned to a specific user. Can only be skipped by the user that has the activity assigned (or under a valid delegation).

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

ActivityId
:   Type: mandatory, Activity Identifier.  
    Activity Identifier

DelegatedBy
:   Type: optional, User Identifier.  
    User that is delegating the task (when it's a delegation)

Comments
:   Type: optional, Text.  
    Additional comments for the Skip action (optional)

*Outputs*

IsSuccess
:   Type: Boolean.  
    If the action was done successfully

### Case_TakeoverActivity { #Case_TakeoverActivity }

Reassigns the case activity to the user. The user needs to belong to the group assigned to the activity (if the activity group is set)

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

ActivityId
:   Type: mandatory, Activity Identifier.  
    Activity Identifier

DelegatedBy
:   Type: optional, User Identifier.  
    User that is delegating the task (when it's a delegation)

Comments
:   Type: optional, Text.  
    Additional description for takeover action (optional)

*Outputs*

IsSuccess
:   Type: Boolean.  
    If the action was done successfully

### Case_UnblockActivity { #Case_UnblockActivity }

Enables to unblock an existing blocked activity associated to an existing case

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

ActivityId
:   Type: mandatory, Activity Identifier.  
    Id

DelegatedBy
:   Type: optional, User Identifier.  
    User that is delegating the task (when it's a delegation)

Comments
:   Type: optional, Text.  
    Additional description for the unblock action (optional)

### Case_UpdateGroupAccess { #Case_UpdateGroupAccess }

Updates Group access to a given Case

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

GroupId
:   Type: mandatory, Group Identifier.  
    Group Identifier

HasWritePermission
:   Type: mandatory, Boolean.  
    If True the Group is granted read/write permissions to the case. If False only read permission is granted.

### Case_UpdatePriority { #Case_UpdatePriority }

Updates the priority for an existing case

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

PriorityId
:   Type: mandatory, ProcessDefinitionPriority Identifier.  
    The Priority to set

ActivityId
:   Type: optional, Activity Identifier.  
    If the change status was under the scope of an activity

Comments
:   Type: optional, Text.  
    Additional comments for case priority

DelegatedBy
:   Type: optional, User Identifier.  
    User that is delegating the task (when it's a delegation)

### Case_UpdateStatus { #Case_UpdateStatus }

Updates the status for an existing case

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

CaseStatusId
:   Type: mandatory, CaseStatus Identifier.  
    The Status to set

ActivityId
:   Type: optional, Activity Identifier.  
    If the change status was under the scope of an activity

Comments
:   Type: optional, Text.  
    Additional comments for case status

DelegatedBy
:   Type: optional, User Identifier.  
    User that is delegating the task (when it's a delegation)

### Case_UpdateStatusByActivityId { #Case_UpdateStatusByActivityId }

Updates the Status for an existing case from an exisiting activity

*Inputs*

ActivityId
:   Type: mandatory, Activity Identifier.  
    If the change status was under the scope of an activity

CaseStatusId
:   Type: mandatory, CaseStatus Identifier.  
    The Status to set

Comments
:   Type: optional, Text.  
    Additional comments for case Status

DelegatedBy
:   Type: optional, User Identifier.  
    User that is delegating the task (when it's a delegation)

### Case_UpdateUserAccess { #Case_UpdateUserAccess }

Updates User access to a given Case

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

UserId
:   Type: mandatory, User Identifier.  
    User Identifier

HasWritePermission
:   Type: mandatory, Boolean.  
    If True the User is granted read/write permissions to the case. If False only read permission is granted.

### Case_ValidateAccess { #Case_ValidateAccess }

Validates if a User has access to a given Case (either by himself or under an active delegation)

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

UserId
:   Type: optional, User Identifier.  
    User Identifier (if not filled it assumes the user currently logged in)

*Outputs*

CaseAccessDetails
:   Type: [CaseAccess](<#Structure_CaseAccess>).  
    Structure with read/write access information for a case

### CaseActivityAction_Get { #CaseActivityAction_Get }

Get the Action chosen by the user for a specified activity

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

ActivityId
:   Type: mandatory, Activity Identifier.  
    Activity Identifier

*Outputs*

ActionId
:   Type: Text.  
    Action performed by the end-user

UserId
:   Type: User Identifier.  
    Performed by the User with Id

### CaseDefinition_GrantAccessToGroup { #CaseDefinition_GrantAccessToGroup }

Grants a given group access to all cases from a given Case Definition

*Inputs*

CaseDefinitionId
:   Type: mandatory, CaseDefinition Identifier.  
    CaseDefinition Identifier

GroupId
:   Type: mandatory, Group Identifier.  
    Group Identifier

HasWritePermission
:   Type: mandatory, Boolean.  
    If True the User is granted read/write permissions to the cases from the given case definition. If False only read permission is granted.

### CaseDefinition_GrantAccessToUser { #CaseDefinition_GrantAccessToUser }

Grants a given user access to all cases from a given Case Definition

*Inputs*

CaseDefinitionId
:   Type: mandatory, CaseDefinition Identifier.  
    CaseDefinition Identifier

UserId
:   Type: mandatory, User Identifier.  
    User Identifier

HasWritePermission
:   Type: mandatory, Boolean.  
    If True the User is granted read/write permissions to the cases from the given case definition. If False only read permission is granted.

### CaseDefinition_RevokeAccessFromGroup { #CaseDefinition_RevokeAccessFromGroup }

Revokes access to cases from a given Case Definition (from a group)

*Inputs*

CaseDefinitionId
:   Type: mandatory, CaseDefinition Identifier.  
    CaseDefinition Identifier

GroupId
:   Type: mandatory, Group Identifier.  
    Group Identifier

### CaseDefinition_RevokeAccessFromUser { #CaseDefinition_RevokeAccessFromUser }

Revokes access to cases fom a given CaseDefinition (from a user)

*Inputs*

CaseDefinitionId
:   Type: mandatory, CaseDefinition Identifier.  
    CaseDefinition Identifier

UserId
:   Type: mandatory, User Identifier.  
    User Identifier

### CaseDefinition_UpdateGroupAccess { #CaseDefinition_UpdateGroupAccess }

Updates Group access permissions to a given Case definition

*Inputs*

CaseDefinitionId
:   Type: mandatory, CaseDefinition Identifier.  
    CaseDefinition Identifier

GroupId
:   Type: mandatory, Group Identifier.  
    Group Identifier

HasWritePermission
:   Type: mandatory, Boolean.  
    If True the Group is granted read/write permissions to the case. If False only read permission is granted.

### CaseDefinition_UpdateUserAccess { #CaseDefinition_UpdateUserAccess }

Updates User access permissions to a given Case definition

*Inputs*

CaseDefinitionId
:   Type: mandatory, CaseDefinition Identifier.  
    CaseDefinition Identifier

UserId
:   Type: mandatory, User Identifier.  
    User Identifier

HasWritePermission
:   Type: mandatory, Boolean.  
    If True the Group is granted read/write permissions to the case. If False only read permission is granted.

### Delegation_GetAll { #Delegation_GetAll }

Get all delegations which current user has access to.

*Inputs*

FilterResults
:   Type: mandatory, [FilterResults2](<#Structure_FilterResults2>).  
    Filter Delegation Results

Timestamp
:   Type: optional, Date Time.  
    Delegations that are within in this date

*Outputs*

Delegations
:   Type: [Delegation_View](<#Structure_Delegation_View>) List.  
    List of Delegations

TotalResults
:   Type: Long Integer.  
    Total Results

### Delegation_GetById { #Delegation_GetById }

Get a delegation by Identifier, if the user has access to it

*Inputs*

DelegationId
:   Type: mandatory, Delegation Identifier.  
    Delegation Identifier

*Outputs*

Delegation
:   Type: [Delegation_View](<#Structure_Delegation_View>).  
    Delegation

### Delegation_GetByUser { #Delegation_GetByUser }

Gets the active delegations for the specified user in which the Timestamp is between the Delegation's From and To Dates

*Inputs*

Timestamp
:   Type: optional, Date Time.  
    Date Time that will be considered to retrieve the valid delegations

ToUserId
:   Type: optional, User Identifier.  
    User identifier (if not set current user will be used)

*Outputs*

Delegations
:   Type: [Delegation_User](<#Structure_Delegation_User>).  
    List of Delegations

### Delegation_IsValid { #Delegation_IsValid }

Checks if there is an active delegation from user (optional group) for destination user

*Inputs*

FromUserId
:   Type: mandatory, User Identifier.  
    Delegation User Identifier

FromGroupId
:   Type: optional, Group Identifier.  
    Delegation Group Identifier

FromGroupExtendedId
:   Type: optional, GroupExtended Identifier.  
    Delegation Group Identifier. Will be ignored if FromGroupId is also set

ToUserId
:   Type: mandatory, User Identifier.  
    Delegated User Identifier

*Outputs*

IsValid
:   Type: Boolean.  
    True if the delegation exists and is valid

### DEPRECATED_Case_AddAccessToGroup { #DEPRECATED_Case_AddAccessToGroup }

Give access control to a group associated to an exisitng case instance

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

GroupId
:   Type: mandatory, Group Identifier.  
    Group identifier

CanView
:   Type: mandatory, Boolean.  
    If the group has view permission

CanEdit
:   Type: mandatory, Boolean.  
    If the group has edit permission

### DEPRECATED_Case_AddAccessToUser { #DEPRECATED_Case_AddAccessToUser }

Give access control to a user associated to an exisitng case instance

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

UserId
:   Type: mandatory, User Identifier.  
    User identifier

CanView
:   Type: mandatory, Boolean.  
    If the user has view permission

CanEdit
:   Type: mandatory, Boolean.  
    If the user has edit permission

### DEPRECATED_Case_CheckUserPermission { #DEPRECATED_Case_CheckUserPermission }

Checks if the currently logged in user has access to the specified case

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

CanEdit
:   Type: optional, Boolean.  
    If true, Access Control must include CanEdit and not only CanView

*Outputs*

HasAccess
:   Type: Boolean.  
    Will be true if the user has access

### DEPRECATED_Case_RemoveAccessFromGroup { #DEPRECATED_Case_RemoveAccessFromGroup }

Remove access control from a group to an existing case instance

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

GroupId
:   Type: mandatory, Group Identifier.  
    Group identifier

### DEPRECATED_Case_RemoveAccessFromUser { #DEPRECATED_Case_RemoveAccessFromUser }

Remove access control from a user to an existing case instance

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

UserId
:   Type: mandatory, User Identifier.  
    User identifier

### DEPRECATED_Case_SetAccessControlToActivity { #DEPRECATED_Case_SetAccessControlToActivity }

Will check and assign/unassign access control to a case instance

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

ActivityId
:   Type: mandatory, Activity Identifier.  
    Activity Identifier

UserId
:   Type: mandatory, User Identifier.  
    User identifier

IsAssign
:   Type: mandatory, Boolean.  
    If true, will perform an assign, otherwise will perform a unassign

### Email_Send { #Email_Send }

Sends an email in the context of a case. DO NOT call this action to send test emails or preview emails.

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier. To obtain the case identifier from the process please use the action Case_GetIdByProcessId

ActivityId
:   Type: optional, Activity Identifier.  
    Activity Identifier

EmailTemplateId
:   Type: mandatory, EmailTemplate Identifier.  
    EmailTemplate Id

From
:   Type: optional, Text.  
    Email from

To
:   Type: optional, Text.  
    If more than one, separate email addresses with a comma (,). The To or GroupMatrix must be filled in.  
    

ToGroupId
:   Type: optional, Group Identifier.  
    Send the email to all users that belongs to the specified group.  
    (Using this option you can specify an empty value for To input parameter)

Cc
:   Type: optional, Text.  
    If more than one, separate email addresses with a comma (,)

CcGroupId
:   Type: optional, Group Identifier.  
    Send the Cc email to all users that belongs to the specified group.

Bcc
:   Type: optional, Text.  
    If more than one, separate email addresses with a comma (,)

BccGroupId
:   Type: optional, Group Identifier.  
    Send the Bcc email to all users that belongs to the specified group.

UserId
:   Type: optional, User Identifier.  
    User identifier for the user to send the email (optional)

*Outputs*

Success
:   Type: Boolean.  
    If success sending the email

Error
:   Type: Text.  
    Error message

### Group_GetUsersById { #Group_GetUsersById }

Gets the list of users for an existing group. The role is an optional search criteria.

*Inputs*

FilterResults
:   Type: optional, [FilterResults](<#Structure_FilterResults>).  
    Gets the number of records

GroupId
:   Type: mandatory, Group Identifier.  
    Group Identifier

RoleId
:   Type: optional, Role Identifier.  
    Role Identifier

*Outputs*

SearchResults
:   Type: [User_SearchResults](<#Structure_User_SearchResults>).  
    List of Group Matrix

### Group_GetUsersToAssociate { #Group_GetUsersToAssociate }

Gets the list of users that can be assoicated to an existing group

*Inputs*

GroupId
:   Type: mandatory, Group Identifier.  
    Group Identifier

*Outputs*

SearchResults
:   Type: [User_SearchResults](<#Structure_User_SearchResults>).  
    List of Group Matrix

### GroupExtended_CheckUserAssociation { #GroupExtended_CheckUserAssociation }

Checks if the group contains the user association

*Inputs*

GroupId
:   Type: mandatory, Group Identifier.  
    Group  Identifier

UserId
:   Type: mandatory, User Identifier.  
    User Identifier

*Outputs*

IsSuccess
:   Type: Boolean.  
    True if the user is associated to the group matrix

### GroupExtended_GetAll { #GroupExtended_GetAll }

Gets all Group Matrix

*Inputs*

FilterResults
:   Type: optional, [FilterResults](<#Structure_FilterResults>).  
    Filter options for the group matrix

*Outputs*

GroupExtendedDetails
:   Type: [GroupExtended_Detail](<#Structure_GroupExtended_Detail>) List.  
    List for Group Matrix Results

TotalResults
:   Type: Long Integer.  
    Number of total groups that match the criteiria

### GroupExtended_GetByGroupId { #GroupExtended_GetByGroupId }

Gets sepecific group details

*Inputs*

GroupId
:   Type: mandatory, Group Identifier.  
    Group Identifier

*Outputs*

GroupExtendedDetails
:   Type: [GroupExtended_Detail](<#Structure_GroupExtended_Detail>).  
    Group Matrix Details

### GroupExtended_GetByGroupName { #GroupExtended_GetByGroupName }

Gets sepecific group details by group name (exact match)

*Inputs*

GroupName
:   Type: mandatory, Text.  
    Group Name

*Outputs*

GroupExtendedDetails
:   Type: [GroupExtended_Detail](<#Structure_GroupExtended_Detail>).  
    Group Extended Details

### GroupExtended_GetById { #GroupExtended_GetById }

Gets sepecific group details

*Inputs*

Id
:   Type: mandatory, GroupExtended Identifier.  
    Group Matrix Id

*Outputs*

GroupExtendedDetails
:   Type: [GroupExtended_Detail](<#Structure_GroupExtended_Detail>).  
    Group Matrix Details

### GroupExtended_GetGroupIdById { #GroupExtended_GetGroupIdById }

Gets the Group Identifier by the Group extended  Identifier

*Inputs*

Id
:   Type: mandatory, GroupExtended Identifier.  
    Groups Matrix identifier

*Outputs*

GroupId
:   Type: Group Identifier.  
    Group Identifier

### GroupExtended_GetGroupsByUser { #GroupExtended_GetGroupsByUser }

Gets the list of groups that the user belongs to

*Inputs*

FilterResults
:   Type: optional, [FilterResults](<#Structure_FilterResults>).  
    Gets the number of records

UserId
:   Type: mandatory, User Identifier.  
    User Identifier

*Outputs*

GroupExtendedDetails
:   Type: [GroupExtended_Detail](<#Structure_GroupExtended_Detail>) List.  
    List for Group Matrix Results

TotalResults
:   Type: Long Integer.  
    Number of total groups that match the criteiria

### GroupExtended_GetGroupsToAssociate { #GroupExtended_GetGroupsToAssociate }

Returns the list of possible groups to be associated

*Inputs*

GroupExtendedId
:   Type: mandatory, GroupExtended Identifier.  
    Group Matrix Identifier

*Outputs*

GroupExtendedDetails
:   Type: [GroupExtended_Detail](<#Structure_GroupExtended_Detail>) List.  
    List for Group Matrix Results

TotalResults
:   Type: Long Integer.  
    Number of total groups that match the criteiria

### Holiday_GetById { #Holiday_GetById }

Get a Holiday record

*Inputs*

HolidayId
:   Type: mandatory, Holiday Identifier.  
    Holiday Identifier

*Outputs*

HolidayDetail
:   Type: [Holiday_Detail](<#Structure_Holiday_Detail>).  
    Record

### Milestone_SetAchieved { #Milestone_SetAchieved }

Updates the IsAchieved field to True and the AchievedOn date and AchievedBy user from a given Milestone Definition of a Case

*Inputs*

MilestoneDefinitionId
:   Type: mandatory, MilestoneDefinition Identifier.  
    Milestone Definition Identifier

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

AchievementDate
:   Type: optional, Date Time.  
    Date and time of the milestone achievement. Default is Current DateTime

### Milestone_SetUnachieved { #Milestone_SetUnachieved }

Updates the IsAchieved field to False and resets the AchievedOn and AchievedBy fields from a given Milestone Definition of a Case

*Inputs*

MilestoneDefinitionId
:   Type: mandatory, MilestoneDefinition Identifier.  
    Milestone Definition Identifier

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

### NonWorkingDay_GetById { #NonWorkingDay_GetById }

Get a NonWorkingDay record

*Inputs*

NonWorkingDayId
:   Type: mandatory, NonWorkingDay Identifier.  
    NonWorkingDay Identifier

*Outputs*

NonWorkingDayDetail
:   Type: [NonWorkingDay_Detail](<#Structure_NonWorkingDay_Detail>).  
    NonWorkinDay Detail

### Process_CalculateAndSetDueDate { #Process_CalculateAndSetDueDate }

Calculate and set the due date time for an existing process.

*Inputs*

ProcessId
:   Type: mandatory, Process Identifier.  
    Process Identifier

CalendarId
:   Type: optional, Calendar Identifier.  
    (Optional) Calendar associated for SLA Calculation. If the calendar is not filled in and there is a calendar associated with the process it will be used, otherwise it will consider 24/7.

StartDate
:   Type: optional, Date Time.  
    (Optional) Start date for the SLA calculation, if nof filled in it will use the current datetime

MinutesForCompletion
:   Type: mandatory, Integer.  
    Response time in minutes - to use the configured response time fill in with 0. If this value is filled in this will override any configured value.

SetEvent
:   Type: optional, Boolean.  
    If True, an event will be triggered when the process exceeds the SLA to perform specific tasks (ex: send an email).

*Outputs*

DueDate
:   Type: Date Time.  
    Process due date and time

### Process_CalculateExecutionTime { #Process_CalculateExecutionTime }

Calculate and set the execution time for a process based on the Process.

*Inputs*

ProcessId
:   Type: mandatory, Process Identifier.  
    Process Identifier

### Process_CheckIsPriorityValid { #Process_CheckIsPriorityValid }

Checks if the priority has a valid value for an existing process

*Inputs*

ProcessId
:   Type: mandatory, Process Identifier.  
    Process Identifier

ProcessDefinitionPriorityId
:   Type: mandatory, ProcessDefinitionPriority Identifier.  
    Priority Definition Identifier

*Outputs*

IsValid
:   Type: Boolean.  
    If priority is associated with process

### Process_GetIdByActivityId { #Process_GetIdByActivityId }

Gets the process identifier for an existing activity

*Inputs*

ActivityId
:   Type: mandatory, Activity Identifier.  
    Gets the process identifier associated to an existing activity

*Outputs*

ProcessId
:   Type: Process Identifier.  
    

### Process_ResumeSuspendedFromImpactAnalysis { #Process_ResumeSuspendedFromImpactAnalysis }

Will try to resume the processes that were suspended due Impact Analysis after a deployment

*Inputs*

ProcessDefinitionId
:   Type: mandatory, Process_Definition Identifier.  
    ProcessDefinitionId

### Process_SetCalendar { #Process_SetCalendar }

Enables to modify the calendar of an existing process

*Inputs*

ProcessId
:   Type: mandatory, Process Identifier.  
    Identifier

CalendarId
:   Type: optional, Calendar Identifier.  
    Calendar Identifier

### Process_SetDueDate { #Process_SetDueDate }

Sets the due date and time for an existing process

*Inputs*

ProcessId
:   Type: mandatory, Process Identifier.  
    Process Identifier

DueDatetime
:   Type: mandatory, Date Time.  
    Due date and time

SetEvent
:   Type: optional, Boolean.  
    If True, an event will be triggered when the activity exceeds the SLA to perform specific tasks (ex: send an email).

### ProcessEvent_Set { #ProcessEvent_Set }

Creates a process event

*Inputs*

ProcessEventCreateRec
:   Type: mandatory, [ProcessEvent_Create](<#Structure_ProcessEvent_Create>).  
    Process Event Record

### Purge_AllCases { #Purge_AllCases }

Will purge all cases that are closed and meet the conditions to be purged.  
The purge will be asynchronous.

### Purge_CaseId { #Purge_CaseId }

Purges a specific case Id, if already closed.

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    

### Rule_ExecuteActivityConditon { #Rule_ExecuteActivityConditon }

Exceutes a rule associated to an activity to return a customized output  (as Text)  
To identify the rule, use RuleId or RuleName/CaseDefinitionId.

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

RuleId
:   Type: mandatory, Rule Identifier.  
    Rule Id

*Outputs*

ActivityActionOutput
:   Type: [ActivityActionOutput_View](<#Structure_ActivityActionOutput_View>).  
    Returned action

### Rule_ExecuteCustom { #Rule_ExecuteCustom }

Exceutes a rule associated to an object/activity to return a customized output  (as Text)  
To identify the rule, use RuleId or RuleName/CaseDefinitionId.

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

RuleId
:   Type: mandatory, Rule Identifier.  
    Rule Id

*Outputs*

Value
:   Type: Text.  
    Returned custom data value

### Rule_ExecuteGroup { #Rule_ExecuteGroup }

Exceutes a rule associated to an object/activity to return a specific group identifier.  
To identify the rule, use RuleId or RuleName/CaseDefinitionId.

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

RuleId
:   Type: mandatory, Rule Identifier.  
    Rule Id

*Outputs*

GroupId
:   Type: Group Identifier.  
    Evaluated Group Id

### Rule_ExecuteLogic { #Rule_ExecuteLogic }

Exceutes a rule associated to an object/activity to return true if the rule is applicable and valid, false otherwise.  
To identify the rule, use RuleId or RuleName/CaseDefinitionId.

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

RuleId
:   Type: mandatory, Rule Identifier.  
    Ruke Id

*Outputs*

IsValid
:   Type: Boolean.  
    True if rule is valid, false otherwise

### Rule_ExecuteStatus { #Rule_ExecuteStatus }

Exceutes a rule associated to an object/activity to return a list of existing status (one or more).  
To identify the rule, use RuleId or RuleName/CaseDefinitionId.

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

RuleId
:   Type: mandatory, Rule Identifier.  
    Rule Id

*Outputs*

CaseStatusList
:   Type: CaseStatus Identifier List.  
    StatusId  List

### Rule_ExecuteUser { #Rule_ExecuteUser }

Exceutes a rule associated to an object/activity to return a specific user identifier.  
To identify the rule, use RuleId or RuleName/CaseDefinitionId.

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

RuleId
:   Type: mandatory, Rule Identifier.  
    Rule Id

*Outputs*

UserId
:   Type: User Identifier.  
    User Id

### SampleUser_GetList { #SampleUser_GetList }

Retrieves the list of sample users

*Inputs*

CaseDefinitionId
:   Type: mandatory, CaseDefinition Identifier.  
    Case Definition Id

*Outputs*

IsDevelopment
:   Type: Boolean.  
    Yes if environment purpose is development

ListSampleUsers
:   Type: [SampleUser](<#Structure_SampleUser>) List.  
    List Sample Users for the Case Definition given

### SampleUser_Login { #SampleUser_Login }

Login for sample users

*Inputs*

UserId
:   Type: mandatory, User Identifier.  
    

CaseDefinitionId
:   Type: mandatory, CaseDefinition Identifier.  
    

### Timezone_ConvertFromServerTime { #Timezone_ConvertFromServerTime }

Converts a server's timezone DateTime to a specific timezone.

*Inputs*

TimezoneId
:   Type: mandatory, Timezone Identifier.  
    Timezone Id of the DateTime output

DateTimeToConvert
:   Type: mandatory, Date Time.  
    DateTime to convert.

*Outputs*

TimezoneDateTime
:   Type: Date Time.  
    DateTime converted to the specified timezone

### Timezone_ConvertToServerTime { #Timezone_ConvertToServerTime }

Converts a specific timezone DateTime to the server's timezone.

*Inputs*

TimezoneId
:   Type: mandatory, Timezone Identifier.  
    Timezone Id of the DateTime input

DateTimeToConvert
:   Type: mandatory, Date Time.  
    DateTime to convert.

*Outputs*

ServerDateTime
:   Type: Date Time.  
    DateTime converted to server's timezone

### User_GetIdByUsername { #User_GetIdByUsername }

Gets the user identifier from the username.

*Inputs*

Username
:   Type: mandatory, Text.  
    User username

*Outputs*

UserId
:   Type: User Identifier.  
    User Identifier

### UserExtended_GetById { #UserExtended_GetById }

Gets an user extended details

*Inputs*

UserId
:   Type: mandatory, User Identifier.  
    UserId

*Outputs*

UserDetail
:   Type: [UserExtended_Details](<#Structure_UserExtended_Details>).  
    User detail


## Service Actions

### Activity_GetActionList { #Service_Activity_GetActionList }

Returns the list of available actions for an existing activity based on its current details

*Inputs*

ActivityId
:   Type: mandatory, Activity Identifier.  
    

UserId
:   Type: mandatory, User Identifier.  
    User Identifier

ExcludeActivityActionIds
:   Type: optional, ActivityAction Identifier List.  
    ActivitiesActions to exclude

*Outputs*

ActivityActionDetailsList
:   Type: [ActivityAction_Details](<#Structure_ActivityAction_Details>) List.  
    List of activity actions

### Activity_GetExtraFieldValue { #Service_Activity_GetExtraFieldValue }

Gets the actual value of an extra field for a specific activity

*Inputs*

ActivityExtraFieldId
:   Type: mandatory, ActivityExtraField Identifier.  
    ActivityExtraField Identifier

ActivityId
:   Type: mandatory, Activity Identifier.  
    Activity Identifier

ReturnKeyLabel
:   Type: optional, Boolean.  
    If true, the label/name of target entity will be returned instead of the value itself.

*Outputs*

ExtraFieldValue
:   Type: [ExtraFieldValue](<#Structure_ExtraFieldValue>).  
    Extra Field Value

### Case_GetActivities { #Service_Case_GetActivities }

Gets all activities that match the provided scope and search criteria

*Inputs*

ActivityScope
:   Type: mandatory, [ActivityScope](<#Structure_ActivityScope>).  
    Defines how Activities are filtered by who the activity is assigned to, its assignment type and its progress.

SearchCriteria
:   Type: optional, [SearchCriteria](<#Structure_SearchCriteria>).  
    Defines how the Activities are filtered base on their attributes.

SortFieldList
:   Type: optional, [ActivitySort](<#Structure_ActivitySort>) List.  
    Defines how the Activities are sorted.

IncludeCounters
:   Type: optional, Boolean.  
    If set to True will display the counters for the different activity progress statuses (ToDo, InProgress, Active, Done, All)

PageNumber
:   Type: optional, Integer.  
    Page number

MaxResultsPerPage
:   Type: optional, Integer.  
    Number of results per page

*Outputs*

ActivityResults
:   Type: [ActivityResult](<#Structure_ActivityResult>) List.  
    Activities that matched the provided scope and search criteria

TotalResults
:   Type: Integer.  
    Number of activities that matched the provided scope and search criteria

ActivityCounters
:   Type: [ActivityCounter](<#Structure_ActivityCounter>) List.  
    List of activity counters for each progress status

### Case_GetActivitiesTimeline { #Service_Case_GetActivitiesTimeline }

Gets the list of completed and ongoing activities for a given case

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    

*Outputs*

ActivityTimelineList
:   Type: [HumanActivityTimelineDetails](<#Structure_HumanActivityTimelineDetails>) List.  
    

### Case_GetActivityCounters { #Service_Case_GetActivityCounters }

Gets the counters for each activity progress status that match the provided scope and search criteria

*Inputs*

ActivityScope
:   Type: optional, [ActivityScopeCounters](<#Structure_ActivityScopeCounters>).  
    Defines how Activities are filtered by who the activity is assigned to and the assignment status.

SearchCriteria
:   Type: optional, [SearchCriteria](<#Structure_SearchCriteria>).  
    Defines how the Activities are filtered base on their attributes.

*Outputs*

ActivityCounterList
:   Type: [ActivityCounter](<#Structure_ActivityCounter>) List.  
    List of activity counters for each progress status

### Case_GetAllByExternalRequester { #Service_Case_GetAllByExternalRequester }

Gets all the Case instances requested by the specified external requester details

*Inputs*

ExternalRequesterDetails
:   Type: mandatory, [CaseExternalRequest_Details](<#Structure_CaseExternalRequest_Details>).  
    External Requester Details

*Outputs*

CaseDetailsList
:   Type: [CaseDetails](<#Structure_CaseDetails>) List.  
    List of Case Details

### Case_GetAllHistoryByIdAndDate { #Service_Case_GetAllHistoryByIdAndDate }

Get the list of all case operations associated to an existing case instance

*Inputs*

FilterHistoryResults
:   Type: mandatory, [FilterHistoryResults](<#Structure_FilterHistoryResults>).  
    Filter History Results

OrderHistoryResult
:   Type: optional, [OrderHistoryResult](<#Structure_OrderHistoryResult>) List.  
    Orders history result by fields

SearchDate
:   Type: mandatory, Date.  
    Date to search

*Outputs*

CaseHistoryList
:   Type: [Case_Information](<#Structure_Case_Information>) List.  
    List of operations associated to a case

TotalResults
:   Type: Long Integer.  
    Number of records

### Case_GetAllPossibleStatus { #Service_Case_GetAllPossibleStatus }

Gets the list of valid status for a given case, based on the current case status and on the defined state machine (otherwise no status will be returned)

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

*Outputs*

CaseStatusDetailsList
:   Type: [CaseStatus_Details](<#Structure_CaseStatus_Details>) List.  
    List of status details

### Case_GetAllStatus { #Service_Case_GetAllStatus }

Gets the list of all active status for a given case

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

*Outputs*

CaseStatusDetailsList
:   Type: [CaseStatus_Details](<#Structure_CaseStatus_Details>) List.  
    List of status details

### Case_GetAllSubcases { #Service_Case_GetAllSubcases }

Gets the list of all child cases for a given parent case

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Parent Case Identifier

*Outputs*

CaseDetailsList
:   Type: [Case_Details](<#Structure_Case_Details>) List.  
    List of Subcases details

### Case_GetAllTags { #Service_Case_GetAllTags }

Gets all the tags associated to a specific case instance

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case identifier

*Outputs*

TagsList
:   Type: [TagDetails](<#Structure_TagDetails>) List.  
    List of tags

### Case_GetByTagId { #Service_Case_GetByTagId }

Gets the list of case details that have matching tags with the input tag id list (exact match)

*Inputs*

TagIdList
:   Type: mandatory, [TagIdentifier](<#Structure_TagIdentifier>) List.  
    Tag Identifier List

*Outputs*

CaseDetailsList
:   Type: [CaseDetails_Lite](<#Structure_CaseDetails_Lite>) List.  
    List of case identifier and case number that match the input tag criteria

### Case_GetByTagLabel { #Service_Case_GetByTagLabel }

Gets the list of case details that have matching tags with the input tag label (partial match)

*Inputs*

Label
:   Type: mandatory, Text.  
    Tag label

*Outputs*

CaseDetailsList
:   Type: [CaseDetails_Lite](<#Structure_CaseDetails_Lite>) List.  
    List Case identifier and number that match the input criteria

### Case_GetCases { #Service_Case_GetCases }

Gets all cases that meet the filter criteria

*Inputs*

CaseScope
:   Type: mandatory, [CaseScope](<#Structure_CaseScope>).  
    Filter Results

CaseSearchCriteria
:   Type: optional, [CaseSearchCriteria](<#Structure_CaseSearchCriteria>).  
    Possible Case filters. Note: the result of mixing values for filters of different types works as an &quot;AND&quot; and inside filters of the same type as an &quot;OR&quot;, for the list of cases to return.

SortFieldList
:   Type: optional, [CaseSort](<#Structure_CaseSort>) List.  
    

IncludeCounters
:   Type: optional, Boolean.  
    If set to True will display the counters for the different CaseStateFilter criteria (Active, Closed, All)

PageNumber
:   Type: optional, Integer.  
    Page number

MaxResultsPerPage
:   Type: optional, Integer.  
    Number of results per page

*Outputs*

CaseResults
:   Type: [Search_CaseDetails](<#Structure_Search_CaseDetails>) List.  
    Contains the details for each case

TotalResults
:   Type: Long Integer.  
    

CaseCounters
:   Type: [CaseCounter](<#Structure_CaseCounter>) List.  
    Case State Counters List (will only return results if the IncludeCounters input parameter is set to True)

### Case_GetCasesByActivity { #Service_Case_GetCasesByActivity }

Gets all cases that meet the filter criteria based on their activities

*Inputs*

CaseActivityScope
:   Type: mandatory, [CaseActivityScope](<#Structure_CaseActivityScope>).  
    Input parameter with the structure that defines how Cases are filtered by Activities

SearchCriteria
:   Type: optional, [SearchCriteria](<#Structure_SearchCriteria>).  
    Defines how the Cases and Activities are filtered base on their attributes.

SortFieldList
:   Type: optional, [CaseSort](<#Structure_CaseSort>) List.  
    

IncludeCounters
:   Type: optional, Boolean.  
    If set to True will display the counters for the different CaseStateFilter criteria (Active, Closed, All)

PageNumber
:   Type: optional, Integer.  
    Page number

MaxResultsPerPage
:   Type: optional, Integer.  
    Number of results per page

*Outputs*

CaseResults
:   Type: [Search_CaseDetails](<#Structure_Search_CaseDetails>) List.  
    Contains the details for each case

TotalResults
:   Type: Long Integer.  
    

CaseCounters
:   Type: [CaseCounter](<#Structure_CaseCounter>) List.  
    Case State Counters List (will only return results if the IncludeCounters input parameter is set to True)

### Case_GetCasesByActivityCounters { #Service_Case_GetCasesByActivityCounters }

Gets the Case state counters (Active, Closed, All) for the selected filters

*Inputs*

CaseActivityScope
:   Type: mandatory, [CaseActivityScope](<#Structure_CaseActivityScope>).  
    Input parameter with the structure that defines how Cases are filtered by Activities

SearchCriteria
:   Type: optional, [SearchCriteria](<#Structure_SearchCriteria>).  
    Defines how the Activities are filtered base on their attributes.

*Outputs*

CaseRequestCounts
:   Type: [CaseCounter](<#Structure_CaseCounter>) List.  
    Case Requests Count List

### Case_GetCounters { #Service_Case_GetCounters }

Gets the Case state counters (Active, Closed, All) for the selected filters

*Inputs*

RequesterScopeId
:   Type: optional, RequesterScope Identifier.  
    Input parameter with the structure that defines how Cases are filtered by Requester Scope and Case State  
    Indicates which cases will be returned based on the Requester field, where by default, the logged in user's cases are returned.

CaseSearchCriteria
:   Type: optional, [CaseSearchCriteria](<#Structure_CaseSearchCriteria>).  
    Possible Case filters. Note: the result of mixing values for filters of different types works as an &quot;AND&quot; and inside filters of the same type as an &quot;OR&quot;, for the list of cases to return.

*Outputs*

CaseRequestCounts
:   Type: [CaseCounter](<#Structure_CaseCounter>) List.  
    Case Requests Count List

### Case_GetDefinitionDetails { #Service_Case_GetDefinitionDetails }

Gets information about activity statistics for a Case Definition

*Inputs*

CaseDefinitionId
:   Type: mandatory, CaseDefinition Identifier.  
    CaseDefinition Id

*Outputs*

Case_DefinitionDetails
:   Type: [Case_DefinitionDetails](<#Structure_Case_DefinitionDetails>).  
    Case Definition Details

### Case_GetDetailsByCaseId { #Service_Case_GetDetailsByCaseId }

Gets details for an exisiting case identifier

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

*Outputs*

CaseDetails
:   Type: [Case_Details](<#Structure_Case_Details>).  
    Case Details

### Case_GetExtraFieldValue { #Service_Case_GetExtraFieldValue }

Gets the actual value of an extra field for a specific case

*Inputs*

CaseExtraFieldId
:   Type: mandatory, CaseExtraField Identifier.  
    ExtraField Identifier

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

ReturnKeyLabel
:   Type: optional, Boolean.  
    If true, the label/name of target entity will be returned instead of the value itself.

*Outputs*

ExtraFieldValue
:   Type: [ExtraFieldValue](<#Structure_ExtraFieldValue>).  
    Extra Field Value

### Case_GetGroupsUsersWithAccess { #Service_Case_GetGroupsUsersWithAccess }

Gets all Users and Groups that have access to this Case instance

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Instance Identifier.

EvaluateUsersByGroup
:   Type: optional, Boolean.  
    If true, will also return the users that have access through associated group(s)

OnlyCanEdit
:   Type: optional, Boolean.  
    If true, only write Access Control permissions are returned

*Outputs*

UsersList
:   Type: [User_Details](<#Structure_User_Details>) List.  
    List of Users that have access

GroupDetailsList
:   Type: [CaseAccessControl_GroupDetails](<#Structure_CaseAccessControl_GroupDetails>) List.  
    List of Groups that have access

### Case_GetHistory { #Service_Case_GetHistory }

Get the list of all case operations associated to an existing case instance

*Inputs*

FilterHistoryResults
:   Type: mandatory, [FilterHistoryResults](<#Structure_FilterHistoryResults>).  
    Filter History Results

OrderByAscending
:   Type: optional, Boolean.  
    Orders the history events by ascending execution order. Default is descending order.

*Outputs*

CaseHistoryList
:   Type: [Case_Information](<#Structure_Case_Information>) List.  
    List of operations associated to a case

TotalResults
:   Type: Long Integer.  
    Number of records

### Case_GetMilestones { #Service_Case_GetMilestones }

Gets the details of the Milestones associated with a given Case

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    

*Outputs*

MilestoneDetails
:   Type: [MilestoneDetails](<#Structure_MilestoneDetails>) List.  
    

### Case_GetStatusTimeline { #Service_Case_GetStatusTimeline }

Gets the status timeline (past and current) for a given case

*Inputs*

CaseId
:   Type: mandatory, Case Identifier.  
    Case Identifier

*Outputs*

StatusDetailsList
:   Type: [StatusDetails](<#Structure_StatusDetails>) List.  
    List of Status Details

### DEPRECATED_Case_GetActivities { #Service_DEPRECATED_Case_GetActivities }

Gets all activities associated with cases

*Inputs*

FilterResults
:   Type: mandatory, [CaseActivities_FilterResults](<#Structure_CaseActivities_FilterResults>).  
    Filter Results

*Outputs*

CaseActivityViewList
:   Type: [CaseActivity_View](<#Structure_CaseActivity_View>) List.  
    Contains the details for each case and associated activity

TotalResults
:   Type: Long Integer.  
    Number of total activities that match the criteiria

CaseActivityCounts
:   Type: [Case_ActivityCount](<#Structure_Case_ActivityCount>) List.  
    Case Activity Count List

### DEPRECATED_Case_GetActivitiesByCaseId { #Service_DEPRECATED_Case_GetActivitiesByCaseId }

Gets all activities associated with specific cases

*Inputs*

FilterResults
:   Type: mandatory, [CaseActivities_FilterResults](<#Structure_CaseActivities_FilterResults>).  
    Filter Results

CaseIdentifierList
:   Type: mandatory, [Case_Identifier](<#Structure_Case_Identifier>) List.  
    List of case identifier

*Outputs*

CaseActivityViewList
:   Type: [CaseActivity_View](<#Structure_CaseActivity_View>) List.  
    Contains the details for each case and associated activity

### DEPRECATED_Case_GetActivityCounters { #Service_DEPRECATED_Case_GetActivityCounters }

Get activities count by each activity filter type

*Inputs*

CaseDefinitionId
:   Type: mandatory, CaseDefinition Identifier.  
    CaseDefinition Id.  
    Set to Null to get all.

AnonymousCriteriaId
:   Type: optional, AnonymousCriteria Identifier.  
    Anonymous Criteria filter

IsReturnAll
:   Type: optional, Boolean.  
    If true, will return all activities (to be used by admin users for instance)

RequesterUserId
:   Type: optional, User Identifier.  
    To have in mind only tasks regarding this given requester

*Outputs*

CaseActivityCounts
:   Type: [Case_ActivityCount](<#Structure_Case_ActivityCount>) List.  
    Case Activity Count List

### DEPRECATED_Case_GetCases { #Service_DEPRECATED_Case_GetCases }

Gets all cases that meets the filter criterias

*Inputs*

FilterResults
:   Type: mandatory, [Case_FilterResults](<#Structure_Case_FilterResults>).  
    Filter Results

*Outputs*

CaseRequestViewList
:   Type: [CaseRequest_View](<#Structure_CaseRequest_View>) List.  
    Contains the details for each case

TotalResults
:   Type: Long Integer.  
    Number of total cases that match the filter

CaseRequestCounts
:   Type: [Case_RequestCount](<#Structure_Case_RequestCount>) List.  
    Case Requests Count List

### DEPRECATED_Case_GetCasesCounters { #Service_DEPRECATED_Case_GetCasesCounters }

Get requests (Case) count by each case filter type

*Inputs*

CaseDefinitionId
:   Type: optional, CaseDefinition Identifier.  
    CaseDefinition Id

AnonymousCriteriaId
:   Type: optional, AnonymousCriteria Identifier.  
    Anonymous Criteria filter

IsReturnAll
:   Type: optional, Boolean.  
    If true, will return all activities (to be used by admin users for instance)

RequesterUserId
:   Type: optional, User Identifier.  
    To have in mind only cases regarding this given requester

*Outputs*

CaseRequestCounts
:   Type: [Case_RequestCount](<#Structure_Case_RequestCount>) List.  
    Case Requests Count List

### Tag_GetAllByLabel { #Service_Tag_GetAllByLabel }

Gets all Tags for a given Case Definition that match the specified label. If no label is specified all tags are returned up to the MaxResults input parameter value

*Inputs*

CaseDefinitionId
:   Type: mandatory, CaseDefinition Identifier.  
    Case Definition Identifier

TagLabel
:   Type: optional, Text.  
    Tag Label

IncludeGlobalTags
:   Type: optional, Boolean.  
    If True global tags (tags no associated with a specific case definition) will be returned as well.

MaxResults
:   Type: optional, Integer.  
    Max number of returned results

*Outputs*

TagList
:   Type: [TagDetails](<#Structure_TagDetails>) List.  
    List with Tag details that match the input criteria


## Structures

### Activity_AssignDetails { #Structure_Activity_AssignDetails }

Details about activity assignment details

*Attributes*

ActivityUserId
:   Type: User Identifier.  
    User Identifier

ActivityGroupId
:   Type: Group Identifier.  
    Group Identifier

ActivityStatusId
:   Type: Activity_Status Identifier.  
    Activity Status

ActivityOpenDate
:   Type: Date Time.  
    Acitivty open date

ActivityIsBlocked
:   Type: Boolean.  
    If the activity is blocked

ProcessIsBlocked
:   Type: Boolean.  
    If the Process is blocked

### Activity_CaseView { #Structure_Activity_CaseView }

For specific case, holds the activity view details

*Attributes*

Activity_Details
:   Type: [Activity_Details](<#Structure_Activity_Details>).  
    Activity Detail

ActivityAction_DetaislList
:   Type: [ActivityAction_Details](<#Structure_ActivityAction_Details>) List.  
    List of possible activity actions

User_Details
:   Type: [User_Details](<#Structure_User_Details>).  
    User details

Group_Details
:   Type: [Group_Details](<#Structure_Group_Details>).  
    Group details

Delegation_Details
:   Type: [User_Details](<#Structure_User_Details>).  
    Delegation details (if applicable)

### Activity_Details { #Structure_Activity_Details }

Activity details

*Attributes*

ActivityId
:   Type: Activity Identifier.  
    

Name
:   Type: Text (100).  
    Activity Name

ActivityStatusId
:   Type: Activity_Status Identifier.  
    Activity Status Identifier

IsBlocked
:   Type: Boolean.  
    If activity is blocked

CreatedOn
:   Type: Date Time.  
    Creation On

OpenedOn
:   Type: Date Time.  
    Opened On

ClosedOn
:   Type: Date Time.  
    Closed On

LastModifiedOn
:   Type: Date Time.  
    Last Modified Date

DueDatetime
:   Type: Date Time.  
    Activity Due Date

HasDelegation
:   Type: Boolean.  
    If the user has access to the activity under delegation

HasOpenAccess
:   Type: Boolean.  
    True if the user has access to open the activity

ActivityActionId
:   Type: ActivityAction Identifier.  
    Activity Action Identifier

StartExecutionDate
:   Type: Date Time.  
    Start date and time for the Activity SLA

DueDate
:   Type: Date Time.  
    Due Date for the Activity

ExecutionTimeInMinutes
:   Type: Long Integer.  
    Activity duration in minutes (if exists a SLA associated, takes the calendar into account if applicable)

IsResponseTimeExceeded
:   Type: Boolean.  
    If the SLA response time was exceeded

ActivityDefinitionId
:   Type: Activity_Definition Identifier.  
    Activity Definition Id

ActivityDefinitionSSKey
:   Type: Text.  
    Activity Definition SS Key

PreviousActivityId
:   Type: Activity Identifier.  
    PreviousActivityId executed in the flow

ClosedStatusId
:   Type: CaseStatus Identifier.  
    Case Status Id after the close of the activity

ClosedStatusName
:   Type: Text (50).  
    Case Status Name after the close of the activity

ClosedActionId
:   Type: CaseAction Identifier.  
    Case Action Id that triggered the activity to close

ClosedActionName
:   Type: Text (50).  
    Case Action Name that triggered the activity to close

### Activity_Details2 { #Structure_Activity_Details2 }

Holds information for a case activity details

*Attributes*

ActivityId
:   Type: Activity Identifier.  
    Activity Id

ActivityName
:   Type: Text.  
    Activity Name

ActivityNameLang
:   Type: Text.  
    Activity Name translated to the currently set locale

ActivitySSKey
:   Type: Text (36).  
    Activity SS Key

GroupId
:   Type: Group Identifier.  
    Group Id

GroupName
:   Type: Text.  
    Group Name

UserId
:   Type: User Identifier.  
    User Identifier

UserName
:   Type: Text.  
    Name of the user

PreviousActivityId
:   Type: Activity Identifier.  
    PreviousActivityId executed in the flow

SLADetails
:   Type: [SLA_Details](<#Structure_SLA_Details>).  
    SLA Details

### ActivityAction_Details { #Structure_ActivityAction_Details }

Activity Action Detail

*Attributes*

ActivityActionId
:   Type: ActivityAction Identifier.  
    Activity Action Identifier

Description
:   Type: Text.  
    Descritpion

### ActivityActionOutput_View { #Structure_ActivityActionOutput_View }

Structure that a represents output action condition from a condition activity from the builder

*Attributes*

ActionId
:   Type: Text.  
    Action Id

Name
:   Type: Text.  
    Action name

StatusId
:   Type: Text.  
    Status

NextActivityId
:   Type: Text.  
    Next Activity Id

### ActivityCounter { #Structure_ActivityCounter }

Counter for a specific activity progress status

*Attributes*

ActivityProgressStatusId
:   Type: ActivityProgressStatus Identifier.  
    Activity Progress Status Identifier

Label
:   Type: Text.  
    Label

Count
:   Type: Integer.  
    Number of activities

Order
:   Type: Integer.  
    Order

### ActivityDetails { #Structure_ActivityDetails }



*Attributes*

IsBlocked
:   Type: Boolean.  
    If activity is blocked

CreatedOn
:   Type: Date Time.  
    Creation On

OpenedOn
:   Type: Date Time.  
    Opened On

ClosedOn
:   Type: Date Time.  
    Closed On

LastModifiedOn
:   Type: Date Time.  
    Last Modified Date

DueDate
:   Type: Date Time.  
    Activity Due Date

StartExecutionDate
:   Type: Date Time.  
    Start date and time for the Activity SLA

ExecutionTimeInMinutes
:   Type: Long Integer.  
    Activity duration in minutes (if exists a SLA associated, takes the calendar into account if applicable)

IsResponseTimeExceeded
:   Type: Boolean.  
    If the SLA response time was exceeded

ProcessId
:   Type: Process Identifier.  
    

ActivityDefinitionId
:   Type: Activity_Definition Identifier.  
    Activity Definition Id

ActivityDefinitionSSKey
:   Type: Text.  
    Activity Definition SS Key

PreviousActivityId
:   Type: Activity Identifier.  
    PreviousActivityId executed in the flow

ClosedActionId
:   Type: CaseAction Identifier.  
    Case Action Id that triggered the activity to close

ClosedActionName
:   Type: Text (50).  
    Case Action Name that triggered the activity to close

ClosedActionNameLang
:   Type: Text (50).  
    Case Action Name Lang that triggered the activity to close

ClosedStatusId
:   Type: CaseStatus Identifier.  
    Case Status Id associated with the activity to close

ClosedStatusName
:   Type: Text (50).  
    Case Status Name associated with the activity to close

ClosedStatusNameLang
:   Type: Text (50).  
    Case Status Name Lang associated with the activity to close

### ActivityDueDate { #Structure_ActivityDueDate }

Structure that defines the considered time range of an Activity due date

*Attributes*

FromDate
:   Type: Date Time.  
    From Date

ToDate
:   Type: Date Time.  
    To Date

### ActivityEvent_Create { #Structure_ActivityEvent_Create }

Public structure to create a new activity event

*Attributes*

ActivityId
:   Type: Activity Identifier.  
    Activity Identifier

ActivityEventTypeId
:   Type: ActivityEventType Identifier.  
    Activity Event Type

EventOn
:   Type: Date Time.  
    Date and time for the event

### ActivityHistory { #Structure_ActivityHistory }



*Attributes*

ActivityId
:   Type: Activity Identifier.  
    Activity identifier

ActivityName
:   Type: Text.  
    Name of the activity

ClosedOn
:   Type: Date Time.  
    The date the activity was closed

FirstUserAssignedOn
:   Type: Date Time.  
    The date when the first user was assigned to the activity

CurrentAssignmentDate
:   Type: Date Time.  
    The date when the current responsible for the activity (user or group) was assigned to it. If a user was not assigned yet, the date corresponds to the assignment of the responsible group.

### ActivityResult { #Structure_ActivityResult }



*Attributes*

ActivityId
:   Type: Activity Identifier.  
    

ActivityLabel
:   Type: Text.  
    

ActivityLabelLang
:   Type: Text.  
    

ActivityStatusId
:   Type: Activity_Status Identifier.  
    

ActivityDetails
:   Type: [ActivityDetails](<#Structure_ActivityDetails>).  
    

AssignedUserDetails
:   Type: [User_Details](<#Structure_User_Details>).  
    

AssignedGroupDetails
:   Type: [Group_Details](<#Structure_Group_Details>).  
    

CaseDetails
:   Type: [Search_CaseDetails](<#Structure_Search_CaseDetails>).  
    

### ActivityScope { #Structure_ActivityScope }



*Attributes*

ActivityAssigneeTypeId
:   Type: ActivityAssigneeType Identifier.  
    Indicates which activities will be returned based on the type of assignee. To use this filter add the &quot;ActivityAssigneeType&quot; static entity from the &quot;CM_CaseServices_BL&quot; module as a dependency.  
    Options:  
    -MyActivities: will return the activities that the currently logged in user can work on.  
    1. Activities assigned to the currently logged in user.  
    2. Activities that are assigned to a group that the currently logged in user belongs to.  
    3. Activities that have neither a user nor a group assigned to them.  
    -All: will return all activities regardless of the currently logged in user.

ActivityAssignmentStatusId
:   Type: ActivityAssignmentStatus Identifier.  
    Indicates which activities will be returned based on their assignment status. To use this filter add the &quot;ActivityAssignmentStatus&quot; static entity from the &quot;CM_CaseServices_BL&quot; module as a dependency.  
    Options:  
    -AssignedToAnyone: will return the activities that have a user assigned to them.  
    -AssignedToMe: will return the activities that are assigned to the currently logged in user.  
    -AssignedToOthers: will return the activities that are assigned to a user that is not the currently logged in user.  
    -Unassigned: will return the activities that do not have a user assigned to them.  
    -All: will return all activities regardless of having a user assigned to them or not.

ActivityProgressStatusId
:   Type: ActivityProgressStatus Identifier.  
    Indicates which activities will be returned based on their progress status. To use this filter add the &quot;ActivityProgressStatus&quot; static entity from the &quot;CM_CaseServices_BL&quot; module as a dependency.  
    Options:  
    -ToDo: will return the activities that have not been opened.  
    -InProgress: will return the activities that have been opened by their assignee.  
    -Active: will return the activities that fall under the &quot;ToDo&quot; or &quot;InProgress&quot; options.  
    -Done: will return the activities that have been closed.  
    -All: will return all activities regardless of their progress status.

### ActivityScopeCounters { #Structure_ActivityScopeCounters }



*Attributes*

ActivityAssigneeTypeId
:   Type: ActivityAssigneeType Identifier.  
    Indicates which activities will be returned based on the type of assignee. To use this filter add the &quot;ActivityAssigneeType&quot; static entity from the &quot;CM_CaseServices_BL&quot; module as a dependency.  
    Options:  
    -MyActivities: will return the activities that the currently logged in user can work on.  
    1. Activities assigned to the currently logged in user.  
    2. Activities assigned to a group the currently logged in user belongs to.  
    3. Activities that have neither a user nor a group assigned to them.  
    -All: will return all activities regardless of the currently logged in user.

ActivityAssignmentStatusId
:   Type: ActivityAssignmentStatus Identifier.  
    Indicates which activities will be returned based on their assignment status. To use this filter add the &quot;ActivityAssignmentStatus&quot; static entity from the &quot;CM_CaseServices_BL&quot; module as a dependency.  
    Options:  
    -Assigned: will return the activities that currently have a user assigned to them.  
    -Unassigned: will return the activities that currently do not have a user assigned to them.  
    -All: will return all activities regardless of having a user assigned to them or not.

### ActivitySearchCriteria { #Structure_ActivitySearchCriteria }

Input parameter with Activity filters. When values for different filter criteria types are sent, returned activities will match all filters (&quot;AND&quot; condition). Inside each criteria attribute list, the returned cases will match at least one of those values (&quot;OR&quot; condition).

*Attributes*

AssignedUserIdList
:   Type: [User Identifier](<#Structure_User Identifier>) List.  
    List of Assigned User identifiers

AssignedGroupIdList
:   Type: [Group Identifier](<#Structure_Group Identifier>) List.  
    List of Assigned Group identifiers

ExcludeUnassignedGroupAndUser
:   Type: Boolean.  
    If True, activities without group and user assigned to them will be excluded. Included otherwise.

IncludeDelegations
:   Type: Boolean.  
    True if Activities delegated are included. False if only assigned to the User/Group are included. False by default.

DueDate
:   Type: [ActivityDueDate](<#Structure_ActivityDueDate>).  
    Structure that defines the considered time range of an Activity due date

### ActivitySort { #Structure_ActivitySort }

Activity fields to sort for

*Attributes*

ActivitySortFieldTypeId
:   Type: ActivitySortFieldType Identifier.  
    Activity Field Sort Type. To use this filter add the &quot;ActivitySortFieldType&quot; static entity from the &quot;CM_CaseServices_BL&quot; module as a dependency.

Ascending
:   Type: Boolean.  
    If true, order by ASC. If false order by DESC

### Calendar_Detail { #Structure_Calendar_Detail }

Public structure with the calendar deailts

*Attributes*

Id
:   Type: Calendar Identifier.  
    Identifier

Name
:   Type: Text (50).  
    Description

Description
:   Type: Text (200).  
    Description

WorkingHourStart
:   Type: Time.  
    Working Hour Start

WorkingHourEnd
:   Type: Time.  
    Working Hour Start

TimezoneId
:   Type: Timezone Identifier.  
    Timezone identifier

IsActive
:   Type: Boolean.  
    If is active

Timezone
:   Type: [Timezone](<#Structure_Timezone>).  
    Timezone for calendar

HolidayDetailList
:   Type: [Holiday_Detail](<#Structure_Holiday_Detail>) List.  
    Holiday Detail List

NonWorkingDayDetailList
:   Type: [NonWorkingDay_Detail](<#Structure_NonWorkingDay_Detail>) List.  
    Non Working Day Detail List

### Calendar_FilterResults { #Structure_Calendar_FilterResults }

Generic Filter Serch Structure

*Attributes*

PageNumber
:   Type: Integer.  
    Page number

MaxResultsPerPage
:   Type: Integer.  
    Number of results per page

OnlyActive
:   Type: Boolean.  
    Filter only active

### Case_ActivityCount { #Structure_Case_ActivityCount }

Count of each activity filter type

*Attributes*

ActivityFilterCriteriaId
:   Type: ActivityFilterCriteria2 Identifier.  
    Activity Filter Criteria

Label
:   Type: Text.  
    Label

Count
:   Type: Integer.  
    Number of activities

Order
:   Type: Integer.  
    Order

### Case_DefinitionDetails { #Structure_Case_DefinitionDetails }

Holds activities statistics about a case definition

*Attributes*

CaseDefinitionId
:   Type: CaseDefinition Identifier.  
    Case Definition

AverageDuration
:   Type: Integer.  
    Average Duration in minutes for a request

AverageNumberOfActivities
:   Type: Integer.  
    Average number of activities that are executed in a request (not repeated for the same activity definition)

MaxNumberOfActivities
:   Type: Integer.  
    Max number of active activities definitions defined in the BPT for the CaseDefinition

ActivityList
:   Type: [CaseActivity_Details](<#Structure_CaseActivity_Details>) List.  
    List of activity statistics details

### Case_Details { #Structure_Case_Details }

Details for an existing case

*Attributes*

CaseId
:   Type: Case Identifier.  
    Case Identifier

CaseDefinitionId
:   Type: CaseDefinition Identifier.  
    Case Definition Identifier

CaseNumber
:   Type: Long Integer.  
    Case Number

CaseDefinitionName
:   Type: Text.  
    Case Definition Name

StatusId
:   Type: CaseStatus Identifier.  
    Status Identifier

StatusName
:   Type: Text.  
    Status name

PriorityId
:   Type: ProcessDefinitionPriority Identifier.  
    Priority identifier

PriorityName
:   Type: Text.  
    Priority Name

ProcessId
:   Type: Process Identifier.  
    Process associated with the status change (optional)

CreatedOn
:   Type: Date Time.  
    Execution date and time

LastUpdatedOn
:   Type: Date Time.  
    Last update date and time

CompletedOn
:   Type: Date Time.  
    Completion date and time

### Case_Details2 { #Structure_Case_Details2 }

Holds information for a case details

*Attributes*

CaseDefinitionId
:   Type: CaseDefinition Identifier.  
    Case Definition Identifier

StatusId
:   Type: CaseStatus Identifier.  
    Status Identifier

StatusName
:   Type: Text (100).  
    Status name

StatusNameLang
:   Type: Text (100).  
    Status name translated to the currently set locale

PriorityId
:   Type: ProcessDefinitionPriority Identifier.  
    Priority identifier

PriorityName
:   Type: Text (100).  
    Priority name

PreviousStatusId
:   Type: CaseStatus Identifier.  
    Previous Status Identifier

PreviousStatusName
:   Type: Text (100).  
    PreviousStatus name

PreviousStatusNameLang
:   Type: Text (100).  
    Previous Status name translated to the currently set locale

ActionId
:   Type: CaseAction Identifier.  
    Workflow Action Id

ActionName
:   Type: Text (50).  
    Action Name

ActionNameLang
:   Type: Text (50).  
    Action Name translated to the currently set locale

EventObjectId
:   Type: Text (36).  
    Event Object Id

EventDetails
:   Type: Text (50).  
    Event Details

ExecutionDetails
:   Type: [Case_ExecutionDetails](<#Structure_Case_ExecutionDetails>).  
    Execution Details

### Case_ExecutionDetails { #Structure_Case_ExecutionDetails }

Holds information for case sla details

*Attributes*

StartDate
:   Type: Date Time.  
    Start date and time for the Case

CompletedOn
:   Type: Date Time.  
    Completion date and time

CreatedBy
:   Type: User Identifier.  
    User identifier created case

CreatedName
:   Type: Text.  
    User creation name

### Case_FilterResults { #Structure_Case_FilterResults }

Case Filter Search Structure

*Attributes*

CaseFilterCriteriaId
:   Type: CaseFilterCriteria Identifier.  
    Case filter criteria

SearchFieldList
:   Type: [CaseSearchField](<#Structure_CaseSearchField>) List.  
    Search field list

SortFieldList
:   Type: [CaseSortField](<#Structure_CaseSortField>) List.  
    Sort field list

UserAssigneeCriteriaId
:   Type: UserAssigneeCriteria Identifier.  
    User assignee criteria that enables to filter the user assignee of an activity

AnonymousCriteriaId
:   Type: AnonymousCriteria Identifier.  
    Anonymous criteria enables to return activities that don't have user and group assigned.

IsReturnAll
:   Type: Boolean.  
    If true, will return all activities even if the user doesn't belong to the activity group or activity user assignee (to be used by administrator users for instance).

ExcludeActivityActionIds
:   Type: [ActivityAction Identifier](<#Structure_ActivityAction Identifier>) List.  
    Activity actions to be excluded

DelegatedBy
:   Type: User Identifier.  
    Fullfil to the call act and return activities that are delegated by that specified user.

OnlyCasesWithOpenActivities
:   Type: Boolean.  
    If true, will only return cases with open activities

CalculateOnlyCounters
:   Type: Boolean.  
    If true, only output counters will be fulfilled

PageNumber
:   Type: Integer.  
    Page number

MaxResultsPerPage
:   Type: Integer.  
    Number of results per page

### Case_Identifier { #Structure_Case_Identifier }

Case Identifier

*Attributes*

CaseId
:   Type: Case Identifier.  
    Case Identifier

### Case_Information { #Structure_Case_Information }

Case Information Details

*Attributes*

EventTypeId
:   Type: EventType Identifier.  
    EventType Id

EventName
:   Type: Text.  
    Event name

EventAssociationTypeId
:   Type: EventAssociationType2 Identifier.  
    Event Association Type

EventAssociationName
:   Type: Text.  
    Event Association name

Comments
:   Type: Text.  
    Comments

OperationOn
:   Type: Date Time.  
    Created On

UserDetails
:   Type: [User_Details](<#Structure_User_Details>).  
    User details

DelegationDetails
:   Type: [User_Details](<#Structure_User_Details>).  
    Delegation user details

CaseDetails
:   Type: [Case_Details2](<#Structure_Case_Details2>).  
    Case information

ActivityDetails
:   Type: [Activity_Details2](<#Structure_Activity_Details2>).  
    Activity Information

ProcessDetails
:   Type: [Process_Details2](<#Structure_Process_Details2>).  
    Process Details

NotificationDetails
:   Type: [Notification_Details](<#Structure_Notification_Details>).  
    Notification details

RuleExecutionDetails
:   Type: [RuleExecution_Details](<#Structure_RuleExecution_Details>).  
    Rule execution details

### Case_RequestCount { #Structure_Case_RequestCount }

Count of each case filter type

*Attributes*

CaseFilterCriteriaId
:   Type: CaseFilterCriteria Identifier.  
    Case Filter Criteria

Label
:   Type: Text.  
    Label

Count
:   Type: Integer.  
    Number of activities

Order
:   Type: Integer.  
    Order

### CaseAccess { #Structure_CaseAccess }

Information about the read/write access of a Case

*Attributes*

CanRead
:   Type: Boolean.  
    

CanWrite
:   Type: Boolean.  
    

### CaseAccessControl_GroupDetails { #Structure_CaseAccessControl_GroupDetails }

Public  structure with Group Details

*Attributes*

Id
:   Type: GroupExtended Identifier.  
    Group Matrix Identifier

GroupId
:   Type: Group Identifier.  
    Group Identifier

ParentId
:   Type: GroupExtended Identifier.  
    Parent Identifier

Name
:   Type: Text (100).  
    Group name

Description
:   Type: Text (500).  
    Group Description

IsActive
:   Type: Boolean.  
    If the group extened is active

### CaseActivities_FilterResults { #Structure_CaseActivities_FilterResults }

Case Activities Filter Search Structure

*Attributes*

ActivityFilterCriteriaId
:   Type: ActivityFilterCriteria2 Identifier.  
    Activity Filter Criteria

SearchFieldList
:   Type: [CaseActivitySearchField](<#Structure_CaseActivitySearchField>) List.  
    Search Field List

SortFieldList
:   Type: [CaseActivitySortField](<#Structure_CaseActivitySortField>) List.  
    Sort Field List

UserAssigneeCriteriaId
:   Type: UserAssigneeCriteria Identifier.  
    User Assignee Criteria

AnonymousCriteriaId
:   Type: AnonymousCriteria Identifier.  
    AnonymousCriteriaId

IsReturnAll
:   Type: Boolean.  
    If true, will return all activities (to be used by admin users for instance)

ExcludeActivityActionIds
:   Type: [ActivityAction Identifier](<#Structure_ActivityAction Identifier>) List.  
    ActivitiesActions to exclude

DelegatedBy
:   Type: User Identifier.  
    Fullfil to the call act and return activities that are delegated by that specified user.

CalculateOnlyCounters
:   Type: Boolean.  
    If true, only output counters will be fulfilled

PageNumber
:   Type: Integer.  
    Page number

MaxResultsPerPage
:   Type: Integer.  
    Number of results per page

### CaseActivity_Details { #Structure_CaseActivity_Details }

Holds details for a case definition activities statistics

*Attributes*

ActivityDefinitionId
:   Type: Activity_Definition Identifier.  
    Activity Definition

ActivityDefinitionSSKey
:   Type: Text.  
    Activity Definition SS Key

Name
:   Type: Text.  
    Activity Name

AverageDuration
:   Type: Integer.  
    AverageDuration in minutes for this activity definition

### CaseActivity_View { #Structure_CaseActivity_View }

Represents an Activity Detail associated with a Case

*Attributes*

Case_Details
:   Type: [Case_Details](<#Structure_Case_Details>).  
    Case information

Activity_Details
:   Type: [Activity_Details](<#Structure_Activity_Details>).  
    Activity Detail

Process_Details
:   Type: [Process_Details](<#Structure_Process_Details>).  
    Case associated Process Details

ActivityAction_DetaislList
:   Type: [ActivityAction_Details](<#Structure_ActivityAction_Details>) List.  
    List of possible activity actions

User_Details
:   Type: [User_Details](<#Structure_User_Details>).  
    User details

Group_Details
:   Type: [Group_Details](<#Structure_Group_Details>).  
    Group details

Delegation_Details
:   Type: [User_Details](<#Structure_User_Details>).  
    Delegation details (if applicable)

### CaseActivityScope { #Structure_CaseActivityScope }

Structure that defines how Cases are filtered by Activities

*Attributes*

CaseStateFilterId
:   Type: CaseStateFilter Identifier.  
    Filters cases based on their state. All cases states are returned by default. To use this filter add the &quot;CaseStateFilter&quot; static entity from the &quot;CM_CaseServices_BL&quot; module as a dependency.

ActivityAssigneeTypeId
:   Type: ActivityAssigneeType Identifier.  
    Indicates which activities will be returned based on the type of assignee. To use this filter add the &quot;ActivityAssigneeType&quot; static entity from the &quot;CM_CaseServices_BL&quot; module as a dependency.  
    Options:  
    -MyActivities: will return the activities that the currently logged in user can work on.  
    1. Activities assigned to the currently logged in user.  
    2. Activities that are assigned to a group that the currently logged in user belongs to.  
    3. Activities that have neither a user nor a group assigned to them.  
    -All: will return all activities regardless of the currently logged in user.

ActivityAssignmentStatusId
:   Type: ActivityAssignmentStatus Identifier.  
    Indicates which activities will be returned based on their assignment status. To use this filter add the &quot;ActivityAssignmentStatus&quot; static entity from the &quot;CM_CaseServices_BL&quot; module as a dependency.  
    Options:  
    -AssignedToAnyone: will return the activities that have a user assigned to them.  
    -AssignedToMe: will return the activities that are assigned to the currently logged in user.  
    -AssignedToOthers: will return the activities that are assigned to a user that is not the currently logged in user.  
    -Unassigned: will return the activities that do not have a user assigned to them.  
    -All: will return all activities regardless of having a user assigned to them or not.

ActivityProgressStatusId
:   Type: ActivityProgressStatus Identifier.  
    Indicates which activities will be returned based on their progress status. To use this filter add the &quot;ActivityProgressStatus&quot; static entity from the &quot;CM_CaseServices_BL&quot; module as a dependency.  
    Options:  
    -ToDo: will return the activities that have not been opened.  
    -InProgress: will return the activities that have been opened by their assignee.  
    -Active: will return the activities that fall under the &quot;ToDo&quot; or &quot;InProgress&quot; options.  
    -Done: will return the activities that have been closed.  
    -All: will return all activities regardless of their progress status.

IncludeMyCases
:   Type: Boolean.  
    If True, include cases created by the logged in user.

### CaseActivitySearchField { #Structure_CaseActivitySearchField }

Holds a field to search for

*Attributes*

CaseActivityFieldSearchTypeId
:   Type: CaseActivityFieldSearchType Identifier.  
    Case Activity Field Search Type

FieldName
:   Type: Text.  
    Used this field to search by a biz field instead of a predefined one (will be ignored if no CaseDefinitionId provided)

FieldValue
:   Type: Text.  
    Field Value to search

### CaseActivitySortField { #Structure_CaseActivitySortField }

Holds a field to sort for

*Attributes*

CaseActivityFieldSortTypeId
:   Type: CaseActivityFieldSortType Identifier.  
    Case Activity Field Sort Type

FieldName
:   Type: Text.  
    Used this field to sort by a biz field instead of a predefined one (will be ignored if no CaseDefinitionId provided)

Ascending
:   Type: Boolean.  
    If true, order by asc. If false order by desc

### CaseCounter { #Structure_CaseCounter }

Count of each case filter type

*Attributes*

CaseStateFilterId
:   Type: CaseStateFilter Identifier.  
    Case State Filter Criteria

Label
:   Type: Text.  
    Label

Count
:   Type: Integer.  
    Number of activities

Order
:   Type: Integer.  
    Order

### CaseDetails { #Structure_CaseDetails }

Case intance details

*Attributes*

CaseId
:   Type: Case Identifier.  
    

CaseDefinitionId
:   Type: CaseDefinition Identifier.  
    Case Definition Identifier

CaseNumber
:   Type: Long Integer.  
    Case Number

StatusId
:   Type: CaseStatus Identifier.  
    Status Identifier

StatusName
:   Type: Text.  
    Status name

CreatedOn
:   Type: Date Time.  
    Execution date and time

CompletedOn
:   Type: Date Time.  
    Completion date and time

CaseRequesterUserId
:   Type: User Identifier.  
    Requester of the Case

CreatedBy
:   Type: User Identifier.  
    User who created the Case

### CaseDetails_Lite { #Structure_CaseDetails_Lite }

Details for an existing case (Case identifier and Case number)

*Attributes*

CaseId
:   Type: Case Identifier.  
    Case identifier

CaseNumber
:   Type: Long Integer.  
    Case number

### CaseExternalRequest_Create { #Structure_CaseExternalRequest_Create }

Public structure that enables to create case external request instances

*Attributes*

RequesterName
:   Type: Text (256).  
    Requester Name

RequesterEmail
:   Type: Email.  
    Requester Email

RequesterPhone
:   Type: Phone Number.  
    Requester Phone

RequesterExternalId
:   Type: Text (50).  
    The user identifier in an external system

### CaseExternalRequest_Details { #Structure_CaseExternalRequest_Details }

Public structure with CaseExternalRequest details

*Attributes*

RequesterName
:   Type: Text (256).  
    Requester Name

RequesterEmail
:   Type: Email.  
    Requester Email

RequesterPhone
:   Type: Phone Number.  
    Requester Phone

RequesterExternalId
:   Type: Text (50).  
    The user identifier in an external system

### CaseRequest_View { #Structure_CaseRequest_View }

Represents a Case Detail

*Attributes*

Case_Details
:   Type: [Case_Details](<#Structure_Case_Details>).  
    Case information

Activity_CaseViewList
:   Type: [Activity_CaseView](<#Structure_Activity_CaseView>) List.  
    

### CaseScope { #Structure_CaseScope }

Structure that defines how Cases are filtered by Requester Scope and Case State Filter

*Attributes*

RequesterScopeId
:   Type: RequesterScope Identifier.  
    Indicates which cases will be returned based on the Requester field, where by default, the logged in user's cases are returned. To use this filter add the &quot;RequesterScope&quot; static entity from the &quot;CM_CaseServices_BL&quot; module as a dependency.

CaseStateFilterId
:   Type: CaseStateFilter Identifier.  
    Filters cases based on their state. All cases states are returned by default. To use this filter add the &quot;CaseStateFilter&quot; static entity from the &quot;CM_CaseServices_BL&quot; module as a dependency.

### CaseSearchCriteria { #Structure_CaseSearchCriteria }

Possible Case filters. Note: the result of mixing values for filters of different types works as an &quot;AND&quot; and inside filters of the same type as an &quot;OR&quot;, for the list of cases to return.

*Attributes*

CaseDefinitionIdList
:   Type: [CaseDefinition Identifier](<#Structure_CaseDefinition Identifier>) List.  
    List of CaseDefinition identifiers

CaseIdList
:   Type: [Case Identifier](<#Structure_Case Identifier>) List.  
    List of Case identifiers

CaseNumberList
:   Type: [Long Integer](<#Structure_Long Integer>) List.  
    List of Case numbers

CaseStatusIdList
:   Type: [CaseStatus Identifier](<#Structure_CaseStatus Identifier>) List.  
    List of Case Status identifiers

CaseCreatedByList
:   Type: [User Identifier](<#Structure_User Identifier>) List.  
    List of User identifiers (CreatedBy Case attribute)

CaseRequesterIdList
:   Type: [User Identifier](<#Structure_User Identifier>) List.  
    List of User identifiers (CaseRequesterUserId Case attribute). Note that this attribute is automatically filled in with the identifier of the User who created the Case (CreatedBy) if no Requester is sent.

ExternalRequesterList
:   Type: [CaseExternalRequest_Details](<#Structure_CaseExternalRequest_Details>) List.  
    List of Case external requester details

TagIdList
:   Type: [Tag Identifier](<#Structure_Tag Identifier>) List.  
    List of Tag identifiers

### CaseSearchField { #Structure_CaseSearchField }

Holds a field to search for

*Attributes*

CaseFieldSearchTypeId
:   Type: CaseFieldSearchType Identifier.  
    Case Field Search Type

FieldName
:   Type: Text.  
    Used this field to search by a biz field instead of a predefined one (will be ignored if no CaseDefinitionId provided)

FieldValue
:   Type: Text.  
    Field Value to search

### CaseSort { #Structure_CaseSort }

Case fields to sort for

*Attributes*

CaseFieldSortId
:   Type: CaseFieldSort Identifier.  
    Case Field Sort Type

Ascending
:   Type: Boolean.  
    If true, order by asc. If false order by desc

### CaseSortField { #Structure_CaseSortField }

Holds a field to sort for

*Attributes*

CaseFieldSortTypeId
:   Type: CaseFieldSortType Identifier.  
    Case Field Sort Type

FieldName
:   Type: Text.  
    Use this field to search by a biz field instead of a predefined one (CaseDefinitionId is mandatory when sorting by biz field)

Ascending
:   Type: Boolean.  
    If true, order by asc. If false order by desc

### CaseStatus_Details { #Structure_CaseStatus_Details }

Case Status Detail

*Attributes*

Id
:   Type: CaseStatus Identifier.  
    Status Unique Text Identifier

CaseDefinitionId
:   Type: CaseDefinition Identifier.  
    Case Unique Text Identifier

Name
:   Type: Text (50).  
    Status logical name

Alias
:   Type: Text (50).  
    Status alias name

IsInitial
:   Type: Boolean.  
    If the status is a initial

IsActive
:   Type: Boolean.  
    True if status is active, false otherwise

### Delegation_Details { #Structure_Delegation_Details }

Structure that contains the Delegation Details

*Attributes*

UserDetails
:   Type: [Delegation_UserDetails](<#Structure_Delegation_UserDetails>).  
    User Information details

GroupDetails
:   Type: [Group_Details](<#Structure_Group_Details>).  
    Group Information Details

### Delegation_User { #Structure_Delegation_User }

Delegation User Details

*Attributes*

UserDetails
:   Type: [Delegation_UserDetails](<#Structure_Delegation_UserDetails>).  
    User delegation details

Delegations
:   Type: [Delegation_Details](<#Structure_Delegation_Details>) List.  
    Existing delegations

### Delegation_UserDetails { #Structure_Delegation_UserDetails }

User Information

*Attributes*

UserId
:   Type: User Identifier.  
    User Identifier

Name
:   Type: Text.  
    User Name

Username
:   Type: Text.  
    Username

Email
:   Type: Email.  
    Email

### Delegation_View { #Structure_Delegation_View }

Holds a Delegation&#180;

*Attributes*

DelegationId
:   Type: Delegation Identifier.  
    Delegation Identifier

From
:   Type: Date Time.  
    Initial date of delegation

To
:   Type: Date Time.  
    Final date of delegation

IsActive
:   Type: Boolean.  
    If delegation is active

FromUser
:   Type: [Delegation_UserDetails](<#Structure_Delegation_UserDetails>).  
    Delegation User Details

FromGroup
:   Type: [Group_Details](<#Structure_Group_Details>).  
    From Group Details

ToUser
:   Type: [Delegation_UserDetails](<#Structure_Delegation_UserDetails>).  
    Delegated User Details

### ExtraFieldValue { #Structure_ExtraFieldValue }

Public structure with that holds the value for a setting

*Attributes*

SettingTypeId
:   Type: SettingType Identifier.  
    Indicates the data type of the returned value

Value
:   Type: Text.  
    Value

### FilterHistoryResults { #Structure_FilterHistoryResults }

Filter for case history list

*Attributes*

CaseId
:   Type: Case Identifier.  
    Case Identifier

EventTypeId
:   Type: EventType Identifier.  
    Event Type Identifier

OnlyWithComments
:   Type: Boolean.  
    If true, only events with comments will be returned

MaxRecordsResult
:   Type: Integer.  
    Filter result by max number of records

CaseCreatedBy
:   Type: User Identifier.  
    User that created the case request

InformationGroupAccess
:   Type: [InformationGroupAccess](<#Structure_InformationGroupAccess>).  
    InformationGroupAccess

ExcludeEventTypes
:   Type: [EventType Identifier](<#Structure_EventType Identifier>) List.  
    Exclude event types from result

### FilterResults { #Structure_FilterResults }

Filter Search Structure

*Attributes*

PageNumber
:   Type: Integer.  
    Page number

MaxResultsPerPage
:   Type: Integer.  
    Number of results per page

OnlyActive
:   Type: Boolean.  
    Gets groups only active

GroupName
:   Type: Text.  
    Searchs for group name

### FilterResults2 { #Structure_FilterResults2 }

Filter Serch Structure

*Attributes*

PageNumber
:   Type: Integer.  
    Page number

MaxResultsPerPage
:   Type: Integer.  
    Number of results per page

### Group_Details { #Structure_Group_Details }

Group Information

*Attributes*

GroupExtendedId
:   Type: GroupExtended Identifier.  
    Group Extended Identifier

GroupId
:   Type: Group Identifier.  
    Group Identifier

Name
:   Type: Text (100).  
    Group Name

Description
:   Type: Text (500).  
    Group description

### Group_Details2 { #Structure_Group_Details2 }

Public structure with system entity group details

*Attributes*

GroupId
:   Type: Group Identifier.  
    Group Identifier

Name
:   Type: Text (100).  
    Group Name (from system entity Group)

### GroupExtended_Detail { #Structure_GroupExtended_Detail }

Public structure to create a new Group Extended

*Attributes*

Id
:   Type: GroupExtended Identifier.  
    Group extended  Identifier

GroupId
:   Type: Group Identifier.  
    Group Identifier

GroupTypeId
:   Type: GroupType Identifier.  
    Group Type (Requester, Operator, ...)

ParentId
:   Type: GroupExtended Identifier.  
    Parent Identifier

Name
:   Type: Text (100).  
    Group name (If not filled in will assume group name from system entity group)

SystemName
:   Type: Text (100).  
    Name for the systen entity Group

Description
:   Type: Text (500).  
    Group Description

CalendarId
:   Type: Calendar Identifier.  
    Calendar Identifier

IsActive
:   Type: Boolean.  
    If the group extened is active

HasCustomManagement
:   Type: Boolean.  
    If has customer management and if it should not be visibile from Users

### Holiday_Detail { #Structure_Holiday_Detail }

Public structure with the calendar holiday details

*Attributes*

Id
:   Type: Holiday Identifier.  
    Identifier

CalendarId
:   Type: Calendar Identifier.  
    Calendar Identifier

Name
:   Type: Text (50).  
    Event Name  
    The text on an event's element

Date
:   Type: Date.  
    Required. The day where the event will occur

DayOfMonth
:   Type: Integer.  
    Required. The day where the event will occur

Month
:   Type: Integer.  
    Month where will occur

IsRecurrent
:   Type: Boolean.  
    If this event is recurrent

IsActive
:   Type: Boolean.  
    If the event is active

### HumanActivityTimelineDetails { #Structure_HumanActivityTimelineDetails }



*Attributes*

UserDetail
:   Type: [User_Details](<#Structure_User_Details>).  
    

GroupDetail
:   Type: [Group_Details2](<#Structure_Group_Details2>).  
    

ActivityHistory
:   Type: [ActivityHistory](<#Structure_ActivityHistory>).  
    

### InformationGroupAccess { #Structure_InformationGroupAccess }

Holds the flags for each group type access

*Attributes*

RequesterAccess
:   Type: Boolean.  
    Requester Access

OperatorAccess
:   Type: Boolean.  
    Operator Access

### MilestoneDetails { #Structure_MilestoneDetails }

Holds the details of a Milestone

*Attributes*

MilestoneDefinitionId
:   Type: MilestoneDefinition Identifier.  
    

Name
:   Type: Text.  
    

Description
:   Type: Text.  
    

IsAchieved
:   Type: Boolean.  
    

AchievedOn
:   Type: Date Time.  
    

AchievedBy
:   Type: User Identifier.  
    

### NonWorkingDay_Detail { #Structure_NonWorkingDay_Detail }

Public structure with the non working details

*Attributes*

Id
:   Type: NonWorkingDay Identifier.  
    Identifier

CalendarId
:   Type: Calendar Identifier.  
    Calendar Identifier

WeekDayId
:   Type: WeekDay Identifier.  
    

IsActive
:   Type: Boolean.  
    Indicates if its active

WeekDay
:   Type: [WeekDay](<#Structure_WeekDay>).  
    No deal possible on this day

### Notification_Details { #Structure_Notification_Details }

Holds information for a notification case details

*Attributes*

NotificationTypeId
:   Type: NotificationType Identifier.  
    Notification type

TemplateId
:   Type: Text (36).  
    Template Id

TemplateName
:   Type: Text.  
    Template Name

Subject
:   Type: Text (500).  
    Notification subject

NotificationEmail
:   Type: [NotificationEmail_Details](<#Structure_NotificationEmail_Details>).  
    Notification Email Details

### NotificationEmail_Details { #Structure_NotificationEmail_Details }

Holds information for an email notification

*Attributes*

IsToRequester
:   Type: Boolean.  
    True, if requester was on To

IsCCRequester
:   Type: Boolean.  
    True, if requester was on CC

IsBCCRequester
:   Type: Boolean.  
    True, if the requester was on bcc

ToGroupId
:   Type: Group Identifier.  
    Group identifier, if group defined for the To

ToGroupName
:   Type: Text (100).  
    To Group Name

CcGroupId
:   Type: Group Identifier.  
    Group identifier, if group defined for the Cc

CcGroupName
:   Type: Text (100).  
    Cc Group Name

BccGroupId
:   Type: Group Identifier.  
    Group identifier, if group defined for the Bcc

BccGroupName
:   Type: Text (100).  
    Bcc Group Name

To
:   Type: Text (2000).  
    To emails

Cc
:   Type: Text (2000).  
    Cc emails

Bcc
:   Type: Text (2000).  
    Bcc emails

### OrderHistoryResult { #Structure_OrderHistoryResult }

Order history results

*Attributes*

OrderFieldId
:   Type: OrderField Identifier.  
    Order by field history query result

OrderByAscending
:   Type: Boolean.  
    Order direction

### Process_Details { #Structure_Process_Details }

Process details

*Attributes*

ProcessId
:   Type: Process Identifier.  
    Process Identifier

Name
:   Type: Text.  
    Process Name

ProcessStatusId
:   Type: Process_Status Identifier.  
    Process Status Identifier

IsBlocked
:   Type: Boolean.  
    If the process is blocked

CreatedOn
:   Type: Date Time.  
    Creation On

### Process_Details2 { #Structure_Process_Details2 }

Holds information for a case process details

*Attributes*

ProcessId
:   Type: Process Identifier.  
    Process Id

SLADetails
:   Type: [SLA_Details](<#Structure_SLA_Details>).  
    SLA Details

### ProcessEvent_Create { #Structure_ProcessEvent_Create }

Public structure to create a new process event

*Attributes*

ProcessId
:   Type: Process Identifier.  
    Identifier

ProcessEventTypeId
:   Type: ProcessEventType Identifier.  
    Process Event Type

EventOn
:   Type: Date Time.  
    Date and time for the event

### RuleExecution_Details { #Structure_RuleExecution_Details }

Holds information for a rule execution case details

*Attributes*

RuleId
:   Type: Text (36).  
    Rule Id

RuleName
:   Type: Text (100).  
    Rule Name

RuleTypeId
:   Type: Integer.  
    RuleType Id

Output
:   Type: Text (1000).  
    Rule output value

OutputLabel
:   Type: Text (1000).  
    Rule output label

### SampleUser { #Structure_SampleUser }

SampleUser

*Attributes*

UserId
:   Type: User Identifier.  
    UserId

Username
:   Type: Text.  
    Username

Name
:   Type: Text.  
    Name

GroupId
:   Type: Group Identifier.  
    GroupId

GroupName
:   Type: Text.  
    Group name

### Search_CaseDetails { #Structure_Search_CaseDetails }

Represents the details of a Case instance

*Attributes*

CaseId
:   Type: Case Identifier.  
    Case Identifier

CaseDefinitionId
:   Type: CaseDefinition Identifier.  
    Case Definition Identifier

CaseDefinitionName
:   Type: Text.  
    Case Definition Name

CaseDefinitionNameLang
:   Type: Text.  
    Case Definition Name Lang

CaseNumber
:   Type: Long Integer.  
    Case Number

StatusId
:   Type: CaseStatus Identifier.  
    Status Identifier

StatusName
:   Type: Text.  
    Status name

StatusNameLang
:   Type: Text.  
    Status Name Lang

StatusAlias
:   Type: Text.  
    Status alias

StatusAliasLang
:   Type: Text.  
    Status Alias Lang

PriorityId
:   Type: ProcessDefinitionPriority Identifier.  
    Priority identifier

PriorityName
:   Type: Text.  
    Priority Name

CreatedBy
:   Type: User Identifier.  
    

CreatedByName
:   Type: Text.  
    Name of the User who created the Case

RequesterId
:   Type: User Identifier.  
    Case Requester identifier

RequesterName
:   Type: Text.  
    Name of the Case Requester

CreatedOn
:   Type: Date Time.  
    Execution date and time

LastUpdatedOn
:   Type: Date Time.  
    Last update date and time

CompletedOn
:   Type: Date Time.  
    Completion date and time

### SearchCriteria { #Structure_SearchCriteria }

Result set filter criteria

*Attributes*

ActivitySearchCriteria
:   Type: [ActivitySearchCriteria](<#Structure_ActivitySearchCriteria>).  
    Activity filters. When values for different filter criteria types are sent, returned activities will match all filters (&quot;AND&quot; condition). Inside each criteria attribute list, the returned activities will match at least one of those values (&quot;OR&quot; condition).

CaseSearchCriteria
:   Type: [CaseSearchCriteria](<#Structure_CaseSearchCriteria>).  
    Case filters. When values for different filter criteria types are sent, returned activities will match all filters (&quot;AND&quot; condition). Inside each criteria attribute list, the returned activities will match at least one of those values (&quot;OR&quot; condition).

### SLA_Details { #Structure_SLA_Details }

Holds information for sla details

*Attributes*

StartExecutionDate
:   Type: Date Time.  
    Start date and time for the SLA

DueDate
:   Type: Date Time.  
    Due Date for the SLA

ExecutionTimeInMinutes
:   Type: Long Integer.  
    Duration in minutes (if exists a SLA associated, takes the calendar into account if applicable)

IsResponseTimeExceeded
:   Type: Boolean.  
    If the SLA response time was exceeded

CompletedExecutionDate
:   Type: Date Time.  
    Completion date and time

### StatusDetails { #Structure_StatusDetails }

Case Status Details

*Attributes*

CaseStatusId
:   Type: CaseStatus Identifier.  
    Case Status Identifier

Name
:   Type: Text (50).  
    Case Status name

Alias
:   Type: Text (50).  
    Case Status alias name

DateTime
:   Type: Date Time.  
    Date time of the update status event

UserId
:   Type: User Identifier.  
    User who updated the status. If the action to update is called automatically by system events or inside the bpt flow, the user identifier returned will be null

### TagDetails { #Structure_TagDetails }

Public structure with Tag details

*Attributes*

TagId
:   Type: Tag Identifier.  
    Tag Identifier

Label
:   Type: Text.  
    Tag label

CaseDefinitionId
:   Type: CaseDefinition Identifier.  
    Case Definition Identifier

CreatedBy
:   Type: User Identifier.  
    Creation User Identifier

CreatedOn
:   Type: Date Time.  
    Creation date and time

LastUpdatedBy
:   Type: User Identifier.  
    Last User who edited the record

LastUpdatedOn
:   Type: Date Time.  
    Last edition date and time

### TagIdentifier { #Structure_TagIdentifier }

Tag Identifier

*Attributes*

TagId
:   Type: Tag Identifier.  
    Tag Identifier

### User_Details { #Structure_User_Details }

Generic structure with user details

*Attributes*

UserId
:   Type: User Identifier.  
    User Identifier

Name
:   Type: Text.  
    Name

Username
:   Type: Text.  
    Username

Email
:   Type: Email.  
    Email

### User_SearchResults { #Structure_User_SearchResults }

Public structure to return the search results for Group extended

*Attributes*

ListUserDetails
:   Type: [UserExtended_Details](<#Structure_UserExtended_Details>) List.  
    List of User Identifiers

NumberResults
:   Type: Long Integer.  
    Number of results

### UserExtended_Details { #Structure_UserExtended_Details }

Details about user

*Attributes*

UserId
:   Type: User Identifier.  
    User Identifier

Name
:   Type: Text.  
    Name

Username
:   Type: Text.  
    Username

Email
:   Type: Email.  
    Email

ManagerUserId
:   Type: User Identifier.  
    User's manager

DefaultGroupExtendedId
:   Type: GroupExtended Identifier.  
    Default user group


