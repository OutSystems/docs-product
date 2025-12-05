---
summary: OutSystems 11 (O11) offers a Case Configurations API for managing case-related entities and operations in applications.
guid: a1e53b88-9aa2-4f25-9f54-f22b9add8907
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: api documentation, case management, crud operations, outsystems platform, case configurations
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - platform administrators
outsystems-tools:
  - service studio
  - case management framework
coverage-type:
  - remember
---

# Case Configurations API

The Case Configurations API includes actions used to configure a case in your app.
Use this API to access all the CRUD operations for different case features, for example, rules, or to set up templates.

For example, this API is used to configure the following entities related to the cases of your application:

* Case Definition.
* Case Statuses.
* StateMachine.
* Rules.

## Summary

| Action | Description |
| ---|--- |
| [BootstrapCaseConfiguration](<#BootstrapCaseConfiguration>) | Bootstraps the case configuration |
| [Calendar_Create](<#Calendar_Create>) | Action to create a new calendar |
| [Calendar_CreateOrUpdate](<#Calendar_CreateOrUpdate>) | Action to create or update a calendar |
| [Calendar_Delete](<#Calendar_Delete>) | Deletes an existiing calendar |
| [Calendar_Update](<#Calendar_Update>) | Update an existing calendar |
| [CaseAction_Bootstrap](<#CaseAction_Bootstrap>) | Bootstraps the list of Case Workflow Actions |
| [CaseDefinition_CheckValidStatus](<#CaseDefinition_CheckValidStatus>) | Checks if the status is valid for a specific case definition |
| [CaseDefinition_Create](<#CaseDefinition_Create>) | Creates a new case definition |
| [CaseDefinition_CreateOrUpdate](<#CaseDefinition_CreateOrUpdate>) | Creates or updates a case definition |
| [CaseDefinition_Delete](<#CaseDefinition_Delete>) | Deletes an existing case definition |
| [CaseDefinition_GetActions](<#CaseDefinition_GetActions>) | Gets the actions associated to a case definition |
| [CaseDefinition_GetAll](<#CaseDefinition_GetAll>) | Gets the list of active CaseDefinitions |
| [CaseDefinition_GetById](<#CaseDefinition_GetById>) | Gets a specific Case Definition by case identifier |
| [CaseDefinition_GetDetailByProcessDefinitionId](<#CaseDefinition_GetDetailByProcessDefinitionId>) | Gets the Case Definition details |
| [CaseDefinition_GetEligibleToPurge](<#CaseDefinition_GetEligibleToPurge>) | Get the case definitions that are eligible to purge, ie, without any case instance and which application is also deleted |
| [CaseDefinition_GetEntityId](<#CaseDefinition_GetEntityId>) | Gets the associated entity identifier |
| [CaseDefinition_GetInitialStatus](<#CaseDefinition_GetInitialStatus>) | Gets the initial status for a given case definition. |
| [CaseDefinition_GetProcessDefinitionId](<#CaseDefinition_GetProcessDefinitionId>) | Gets the associated process definition identifier |
| [CaseDefinition_GetProcessDefinitionList](<#CaseDefinition_GetProcessDefinitionList>) | Gets the list of process definitions associated with case definitions |
| [CaseDefinition_GetStatusList](<#CaseDefinition_GetStatusList>) | Gets the list of all valid statuses for a given case definition. |
| [CaseDefinition_LinkToMilestoneDefinition](<#CaseDefinition_LinkToMilestoneDefinition>) | Sets a relation between a CaseDefinition and a MilestoneDefinition |
| [CaseDefinition_PreviewByProcessDefinition](<#CaseDefinition_PreviewByProcessDefinition>) | Previews the keys for the CaseDefinition based on a ProcessDefinition |
| [CaseDefinition_Purge](<#CaseDefinition_Purge>) | Purges a Case Definition |
| [CaseDefinition_UnlinkFromMilestoneDefinition](<#CaseDefinition_UnlinkFromMilestoneDefinition>) | Removes a relation between a CaseDefinition and a MilestoneDefinition |
| [CaseDefinition_Update](<#CaseDefinition_Update>) | Updates an existing case definition |
| [CaseStateMachine_Create](<#CaseStateMachine_Create>) | Creates a new State Machine entry |
| [CaseStateMachine_CreateOrUpdate](<#CaseStateMachine_CreateOrUpdate>) | Creates or updates a State Machine entry |
| [CaseStateMachine_GetByTransition](<#CaseStateMachine_GetByTransition>) | Gets the case state machine record by status transition |
| [CaseStateMachine_Purge](<#CaseStateMachine_Purge>) | Purge a Case State Machine |
| [CaseStateMachine_Update](<#CaseStateMachine_Update>) | Updates an existing State Machine entry |
| [CaseStatus_Bootstrap](<#CaseStatus_Bootstrap>) | Will replace the existing case definiton statuses (or create if new) for a specific CaseDefinition |
| [CaseStatus_Create](<#CaseStatus_Create>) | Creates a new Case Status |
| [CaseStatus_CreateOrUpdate](<#CaseStatus_CreateOrUpdate>) | Creates or updates a Case Status |
| [CaseStatus_Delete](<#CaseStatus_Delete>) | Deletes a Case Status |
| [CaseStatus_GetById](<#CaseStatus_GetById>) | Gets the status details by identifier |
| [CaseStatus_Update](<#CaseStatus_Update>) | Updates an existing Case Status |
| [CaseTag_Create](<#CaseTag_Create>) | Enables to create a CaseTag instance in the CaseTag entity |
| [CheckApplicationStatus](<#CheckApplicationStatus>) | Check the status of an application |
| [Delegation_Create](<#Delegation_Create>) | Creates a new Delegation |
| [Delegation_CreateOrUpdate](<#Delegation_CreateOrUpdate>) | Creates or updates a delegation |
| [Delegation_Delete](<#Delegation_Delete>) | Deletes an existing Delegation. Can only be removed by the user that created the delegation, if not it will raise an exception. |
| [Delegation_Update](<#Delegation_Update>) | Updates an existing Delegation. Can only be updated by the user that created the delegation, if not it will raise an exc |
| [DEPRECATED_SetupCaseManagementApplication](<#DEPRECATED_SetupCaseManagementApplication>) | Sets up the basic configurations for a case management application |
| [Email_ProcessPlaceholders](<#Email_ProcessPlaceholders>) | It will replace the placeholders by the actual case data |
| [EmailTemplate_Create](<#EmailTemplate_Create>) | Creates an EmailTemplate object |
| [EmailTemplate_CreateOrUpdate](<#EmailTemplate_CreateOrUpdate>) | Creates or updates an EmailTemplate object |
| [EmailTemplate_GetAll](<#EmailTemplate_GetAll>) | Gets all EmailTemplates that matches the search criteria |
| [EmailTemplate_GetById](<#EmailTemplate_GetById>) | Gets a EmailTemplate by Id |
| [EmailTemplate_Update](<#EmailTemplate_Update>) | Updates an EmailTemplate object |
| [EntityAttr_GetByGlobalKey](<#EntityAttr_GetByGlobalKey>) | Gets the AttributeId based on it's GlobalKey |
| [Espace_GetForActivityScreen](<#Espace_GetForActivityScreen>) | Gets list of espaces that can have screens to an activity can be opened by |
| [GetBusinessEntities](<#GetBusinessEntities>) | Gets the list of business entities based on a case definition |
| [GetBusinessEntityAttributes](<#GetBusinessEntityAttributes>) | Gets the list of business entities attributes based on an entity |
| [GetSystemDefaultDaysToPurge](<#GetSystemDefaultDaysToPurge>) | Gets the system sefault days to purge the case data |
| [GlobalKey_Parse](<#GlobalKey_Parse>) | Parses a GlobalKey |
| [Group_AssignGroupToUser](<#Group_AssignGroupToUser>) | Assigns a user to a group |
| [Group_GetGroupsToAssociate](<#Group_GetGroupsToAssociate>) | Gets existing groups not associated with group extended that can be associated |
| [Group_UnassignGroupFromUser](<#Group_UnassignGroupFromUser>) | Removes the user association fromo a group |
| [GroupExtended_CreateOrUpdate](<#GroupExtended_CreateOrUpdate>) | Creates or updates an existing Group Matrix |
| [GroupExtended_Delete](<#GroupExtended_Delete>) | Removes an existing Group Matrix. Can only be removed if no association exists to the group (activity, role or user association) |
| [Holiday_Create](<#Holiday_Create>) | Create a new calendar holiday associated to an existing calendar. |
| [Holiday_CreateOrUpdate](<#Holiday_CreateOrUpdate>) | Action to create or update an event of a calendar |
| [Holiday_Delete](<#Holiday_Delete>) | Deletes an existing calendar holiday |
| [Holiday_Update](<#Holiday_Update>) | Updates an existing calendar holiday |
| [Hostname_Get](<#Hostname_Get>) | Gets Server Hostname |
| [ImportUserHierarchy_GetSample](<#ImportUserHierarchy_GetSample>) | Get a sample of the file content to perform an import |
| [ImportUserHierarchy_GetStatus](<#ImportUserHierarchy_GetStatus>) | Check the status of an import request |
| [Lookup_GetEntityRecords](<#Lookup_GetEntityRecords>) | Lookup an Entity |
| [Lookup_GetExtraFieldRecords](<#Lookup_GetExtraFieldRecords>) | Lookup an Extra field value |
| [MilestoneDefinition_Create](<#MilestoneDefinition_Create>) | Creates a new milestone definition |
| [MilestoneDefinition_CreateOrUpdate](<#MilestoneDefinition_CreateOrUpdate>) | Creates or updates a milestone definition |
| [MilestoneDefinition_Delete](<#MilestoneDefinition_Delete>) | Inactivates an existing milestone definition |
| [MilestoneDefinition_Update](<#MilestoneDefinition_Update>) | Updates an existing milestone definition |
| [NonWorkingDay_Create](<#NonWorkingDay_Create>) | Create a new calendar non working day associated to an existing calendar |
| [NonWorkingDay_CreateOrUpdate](<#NonWorkingDay_CreateOrUpdate>) | Action to create or update a non working day associated to an existing calendar |
| [NonWorkingDay_Delete](<#NonWorkingDay_Delete>) | Deletes an existing calendar non working day |
| [NonWorkingDay_Update](<#NonWorkingDay_Update>) | Updates an existiing calendar non working day |
| [NotificationsEngine_InitializeStaging](<#NotificationsEngine_InitializeStaging>) | It will mark all entries as deleted for the staging process after only import the active ones |
| [PreDefinedTemplate_Create](<#PreDefinedTemplate_Create>) | Creates a PredefinedTemplate object |
| [PreDefinedTemplate_CreateOrUpdate](<#PreDefinedTemplate_CreateOrUpdate>) | Creates or updates a PredefinedTemplate object |
| [PreDefinedTemplate_GetAll](<#PreDefinedTemplate_GetAll>) | Gets all predefined templates |
| [PreDefinedTemplate_GetById](<#PreDefinedTemplate_GetById>) | Gets a predefined template |
| [PreDefinedTemplate_Update](<#PreDefinedTemplate_Update>) | Updates a PredefinedTemplate object |
| [Resource_CreateOrUpdate](<#Resource_CreateOrUpdate>) | Creates or Updates a Resource |
| [Resource_Delete](<#Resource_Delete>) | Deletes a Resource |
| [Resource_GetById](<#Resource_GetById>) | Gets a Resource by Id |
| [Resource_Purge](<#Resource_Purge>) | Resource hard delete |
| [Resources_GetAll](<#Resources_GetAll>) | Gets All Resources |
| [Resources_InitializeStaging](<#Resources_InitializeStaging>) | It will mark all entries as deleted for the staging process after only import the active ones |
| [Rule_Create](<#Rule_Create>) | Create a Rule record |
| [Rule_CreateOrUpdate](<#Rule_CreateOrUpdate>) | Create or update a Rule record |
| [Rule_Delete](<#Rule_Delete>) | Deletes a whole rule |
| [Rule_Update](<#Rule_Update>) | Update a Rule record |
| [RuleGroup_Create](<#RuleGroup_Create>) | Create a Rule Group record |
| [RuleGroup_CreateOrUpdate](<#RuleGroup_CreateOrUpdate>) | Create or update a Rule Group record |
| [RuleGroup_Delete](<#RuleGroup_Delete>) | Deletes a Rule Group |
| [RuleGroup_DeleteAllByRuleId](<#RuleGroup_DeleteAllByRuleId>) | Deletes all Rule Group from a Rule |
| [RuleGroup_Update](<#RuleGroup_Update>) | Update a Rule Group record |
| [RuleGroupOutput_CreateOrUpdate](<#RuleGroupOutput_CreateOrUpdate>) | Create or update a Rule Group Output record |
| [RuleLine_CreateOrUpdate](<#RuleLine_CreateOrUpdate>) | Creates or updates a Rule Line |
| [RuleLine_Delete](<#RuleLine_Delete>) | Deletes a RuleLine |
| [Rules_GetAll](<#Rules_GetAll>) | Get all rules available |
| [Rules_GetById](<#Rules_GetById>) | Get a rule by Id |
| [Rules_InitializeStaging](<#Rules_InitializeStaging>) | It will mark all entries as deleted for the staging process after only import the active ones |
| [RulesGroup_GetAll](<#RulesGroup_GetAll>) | Get all RuleGroups from a Rule |
| [RulesOperator_GetBySettingType](<#RulesOperator_GetBySettingType>) | Returns the operations available for the respective setting type |
| [SampleUser_CreateOrUpdate](<#SampleUser_CreateOrUpdate>) | Create sample users (verifiy if is a second publish and disable all users before create news) and associate to its role and to its group (if applicable). |
| [Setting_ConvertSetting](<#Setting_ConvertSetting>) | Converts a Setting value to an CreateOrUpdate structure |
| [Setting_CreateOrUpdate](<#Setting_CreateOrUpdate>) | Public action that enables to create or update a setting |
| [Setting_Delete](<#Setting_Delete>) | Public action that deletes a setting |
| [Setting_DeleteList](<#Setting_DeleteList>) | Public action that deletes a list of settings |
| [Setting_GetById](<#Setting_GetById>) | Gets a Setting by it's Id |
| [Setting_Purge](<#Setting_Purge>) | Public action to hard delete a setting |
| [SettingType_GetByColumnType](<#SettingType_GetByColumnType>) | Gets the attribute setting type |
| [Tag_Create](<#Tag_Create>) | Enables to create a Tag instance in the Tag entity |
| [Tag_Delete](<#Tag_Delete>) | Asynchronously deletes all CaseTag records for a given Tag before deleting the Tag itself. Saves in each case's History each tag deletion. |
| [Tag_Update](<#Tag_Update>) | Enables to update a Tag instance in the Tag entity |
| [UserExtended_CreateOrUpdate](<#UserExtended_CreateOrUpdate>) | Creates or updates an User extended record |
| [UserHierarchy_Import](<#UserHierarchy_Import>) | Submits a requests to import user's hierarchy |

| Service Action | Description |
| ---|--- |
| [SetupCaseManagementApplication](<#Service_SetupCaseManagementApplication>) | Sets up the basic configurations for a case management application |

| Structure | Description |
| ---|--- |
| [BusinessEntity_View](<#Structure_BusinessEntity_View>) | View for business entities |
| [BusinessEntityAttr_View](<#Structure_BusinessEntityAttr_View>) | View for business entities attributes |
| [Calendar_Create](<#Structure_Calendar_Create>) | Public structure to create a new Calendar |
| [Calendar_Update](<#Structure_Calendar_Update>) | Public structure to update an existing Calendar |
| [CaseAction_CreateOrUpdate](<#Structure_CaseAction_CreateOrUpdate>) | Public structure to create or update a Case Workflow Action |
| [CaseAction_Translation](<#Structure_CaseAction_Translation>) | Translation structure for Case action |
| [CaseAction_View](<#Structure_CaseAction_View>) | View for Case Workflow Action |
| [CaseConfigurationBootstrap](<#Structure_CaseConfigurationBootstrap>) | Holds the bootstrap data |
| [CaseDefinition_Create](<#Structure_CaseDefinition_Create>) | Public structure to create a new case definition |
| [CaseDefinition_CreateOrUpdate](<#Structure_CaseDefinition_CreateOrUpdate>) | Public structure to create a new case definition or to update an existing case definition |
| [CaseDefinition_Details](<#Structure_CaseDefinition_Details>) | Public structure that contains the case defintion details |
| [CaseDefinition_FilterResults](<#Structure_CaseDefinition_FilterResults>) | Filter Serch Structure |
| [CaseDefinition_Translation](<#Structure_CaseDefinition_Translation>) | Translation structure for Case definition |
| [CaseDefinitionMilestoneDefinition_Create](<#Structure_CaseDefinitionMilestoneDefinition_Create>) | Public structure for the Creation of a CaseDefinitionMilestoneDefinition record |
| [CaseStateMachine_Create](<#Structure_CaseStateMachine_Create>) | Public structure for state machine creation |
| [CaseStateMachine_CreateOrUpdate](<#Structure_CaseStateMachine_CreateOrUpdate>) | Structure to enable case state machine creation or update |
| [CaseStateMachine_Details](<#Structure_CaseStateMachine_Details>) | Case State Machine Details |
| [CaseStatus_Create](<#Structure_CaseStatus_Create>) | Public structure to create a new status |
| [CaseStatus_CreateOrUpdate](<#Structure_CaseStatus_CreateOrUpdate>) | Public structure to create or update a status |
| [CaseStatus_Details](<#Structure_CaseStatus_Details>) | Case Status Detail |
| [CaseStatus_Translation](<#Structure_CaseStatus_Translation>) | Translation structure for Case status |
| [CaseTag_Create](<#Structure_CaseTag_Create>) | Public structure that enables to create CaseTage instances |
| [Delegation_Create](<#Structure_Delegation_Create>) | Holds a Delegation entry to be created |
| [Delegation_Update](<#Structure_Delegation_Update>) | Holds a Delegation details for update |
| [DEPRECATED_SetupData](<#Structure_DEPRECATED_SetupData>) | Holds the basic setup data for a case management application |
| [EmailTemplate_CreateOrUpdate](<#Structure_EmailTemplate_CreateOrUpdate>) | Represents a EmailTemplate object to be updated |
| [EmailTemplate_View](<#Structure_EmailTemplate_View>) | Represents a EmailTemplate object |
| [Entity_Lookup](<#Structure_Entity_Lookup>) | Entity to lookup FK |
| [Espace_Detail](<#Structure_Espace_Detail>) | Public structure to hold espace details |
| [FilterResults](<#Structure_FilterResults>) | Filter Search Structure |
| [FilterResults_Espace](<#Structure_FilterResults_Espace>) | Filter Search Structure |
| [FilterResults2](<#Structure_FilterResults2>) | Filter Search Structure |
| [Group_Details](<#Structure_Group_Details>) | Public structure with system entity group details |
| [GroupExtended_CreateOrUpdate](<#Structure_GroupExtended_CreateOrUpdate>) | Public structure to update an existing Group extended |
| [Holiday_Create](<#Structure_Holiday_Create>) | Public structure to create a new Calendar Holiday |
| [Holiday_Update](<#Structure_Holiday_Update>) | Public structure to update an existing Calendar Holiday |
| [MilestoneDefinition_CreateOrUpdate](<#Structure_MilestoneDefinition_CreateOrUpdate>) | Public structure to create a new milestone definition or to update an existing one |
| [MilestoneDefinition_Translation](<#Structure_MilestoneDefinition_Translation>) | Translation structure for Milestone definition |
| [NonWorkingDay_Create](<#Structure_NonWorkingDay_Create>) | Public structure to create a new Calendar Non Working Day |
| [NonWorkingDay_Update](<#Structure_NonWorkingDay_Update>) | Public structure to update an existing Calendar Non Working Day |
| [PreDefinedTemplate_CreateOrUpdate](<#Structure_PreDefinedTemplate_CreateOrUpdate>) | View to create or update a PreDefined Template |
| [PreDefinedTemplate_View](<#Structure_PreDefinedTemplate_View>) | View of a PreDefined Template |
| [ProcessDefinition_Details](<#Structure_ProcessDefinition_Details>) | Contains the generic details for process definition |
| [Resource_CreateOrUpdate](<#Structure_Resource_CreateOrUpdate>) | Structure to create or update a Resource |
| [Resource_View](<#Structure_Resource_View>) | Represents a Resource |
| [Rule_CreateOrUpdate](<#Structure_Rule_CreateOrUpdate>) | Structure to create/update a rule |
| [Rule_View](<#Structure_Rule_View>) | Structure with Rules fields |
| [RuleAttribute_CreateOrUpdate](<#Structure_RuleAttribute_CreateOrUpdate>) | Structure to create or update a Rule Attribute |
| [RuleAttribute_View](<#Structure_RuleAttribute_View>) | Structure with Rule Attribute fields |
| [RuleConfig](<#Structure_RuleConfig>) | Represents a Rule configuration |
| [RuleGroup_CreateOrUpdate](<#Structure_RuleGroup_CreateOrUpdate>) | Public structure to create or update a rule group |
| [RuleGroup_View](<#Structure_RuleGroup_View>) | Structure with Rule Groups fields |
| [RuleGroupOutput_CreateOrUpdate](<#Structure_RuleGroupOutput_CreateOrUpdate>) | Structure to create or update a Rule Group Output |
| [RuleGroupOutput_View](<#Structure_RuleGroupOutput_View>) | Structure with RuleGroupOutput fields |
| [RuleLine_CreateOrUpdate](<#Structure_RuleLine_CreateOrUpdate>) | Structure to create or update a Rule Line |
| [RuleLine_View](<#Structure_RuleLine_View>) | Structure with Rule Line fields |
| [Setting_CreateOrUpdate](<#Structure_Setting_CreateOrUpdate>) | Public structure to create or update a setting |
| [Setting_Value](<#Structure_Setting_Value>) | Public structure with the possible values for a setting |
| [Setup_CaseAction](<#Structure_Setup_CaseAction>) | Public structure to set up case actions |
| [Setup_CaseDefinition](<#Structure_Setup_CaseDefinition>) | Public structure to set up a case definition |
| [Setup_CaseStateMachine](<#Structure_Setup_CaseStateMachine>) | Public structure to set up case state machine transitions |
| [Setup_CaseStatus](<#Structure_Setup_CaseStatus>) | Public structure to set up case statuses |
| [Setup_EmailTemplate](<#Structure_Setup_EmailTemplate>) | Public structure to set up email templates |
| [Setup_MilestoneDefinition](<#Structure_Setup_MilestoneDefinition>) | Public structure to set up a milestone definition |
| [SetupData](<#Structure_SetupData>) | Holds the basic setup data for a case management application |
| [Tag_Create](<#Structure_Tag_Create>) | Public structure that enables to create tag instances |
| [Tag_Update](<#Structure_Tag_Update>) | Public structure that enables to update tag instances |
| [UserExtended_CreateOrUpdate](<#Structure_UserExtended_CreateOrUpdate>) | User extended create or update structure |

## Actions

### BootstrapCaseConfiguration {#BootstrapCaseConfiguration}

Bootstraps the case configuration

_Inputs_

CaseConfigurationBootstrap
:   Type: mandatory, [CaseConfigurationBootstrap](<#Structure_CaseConfigurationBootstrap>).  
    Case Configuration Bootstrap

### Calendar_Create {#Calendar_Create}

Action to create a new calendar

_Inputs_

CalendarCreateRec
:   Type: mandatory, [Calendar_Create](<#Structure_Calendar_Create>).  
    The calendar entity record.

_Outputs_

CalendarId
:   Type: Calendar Identifier.  
    The calendar identifier.

### Calendar_CreateOrUpdate {#Calendar_CreateOrUpdate}

Action to create or update a calendar

_Inputs_

CalendarRec
:   Type: mandatory, [Calendar_Update](<#Structure_Calendar_Update>).  
    The calendar entity record.

_Outputs_

CalendarId
:   Type: Calendar Identifier.  
    The calendar database identifier.

### Calendar_Delete {#Calendar_Delete}

Deletes an existiing calendar

_Inputs_

CalendarId
:   Type: mandatory, Calendar Identifier.  
    Calendar Identifier

### Calendar_Update {#Calendar_Update}

Update an existing calendar

_Inputs_

CalendarUpdateRec
:   Type: mandatory, [Calendar_Update](<#Structure_Calendar_Update>).  
    The calendar update details record.

### CaseAction_Bootstrap {#CaseAction_Bootstrap}

Bootstraps the list of Case Workflow Actions

_Inputs_

CaseDefinitionId
:   Type: mandatory, CaseDefinition Identifier.  
    If defined will only inactive the entries for that case definition

CaseAction_CreateOrUpdateLst
:   Type: mandatory, [CaseAction_CreateOrUpdate](<#Structure_CaseAction_CreateOrUpdate>) List.  
    List of workflow actions to bootstrap

### CaseDefinition_CheckValidStatus {#CaseDefinition_CheckValidStatus}

Checks if the status is valid for a specific case definition

_Inputs_

CaseDefinitionId
:   Type: mandatory, CaseDefinition Identifier.  
    Case Definition Identifier

StatusId
:   Type: mandatory, CaseStatus Identifier.  
    Case Status Identifier

_Outputs_

IsValid
:   Type: Boolean.  
    True if the status is valid False otherwise

### CaseDefinition_Create {#CaseDefinition_Create}

Creates a new case definition

_Inputs_

CaseDefinitionCreateRec
:   Type: mandatory, [CaseDefinition_Create](<#Structure_CaseDefinition_Create>).  
    Case Definition Details

_Outputs_

CaseDefinitionId
:   Type: CaseDefinition Identifier.  
    Case Definition Identifier

### CaseDefinition_CreateOrUpdate {#CaseDefinition_CreateOrUpdate}

Creates or updates a case definition

_Inputs_

CaseDefinitionRec
:   Type: mandatory, [CaseDefinition_CreateOrUpdate](<#Structure_CaseDefinition_CreateOrUpdate>).  
    Case Definition Details

_Outputs_

CaseDefinitionId
:   Type: CaseDefinition Identifier.  
    Case Definition Identifier

### CaseDefinition_Delete {#CaseDefinition_Delete}

Deletes an existing case definition

_Inputs_

CaseDefinitionId
:   Type: optional, CaseDefinition Identifier.  
    Case Definition Identifier

### CaseDefinition_GetActions {#CaseDefinition_GetActions}

Gets the actions associated to a case definition

_Inputs_

CaseDefinitionId
:   Type: mandatory, CaseDefinition Identifier.  
    Case Definition Identifier

_Outputs_

CaseAction_ViewList
:   Type: [CaseAction_View](<#Structure_CaseAction_View>) List.  
    List of workflow actions

### CaseDefinition_GetAll {#CaseDefinition_GetAll}

Gets the list of active CaseDefinitions

_Inputs_

FilterResults
:   Type: mandatory, [CaseDefinition_FilterResults](<#Structure_CaseDefinition_FilterResults>).  
    Filter Results

_Outputs_

CaseDefinitionDetailsList
:   Type: [CaseDefinition_Details](<#Structure_CaseDefinition_Details>) List.  
    List of CaseDefinition details

TotalResults
:   Type: Long Integer.  
    Number of total case definition results

### CaseDefinition_GetById {#CaseDefinition_GetById}

Gets a specific Case Definition by case identifier

_Inputs_

CaseDefinitionId
:   Type: mandatory, CaseDefinition Identifier.  
    Case Definition Identifier

_Outputs_

CaseDefinitionDetail
:   Type: [CaseDefinition_Details](<#Structure_CaseDefinition_Details>).  
    Case Definition details

### CaseDefinition_GetDetailByProcessDefinitionId {#CaseDefinition_GetDetailByProcessDefinitionId}

Gets the Case Definition details

_Inputs_

ProcessDefinitionId
:   Type: mandatory, Process_Definition Identifier.  
    Process Definition Identifier

_Outputs_

CaseDefinitionDetail
:   Type: [CaseDefinition_Details](<#Structure_CaseDefinition_Details>).  
    Case Definition details

### CaseDefinition_GetEligibleToPurge {#CaseDefinition_GetEligibleToPurge}

Get the case definitions that are eligible to purge, ie, without any case instance and which application is also deleted

_Outputs_

CaseDefinitionDetailsList
:   Type: [CaseDefinition_Details](<#Structure_CaseDefinition_Details>) List.  
    List of CaseDefinition details

### CaseDefinition_GetEntityId {#CaseDefinition_GetEntityId}

Gets the associated entity identifier

_Inputs_

CaseDefinitionId
:   Type: mandatory, CaseDefinition Identifier.  
    Case Definition Identifier

_Outputs_

EntityId
:   Type: Entity Identifier.  
    Entity Identifier

### CaseDefinition_GetInitialStatus {#CaseDefinition_GetInitialStatus}

Gets the initial status for a given case definition.

_Inputs_

CaseDefinitionId
:   Type: mandatory, CaseDefinition Identifier.  
    Case Definition Identifier

_Outputs_

CaseStatusId
:   Type: CaseStatus Identifier.  
    Case status Identifier

### CaseDefinition_GetProcessDefinitionId {#CaseDefinition_GetProcessDefinitionId}

Gets the associated process definition identifier

_Inputs_

CaseDefinitionId
:   Type: mandatory, CaseDefinition Identifier.  
    Case Definition Identifier

_Outputs_

ProcessDefinitionId
:   Type: Process_Definition Identifier.  
    Process Definition Identifier

### CaseDefinition_GetProcessDefinitionList {#CaseDefinition_GetProcessDefinitionList}

Gets the list of process definitions associated with case definitions

_Inputs_

FilterResults
:   Type: mandatory, [FilterResults](<#Structure_FilterResults>).  
    Filter Results

_Outputs_

ProcessDefinitionDetailsList
:   Type: [ProcessDefinition_Details](<#Structure_ProcessDefinition_Details>) List.  
    List about process definition

TotalResults
:   Type: Long Integer.  
    Number of total process definition SLA that match the criteiria

### CaseDefinition_GetStatusList {#CaseDefinition_GetStatusList}

Gets the list of all valid statuses for a given case definition.

_Inputs_

CaseDefinitionId
:   Type: mandatory, CaseDefinition Identifier.  
    Case Definition Identifier

_Outputs_

CaseStatusDetailsList
:   Type: [CaseStatus_Details](<#Structure_CaseStatus_Details>) List.  
    List of status details

### CaseDefinition_LinkToMilestoneDefinition {#CaseDefinition_LinkToMilestoneDefinition}

Sets a relation between a CaseDefinition and a MilestoneDefinition

_Inputs_

CaseDefinitionMilestoneDefinitionCreateRec
:   Type: mandatory, [CaseDefinitionMilestoneDefinition_Create](<#Structure_CaseDefinitionMilestoneDefinition_Create>).  
    CaseDefinitionMilestoneDefinition creation details

_Outputs_

CaseDefinitionMilestoneDefinitionId
:   Type: CaseDefinitionMilestoneDefinition Identifier.  
    CaseDefinitionMilestoneDefinition Identifier

### CaseDefinition_PreviewByProcessDefinition {#CaseDefinition_PreviewByProcessDefinition}

Previews the keys for the CaseDefinition based on a ProcessDefinition

_Inputs_

ProcessDefinitionId
:   Type: mandatory, Process_Definition Identifier.  
    Process Definition Identifier

_Outputs_

ProcessName
:   Type: Text.  
    Process Name

EntityId
:   Type: Entity Identifier.  
    Entity Identifier

### CaseDefinition_Purge {#CaseDefinition_Purge}

Purges a Case Definition

_Inputs_

CaseDefinitionId
:   Type: mandatory, CaseDefinition Identifier.  
    CaseDefinition Id

### CaseDefinition_UnlinkFromMilestoneDefinition {#CaseDefinition_UnlinkFromMilestoneDefinition}

Removes a relation between a CaseDefinition and a MilestoneDefinition

_Inputs_

CaseDefinitionMilestoneDefinitionCreateRec
:   Type: mandatory, [CaseDefinitionMilestoneDefinition_Create](<#Structure_CaseDefinitionMilestoneDefinition_Create>).  
    CaseDefinitionMilestoneDefinition creation details

### CaseDefinition_Update {#CaseDefinition_Update}

Updates an existing case definition

_Inputs_

CaseDefinitionUpdateRec
:   Type: mandatory, [CaseDefinition_CreateOrUpdate](<#Structure_CaseDefinition_CreateOrUpdate>).  
    Case Definition Details

### CaseStateMachine_Create {#CaseStateMachine_Create}

Creates a new State Machine entry

_Inputs_

CaseStateMachineCreateRec
:   Type: mandatory, [CaseStateMachine_Create](<#Structure_CaseStateMachine_Create>).  
    Case State Machine Details

_Outputs_

CaseStateMachineId
:   Type: CaseStateMachine Identifier.  
    Case State Machine Identifier

### CaseStateMachine_CreateOrUpdate {#CaseStateMachine_CreateOrUpdate}

Creates or updates a State Machine entry

_Inputs_

CaseStateMachineRec
:   Type: mandatory, [CaseStateMachine_CreateOrUpdate](<#Structure_CaseStateMachine_CreateOrUpdate>).  
    Case State Machine Details

_Outputs_

CaseStateMachineId
:   Type: CaseStateMachine Identifier.  
    Case State Machine Identifier

### CaseStateMachine_GetByTransition {#CaseStateMachine_GetByTransition}

Gets the case state machine record by status transition

_Inputs_

CaseStateMachineTransitionRec
:   Type: mandatory, [CaseStateMachine_Create](<#Structure_CaseStateMachine_Create>).  
    Case status transition

_Outputs_

CaseStateMachineDetails
:   Type: [CaseStateMachine_Details](<#Structure_CaseStateMachine_Details>).  
    Case state machine details

### CaseStateMachine_Purge {#CaseStateMachine_Purge}

Purge a Case State Machine

_Inputs_

CaseStateMachineId
:   Type: mandatory, CaseStateMachine Identifier.  
    CaseStateMachineId

### CaseStateMachine_Update {#CaseStateMachine_Update}

Updates an existing State Machine entry

_Inputs_

CaseStateMachineRec
:   Type: mandatory, [CaseStateMachine_CreateOrUpdate](<#Structure_CaseStateMachine_CreateOrUpdate>).  
    Case State Machine Details

### CaseStatus_Bootstrap {#CaseStatus_Bootstrap}

Will replace the existing case definiton statuses (or create if new) for a specific CaseDefinition

_Inputs_

CaseDefinitionId
:   Type: mandatory, CaseDefinition Identifier.  

CaseStatusList
:   Type: mandatory, [CaseStatus_CreateOrUpdate](<#Structure_CaseStatus_CreateOrUpdate>) List.  
    Case Status List

### CaseStatus_Create {#CaseStatus_Create}

Creates a new Case Status

_Inputs_

CaseStatusCreateRec
:   Type: mandatory, [CaseStatus_Create](<#Structure_CaseStatus_Create>).  
    Case Status Details

_Outputs_

CaseStatusId
:   Type: CaseStatus Identifier.  
    Case Status Identifier

### CaseStatus_CreateOrUpdate {#CaseStatus_CreateOrUpdate}

Creates or updates a Case Status

_Inputs_

CaseStatusRec
:   Type: mandatory, [CaseStatus_CreateOrUpdate](<#Structure_CaseStatus_CreateOrUpdate>).  
    Case Status Details

_Outputs_

CaseStatusId
:   Type: CaseStatus Identifier.  
    Case Status Identifier

### CaseStatus_Delete {#CaseStatus_Delete}

Deletes a Case Status

_Inputs_

CaseStatusId
:   Type: mandatory, CaseStatus Identifier.  
    Case Status Identifier

### CaseStatus_GetById {#CaseStatus_GetById}

Gets the status details by identifier

_Inputs_

Id
:   Type: mandatory, CaseStatus Identifier.  
    Status Identifier

_Outputs_

CaseStatusDetail
:   Type: [CaseStatus_Details](<#Structure_CaseStatus_Details>).  
    The details of an existing status

CaseStateMachineDetailList
:   Type: [CaseStateMachine_Details](<#Structure_CaseStateMachine_Details>) List.  
    State machine details

### CaseStatus_Update {#CaseStatus_Update}

Updates an existing Case Status

_Inputs_

CaseStatusUpdateRec
:   Type: mandatory, [CaseStatus_CreateOrUpdate](<#Structure_CaseStatus_CreateOrUpdate>).  
    Case Status Details

### CaseTag_Create {#CaseTag_Create}

Enables to create a CaseTag instance in the CaseTag entity

_Inputs_

CaseTagCreateRec
:   Type: mandatory, [CaseTag_Create](<#Structure_CaseTag_Create>).  
    Details for the creation of a new CaseTag record

_Outputs_

CaseTagId
:   Type: CaseTag Identifier.  
    CaseTag Identifier

### CheckApplicationStatus {#CheckApplicationStatus}

Check the status of an application

_Inputs_

CaseDefinitionId
:   Type: mandatory, CaseDefinition Identifier.  
    CaseDefinition Id

_Outputs_

StatusId
:   Type: CaseDefinitionStatus Identifier.  
    CaseDefinitionStatus Id

Message
:   Type: Text.  
    Message

### Delegation_Create {#Delegation_Create}

Creates a new Delegation

_Inputs_

DelegationCreateRec
:   Type: mandatory, [Delegation_Create](<#Structure_Delegation_Create>).  
    Delegation creation details

_Outputs_

DelegationId
:   Type: Delegation Identifier.  
    Id

### Delegation_CreateOrUpdate {#Delegation_CreateOrUpdate}

Creates or updates a delegation

_Inputs_

DelegationRec
:   Type: mandatory, [Delegation_Update](<#Structure_Delegation_Update>).  
    Delegation Record

_Outputs_

DelegationId
:   Type: Delegation Identifier.  
    Delegation Identifier

### Delegation_Delete {#Delegation_Delete}

Deletes an existing Delegation. Can only be removed by the user that created the delegation, if not it will raise an exception.

_Inputs_

DelegationId
:   Type: mandatory, Delegation Identifier.  
    Delegation identifier

### Delegation_Update {#Delegation_Update}

Updates an existing Delegation. Can only be updated by the user that created the delegation, if not it will raise an exc

_Inputs_

DelegationUpdateRec
:   Type: mandatory, [Delegation_Update](<#Structure_Delegation_Update>).  
    Record

### DEPRECATED_SetupCaseManagementApplication {#DEPRECATED_SetupCaseManagementApplication}

Sets up the basic configurations for a case management application

_Inputs_

SetupData
:   Type: mandatory, [DEPRECATED_SetupData](<#Structure_DEPRECATED_SetupData>).  
    Setup Data

### Email_ProcessPlaceholders {#Email_ProcessPlaceholders}

It will replace the placeholders by the actual case data

_Inputs_

CaseId
:   Type: mandatory, Case Identifier.  
    Case Id. CaseId or CaseDefinitionId/ObjectId must be fulfilled.

Text
:   Type: mandatory, Text.  
    Text to process

KeepUnknownTags
:   Type: optional, Boolean.  
    If True, tags that do no matches to a valid field will not be clear from the returned text.

IsPreviewMode
:   Type: optional, Boolean.  
    If is preview mode and CaseId empty sample values will be used

_Outputs_

TextProcessed
:   Type: Text.  
    Text replaced with the placeholders

### EmailTemplate_Create {#EmailTemplate_Create}

Creates an EmailTemplate object

_Inputs_

EmailTemplate_CreateOrUpdate
:   Type: mandatory, [EmailTemplate_CreateOrUpdate](<#Structure_EmailTemplate_CreateOrUpdate>).  
    EmailTemplate record

_Outputs_

EmailTemplateId
:   Type: EmailTemplate Identifier.  
    EmailTemplate Id

### EmailTemplate_CreateOrUpdate {#EmailTemplate_CreateOrUpdate}

Creates or updates an EmailTemplate object

_Inputs_

EmailTemplate_CreateOrUpdate
:   Type: mandatory, [EmailTemplate_CreateOrUpdate](<#Structure_EmailTemplate_CreateOrUpdate>).  
    EmailTemplate record

_Outputs_

EmailTemplateId
:   Type: EmailTemplate Identifier.  
    EmailTemplate Id

### EmailTemplate_GetAll {#EmailTemplate_GetAll}

Gets all EmailTemplates that matches the search criteria

_Inputs_

FilterResults
:   Type: mandatory, [FilterResults2](<#Structure_FilterResults2>).  
    Filter Results

CaseDefinitionId
:   Type: optional, CaseDefinition Identifier.  
    Case Definition Id

FetchBody
:   Type: optional, Boolean.  
    Is True, body content will also be retrieved

_Outputs_

EmailTemplateDetailsList
:   Type: [EmailTemplate_View](<#Structure_EmailTemplate_View>) List.  
    EmailTemplates list

TotalResults
:   Type: Long Integer.  
    Number of total groups that match the criteiria

### EmailTemplate_GetById {#EmailTemplate_GetById}

Gets a EmailTemplate by Id

_Inputs_

EmailTemplateId
:   Type: mandatory, EmailTemplate Identifier.  
    Email Template Id

_Outputs_

EmailTemplateDetailsList
:   Type: [EmailTemplate_View](<#Structure_EmailTemplate_View>).  
    EmailTemplates list

### EmailTemplate_Update {#EmailTemplate_Update}

Updates an EmailTemplate object

_Inputs_

EmailTemplate_CreateOrUpdate
:   Type: mandatory, [EmailTemplate_CreateOrUpdate](<#Structure_EmailTemplate_CreateOrUpdate>).  
    EmailTemplate record

### EntityAttr_GetByGlobalKey {#EntityAttr_GetByGlobalKey}

Gets the AttributeId based on it's GlobalKey

_Inputs_

GlobalKey
:   Type: mandatory, Text.  
    GlobalKey

_Outputs_

AttributeId
:   Type: Entity_Attr Identifier.  
    Attribute Id

### Espace_GetForActivityScreen {#Espace_GetForActivityScreen}

Gets list of modules/eSpaces that can have screens to an activity can be opened by

_Inputs_

FilterResults
:   Type: mandatory, [FilterResults_Espace](<#Structure_FilterResults_Espace>).  
    Filter Results

_Outputs_

EspaceDetailList
:   Type: [Espace_Detail](<#Structure_Espace_Detail>) List.  
    Contains all module/eSpace details list

TotalResults
:   Type: Long Integer.  
    Number of total module/eSpace that meet the criteria

### GetBusinessEntities {#GetBusinessEntities}

Gets the list of business entities based on a case definition

_Inputs_

CaseDefinitionId
:   Type: mandatory, CaseDefinition Identifier.  
    CaseDefinition Id

_Outputs_

BusinessEntities
:   Type: [BusinessEntity_View](<#Structure_BusinessEntity_View>) List.  
    List of Entities

### GetBusinessEntityAttributes {#GetBusinessEntityAttributes}

Gets the list of business entities attributes based on an entity

_Inputs_

CaseDefinitionId
:   Type: optional, CaseDefinition Identifier.  
    Case Definition Identifier

EntityId
:   Type: optional, Entity Identifier.  
    Entity Identifier

OnlyEligibleForUsers
:   Type: optional, Boolean.  
    If True, attributes that cannot be used on the engine rules or notification placeholder will be excluded (ex: Binary fields)

IncludePK
:   Type: mandatory, Boolean.  
    If true, the PK will be also returned

IncludeExtraAttributes
:   Type: mandatory, Boolean.  
    If true, extra attributes will be included if already configured to this CaseDefinitionId

IncludeRelated
:   Type: optional, Boolean.  
    If true, attributes from entities that have a FK to the biz entity will also be returned.

_Outputs_

BusinessEntityAttrs
:   Type: [BusinessEntityAttr_View](<#Structure_BusinessEntityAttr_View>) List.  
    Business Entity Attributes

### GetSystemDefaultDaysToPurge {#GetSystemDefaultDaysToPurge}

Gets the system sefault days to purge the case data

_Outputs_

Days
:   Type: Integer.  
    Number of Days

### GlobalKey_Parse {#GlobalKey_Parse}

Parses a GlobalKey

_Inputs_

GlobalKey
:   Type: mandatory, Text.  
    GlobalKey

_Outputs_

EspaceSSKey
:   Type: Text.  
    Espace SSKey

ObjectSSKey
:   Type: Text.  
    Local Object SSKey

### Group_AssignGroupToUser {#Group_AssignGroupToUser}

Assigns a user to a group

_Inputs_

GroupId
:   Type: mandatory, Group Identifier.  
    Group Identifier

UserId
:   Type: mandatory, User Identifier.  
    User Identifier

### Group_GetGroupsToAssociate {#Group_GetGroupsToAssociate}

Gets existing groups not associated with group extended that can be associated

_Outputs_

ListGroupDetails
:   Type: [Group_Details](<#Structure_Group_Details>) List.  
    Group Details

TotalResults
:   Type: Long Integer.  
    Number of total groups that match the criteiria

### Group_UnassignGroupFromUser {#Group_UnassignGroupFromUser}

Removes the user association fromo a group

_Inputs_

GroupId
:   Type: mandatory, Group Identifier.  
    Group Identifier

UserId
:   Type: mandatory, User Identifier.  
    User Identifier

### GroupExtended_CreateOrUpdate {#GroupExtended_CreateOrUpdate}

Creates or updates an existing Group Matrix

_Inputs_

GroupExtendedRec
:   Type: mandatory, [GroupExtended_CreateOrUpdate](<#Structure_GroupExtended_CreateOrUpdate>).  
    Group Extended Details

_Outputs_

GroupExtendedId
:   Type: GroupExtended Identifier.  

### GroupExtended_Delete {#GroupExtended_Delete}

Removes an existing Group Matrix. Can only be removed if no association exists to the group (activity, role or user association)

_Inputs_

GroupExtendedId
:   Type: mandatory, GroupExtended Identifier.  
    Group Extended Identifier

_Outputs_

IsSuccess
:   Type: Boolean.  
    If the group has been deleted

### Holiday_Create {#Holiday_Create}

Create a new calendar holiday associated to an existing calendar.

_Inputs_

HolidayCreateRec
:   Type: mandatory, [Holiday_Create](<#Structure_Holiday_Create>).  
    Calendar Holiday Creation Details

_Outputs_

HolidayId
:   Type: Holiday Identifier.  
    Holiday Identifier

### Holiday_CreateOrUpdate {#Holiday_CreateOrUpdate}

Action to create or update an event of a calendar

_Inputs_

CalendarHolidaytRec
:   Type: mandatory, [Holiday_Update](<#Structure_Holiday_Update>).  
    Calendar Holiday Details

_Outputs_

CalendarHolidayId
:   Type: Holiday Identifier.  
    The calendar holiday identifier

### Holiday_Delete {#Holiday_Delete}

Deletes an existing calendar holiday

_Inputs_

HolidayId
:   Type: mandatory, Holiday Identifier.  
    Calendar Holiday Identifier

### Holiday_Update {#Holiday_Update}

Updates an existing calendar holiday

_Inputs_

HolidayUpdateRec
:   Type: mandatory, [Holiday_Update](<#Structure_Holiday_Update>).  
    The calendar update details record.

### Hostname_Get {#Hostname_Get}

Gets Server Hostname

_Outputs_

Hostaname
:   Type: Text.  
    Server hostname

### ImportUserHierarchy_GetSample {#ImportUserHierarchy_GetSample}

Get a sample of the file content to perform an import

_Inputs_

TypeId
:   Type: mandatory, ImportFileType Identifier.  
    Type

_Outputs_

Content
:   Type: Binary Data.  
    Sample content

Filename
:   Type: Text.  
    Sample filename

### ImportUserHierarchy_GetStatus {#ImportUserHierarchy_GetStatus}

Check the status of an import request

_Inputs_

ImportId
:   Type: mandatory, Text.  
    Import Id Guid

ReturnErrors
:   Type: optional, Boolean.  
    If true, a list of errors for each record that failed will be returned.

_Outputs_

StatusId
:   Type: ImportDataStatus Identifier.  
    Import status

TotalProcessed
:   Type: Integer.  
    Total records that were processed

TotalErrors
:   Type: Integer.  
    Total records that were in error

ListOfErrors
:   Type: Text, Integer List.  
    List of erros (only returned in Return errors is set to True)

### Lookup_GetEntityRecords {#Lookup_GetEntityRecords}

Lookup an Entity

_Inputs_

EntityId
:   Type: mandatory, Entity Identifier.  
    Entity Id

PkValue
:   Type: optional, Text.  
    PK value

_Outputs_

Entity_Lookups
:   Type: [Entity_Lookup](<#Structure_Entity_Lookup>) List.  
    Entity Records

### Lookup_GetExtraFieldRecords {#Lookup_GetExtraFieldRecords}

Lookup an Extra field value

_Inputs_

CaseDefinitionId
:   Type: mandatory, CaseDefinition Identifier.  
    Case Definition Identifier

ExtraFieldId
:   Type: mandatory, ExtraField Identifier.  
    Extra Field Identifier

_Outputs_

Entity_Lookups
:   Type: [Entity_Lookup](<#Structure_Entity_Lookup>) List.  
    Entity Records

### MilestoneDefinition_Create {#MilestoneDefinition_Create}

Creates a new milestone definition

_Inputs_

MilestoneDefinitionCreateRec
:   Type: mandatory, [MilestoneDefinition_CreateOrUpdate](<#Structure_MilestoneDefinition_CreateOrUpdate>).  
    Milestone Definition Details

_Outputs_

MilestoneDefinitionId
:   Type: MilestoneDefinition Identifier.  
    Milestone Definition Identifier

### MilestoneDefinition_CreateOrUpdate {#MilestoneDefinition_CreateOrUpdate}

Creates or updates a milestone definition

_Inputs_

MilestoneDefinitionRec
:   Type: mandatory, [MilestoneDefinition_CreateOrUpdate](<#Structure_MilestoneDefinition_CreateOrUpdate>).  
    Milestone Definition Details

_Outputs_

MilestoneDefinitionId
:   Type: MilestoneDefinition Identifier.  
    Milestone Definition Identifier

### MilestoneDefinition_Delete {#MilestoneDefinition_Delete}

Inactivates an existing milestone definition

_Inputs_

MilestoneDefinitionId
:   Type: optional, MilestoneDefinition Identifier.  
    Milestone Definition Identifier

### MilestoneDefinition_Update {#MilestoneDefinition_Update}

Updates an existing milestone definition

_Inputs_

MilestoneDefinitionUpdateRec
:   Type: mandatory, [MilestoneDefinition_CreateOrUpdate](<#Structure_MilestoneDefinition_CreateOrUpdate>).  
    Milestone Definition Details

### NonWorkingDay_Create {#NonWorkingDay_Create}

Create a new calendar non working day associated to an existing calendar

_Inputs_

NonWorkingDayCreateRec
:   Type: mandatory, [NonWorkingDay_Create](<#Structure_NonWorkingDay_Create>).  
    Calendar Non Working Day Creation Details

_Outputs_

NonWorkingDayId
:   Type: NonWorkingDay Identifier.  
    Calendar Holiday Identifier

### NonWorkingDay_CreateOrUpdate {#NonWorkingDay_CreateOrUpdate}

Action to create or update a non working day associated to an existing calendar

_Inputs_

CalendarNonWorkingDaytRec
:   Type: mandatory, [NonWorkingDay_Update](<#Structure_NonWorkingDay_Update>).  
    The calendar non working day record

_Outputs_

CalendarNonWorkingDayId
:   Type: NonWorkingDay Identifier.  
    The calendar non working day identifier

### NonWorkingDay_Delete {#NonWorkingDay_Delete}

Deletes an existing calendar non working day

_Inputs_

NonWorkingDayId
:   Type: mandatory, NonWorkingDay Identifier.  
    Calendar Non Working Day Identifier

### NonWorkingDay_Update {#NonWorkingDay_Update}

Updates an existiing calendar non working day

_Inputs_

NonWorkingDayUpdateRec
:   Type: mandatory, [NonWorkingDay_Update](<#Structure_NonWorkingDay_Update>).  
    The calendar non working day update details record.

### NotificationsEngine_InitializeStaging {#NotificationsEngine_InitializeStaging}

It will mark all entries as deleted for the staging process after only import the active ones

_Inputs_

CaseDefinitionId
:   Type: optional, CaseDefinition Identifier.  
    If defined will only inactive the entries for that case definition

### PreDefinedTemplate_Create {#PreDefinedTemplate_Create}

Creates a PredefinedTemplate object

_Inputs_

PreDefinedTemplate_CreateOrUpdate
:   Type: mandatory, [PreDefinedTemplate_CreateOrUpdate](<#Structure_PreDefinedTemplate_CreateOrUpdate>).  
    PreDefinedTemplate record

_Outputs_

PreDefinedTemplateId
:   Type: PreDefinedTemplate Identifier.  
    PreDefinedTemplate Id

### PreDefinedTemplate_CreateOrUpdate {#PreDefinedTemplate_CreateOrUpdate}

Creates or updates a PredefinedTemplate object

_Inputs_

PreDefinedTemplate_CreateOrUpdate
:   Type: mandatory, [PreDefinedTemplate_CreateOrUpdate](<#Structure_PreDefinedTemplate_CreateOrUpdate>).  
    PreDefinedTemplate record

_Outputs_

PreDefinedTemplateId
:   Type: PreDefinedTemplate Identifier.  
    PreDefinedTemplate Id

### PreDefinedTemplate_GetAll {#PreDefinedTemplate_GetAll}

Gets all predefined templates

_Inputs_

LoadBody
:   Type: mandatory, Boolean.  
    Is True, body content will also be retrieved

_Outputs_

PreDefinedTemplateDetailList
:   Type: [PreDefinedTemplate_View](<#Structure_PreDefinedTemplate_View>) List.  
    List of PreDefined Templates

### PreDefinedTemplate_GetById {#PreDefinedTemplate_GetById}

Gets a predefined template

_Inputs_

PreDefinedTemplateId
:   Type: mandatory, PreDefinedTemplate Identifier.  
    PreDefinedTemplate Id

_Outputs_

PreDefinedTemplateDetail
:   Type: [PreDefinedTemplate_View](<#Structure_PreDefinedTemplate_View>).  
    PreDefined Template

### PreDefinedTemplate_Update {#PreDefinedTemplate_Update}

Updates a PredefinedTemplate object

_Inputs_

PreDefinedTemplate_CreateOrUpdate
:   Type: mandatory, [PreDefinedTemplate_CreateOrUpdate](<#Structure_PreDefinedTemplate_CreateOrUpdate>).  
    PreDefinedTemplate record

### Resource_CreateOrUpdate {#Resource_CreateOrUpdate}

Creates or Updates a Resource

_Inputs_

ResourceCreateOrUpdate
:   Type: mandatory, [Resource_CreateOrUpdate](<#Structure_Resource_CreateOrUpdate>).  
    Resource to create or update

_Outputs_

Id
:   Type: Resource Identifier.  
    Resource Id

### Resource_Delete {#Resource_Delete}

Deletes a Resource

_Inputs_

Id
:   Type: mandatory, Resource Identifier.  
    Id

### Resource_GetById {#Resource_GetById}

Gets a Resource by Id

_Inputs_

Id
:   Type: mandatory, Resource Identifier.  
    Id

_Outputs_

ResourceDetail
:   Type: [Resource_View](<#Structure_Resource_View>).  
    Resource detail

### Resource_Purge {#Resource_Purge}

Resource hard delete

_Inputs_

Id
:   Type: mandatory, Resource Identifier.  
    Id

### Resources_GetAll {#Resources_GetAll}

Gets All Resources

_Inputs_

CaseDefinitionId
:   Type: optional, Text.  
    CaseDefinition Id

LoadBinaryData
:   Type: mandatory, Boolean.  
    If true, Binary data will also be loaded

OnlyActive
:   Type: optional, Boolean.  
    Only Active

_Outputs_

ResourceDetailsList
:   Type: [Resource_View](<#Structure_Resource_View>) List.  
    List of Resource

### Resources_InitializeStaging {#Resources_InitializeStaging}

It will mark all entries as deleted for the staging process after only import the active ones

_Inputs_

CaseDefinitionId
:   Type: optional, Text.  
    If defined will only inactive the entries for that case definition

### Rule_Create {#Rule_Create}

Create a Rule record

_Inputs_

RuleRec
:   Type: mandatory, [Rule_CreateOrUpdate](<#Structure_Rule_CreateOrUpdate>).  
    Rule record

_Outputs_

Rule
:   Type: [Rule_View](<#Structure_Rule_View>).  
    Rule record created or updated

### Rule_CreateOrUpdate {#Rule_CreateOrUpdate}

Create or update a Rule record

_Inputs_

RuleRec
:   Type: mandatory, [Rule_CreateOrUpdate](<#Structure_Rule_CreateOrUpdate>).  
    Rule record

_Outputs_

Rule
:   Type: [Rule_View](<#Structure_Rule_View>).  
    Rule record created or updated

### Rule_Delete {#Rule_Delete}

Deletes a whole rule

_Inputs_

RuleId
:   Type: mandatory, Rule Identifier.  
    Rule Id

### Rule_Update {#Rule_Update}

Update a Rule record

_Inputs_

RuleRec
:   Type: mandatory, [Rule_CreateOrUpdate](<#Structure_Rule_CreateOrUpdate>).  
    Rule record

_Outputs_

Rule
:   Type: [Rule_View](<#Structure_Rule_View>).  
    Rule record created or updated

### RuleGroup_Create {#RuleGroup_Create}

Create a Rule Group record

_Inputs_

RuleGroup_Record
:   Type: mandatory, [RuleGroup_CreateOrUpdate](<#Structure_RuleGroup_CreateOrUpdate>).  
    RuleGroup record

_Outputs_

Id
:   Type: RuleGroup Identifier.  
    RuleGroup Id

### RuleGroup_CreateOrUpdate {#RuleGroup_CreateOrUpdate}

Create or update a Rule Group record

_Inputs_

RuleGroup_Record
:   Type: mandatory, [RuleGroup_CreateOrUpdate](<#Structure_RuleGroup_CreateOrUpdate>).  
    RuleGroup record

_Outputs_

Id
:   Type: RuleGroup Identifier.  
    RuleGroup Id

### RuleGroup_Delete {#RuleGroup_Delete}

Deletes a Rule Group

_Inputs_

RuleGroupId
:   Type: mandatory, RuleGroup Identifier.  
    RuleGroup Id

### RuleGroup_DeleteAllByRuleId {#RuleGroup_DeleteAllByRuleId}

Deletes all Rule Group from a Rule

_Inputs_

RuleId
:   Type: mandatory, Rule Identifier.  
    Rule Id

### RuleGroup_Update {#RuleGroup_Update}

Update a Rule Group record

_Inputs_

RuleGroup_Record
:   Type: mandatory, [RuleGroup_CreateOrUpdate](<#Structure_RuleGroup_CreateOrUpdate>).  
    RuleGroup record

### RuleGroupOutput_CreateOrUpdate {#RuleGroupOutput_CreateOrUpdate}

Create or update a Rule Group Output record

_Inputs_

RuleGroupOutputRec
:   Type: mandatory, [RuleGroupOutput_CreateOrUpdate](<#Structure_RuleGroupOutput_CreateOrUpdate>).  
    RuleGroupOutput record

_Outputs_

RuleGroupOutput_View
:   Type: [RuleGroupOutput_View](<#Structure_RuleGroupOutput_View>).  
    RuleGroupOutput record created or updated

### RuleLine_CreateOrUpdate {#RuleLine_CreateOrUpdate}

Creates or updates a Rule Line

_Inputs_

RuleLineRec
:   Type: mandatory, [RuleLine_CreateOrUpdate](<#Structure_RuleLine_CreateOrUpdate>).  
    RuleLine record

_Outputs_

RuleLine_View
:   Type: [RuleLine_View](<#Structure_RuleLine_View>).  
    RuleLine record created or updated

### RuleLine_Delete {#RuleLine_Delete}

Deletes a RuleLine

_Inputs_

RuleLineId
:   Type: mandatory, RuleLine Identifier.  
    RuleLine Id

### Rules_GetAll {#Rules_GetAll}

Get all rules available

_Inputs_

CaseDefinitionId
:   Type: mandatory, CaseDefinition Identifier.  
    Case Definition Id

_Outputs_

RulesLst
:   Type: [Rule_View](<#Structure_Rule_View>) List.  
    Rules list

### Rules_GetById {#Rules_GetById}

Get a rule by Id

_Inputs_

RuleId
:   Type: mandatory, Rule Identifier.  
    Rule Id

_Outputs_

Rule
:   Type: [Rule_View](<#Structure_Rule_View>).  
    Rule record

### Rules_InitializeStaging {#Rules_InitializeStaging}

It will mark all entries as deleted for the staging process after only import the active ones

_Inputs_

CaseDefinitionId
:   Type: optional, CaseDefinition Identifier.  
    If defined will only inactive the entries for that case definition

### RulesGroup_GetAll {#RulesGroup_GetAll}

Get all RuleGroups from a Rule

_Inputs_

RuleId
:   Type: optional, Rule Identifier.  
    Rule Id

RuleGroupId
:   Type: optional, RuleGroup Identifier.  
    RuleGroup Id

_Outputs_

RuleGroups
:   Type: [RuleGroup_View](<#Structure_RuleGroup_View>) List.  
    RuleGroups record list

### RulesOperator_GetBySettingType {#RulesOperator_GetBySettingType}

Returns the operations available for the respective setting type

_Inputs_

SettingTypeId
:   Type: mandatory, SettingType Identifier.  
    SettingType Id

_Outputs_

RuleOperators
:   Type: [RuleOperator](<#Structure_RuleOperator>) List.  
    List of permited Rule Operations

### SampleUser_CreateOrUpdate {#SampleUser_CreateOrUpdate}

Create sample users (verifiy if is a second publish and disable all users before create news) and associate to its role and to its group (if applicable).

_Inputs_

CaseDefinitionId
:   Type: mandatory, CaseDefinition Identifier.  
    Case Definition Id

RequesterGroupId
:   Type: mandatory, GroupExtended Identifier.  
    Requester Group Id

OperatorGroupsId
:   Type: mandatory, GroupExtended Identifier List.  
    Groups to associate the user to

AdministratorGroupId
:   Type: mandatory, GroupExtended Identifier.  
    Administrator Group Id

CreateRequesterManager
:   Type: mandatory, Boolean.  
    True if Requester Manager user need to be created

CreateAdministrator
:   Type: mandatory, Boolean.  
    True if Administrator user needs to be created

### Setting_ConvertSetting {#Setting_ConvertSetting}

Converts a Setting value to an CreateOrUpdate structure

_Inputs_

SettingValue
:   Type: mandatory, [Setting_Value](<#Structure_Setting_Value>).  
    Setting properties

_Outputs_

SettingCreateOrUpdate
:   Type: [Setting_CreateOrUpdate](<#Structure_Setting_CreateOrUpdate>).  
    Setting details after conversion

### Setting_CreateOrUpdate {#Setting_CreateOrUpdate}

Public action that enables to create or update a setting

_Inputs_

SettingRec
:   Type: mandatory, [Setting_CreateOrUpdate](<#Structure_Setting_CreateOrUpdate>).  
    Details to create or update a setting

_Outputs_

SettingId
:   Type: Setting Identifier.  
    Setting Id

### Setting_Delete {#Setting_Delete}

Public action that deletes a setting

_Inputs_

SettingId
:   Type: mandatory, Setting Identifier.  
    Setting Id

### Setting_DeleteList {#Setting_DeleteList}

Public action that deletes a list of settings

_Inputs_

SettingIds
:   Type: mandatory, Setting Identifier List.  
    Setting Id

### Setting_GetById {#Setting_GetById}

Gets a Setting by it's Id

_Inputs_

SettingId
:   Type: mandatory, Setting Identifier.  
    Setting Id

_Outputs_

SettingValue
:   Type: [Setting_Value](<#Structure_Setting_Value>).  
    Setting record

### Setting_Purge {#Setting_Purge}

Public action to hard delete a setting

_Inputs_

SettingId
:   Type: mandatory, Setting Identifier.  
    Setting Id

### SettingType_GetByColumnType {#SettingType_GetByColumnType}

Gets the attribute setting type

_Inputs_

AttributeId
:   Type: optional, Entity_Attr Identifier.  
    Attribute Id

AttributeType
:   Type: optional, Text.  
    rt Type (from Entity_Attr)

EvaluateFKTargetType
:   Type: mandatory, Boolean.  
    If true, when the Attribute it's a FK will check the basic type of the Attribute

_Outputs_

SettingTypeId
:   Type: SettingType Identifier.  
    SettingType Id

IsFK
:   Type: Boolean.  
    If true, the Attribute it's a FK

TargetEntityId
:   Type: Entity Identifier.  
    EntityId, only calculated then it's a FK and EvaluateFKTargetType is set to True

### Tag_Create {#Tag_Create}

Enables to create a Tag instance in the Tag entity

_Inputs_

TagCreateRec
:   Type: mandatory, [Tag_Create](<#Structure_Tag_Create>).  
    Details for the creation of a new Tag record

_Outputs_

TagId
:   Type: Tag Identifier.  
    Tag Identifier

### Tag_Delete {#Tag_Delete}

Asynchronously deletes all CaseTag records for a given Tag before deleting the Tag itself. Saves in each case's History each tag deletion.

_Inputs_

TagId
:   Type: mandatory, Tag Identifier.  
    Tag Identifier

### Tag_Update {#Tag_Update}

Enables to update a Tag instance in the Tag entity

_Inputs_

TagUpdateRec
:   Type: mandatory, [Tag_Update](<#Structure_Tag_Update>).  
    Details for the update of a Tag record

_Outputs_

TagId
:   Type: Tag Identifier.  
    Tag Identifier

### UserExtended_CreateOrUpdate {#UserExtended_CreateOrUpdate}

Creates or updates an User extended record

_Inputs_

UserExtendedRec
:   Type: mandatory, [UserExtended_CreateOrUpdate](<#Structure_UserExtended_CreateOrUpdate>).  
    User extended info

### UserHierarchy_Import {#UserHierarchy_Import}

Submits a requests to import user's hierarchy

_Inputs_

IsIgnoreEmpty
:   Type: optional, Boolean.  
    If there is a reporter not filled in if is true, should not clear the value for the user. If false, should clear the reporter.

Content
:   Type: mandatory, Binary Data.  
    Binary content

ContentTypeId
:   Type: mandatory, ImportFileType Identifier.  
    ContentTypeId

_Outputs_

ImportId
:   Type: Text.  
    Import request Guid

## Service Actions

### SetupCaseManagementApplication {#Service_SetupCaseManagementApplication}

Sets up the basic configurations for a case management application

_Inputs_

SetupData
:   Type: mandatory, [SetupData](<#Structure_SetupData>).  
    Setup Data

## Structures

### BusinessEntity_View {#Structure_BusinessEntity_View}

View for business entities

_Attributes_

EntityId
:   Type: Entity Identifier.  
    Entity Id

Name
:   Type: Text.  
    Name

### BusinessEntityAttr_View {#Structure_BusinessEntityAttr_View}

View for business entities attributes

_Attributes_

AttributeName
:   Type: Text.  
    Entity Attribute Name

AttributeId
:   Type: Entity_Attr Identifier.  
    Entity Attribute Id

EntityName
:   Type: Text.  
    Entity Name

EntityId
:   Type: Entity Identifier.  
    Entity Id

AttrLabel
:   Type: Text.  
    Attribute Label

Label
:   Type: Text.  
    Label to be displayed in the UI

ExtraFieldId
:   Type: ExtraField Identifier.  
    Extra field identifier

FollowFK
:   Type: Boolean.  
    If it's a FK follow the FK to fetch the value

IsFromBusinessEntity
:   Type: Boolean.  
    Is From Business Entity

### Calendar_Create {#Structure_Calendar_Create}

Public structure to create a new Calendar

_Attributes_

Id
:   Type: Calendar Identifier.  
    Calendar Identifier

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
    Timezone for calendar

### Calendar_Update {#Structure_Calendar_Update}

Public structure to update an existing Calendar

_Attributes_

Id
:   Type: Calendar Identifier.  
    Calendar Identifier

Name
:   Type: Text (50).  
    Name

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
    Timezone for calendar

IsActive
:   Type: Boolean.  
    If is active

### CaseAction_CreateOrUpdate {#Structure_CaseAction_CreateOrUpdate}

Public structure to create or update a Case Workflow Action

_Attributes_

Id
:   Type: CaseAction Identifier.  
    Identifier

Label
:   Type: Text (100).  
    Label

CaseDefinitionId
:   Type: CaseDefinition Identifier.  
    Case Definition Id

CaseStatusId
:   Type: CaseStatus Identifier.  
    Case Status Id

IsActive
:   Type: Boolean.  

TranslationList
:   Type: [CaseAction_Translation](<#Structure_CaseAction_Translation>) List.  

### CaseAction_Translation {#Structure_CaseAction_Translation}

Translation structure for Case action

_Attributes_

Locale
:   Type: Text (10).  
    Locale

Label
:   Type: Text (100).  
    Label

### CaseAction_View {#Structure_CaseAction_View}

View for Case Workflow Action

_Attributes_

Id
:   Type: Text (36).  
    Identifier

Label
:   Type: Text (100).  
    Label

CaseDefinitionId
:   Type: CaseDefinition Identifier.  
    Case Definition Id

CaseStatusId
:   Type: CaseStatus Identifier.  
    Case Status Id

IsActive
:   Type: Boolean.  
    If the record is active

### CaseConfigurationBootstrap {#Structure_CaseConfigurationBootstrap}

Holds the bootstrap data

_Attributes_

CaseDefinition
:   Type: [CaseDefinition_CreateOrUpdate](<#Structure_CaseDefinition_CreateOrUpdate>).  
    Case Definition

RuleConfigList
:   Type: [RuleConfig](<#Structure_RuleConfig>) List.  
    Rule Config List

GroupMatrixRecList
:   Type: [GroupExtended_CreateOrUpdate](<#Structure_GroupExtended_CreateOrUpdate>) List.  
    Group extended  Details

StatusList
:   Type: [CaseStatus_CreateOrUpdate](<#Structure_CaseStatus_CreateOrUpdate>) List.  
    List of status to create or update

CaseActionList
:   Type: [CaseAction_CreateOrUpdate](<#Structure_CaseAction_CreateOrUpdate>) List.  
    List of workflow actions to bootstrap

EmailNotificationList
:   Type: [EmailTemplate_CreateOrUpdate](<#Structure_EmailTemplate_CreateOrUpdate>) List.  
    Notifications emails list

CaseResourceList
:   Type: [Resource_CreateOrUpdate](<#Structure_Resource_CreateOrUpdate>) List.  

EspaceId
:   Type: Espace Identifier.  
    Conf module Id of the end user app

CreateSampleUsers
:   Type: Boolean.  
    If it's to create sample users

HasRequesterManager
:   Type: Boolean.  
    If True, the application has associated requester manager (user hierarchy). Enables to create requester manager sample user.

Requester_RoleId
:   Type: Role Identifier.  
    Requester Role Id

Operator_RoleId
:   Type: Role Identifier.  
    Operator Role Id

Admin_RoleId
:   Type: Role Identifier.  
    Administrator Role Id

### CaseDefinition_Create {#Structure_CaseDefinition_Create}

Public structure to create a new case definition

_Attributes_

Id
:   Type: CaseDefinition Identifier.  
    Case Identifier

Name
:   Type: Text (50).  
    Case Name

Description
:   Type: Text (200).  
    Case description

EntityId
:   Type: Entity Identifier.  
    Entity Id

CalendarId
:   Type: Calendar Identifier.  
    Associated calendar identifier

PurgeTypeId
:   Type: PurgeType Identifier.  
    Option of purge type for current case definition

DaysToPurge
:   Type: Integer.  
    After a case is closed, number of days to keep the data in the system until being deleted.  
    &lt; 0 : Never purge  
    0   : Use system defaults  
    &gt; 0 : number of days

DaysToProcessPurge
:   Type: Integer.  
    After a case is closed, number of days to keep the process data in the system until being deleted.

IsAccessControl
:   Type: Boolean.  
    If the case definition is under access control

StatusId
:   Type: CaseDefinitionStatus Identifier.  
    Case definition status Id

TranslationList
:   Type: [CaseDefinition_Translation](<#Structure_CaseDefinition_Translation>) List.  

### CaseDefinition_CreateOrUpdate {#Structure_CaseDefinition_CreateOrUpdate}

Public structure to create a new case definition or to update an existing case definition

_Attributes_

Id
:   Type: CaseDefinition Identifier.  
    Case Identifier

Name
:   Type: Text (50).  
    Case Name

Description
:   Type: Text (200).  
    Case description

EntityId
:   Type: Entity Identifier.  
    Entity Id

CalendarId
:   Type: Calendar Identifier.  
    Associated calendar identifier

IsAccessControl
:   Type: Boolean.  
    If the case definition is under access control

PurgeTypeId
:   Type: PurgeType Identifier.  
    Option of purge type for current case definition

DaysToPurge
:   Type: Integer.  
    After a case is closed, number of days to keep the data in the system until being deleted.  
    &lt; 0 : Never purge  
    0   : Use system defaults  
    &gt; 0 : number of days

DaysToProcessPurge
:   Type: Integer.  
    After a case is closed, number of days to keep the process data in the system until being deleted.

StatusId
:   Type: CaseDefinitionStatus Identifier.  
    Case definition status Id

IsActive
:   Type: Boolean.  
    If the case is active

TranslationList
:   Type: [CaseDefinition_Translation](<#Structure_CaseDefinition_Translation>) List.  

### CaseDefinition_Details {#Structure_CaseDefinition_Details}

Public structure that contains the case defintion details

_Attributes_

Id
:   Type: CaseDefinition Identifier.  
    Case Identifier

Name
:   Type: Text (50).  
    Case Name

Description
:   Type: Text (200).  
    Case description

ProcessDefinitionId
:   Type: Process_Definition Identifier.  
    Process Definition Id

EntityId
:   Type: Entity Identifier.  
    Entity Id

CalendarId
:   Type: Calendar Identifier.  
    Associated calendar identifier

IsAccessControl
:   Type: Boolean.  
    If the case definition is under access control

ProcessDefinitionGlobalKey
:   Type: Text.  
    ProcessDefinition GlobalKey

EntityGlobalKey
:   Type: Text.  
    Entity GlobalKey

PurgeTypeId
:   Type: PurgeType Identifier.  
    Option of purge type for current case definition

DaysToPurge
:   Type: Integer.  
    After a case is closed, number of days to keep the data in the system until being deleted.  
    &lt; 0 : Never purge  
    0   : Use system defaults  
    &gt; 0 : number of days

DaysToProcessPurge
:   Type: Integer.  
    After a case is closed, number of days to keep the process data in the system until being deleted.

StatusId
:   Type: CaseDefinitionStatus Identifier.  
    Case definition status Id

IsActive
:   Type: Boolean.  
    If the case definition is active

### CaseDefinition_FilterResults {#Structure_CaseDefinition_FilterResults}

Filter Serch Structure

_Attributes_

PageNumber
:   Type: Integer.  
    Page number

MaxResultsPerPage
:   Type: Integer.  
    Number of results per page

OnlyActive
:   Type: Boolean.  
    Only active results

CaseName
:   Type: Text (50).  
    Case definition name

### CaseDefinition_Translation {#Structure_CaseDefinition_Translation}

Translation structure for Case definition

_Attributes_

Locale
:   Type: Text (10).  
    Locale

Name
:   Type: Text (50).  
    Name

Description
:   Type: Text (200).  
    Case description

### CaseDefinitionMilestoneDefinition_Create {#Structure_CaseDefinitionMilestoneDefinition_Create}

Public structure for the Creation of a CaseDefinitionMilestoneDefinition record

_Attributes_

CaseDefinitionId
:   Type: CaseDefinition Identifier.  
    Case Definition identifier

MilestoneDefinitionId
:   Type: MilestoneDefinition Identifier.  
    Milestone Definition Identifier

### CaseStateMachine_Create {#Structure_CaseStateMachine_Create}

Public structure for state machine creation

_Attributes_

CaseStatusId
:   Type: CaseStatus Identifier.  
    CaseStatus identifier

NextCaseStatusId
:   Type: CaseStatus Identifier.  
    The next status transition

### CaseStateMachine_CreateOrUpdate {#Structure_CaseStateMachine_CreateOrUpdate}

Structure to enable case state machine creation or update

_Attributes_

Id
:   Type: CaseStateMachine Identifier.  
    Status Machine Unique Text Identifier

CaseStatusId
:   Type: CaseStatus Identifier.  
    CaseStatus identifier

NextCaseStatusId
:   Type: CaseStatus Identifier.  
    The next case status transition

IsActive
:   Type: Boolean.  
    True if Status transition is active, false otherwise

### CaseStateMachine_Details {#Structure_CaseStateMachine_Details}

Case State Machine Details

_Attributes_

Id
:   Type: CaseStateMachine Identifier.  
    Status Machine Unique Text Identifier

CaseStatusId
:   Type: CaseStatus Identifier.  
    CaseStatus identifier

NextCaseStatusId
:   Type: CaseStatus Identifier.  
    The next case status transition

IsActive
:   Type: Boolean.  
    True if status transition is active, false otherwise

### CaseStatus_Create {#Structure_CaseStatus_Create}

Public structure to create a new status

_Attributes_

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

TranslationList
:   Type: [CaseStatus_Translation](<#Structure_CaseStatus_Translation>) List.  

### CaseStatus_CreateOrUpdate {#Structure_CaseStatus_CreateOrUpdate}

Public structure to create or update a status

_Attributes_

Id
:   Type: CaseStatus Identifier.  
    Status Unique Identifier

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

TranslationList
:   Type: [CaseStatus_Translation](<#Structure_CaseStatus_Translation>) List.  

### CaseStatus_Details {#Structure_CaseStatus_Details}

Case Status Detail

_Attributes_

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

### CaseStatus_Translation {#Structure_CaseStatus_Translation}

Translation structure for Case status

_Attributes_

Locale
:   Type: Text (10).  
    Locale

Name
:   Type: Text (50).  
    Name

Alias
:   Type: Text (50).  
    Alias

### CaseTag_Create {#Structure_CaseTag_Create}

Public structure that enables to create CaseTage instances

_Attributes_

CaseId
:   Type: Case Identifier.  
    Case Identifier

TagId
:   Type: Tag Identifier.  
    Tag Identifier

### Delegation_Create {#Structure_Delegation_Create}

Holds a Delegation entry to be created

_Attributes_

From
:   Type: Date Time.  
    Initial date of delegation

To
:   Type: Date Time.  
    Final date of delegation

FromUserId
:   Type: User Identifier.  
    Delegation UserId

FromGroupId
:   Type: Group Identifier.  
    Delegation GroupId (FromGroupId or FromGroupMatrixId must be set)

FromGroupExtendedId
:   Type: GroupExtended Identifier.  
    Group Extended Id (FromGroupId or FromGroupMatrixId must be set)

ToUserId
:   Type: User Identifier.  
    Delegated UserId

IsActive
:   Type: Boolean.  
    If is active

### Delegation_Update {#Structure_Delegation_Update}

Holds a Delegation details for update

_Attributes_

DelegationId
:   Type: Delegation Identifier.  
    Delegation Identifier

From
:   Type: Date Time.  
    Initial date of delegation

To
:   Type: Date Time.  
    Final date of delegation

FromUserId
:   Type: User Identifier.  
    Delegation UserId

FromGroupId
:   Type: Group Identifier.  
    Delegation GroupId (FromGroupId or FromGroupMatrixId must be set)

FromGroupExtendedId
:   Type: GroupExtended Identifier.  
    Group Extended Id (FromGroupId or FromGroupMatrixId must be set)

ToUserId
:   Type: User Identifier.  
    Delegated UserId

IsActive
:   Type: Boolean.  
    If the delegation is active

### DEPRECATED_SetupData {#Structure_DEPRECATED_SetupData}

Holds the basic setup data for a case management application

_Attributes_

BusinessEntityEspaceId
:   Type: Espace Identifier.  
    The Identifier of the module/eSpace where your business entity is defined, use the GetOwnerEspaceId() built-in function if the entity is defined in the same module/eSpace where the setup action will be run

CaseDefinition
:   Type: [Setup_CaseDefinition](<#Structure_Setup_CaseDefinition>).  
    Holds the data to setup a Case Definition

CaseStatusList
:   Type: [Setup_CaseStatus](<#Structure_Setup_CaseStatus>) List.  
    Holds the data to setup a list of Case Statuses

CaseStateMachineList
:   Type: [Setup_CaseStateMachine](<#Structure_Setup_CaseStateMachine>) List.  
    Holds the data to setup a list of Case State Machine transitions

CaseActionList
:   Type: [Setup_CaseAction](<#Structure_Setup_CaseAction>) List.  
    Holds the data to setup a list of Case Actions

EmailTemplateList
:   Type: [Setup_EmailTemplate](<#Structure_Setup_EmailTemplate>) List.  
    Holds the data to setup a list of Email Templates

### EmailTemplate_CreateOrUpdate {#Structure_EmailTemplate_CreateOrUpdate}

Represents a EmailTemplate object to be updated

_Attributes_

Id
:   Type: EmailTemplate Identifier.  
    Email Template Identifier

CaseDefinitionId
:   Type: CaseDefinition Identifier.  
    Case Definition Identifier

Name
:   Type: Text (20).  
    Name of the template

Subject
:   Type: Text (256).  
    The email subject

FromDisplayName
:   Type: Text (250).  
    Email From Name

FromEmail
:   Type: Email.  
    Email From

IsActive
:   Type: Boolean.  
    If is active

EmailBody
:   Type: Text (50000).  
    Email Body

### EmailTemplate_View {#Structure_EmailTemplate_View}

Represents a EmailTemplate object

_Attributes_

Id
:   Type: EmailTemplate Identifier.  
    Email Template Identifier

CaseDefinitionId
:   Type: CaseDefinition Identifier.  
    Case Definition Identifier

Name
:   Type: Text (200).  
    Name of the template

Subject
:   Type: Text (256).  
    The email subject

FromDisplayName
:   Type: Text (250).  
    Email From Name

FromEmail
:   Type: Email.  
    Email From

IsActive
:   Type: Boolean.  
    If is active

EmailBody
:   Type: Text (50000).  
    Email Body

CreatedBy
:   Type: User Identifier.  
    Created DateTime

CreatedOn
:   Type: Date Time.  
    Created On

UpdatedBy
:   Type: User Identifier.  
    Updated by

UpdatedOn
:   Type: Date Time.  
    Updated On

### Entity_Lookup {#Structure_Entity_Lookup}

Entity to lookup FK

_Attributes_

Key
:   Type: Text.  
    Key

Value
:   Type: Text.  
    Value

### Espace_Detail {#Structure_Espace_Detail}

Public structure to hold module/eSpace details

_Attributes_

EspaceId
:   Type: Espace Identifier.  
    Espace Id

EspaceKey
:   Type: Text (100).  
    Espace Key

Name
:   Type: Text (100).  
    Espace Name

### FilterResults {#Structure_FilterResults}

Filter Search Structure

_Attributes_

PageNumber
:   Type: Integer.  
    Page number

MaxResultsPerPage
:   Type: Integer.  
    Number of results per page

OnlyActive
:   Type: Boolean.  
    Gets only active Status Set

CaseName
:   Type: Text.  
    Filter by Case Definition Name

OnlyWithCaseDefinition
:   Type: Boolean.  
    If only associated with a Case Definition

### FilterResults_Espace {#Structure_FilterResults_Espace}

Filter Search Structure

_Attributes_

PageNumber
:   Type: Integer.  
    Page number

MaxResultsPerPage
:   Type: Integer.  
    Number of results per page

OnlyActive
:   Type: Boolean.  
    Only active results

### FilterResults2 {#Structure_FilterResults2}

Filter Search Structure

_Attributes_

PageNumber
:   Type: Integer.  
    Page number

MaxResultsPerPage
:   Type: Integer.  
    Number of results per page

OnlyActive
:   Type: Boolean.  
    If only active results

### Group_Details {#Structure_Group_Details}

Public structure with system entity group details

_Attributes_

GroupId
:   Type: Group Identifier.  
    Group Identifier

Name
:   Type: Text (100).  
    Group Name (from system entity Group)

Description
:   Type: Text (500).  
    Group Description

### GroupExtended_CreateOrUpdate {#Structure_GroupExtended_CreateOrUpdate}

Public structure to update an existing Group extended

_Attributes_

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
    Calendar Identifier (optional)

IsActive
:   Type: Boolean.  
    If the group extened is active

HasCustomManagement
:   Type: Boolean.  
    Is it has customer management and should or not be visibile through users

### Holiday_Create {#Structure_Holiday_Create}

Public structure to create a new Calendar Holiday

_Attributes_

Id
:   Type: Holiday Identifier.  
    Calendar Holiday Identifier

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

IsRecurrent
:   Type: Boolean.  
    If this event is recurrent

### Holiday_Update {#Structure_Holiday_Update}

Public structure to update an existing Calendar Holiday

_Attributes_

Id
:   Type: Holiday Identifier.  
    Calendar Holiday Identifier

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

IsRecurrent
:   Type: Boolean.  
    If this event is recurrent

IsActive
:   Type: Boolean.  
    If the event is active

### MilestoneDefinition_CreateOrUpdate {#Structure_MilestoneDefinition_CreateOrUpdate}

Public structure to create a new milestone definition or to update an existing one

_Attributes_

Id
:   Type: MilestoneDefinition Identifier.  
    Milestone Definition Identifier

Name
:   Type: Text (50).  
    Milestone Name

Description
:   Type: Text (200).  
    Milestone description

IsActive
:   Type: Boolean.  
    True if the milestone definition is active

TranslationList
:   Type: [MilestoneDefinition_Translation](<#Structure_MilestoneDefinition_Translation>) List.  

### MilestoneDefinition_Translation {#Structure_MilestoneDefinition_Translation}

Translation structure for Milestone definition

_Attributes_

Locale
:   Type: Text (10).  
    Locale

Name
:   Type: Text (50).  
    Name

Description
:   Type: Text (200).  
    Milestone description

### NonWorkingDay_Create {#Structure_NonWorkingDay_Create}

Public structure to create a new Calendar Non Working Day

_Attributes_

Id
:   Type: NonWorkingDay Identifier.  
    Calendar Non Working Day Identifier

CalendarId
:   Type: Calendar Identifier.  
    Calendar Identifier

WeekDayId
:   Type: WeekDay Identifier.  
    No deal possible on this day

### NonWorkingDay_Update {#Structure_NonWorkingDay_Update}

Public structure to update an existing Calendar Non Working Day

_Attributes_

Id
:   Type: NonWorkingDay Identifier.  
    Calendar Non Working Day Identifier

CalendarId
:   Type: Calendar Identifier.  
    Calendar Identifier

WeekDayId
:   Type: WeekDay Identifier.  
    No deal possible on this day

IsActive
:   Type: Boolean.  
    Indicates if its active

### PreDefinedTemplate_CreateOrUpdate {#Structure_PreDefinedTemplate_CreateOrUpdate}

View to create or update a PreDefined Template

_Attributes_

Id
:   Type: PreDefinedTemplate Identifier.  
    Identifier

Name
:   Type: Text (200).  
    Template name

Subject
:   Type: Text (256).  
    Template subject

Body
:   Type: Text (50000).  
    Template body

IsActive
:   Type: Boolean.  
    If is active

### PreDefinedTemplate_View {#Structure_PreDefinedTemplate_View}

View of a PreDefined Template

_Attributes_

Id
:   Type: PreDefinedTemplate Identifier.  
    Identifier

Name
:   Type: Text (200).  
    Template name

Subject
:   Type: Text (256).  
    Template subject

Body
:   Type: Text (50000).  
    Template body

IsActive
:   Type: Boolean.  
    If is active

### ProcessDefinition_Details {#Structure_ProcessDefinition_Details}

Contains the generic details for process definition

_Attributes_

Id
:   Type: Process_Definition Identifier.  
    Process Definition Identifier

Label
:   Type: Text (100).  
    Activity Definition Label

### Resource_CreateOrUpdate {#Structure_Resource_CreateOrUpdate}

Structure to create or update a Resource

_Attributes_

Id
:   Type: Resource Identifier.  
    Id

Filename
:   Type: Text (100).  
    Filename

Filetype
:   Type: Text (100).  
    Filetype

Size
:   Type: Integer.  
    In bytes

CaseDefinitionId
:   Type: Text (36).  
    CaseDefinition Id

IsActive
:   Type: Boolean.  
    If the record is active

Data
:   Type: Binary Data.  
    Binary Data

### Resource_View {#Structure_Resource_View}

Represents a Resource

_Attributes_

Id
:   Type: Resource Identifier.  
    Id

Filename
:   Type: Text (100).  
    Filename

Filetype
:   Type: Text (100).  
    Filetype

Size
:   Type: Integer.  
    In bytes

CaseDefinitionId
:   Type: Text (36).  
    CaseDefinition Id

IsActive
:   Type: Boolean.  
    If the record is active

Data
:   Type: Binary Data.  
    Binary Data

### Rule_CreateOrUpdate {#Structure_Rule_CreateOrUpdate}

Structure to create/update a rule

_Attributes_

Id
:   Type: Rule Identifier.  
    Rule Id

Name
:   Type: Text (50).  
    Rule Name

Description
:   Type: Text.  
    Rule description

CaseDefinitionId
:   Type: CaseDefinition Identifier.  
    Case Definition Id

RuleTypeId
:   Type: RuleType Identifier.  
    RuleType Id

IsExternal
:   Type: Boolean.  
    If true, the rule outcome will become from a REST call

ExternalURL
:   Type: Text (500).  
    Relative REST endpoint for external rules

### Rule_View {#Structure_Rule_View}

Structure with Rules fields

_Attributes_

Id
:   Type: Rule Identifier.  
    Rule Id

Name
:   Type: Text.  
    Rule Name

Description
:   Type: Text.  
    Rule description

CaseDefinitionId
:   Type: CaseDefinition Identifier.  
    Case Definition Id

IsActive
:   Type: Boolean.  
    If the rule is active

LastUpdatedBy
:   Type: User Identifier.  
    Identify the user responsable for the record updated

LastUpdateOn
:   Type: Date Time.  
    Instant of the last record update

RuleType
:   Type: [RuleType](<#Structure_RuleType>).  
    Rule Type

IsExternal
:   Type: Boolean.  
    If true, the rule outcome will become from a REST call

ExternalURL
:   Type: Text (500).  
    Relative REST endpoint for external rules

NumRulesGroup
:   Type: Integer.  
    Number of rule groups that this rule has

### RuleAttribute_CreateOrUpdate {#Structure_RuleAttribute_CreateOrUpdate}

Structure to create or update a Rule Attribute

_Attributes_

Id
:   Type: RuleAttribute Identifier.  
    RuleAttribute Id

AttributeId
:   Type: Entity_Attr Identifier.  
    Attibute Id

ExtraFieldId
:   Type: ExtraField Identifier.  

RuleAttributeTypeId
:   Type: RuleAttributeType Identifier.  
    RuleAttributeType Id

Setting_CreateOrUpdate
:   Type: [Setting_CreateOrUpdate](<#Structure_Setting_CreateOrUpdate>).  
    Setting record

### RuleAttribute_View {#Structure_RuleAttribute_View}

Structure with Rule Attribute fields

_Attributes_

Id
:   Type: RuleAttribute Identifier.  
    RuleAttribute Id

AttributeId
:   Type: Entity_Attr Identifier.  
    Attibute Id

ExtraFieldId
:   Type: ExtraField Identifier.  

RuleAttributeTypeId
:   Type: RuleAttributeType Identifier.  
    RuleAttributeType Id

GlobalKey
:   Type: Text.  
    GlobalKey (when it's a business field)

Setting_Value
:   Type: [Setting_Value](<#Structure_Setting_Value>).  
    Setting record

### RuleConfig {#Structure_RuleConfig}

Represents a Rule configuration

_Attributes_

RuleView
:   Type: [Rule_View](<#Structure_Rule_View>).  
    Rule View

RuleGroups
:   Type: [RuleGroup_View](<#Structure_RuleGroup_View>) List.  
    Rule Groups

### RuleGroup_CreateOrUpdate {#Structure_RuleGroup_CreateOrUpdate}

Public structure to create or update a rule group

_Attributes_

Id
:   Type: RuleGroup Identifier.  
    RuleGroup Id

RuleId
:   Type: Rule Identifier.  
    Rule Id

Order
:   Type: Integer.  
    Order

Description
:   Type: Text.  
    Description

### RuleGroup_View {#Structure_RuleGroup_View}

Structure with Rule Groups fields

_Attributes_

Id
:   Type: RuleGroup Identifier.  
    RuleGroup Id

RuleId
:   Type: Rule Identifier.  
    Rule Id

Order
:   Type: Integer.  
    Order

Description
:   Type: Text.  
    Description

RuleLines
:   Type: [RuleLine_View](<#Structure_RuleLine_View>) List.  
    RuleLines of this RuleGroup

RuleGroupOutput
:   Type: [RuleGroupOutput_View](<#Structure_RuleGroupOutput_View>).  
    Output of this RuleGroup

### RuleGroupOutput_CreateOrUpdate {#Structure_RuleGroupOutput_CreateOrUpdate}

Structure to create or update a Rule Group Output

_Attributes_

Id
:   Type: RuleGroupOutput Identifier.  
    RuleGroupOutput Id

RuleGroupId
:   Type: RuleGroup Identifier.  
    RuleGroup Id

Setting_CreateOrUpdate
:   Type: [Setting_CreateOrUpdate](<#Structure_Setting_CreateOrUpdate>).  
    Setting record

### RuleGroupOutput_View {#Structure_RuleGroupOutput_View}

Structure with RuleGroupOutput fields

_Attributes_

Id
:   Type: RuleGroupOutput Identifier.  
    RuleGroupOutput Id

RuleGroupId
:   Type: RuleGroup Identifier.  
    RuleGroup Id

Setting
:   Type: [Setting_Value](<#Structure_Setting_Value>).  
    Setting record

### RuleLine_CreateOrUpdate {#Structure_RuleLine_CreateOrUpdate}

Structure to create or update a Rule Line

_Attributes_

Id
:   Type: RuleLine Identifier.  
    RuleLine Id

RuleGroupId
:   Type: RuleGroup Identifier.  
    RuleGroup Id

RuleOperatorId
:   Type: RuleOperator Identifier.  
    RuleOperator Id

Order
:   Type: Integer.  
    Order

LeftAttribute
:   Type: [RuleAttribute_CreateOrUpdate](<#Structure_RuleAttribute_CreateOrUpdate>).  
    LeftAttribute record

RightAttribute
:   Type: [RuleAttribute_CreateOrUpdate](<#Structure_RuleAttribute_CreateOrUpdate>).  
    RightAttribute record

### RuleLine_View {#Structure_RuleLine_View}

Structure with Rule Line fields

_Attributes_

Id
:   Type: RuleLine Identifier.  
    RuleLine Id

Order
:   Type: Integer.  
    Order

LeftAttribute
:   Type: [RuleAttribute_View](<#Structure_RuleAttribute_View>).  
    Left Rule Attribute

RightAttribute
:   Type: [RuleAttribute_View](<#Structure_RuleAttribute_View>).  
    Right Rule Attribute

RuleOperator
:   Type: [RuleOperator](<#Structure_RuleOperator>).  
    Rule Operator

### Setting_CreateOrUpdate {#Structure_Setting_CreateOrUpdate}

Public structure to create or update a setting

_Attributes_

Id
:   Type: Setting Identifier.  
    Setting Id

Name
:   Type: Text.  
    Setting name (optional)

SettingTypeId
:   Type: SettingType Identifier.  
    Setting type Id

Decimal
:   Type: Decimal (37, 0).  
    Decimal field

Integer
:   Type: Long Integer.  
    Integer field

LongInteger
:   Type: Long Integer.  
    LongInteger field

Text
:   Type: Text.  
    Text field

Date
:   Type: Date.  
    Date field

Time
:   Type: Time.  
    Time

Boolean
:   Type: Boolean.  
    Boolean field

IsActive
:   Type: Boolean.  
    True - is active, False - is not

### Setting_Value {#Structure_Setting_Value}

Public structure with the possible values for a setting

_Attributes_

Id
:   Type: Setting Identifier.  
    Setting Id

Name
:   Type: Text.  
    Setting name (optional)

SettingTypeId
:   Type: SettingType Identifier.  
    Setting type Id

Decimal
:   Type: Decimal (37, 0).  
    Decimal field

Integer
:   Type: Long Integer.  
    Integer field

LongInteger
:   Type: Long Integer.  
    LongInteger field

Text
:   Type: Text (50).  
    Text field

Date
:   Type: Date.  
    Date field

Time
:   Type: Time.  
    Time field

Boolean
:   Type: Boolean.  
    Boolean field

### Setup_CaseAction {#Structure_Setup_CaseAction}

Public structure to set up case actions

_Attributes_

CaseActionId
:   Type: CaseAction Identifier.  
    Case Action Identifier

Label
:   Type: Text (50).  
    Label

CaseStatusId
:   Type: CaseStatus Identifier.  
    Case Status Identifier

IsActive
:   Type: Boolean.  
    True if the case action is active, False otherwise

TranslationList
:   Type: [CaseAction_Translation](<#Structure_CaseAction_Translation>) List.  
    Translation structure for Case action

### Setup_CaseDefinition {#Structure_Setup_CaseDefinition}

Public structure to set up a case definition

_Attributes_

CaseDefinitionId
:   Type: CaseDefinition Identifier.  
    Case Definition unique Identifier

Name
:   Type: Text (50).  
    Case Definition Name

Description
:   Type: Text (200).  
    Case Definition Description

HasAccessControl
:   Type: Boolean.  
    If the case definition is under access control

PurgeTypeId
:   Type: PurgeType Identifier.  
    Option of purge type for current case definition

DaysToPurgeCase
:   Type: Integer.  
    After a case is closed, number of days to keep the data in the system until being deleted.  
    &lt; 0 : Never purge  
    0   : Use system defaults  
    &gt; 0 : Number of days

DaysToPurgeProcess
:   Type: Integer.  
    After a case is closed, number of days to keep the process data in the system until being deleted.

TranslationList
:   Type: [CaseDefinition_Translation](<#Structure_CaseDefinition_Translation>) List.  
    Translation structure for Case definition

### Setup_CaseStateMachine {#Structure_Setup_CaseStateMachine}

Public structure to set up case state machine transitions

_Attributes_

FromCaseStatusId
:   Type: CaseStatus Identifier.  
    The current Case Status Identifier

ToCaseStatusId
:   Type: CaseStatus Identifier.  
    The next Case Status Identifier

IsActive
:   Type: Boolean.  
    True if the case state machine transition is active, False otherwise

### Setup_CaseStatus {#Structure_Setup_CaseStatus}

Public structure to set up case statuses

_Attributes_

CaseStatusId
:   Type: CaseStatus Identifier.  
    Case Status Unique Identifier

Name
:   Type: Text (50).  
    Case Status logical name

Alias
:   Type: Text (50).  
    Case Status alias name

IsInitial
:   Type: Boolean.  
    True If the case status is initial, False otherwise. Only one case status can be defined as Initial. By doing so this will be the default status the case instances in your appplication will take once they are created.

IsActive
:   Type: Boolean.  
    True if the status is active, False otherwise

TranslationList
:   Type: [CaseStatus_Translation](<#Structure_CaseStatus_Translation>) List.  
    Translation structure for Case status

### Setup_EmailTemplate {#Structure_Setup_EmailTemplate}

Public structure to set up email templates

_Attributes_

EmailTemplateId
:   Type: EmailTemplate Identifier.  
    Email Template Identifier

Name
:   Type: Text (20).  
    Name of the template

Subject
:   Type: Text (256).  
    The email subject

FromDisplayName
:   Type: Text (250).  
    Email From Name

FromEmail
:   Type: Email.  
    Email From

Body
:   Type: Text (50000).  
    The email Body

IsActive
:   Type: Boolean.  
    True if the email template is active, False otherwise

### Setup_MilestoneDefinition {#Structure_Setup_MilestoneDefinition}

Public structure to set up a milestone definition

_Attributes_

MilestoneDefinitionId
:   Type: MilestoneDefinition Identifier.  
    Milestone Definition unique Identifier

Name
:   Type: Text (50).  
    Case Definition Name

Description
:   Type: Text (200).  
    Case Definition Description

IsActive
:   Type: Boolean.  
    True if the milestone definition is active

TranslationList
:   Type: [MilestoneDefinition_Translation](<#Structure_MilestoneDefinition_Translation>) List.  
    Translation structure for Milestone definition

### SetupData {#Structure_SetupData}

Holds the basic setup data for a case management application

_Attributes_

BusinessEntityEspaceId
:   Type: Espace Identifier.  
    The Identifier of the module/eSpace where your business entity is defined, use the GetOwnerEspaceId() built-in function if the entity is defined in the same module where the setup action will be run

CaseDefinition
:   Type: [Setup_CaseDefinition](<#Structure_Setup_CaseDefinition>).  
    Holds the data to setup a Case Definition

CaseStatusList
:   Type: [Setup_CaseStatus](<#Structure_Setup_CaseStatus>) List.  
    Holds the data to setup a list of Case Statuses

CaseStateMachineList
:   Type: [Setup_CaseStateMachine](<#Structure_Setup_CaseStateMachine>) List.  
    Holds the data to setup a list of Case State Machine transitions

CaseActionList
:   Type: [Setup_CaseAction](<#Structure_Setup_CaseAction>) List.  
    Holds the data to setup a list of Case Actions

EmailTemplateList
:   Type: [Setup_EmailTemplate](<#Structure_Setup_EmailTemplate>) List.  
    Holds the data to setup a list of Email Templates

MilestoneDefinitionList
:   Type: [Setup_MilestoneDefinition](<#Structure_Setup_MilestoneDefinition>) List.  
    Holds the data to setup a Milestone Definition

### Tag_Create {#Structure_Tag_Create}

Public structure that enables to create tag instances

_Attributes_

Label
:   Type: Text (50).  
    Tag label

CaseDefinitionId
:   Type: CaseDefinition Identifier.  
    Case Definition Identifier (Optional). By not associating a new Tag with an existing case definition the tag may be used by all case definitions.

### Tag_Update {#Structure_Tag_Update}

Public structure that enables to update tag instances

_Attributes_

Id
:   Type: Tag Identifier.  
    Tag Identifier

Label
:   Type: Text (50).  
    Tag label

### UserExtended_CreateOrUpdate {#Structure_UserExtended_CreateOrUpdate}

User extended create or update structure

_Attributes_

UserId
:   Type: User Identifier.  
    User Id

ManagerUserId
:   Type: User Identifier.  
    User's manager

GroupExtendedId
:   Type: GroupExtended Identifier.  
    Default user group
