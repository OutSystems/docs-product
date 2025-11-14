---
summary: OutSystems 11 (O11) Case Process Configurations API provides tools for configuring SLAs and process activities within a case.
guid: 576b9623-c10e-489c-b7de-22e36fcf92db
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: api documentation, business process technology, service level agreements (sla), process automation, activity management
audience:
  - backend developers
  - full stack developers
  - architects
  - platform administrators
outsystems-tools:
  - service studio
  - case management framework
coverage-type:
  - remember
---

# Case Process Configurations API

The Case Process Configurations API includes actions used to configure the underlying BPT process associated with a case. Use this API to configure SLAs associated with a Process or with an Activity from a Process.

## Summary

| Action | Description |
| ---|--- |
| [Activity_GetAssignDetailsByActivityId](<#Activity_GetAssignDetailsByActivityId>) | Gets the activity assignment details (user and group) and if the acitivity is blocked |
| [ActivityDefinitionConfiguration_Get](<#ActivityDefinitionConfiguration_Get>) | Gets the configuration of an activity definition |
| [ActivityDefinitionConfiguration_GetAll](<#ActivityDefinitionConfiguration_GetAll>) | Gets all the activity configuration of an process definition |
| [ActivityDefinitionConfiguration_Save](<#ActivityDefinitionConfiguration_Save>) | Saves the configuration of an activity definition |
| [ActivityDefinitionSLA_Create](<#ActivityDefinitionSLA_Create>) | Creates a new Activity Definition SLA |
| [ActivityDefinitionSLA_CreateOrUpdate](<#ActivityDefinitionSLA_CreateOrUpdate>) | Creates or updates the Activity Definition SLA details |
| [ActivityDefinitionSLA_Delete](<#ActivityDefinitionSLA_Delete>) | Deletes an existing Activity Definition SLA |
| [ActivityDefinitionSLA_GetById](<#ActivityDefinitionSLA_GetById>) | Gets an Activity Configuration associated with activity definition. |
| [ActivityDefinitionSLA_GetList](<#ActivityDefinitionSLA_GetList>) | Gets the list of SLA configurations associated with activity definitions. Can be filtered based on a process definition. |
| [ActivityDefinitionSLA_Update](<#ActivityDefinitionSLA_Update>) | Updates an existing Activity Definition SLA |
| [Configurations_Load](<#Configurations_Load>) | Load the input configuratins (usually from a bootstrap process). Already calls Configurations_InitializeStaging. |
| [ProcessConfigurations_GetAll](<#ProcessConfigurations_GetAll>) | Gets all the configuration of a process definition |
| [ProcessDefinition_GetByGlobalKey](<#ProcessDefinition_GetByGlobalKey>) | Gets the Process Definition Id by it's GlobalKey |
| [ProcessDefinitionConfiguration_Get](<#ProcessDefinitionConfiguration_Get>) | Gets the configuration of an process definition |
| [ProcessDefinitionConfiguration_Save](<#ProcessDefinitionConfiguration_Save>) | Saves the configuration of an process definition |
| [ProcessDefinitionExtended_Create](<#ProcessDefinitionExtended_Create>) | Creates a new Process Definition Extended |
| [ProcessDefinitionExtended_CreateOrUpdate](<#ProcessDefinitionExtended_CreateOrUpdate>) | Creates or updates the Process Definition Extended details. |
| [ProcessDefinitionExtended_Delete](<#ProcessDefinitionExtended_Delete>) | Deletes an existing Process Definition Extended |
| [ProcessDefinitionExtended_Update](<#ProcessDefinitionExtended_Update>) | Updates an existing Process Definition Extended |
| [ProcessDefinitionPriority_Create](<#ProcessDefinitionPriority_Create>) | Creates a new priority type |
| [ProcessDefinitionPriority_CreateOrUpdate](<#ProcessDefinitionPriority_CreateOrUpdate>) | Creates or updates the Priority Type details |
| [ProcessDefinitionPriority_Delete](<#ProcessDefinitionPriority_Delete>) | Removes an existing priority type. |
| [ProcessDefinitionPriority_Update](<#ProcessDefinitionPriority_Update>) | Updates an existing priority type. |
| [ProcessDefinitionPriorityGetAll](<#ProcessDefinitionPriorityGetAll>) | Gets the list of priorities. |
| [ProcessDefinitionPriorityGetById](<#ProcessDefinitionPriorityGetById>) | Gets a priority. |
| [ProcessDefinitionSLA_Create](<#ProcessDefinitionSLA_Create>) | Creates a new Process Definition SLA |
| [ProcessDefinitionSLA_CreateOrUpdate](<#ProcessDefinitionSLA_CreateOrUpdate>) | Creates or updates the Process Definition SLA details. |
| [ProcessDefinitionSLA_Delete](<#ProcessDefinitionSLA_Delete>) | Deletes an existing Process Definition SLA |
| [ProcessDefinitionSLA_GetById](<#ProcessDefinitionSLA_GetById>) | Gets a process definition configuration. |
| [ProcessDefinitionSLA_GetList](<#ProcessDefinitionSLA_GetList>) | Gets the list of process definition configuration. |
| [ProcessDefinitionSLA_Update](<#ProcessDefinitionSLA_Update>) | Updates an existing Process Definition SLA |
| [ProcessExtended_InitializeStaging](<#ProcessExtended_InitializeStaging>) | It will mark all entries as deleted for the staging process after only import the active ones |
| [ProcessPriority_InitializeStaging](<#ProcessPriority_InitializeStaging>) | It will mark all entries as deleted for the staging process after only import the active ones |
| [ProcessSLA_InitializeStaging](<#ProcessSLA_InitializeStaging>) | It will mark all entries as deleted for the staging process after only import the active ones |

| Structure | Description |
| ---|--- |
| [Activity_AssignDetails](<#Structure_Activity_AssignDetails>) | Details about activity assignment details |
| [ActivityDefinition_Detail](<#Structure_ActivityDefinition_Detail>) | Contains the generic details for activity definition |
| [ActivityDefinition_DetailWithSLA](<#Structure_ActivityDefinition_DetailWithSLA>) | Contains the generic details for activity definition SLA |
| [ActivityDefinitionSLA_Config](<#Structure_ActivityDefinitionSLA_Config>) | ActivityDefinitionSLA Config |
| [ActivityDefinitionSLA_Create](<#Structure_ActivityDefinitionSLA_Create>) | Public structure to enable to create a new activity definition extended configuration |
| [ActivityDefinitionSLA_CreateOrUpdate](<#Structure_ActivityDefinitionSLA_CreateOrUpdate>) | Public structure to enable to create or update an existing activity definition extended |
| [ActivityDefinitionSLA_Detail](<#Structure_ActivityDefinitionSLA_Detail>) | Public structure to retrieve details about activity definition configuration details |
| [ActivityDefiniton_Config](<#Structure_ActivityDefiniton_Config>) | ActivityDefiniton Config |
| [FilterResults4](<#Structure_FilterResults4>) | Filter Search Structure |
| [FilterResults5](<#Structure_FilterResults5>) | Filter Search Structure |
| [ProcessActivityConfigs](<#Structure_ProcessActivityConfigs>) | Config |
| [ProcessConfiguration_Save](<#Structure_ProcessConfiguration_Save>) | Save Activity Definition Configuration structure |
| [ProcessConfiguration_View](<#Structure_ProcessConfiguration_View>) | Activity Definition Configuration structure |
| [ProcessDefinition_Detail](<#Structure_ProcessDefinition_Detail>) | Contains the generic details for process definition |
| [ProcessDefinitionExtended_Config](<#Structure_ProcessDefinitionExtended_Config>) | ProcessDefinitionExtended Config |
| [ProcessDefinitionExtended_Create](<#Structure_ProcessDefinitionExtended_Create>) | Public structure to enable to create a new process definition extended confgurations |
| [ProcessDefinitionExtended_CreateOrUpdate](<#Structure_ProcessDefinitionExtended_CreateOrUpdate>) | Public structure to enable to create/update an existing process definition configuration |
| [ProcessDefinitionPriority_Config](<#Structure_ProcessDefinitionPriority_Config>) | ProcessDefinitionPriority Config |
| [ProcessDefinitionPriorityCreate](<#Structure_ProcessDefinitionPriorityCreate>) | Public structure to create a new priority associated to an existing process definition. |
| [ProcessDefinitionPriorityCreateOrUpdate](<#Structure_ProcessDefinitionPriorityCreateOrUpdate>) | Public structure to create/update priority associated to an existing process definition. |
| [ProcessDefinitionPriorityDetail](<#Structure_ProcessDefinitionPriorityDetail>) | Public structure to return the details for process priority |
| [ProcessDefinitionSLA_Config](<#Structure_ProcessDefinitionSLA_Config>) | ProcessDefinitionSLA Config |
| [ProcessDefinitionSLA_Create](<#Structure_ProcessDefinitionSLA_Create>) | Public structure to enable to create a new process definition SLA |
| [ProcessDefinitionSLA_CreateOrUpdate](<#Structure_ProcessDefinitionSLA_CreateOrUpdate>) | Public structure to enable to create/update an existing process definition sla |
| [ProcessDefinitionSLA_DetailWithProcessDefinition](<#Structure_ProcessDefinitionSLA_DetailWithProcessDefinition>) | Public structure to retrieve details about process definition configuration |

## Actions

### Activity_GetAssignDetailsByActivityId { #Activity_GetAssignDetailsByActivityId }

Gets the activity assignment details (user and group) and if the acitivity is blocked

_Inputs_

ActivityId
:   Type: mandatory, Activity Identifier.  
    Activity Identifier

_Outputs_

ActivityAssignDetails
:   Type: [Activity_AssignDetails](<#Structure_Activity_AssignDetails>).  
    ActivityA ssignment Details

### ActivityDefinitionConfiguration_Get { #ActivityDefinitionConfiguration_Get }

Gets the configuration of an activity definition

_Inputs_

ActivityDefinitionId
:   Type: mandatory, Activity_Definition Identifier.  
    ActivityDefinition Id

_Outputs_

ProcessConfiguration
:   Type: [ProcessConfiguration_View](<#Structure_ProcessConfiguration_View>).  
    ProcessConfiguration View

### ActivityDefinitionConfiguration_GetAll { #ActivityDefinitionConfiguration_GetAll }

Gets all the activity configuration of an process definition

_Inputs_

ProcessDefinitionId
:   Type: mandatory, Process_Definition Identifier.  
    ProcessDefinition Id

_Outputs_

ProcessConfigurationLst
:   Type: [ProcessConfiguration_View](<#Structure_ProcessConfiguration_View>) List.  
    ProcessConfiguration View list

### ActivityDefinitionConfiguration_Save { #ActivityDefinitionConfiguration_Save }

Saves the configuration of an activity definition

_Inputs_

ProcessConfiguration
:   Type: mandatory, [ProcessConfiguration_Save](<#Structure_ProcessConfiguration_Save>).  
    ProcessConfiguration View

### ActivityDefinitionSLA_Create { #ActivityDefinitionSLA_Create }

Creates a new Activity Definition SLA

_Inputs_

ActivityDefinitionSLACreateRec
:   Type: mandatory, [ActivityDefinitionSLA_Create](<#Structure_ActivityDefinitionSLA_Create>).  
    Activity Definition SLA creation details

_Outputs_

ActivityDefinitionSLAId
:   Type: ActivityDefinitionSLA Identifier.  
    Activity Definition SLA Identifier

### ActivityDefinitionSLA_CreateOrUpdate { #ActivityDefinitionSLA_CreateOrUpdate }

Creates or updates the Activity Definition SLA details

_Inputs_

ActivityDefinitionSLARec
:   Type: mandatory, [ActivityDefinitionSLA_CreateOrUpdate](<#Structure_ActivityDefinitionSLA_CreateOrUpdate>).  
    Activity Definition SLA Record

_Outputs_

ActivityDefinitionSLAId
:   Type: ActivityDefinitionSLA Identifier.  
    Activity Definition SLA Identifier

### ActivityDefinitionSLA_Delete { #ActivityDefinitionSLA_Delete }

Deletes an existing Activity Definition SLA

_Inputs_

Id
:   Type: mandatory, ActivityDefinitionSLA Identifier.  
    Activity SLA Identifier

### ActivityDefinitionSLA_GetById { #ActivityDefinitionSLA_GetById }

Gets an Activity Configuration associated with activity definition.

_Inputs_

ActivityDefinitionSLAId
:   Type: mandatory, ActivityDefinitionSLA Identifier.  
    ActivityDefinitionSLA Id

_Outputs_

ActivityDefinitionSLADetail
:   Type: [ActivityDefinition_DetailWithSLA](<#Structure_ActivityDefinition_DetailWithSLA>).  
    Activity definition configuration

### ActivityDefinitionSLA_GetList { #ActivityDefinitionSLA_GetList }

Gets the list of SLA configurations associated with activity definitions. Can be filtered based on a process definition.

_Inputs_

FilterResults
:   Type: mandatory, [FilterResults5](<#Structure_FilterResults5>).  
    Filter Results

ProcessDefinitionId
:   Type: optional, Process_Definition Identifier.  
    Process Definition Identifier

_Outputs_

ActivityDefinitionSLADetailsList
:   Type: [ActivityDefinition_DetailWithSLA](<#Structure_ActivityDefinition_DetailWithSLA>) List.  
    List about activity definition configuration

TotalResults
:   Type: Long Integer.  
    Number of total activity definition SLA that match the criteiria

### ActivityDefinitionSLA_Update { #ActivityDefinitionSLA_Update }

Updates an existing Activity Definition SLA

_Inputs_

ActivityDefinitionSLAUpdateRec
:   Type: mandatory, [ActivityDefinitionSLA_CreateOrUpdate](<#Structure_ActivityDefinitionSLA_CreateOrUpdate>).  
    Activity Definition SLA update details

### Configurations_Load { #Configurations_Load }

Load the input configuratins (usually from a bootstrap process). Already calls Configurations_InitializeStaging.

_Inputs_

LoadProcessDefinitionSSkey
:   Type: optional, Text.  
    ProcessDefinition SSKey

Configurations
:   Type: mandatory, [ProcessActivityConfigs](<#Structure_ProcessActivityConfigs>).  
    List of all configurations

_Outputs_

FoundDefinition
:   Type: Boolean.  
    If false the input process definition was not found

### ProcessConfigurations_GetAll { #ProcessConfigurations_GetAll }

Gets all the configuration of a process definition

_Inputs_

ProcessDefinitionId
:   Type: optional, Process_Definition Identifier.  
    ProcessDefinition Id

_Outputs_

Configurations
:   Type: [ProcessActivityConfigs](<#Structure_ProcessActivityConfigs>).  
    List of all configurations

### ProcessDefinition_GetByGlobalKey { #ProcessDefinition_GetByGlobalKey }

Gets the Process Definition Id by it's GlobalKey

_Inputs_

ProcessDefinitionGlobalKey
:   Type: mandatory, Text.  
    ProcessDefinition GlobalKey

_Outputs_

ProcessDefinitionId
:   Type: Process_Definition Identifier.  
    ProcessDefinition Id

### ProcessDefinitionConfiguration_Get { #ProcessDefinitionConfiguration_Get }

Gets the configuration of an process definition

_Inputs_

ProcessDefinitionId
:   Type: mandatory, Process_Definition Identifier.  
    ProcessDefinition Id

_Outputs_

ProcessConfiguration
:   Type: [ProcessConfiguration_View](<#Structure_ProcessConfiguration_View>).  
    ProcessConfiguration View

### ProcessDefinitionConfiguration_Save { #ProcessDefinitionConfiguration_Save }

Saves the configuration of an process definition

_Inputs_

ProcessConfiguration
:   Type: mandatory, [ProcessConfiguration_Save](<#Structure_ProcessConfiguration_Save>).  
    ProcessConfiguration View

### ProcessDefinitionExtended_Create { #ProcessDefinitionExtended_Create }

Creates a new Process Definition Extended

_Inputs_

ProcessDefinitionExtendedCreateRec
:   Type: mandatory, [ProcessDefinitionExtended_Create](<#Structure_ProcessDefinitionExtended_Create>).  
    Process Definition Extended creation details

_Outputs_

ProcessDefinitionExtendedId
:   Type: ProcessDefinitionExtended Identifier.  
    Process Definition Extended Identifier

### ProcessDefinitionExtended_CreateOrUpdate { #ProcessDefinitionExtended_CreateOrUpdate }

Creates or updates the Process Definition Extended details.

_Inputs_

ProcessDefinitionExtendedRec
:   Type: mandatory, [ProcessDefinitionExtended_CreateOrUpdate](<#Structure_ProcessDefinitionExtended_CreateOrUpdate>).  
    Process Definition Extended Details

_Outputs_

ProcessDefinitionExtendedId
:   Type: ProcessDefinitionExtended Identifier.  
    Process Definition Extended Identifier

### ProcessDefinitionExtended_Delete { #ProcessDefinitionExtended_Delete }

Deletes an existing Process Definition Extended

_Inputs_

ProcessDefinitionExtendedId
:   Type: mandatory, ProcessDefinitionExtended Identifier.  
    Process Definition Extended Identifier

### ProcessDefinitionExtended_Update { #ProcessDefinitionExtended_Update }

Updates an existing Process Definition Extended

_Inputs_

ProcessDefinitionExtendedUpdateRec
:   Type: mandatory, [ProcessDefinitionExtended_CreateOrUpdate](<#Structure_ProcessDefinitionExtended_CreateOrUpdate>).  
    Process Definition Extended update details

### ProcessDefinitionPriority_Create { #ProcessDefinitionPriority_Create }

Creates a new priority type

_Inputs_

ProcessDefinitionPriorityCreateRec
:   Type: mandatory, [ProcessDefinitionPriorityCreate](<#Structure_ProcessDefinitionPriorityCreate>).  
    Priority type creation details

_Outputs_

ProcessDefinitionPriorityId
:   Type: ProcessDefinitionPriority Identifier.  
    Priority Type Identifier

### ProcessDefinitionPriority_CreateOrUpdate { #ProcessDefinitionPriority_CreateOrUpdate }

Creates or updates the Priority Type details

_Inputs_

ProcessDefinitionPriorityRec
:   Type: mandatory, [ProcessDefinitionPriorityCreateOrUpdate](<#Structure_ProcessDefinitionPriorityCreateOrUpdate>).  
    Priority type creation/update details

_Outputs_

ProcessDefinitionPriorityId
:   Type: ProcessDefinitionPriority Identifier.  
    Priority Type Identifier

### ProcessDefinitionPriority_Delete { #ProcessDefinitionPriority_Delete }

Removes an existing priority type.

_Inputs_

ProcessDefinitionPriorityId
:   Type: mandatory, ProcessDefinitionPriority Identifier.  
    Process Definition Priority Identifier

### ProcessDefinitionPriority_Update { #ProcessDefinitionPriority_Update }

Updates an existing priority type.

_Inputs_

ProcessDefinitionPriorityUpdateRec
:   Type: mandatory, [ProcessDefinitionPriorityCreateOrUpdate](<#Structure_ProcessDefinitionPriorityCreateOrUpdate>).  
    Priority type creation details

### ProcessDefinitionPriorityGetAll { #ProcessDefinitionPriorityGetAll }

Gets the list of priorities.

_Inputs_

FilterResults
:   Type: mandatory, [FilterResults4](<#Structure_FilterResults4>).  
    Filter Results

ProcessDefinitionId
:   Type: optional, Process_Definition Identifier.  
    Process Definition Identifier

_Outputs_

PriorityDetailsList
:   Type: [ProcessDefinitionPriorityDetail](<#Structure_ProcessDefinitionPriorityDetail>) List.  
    List of Priority Detail

TotalResults
:   Type: Long Integer.  
    Number of total activity definition SLA that match the criteiria

### ProcessDefinitionPriorityGetById { #ProcessDefinitionPriorityGetById }

Gets a priority.

_Inputs_

ProcessDefinitionPriorityId
:   Type: mandatory, ProcessDefinitionPriority Identifier.  
    Priority Id

_Outputs_

ProcessDefinitionPriorityDetail
:   Type: [ProcessDefinitionPriorityDetail](<#Structure_ProcessDefinitionPriorityDetail>).  
    Priority Detail

### ProcessDefinitionSLA_Create { #ProcessDefinitionSLA_Create }

Creates a new Process Definition SLA

_Inputs_

ProcessDefinitionSLACreateRec
:   Type: mandatory, [ProcessDefinitionSLA_Create](<#Structure_ProcessDefinitionSLA_Create>).  
    Process Definition SLA creation details

_Outputs_

ProcessDefinitionSLAId
:   Type: ProcessDefinitionSLA Identifier.  
    Process Definition SLA Identifier

### ProcessDefinitionSLA_CreateOrUpdate { #ProcessDefinitionSLA_CreateOrUpdate }

Creates or updates the Process Definition SLA details.

_Inputs_

ProcessDefinitionSLARec
:   Type: mandatory, [ProcessDefinitionSLA_CreateOrUpdate](<#Structure_ProcessDefinitionSLA_CreateOrUpdate>).  
    Process Definition SLA Details

_Outputs_

ProcessDefinitionSLAId
:   Type: ProcessDefinitionSLA Identifier.  
    Process Definition SLA Identifier

### ProcessDefinitionSLA_Delete { #ProcessDefinitionSLA_Delete }

Deletes an existing Process Definition SLA

_Inputs_

ProcessDefinitionSLAId
:   Type: mandatory, ProcessDefinitionSLA Identifier.  
    Process Definition SLA Identifier

### ProcessDefinitionSLA_GetById { #ProcessDefinitionSLA_GetById }

Gets a process definition configuration.

_Inputs_

ProcessDefinitionSLAId
:   Type: mandatory, ProcessDefinitionSLA Identifier.  
    Process Definition Config Id

_Outputs_

ProcessDefinitionSLADetail
:   Type: [ProcessDefinitionSLA_DetailWithProcessDefinition](<#Structure_ProcessDefinitionSLA_DetailWithProcessDefinition>).  
    Process definition configuration

### ProcessDefinitionSLA_GetList { #ProcessDefinitionSLA_GetList }

Gets the list of process definition configuration.

_Inputs_

FilterResults
:   Type: mandatory, [FilterResults5](<#Structure_FilterResults5>).  
    Filter Results

ProcessDefinitionId
:   Type: optional, Process_Definition Identifier.  
    Process Definition Identifier

_Outputs_

ProcessDefinitionSLADetailsList
:   Type: [ProcessDefinitionSLA_DetailWithProcessDefinition](<#Structure_ProcessDefinitionSLA_DetailWithProcessDefinition>) List.  
    List about process definition configuration

TotalResults
:   Type: Long Integer.  
    Number of total process definition SLA that match the criteiria

### ProcessDefinitionSLA_Update { #ProcessDefinitionSLA_Update }

Updates an existing Process Definition SLA

_Inputs_

ProcessDefinitionSLAUpdateRec
:   Type: mandatory, [ProcessDefinitionSLA_CreateOrUpdate](<#Structure_ProcessDefinitionSLA_CreateOrUpdate>).  
    Process Definition Extended update details

### ProcessExtended_InitializeStaging { #ProcessExtended_InitializeStaging }

It will mark all entries as deleted for the staging process after only import the active ones

_Inputs_

ProcessDefinitionId
:   Type: optional, Process_Definition Identifier.  

### ProcessPriority_InitializeStaging { #ProcessPriority_InitializeStaging }

It will mark all entries as deleted for the staging process after only import the active ones

_Inputs_

ProcessDefinitionId
:   Type: optional, Process_Definition Identifier.  

### ProcessSLA_InitializeStaging { #ProcessSLA_InitializeStaging }

It will mark all entries as deleted for the staging process after only import the active ones

_Inputs_

ProcessDefinitionId
:   Type: optional, Process_Definition Identifier.  

## Structures

### Activity_AssignDetails { #Structure_Activity_AssignDetails }

Details about activity assignment details

_Attributes_

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

### ActivityDefinition_Detail { #Structure_ActivityDefinition_Detail }

Contains the generic details for activity definition

_Attributes_

ActivityDefinitionId
:   Type: Activity_Definition Identifier.  
    Activity Definition Identifier

Label
:   Type: Text (100).  
    Activity Definition Label

ProcessDefinitionId
:   Type: Process_Definition Identifier.  
    Process Definition Id

### ActivityDefinition_DetailWithSLA { #Structure_ActivityDefinition_DetailWithSLA }

Contains the generic details for activity definition SLA

_Attributes_

ActivityDefinition_Detail
:   Type: [ActivityDefinition_Detail](<#Structure_ActivityDefinition_Detail>).  
    Activity Definition Detail

ActivityDefinitionSLA_Detail
:   Type: [ActivityDefinitionSLA_Detail](<#Structure_ActivityDefinitionSLA_Detail>).  
    Activity Definition Config Detail

### ActivityDefinitionSLA_Config { #Structure_ActivityDefinitionSLA_Config }

ActivityDefinitionSLA Config

_Attributes_

ActivityDefinitionSLAId
:   Type: ActivityDefinitionSLA Identifier.  
    Identifier

ActivityDefinitionId
:   Type: Activity_Definition Identifier.  
    Activity Definition Identifier

ActivityDefinitionGlobalKey
:   Type: Text.  
    ActivityDefinition GlobalKey

ProcessDefinitionId
:   Type: Process_Definition Identifier.  
    ProcessDefinition Id

ProcessDefinitionGlobalKey
:   Type: Text.  
    ProcessDefinition GlobalKey

ResponseTimeInMinutes
:   Type: Integer.  
    Duration that the activty has to be completed

### ActivityDefinitionSLA_Create { #Structure_ActivityDefinitionSLA_Create }

Public structure to enable to create a new activity definition extended configuration

_Attributes_

Id
:   Type: ActivityDefinitionSLA Identifier.  
    Activity Definition SLA Identifier

ActivityDefinitionId
:   Type: Activity_Definition Identifier.  
    Activity Definition Identifier

ResponseTimeInMinutes
:   Type: Integer.  
    Activity SLA minutes to be completed

### ActivityDefinitionSLA_CreateOrUpdate { #Structure_ActivityDefinitionSLA_CreateOrUpdate }

Public structure to enable to create or update an existing activity definition extended

_Attributes_

Id
:   Type: ActivityDefinitionSLA Identifier.  
    Activity Definition SLA Identifier

ActivityDefinitionId
:   Type: Activity_Definition Identifier.  
    Process Definition SLA Identifier

CalendarId
:   Type: Calendar Identifier.  
    Calendar Id

ResponseTimeInMinutes
:   Type: Integer.  
    Activity SLA in minutes to be completed

IsActive
:   Type: Boolean.  
    True if the extended definition is active

### ActivityDefinitionSLA_Detail { #Structure_ActivityDefinitionSLA_Detail }

Public structure to retrieve details about activity definition configuration details

_Attributes_

Id
:   Type: ActivityDefinitionSLA Identifier.  
    Activity Definition SLA Identifier

ActivityDefinitionId
:   Type: Activity_Definition Identifier.  
    Process Definition SLA Identifier

ResponseTimeInMinutes
:   Type: Integer.  
    Activity SLA in minutes to be completed

IsActive
:   Type: Boolean.  
    True if the extended definition is active

ActivityDefinition
:   Type: [ActivityDefinition_Detail](<#Structure_ActivityDefinition_Detail>).  
    Activity Identifier

ProcessDefinition
:   Type: [ProcessDefinition_Detail](<#Structure_ProcessDefinition_Detail>).  
    Process Definition Identifier

### ActivityDefiniton_Config { #Structure_ActivityDefiniton_Config }

ActivityDefiniton Config

_Attributes_

ActivityDefinitionId
:   Type: Activity_Definition Identifier.  
    Activity Definition Identifier

ActivityDefinitionGlobalKey
:   Type: Text.  
    Activity Definition  GlobalKey

ProcessDefinitionId
:   Type: Process_Definition Identifier.  
    ProcessDefinition Id

ProcessDefinitionGlobalKey
:   Type: Text.  
    ProcessDefinition GlobalKey

ActivityName
:   Type: Text.  
    Activity Name

### FilterResults4 { #Structure_FilterResults4 }

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

### FilterResults5 { #Structure_FilterResults5 }

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

### ProcessActivityConfigs { #Structure_ProcessActivityConfigs }

Config

_Attributes_

ProcessDefinitionExtendedConfigs
:   Type: [ProcessDefinitionExtended_Config](<#Structure_ProcessDefinitionExtended_Config>) List.  
    ProcessDefinitionExtendedConfigs

ProcessDefinitionPriorityConfigs
:   Type: [ProcessDefinitionPriority_Config](<#Structure_ProcessDefinitionPriority_Config>) List.  
    ProcessDefinitionPriorityConfigs

ProcessDefinitionSLAConfigs
:   Type: [ProcessDefinitionSLA_Config](<#Structure_ProcessDefinitionSLA_Config>) List.  
    ProcessDefinitionSLAConfigs

ActivityDefinitionSLAConfigs
:   Type: [ActivityDefinitionSLA_Config](<#Structure_ActivityDefinitionSLA_Config>) List.  
    ActivityDefinitionSLAConfigs

ActivityDefinitonConfigs
:   Type: [ActivityDefiniton_Config](<#Structure_ActivityDefiniton_Config>) List.  
    ActivityDefiniton Configs

### ProcessConfiguration_Save { #Structure_ProcessConfiguration_Save }

Save Activity Definition Configuration structure

_Attributes_

ProcessDefinitionId
:   Type: Process_Definition Identifier.  
    ProcessDefinition Id

ActivityDefinitionId
:   Type: Activity_Definition Identifier.  
    ActivityDefinition Id

EspaceId
:   Type: Espace Identifier.  
    Contains the User interface associated espace for the activity execution

ScreenUI
:   Type: Text.  
    Definition for Screen Name for the activity

ResponseTimeInMinutes
:   Type: Integer.  
    Duration that the activty has to be completed

CalendarId
:   Type: Calendar Identifier.  
    Calendar Id

IsActive
:   Type: Boolean.  
    If is active

### ProcessConfiguration_View { #Structure_ProcessConfiguration_View }

Activity Definition Configuration structure

_Attributes_

ProcessDefinitionId
:   Type: Process_Definition Identifier.  
    ProcessDefinition Id

ActivityDefinitionId
:   Type: Activity_Definition Identifier.  
    ActivityDefinition Id

ProcessName
:   Type: Text.  
    Process name

ActivityName
:   Type: Text.  
    Activity name

ProcessDefinitionSSKey
:   Type: Text.  
    ProcessDefinition SSKey

ActivityDefinitionSSKey
:   Type: Text.  
    ActivityDefinition SSKey

EspaceId
:   Type: Espace Identifier.  
    Contains the User interface associated espace for the activity execution

EspaceName
:   Type: Text.  
    Espace Name

ScreenUI
:   Type: Text.  
    Definition for Screen Name for the activity

ResponseTimeInMinutes
:   Type: Integer.  
    Duration that the activty has to be completed

CalendarId
:   Type: Calendar Identifier.  
    Calendar Id

### ProcessDefinition_Detail { #Structure_ProcessDefinition_Detail }

Contains the generic details for process definition

_Attributes_

ProcessDefinitionId
:   Type: Process_Definition Identifier.  
    Process Definition Identifier

Label
:   Type: Text (100).  
    Activity Definition Label

### ProcessDefinitionExtended_Config { #Structure_ProcessDefinitionExtended_Config }

ProcessDefinitionExtended Config

_Attributes_

ProcessDefinitionExtendedId
:   Type: ProcessDefinitionExtended Identifier.  
    Identifier

ProcessDefinitionGlobalKey
:   Type: Text.  
    ProcessDefinition GlobalKey

ProcessDefinitionId
:   Type: Process_Definition Identifier.  
    Process Definition Identifier

CalendarId
:   Type: Calendar Identifier.  
    Possible calendar associated with the process

### ProcessDefinitionExtended_Create { #Structure_ProcessDefinitionExtended_Create }

Public structure to enable to create a new process definition extended confgurations

_Attributes_

Id
:   Type: ProcessDefinitionExtended Identifier.  
    Process Definition SLA Identifier

ProcessDefinitionId
:   Type: Process_Definition Identifier.  
    Unique Identifier

CalendarId
:   Type: Calendar Identifier.  
    Ccalendar associated with the process

### ProcessDefinitionExtended_CreateOrUpdate { #Structure_ProcessDefinitionExtended_CreateOrUpdate }

Public structure to enable to create/update an existing process definition configuration

_Attributes_

Id
:   Type: ProcessDefinitionExtended Identifier.  
    Process Definition SLA Identifier

ProcessDefinitionId
:   Type: Process_Definition Identifier.  
    Process Definition SLA Identifier

CalendarId
:   Type: Calendar Identifier.  
    Ccalendar associated with the process

IsActive
:   Type: Boolean.  
    True if the extended definition is active

### ProcessDefinitionPriority_Config { #Structure_ProcessDefinitionPriority_Config }

ProcessDefinitionPriority Config

_Attributes_

ProcessDefinitionPriorityId
:   Type: ProcessDefinitionPriority Identifier.  
    Identifier

ProcessDefinitionId
:   Type: Process_Definition Identifier.  
    Process Definition Identifier

ProcessDefinitionGlobalKey
:   Type: Text.  
    ProcessDefinition GlobalKey

Label
:   Type: Text.  
    Description

Order
:   Type: Integer.  
    Order

### ProcessDefinitionPriorityCreate { #Structure_ProcessDefinitionPriorityCreate }

Public structure to create a new priority associated to an existing process definition.

_Attributes_

Id
:   Type: ProcessDefinitionPriority Identifier.  
    Process Definition Priority Identifier

Name
:   Type: Text (50).  
    Description

Order
:   Type: Integer.  
    Order

ProcessDefinitionId
:   Type: Process_Definition Identifier.  
    Process Definition Identifier

### ProcessDefinitionPriorityCreateOrUpdate { #Structure_ProcessDefinitionPriorityCreateOrUpdate }

Public structure to create/update priority associated to an existing process definition.

_Attributes_

Id
:   Type: ProcessDefinitionPriority Identifier.  
    Priority type identifier

Name
:   Type: Text (50).  
    Description

Order
:   Type: Integer.  
    Order

IsActive
:   Type: Boolean.  
    True if is active

ProcessDefinitionId
:   Type: Process_Definition Identifier.  
    Process Definition Id

### ProcessDefinitionPriorityDetail { #Structure_ProcessDefinitionPriorityDetail }

Public structure to return the details for process priority

_Attributes_

Id
:   Type: ProcessDefinitionPriority Identifier.  
    Process Definition Priority Identifier

Name
:   Type: Text.  
    Description

IsActive
:   Type: Boolean.  
    If priority is active

Order
:   Type: Integer.  
    Priority Order

ProcessDefinitionId
:   Type: Process_Definition Identifier.  
    Process Definition Identifier

### ProcessDefinitionSLA_Config { #Structure_ProcessDefinitionSLA_Config }

ProcessDefinitionSLA Config

_Attributes_

ProcessDefinitionSLAId
:   Type: ProcessDefinitionSLA Identifier.  
    Identifier

ProcessDefinitionId
:   Type: Process_Definition Identifier.  
    Process Definition Identifier

ProcessDefinitionGlobalKey
:   Type: Text.  
    ProcessDefinition GlobalKey

ResponseTimeInMinutes
:   Type: Integer.  
    Process SLA minutes to be completed

### ProcessDefinitionSLA_Create { #Structure_ProcessDefinitionSLA_Create }

Public structure to enable to create a new process definition SLA

_Attributes_

Id
:   Type: ProcessDefinitionSLA Identifier.  
    Process Definition SLA Identifier

ProcessDefinitionId
:   Type: Process_Definition Identifier.  
    Unique Identifier

ResponseTimeInMinutes
:   Type: Integer.  
    Process SLA in minutes to be completed

### ProcessDefinitionSLA_CreateOrUpdate { #Structure_ProcessDefinitionSLA_CreateOrUpdate }

Public structure to enable to create/update an existing process definition sla

_Attributes_

Id
:   Type: ProcessDefinitionSLA Identifier.  
    Process Definition SLA Identifier

ProcessDefinitionId
:   Type: Process_Definition Identifier.  
    Process Definition SLA Identifier

ResponseTimeInMinutes
:   Type: Integer.  
    Process SLA in minutes to be completed

IsActive
:   Type: Boolean.  
    True if the extended definition is active

### ProcessDefinitionSLA_DetailWithProcessDefinition { #Structure_ProcessDefinitionSLA_DetailWithProcessDefinition }

Public structure to retrieve details about process definition configuration

_Attributes_

Id
:   Type: ProcessDefinitionSLA Identifier.  
    Process Definition SLA Identifier

ProcessDefinitionId
:   Type: Process_Definition Identifier.  
    Process Definition SLA Identifier

ResponseTimeInMinutes
:   Type: Integer.  
    Process SLA in minutes to be completed

IsActive
:   Type: Boolean.  
    True if the extended definition is active

ProcessDefinition
:   Type: [ProcessDefinition_Detail](<#Structure_ProcessDefinition_Detail>).  
    Process Definition Identifier
