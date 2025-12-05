---
summary: Explore the EPA Taskbox API functionalities in OutSystems 11 (O11) for managing user activities in Traditional Web Apps.
tags: epa taskbox api, user activities management, traditional web api integration, outsystems traditional web apps, pending activities visualization
locale: en-us
guid: 24b83310-17ec-4eea-a688-89da29816145
app_type: traditional web apps
platform-version: o11
figma:
audience:
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# EPA Taskbox API

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

The Embedded Process Automation (EPA) shows automatically a floating taskbox in the browser, with all pending activities. Each item includes instructions and a link that opens the activity page, so the user can work on the activity. Mobile apps require a custom UI solution.

<div class="info" markdown="1">

See [Using Taskbox in Reactive Web Apps](https://success.outsystems.com/Documentation/How-to_Guides/Processes/Using_Taskbox_in_Reactive_Web_Apps) for  more information about a sample Forge component for a taskbox in Reactive Web Apps, and the instructions how to use the component. The focus of this article is the taskbox in Traditional Web Apps.

</div>

## Summary

| Action | Description |
| ---|--- |
| [API_GetActivities](<#API_GetActivities>) | Returns the activities of a user.<br/>Activity filtering and pagination are allowed. |
| [API_GetActivityGuidanceHtml](<#API_GetActivityGuidanceHtml>) | Encodes the activity guidance instructions in HTML format. |
| [API_GetActivityPagination](<#API_GetActivityPagination>) | Returns the pagination information of all activities currently displayed in the Taskbox of the user. |
| [API_GetActivityVisualization](<#API_GetActivityVisualization>) | Returns information on how an open activity is displayed in the Taskbox. |
| [API_GetDynamicHtml](<#API_GetDynamicHtml>) | [Deprecated] Returns the JavaScript code for the Taskbox and its current content. |
| [API_GetNewOpenActivity](<#API_GetNewOpenActivity>) | Returns the activity that is currently open by the user and has the indicated activity as one of the previous activities in the process flow. |
| [API_GetStaticHtml](<#API_GetStaticHtml>) | [Deprecated] Returns the HTML of the Taskbox with absolute URLs, i.e., starting with &quot;http://&lt;Server Name&gt;/&quot;. |
| [API_MarkActivitiesAsSeen](<#API_MarkActivitiesAsSeen>) | Displays all Taskbox activities for the user as already seen, i.e., only new activities will be displayed as not seen in the Taskbox. |
| [API_SetActivityVisualization](<#API_SetActivityVisualization>) | Sets how an open activity is displayed in the Taskbox. |
| [Inbox_DisableInServer](<#Inbox_DisableInServer>) | Disables the Taskbox in the environment. |
| [Inbox_EnableInServer](<#Inbox_EnableInServer>) | Enables the Taskbox in the environment. |

| Structure | Description |
| ---|--- |
| [Inbox_FilterCriteria](<#Structure_Inbox_FilterCriteria>) | |
| [Inbox_PaginationCriteria](<#Structure_Inbox_PaginationCriteria>) | |
| [Activity](<#Structure_Activity>) | The structure with the information of an activity in the TaskBox. |
| [PaginationInfo](#Structure_PaginationInfo) | The structure with information of the number of activities in the TaskBox. |

## Actions

### API_GetActivities {#API_GetActivities}

Returns the activities of a user.  
Activity filtering and pagination are allowed.

_Inputs_

UserId
:   Type: mandatory, User Identifier.  
    The identifier of the user.

FilterCriteria
:   Type: optional, [Inbox_FilterCriteria](<#Structure_Inbox_FilterCriteria>).  
    The criteria for filtering activities.  
    Leave it empty for no filtering.

PaginationCriteria
:   Type: mandatory, [Inbox_PaginationCriteria](<#Structure_Inbox_PaginationCriteria>).  
    The pagination criteria for displaying the activities in the Taskbox of the user.  
    Leave it empty for no pagination.

_Outputs_

ActivityList
:   Type: [Activity](#Structure_Activity) Record List.  
    The list of activities.

PaginationInfo
:   Type: [PaginationInfo](#Structure_PaginationInfo).  
    The definite pagination information for displaying the activities in the Taskbox of the user.

### API_GetActivityGuidanceHtml {#API_GetActivityGuidanceHtml}

Encodes the activity guidance instructions in HTML format.

_Inputs_

Guidance
:   Type: mandatory, Text.  
    The activity guidance instructions.

_Outputs_

GuidanceHtml
:   Type: Text.  
    The activity guidance instructions encoded in HTML format.

### API_GetActivityPagination {#API_GetActivityPagination}

Returns the pagination information of all activities currently displayed in the Taskbox of the user.

_Inputs_

UserId
:   Type: mandatory, User Identifier.  
    The identifier of the user.

FilterCriteria
:   Type: optional, [Inbox_FilterCriteria](<#Structure_Inbox_FilterCriteria>).  
    The criteria for filtering activities.  
    Leave it empty for no filtering.

_Outputs_

PaginationInfo
:   Type: [PaginationInfo](#Structure_PaginationInfo).  
    The pagination information of all activities currently displayed in the Taskbox of the user.

### API_GetActivityVisualization {#API_GetActivityVisualization}

Returns information on how an open activity is displayed in the Taskbox.

_Inputs_

ActivityId
:   Type: mandatory, Activity Identifier.  
    The identifier of the activity.

_Outputs_

HideDone
:   Type: Boolean.  
    If True, the 'Done' button is not available when the activity is open in the Taskbox.

HideRelease
:   Type: Boolean.  
    If True, the 'Release' button is not available when the activity is open in the Taskbox.

CustomInstructions
:   Type: Text.  
    The text/HTML of custom instructions displayed below the normal activity instructions when the activity is open in the Taskbox.  
    The instructions have a maximum length of 500 characters.

### API_GetDynamicHtml {#API_GetDynamicHtml}

[Deprecated] Returns the JavaScript code for the Taskbox and its current content.

_Inputs_

EspaceId
:   Type: mandatory, Espace Identifier.  
    [Deprecated]

UserId
:   Type: mandatory, User Identifier.  
    The identifier of the user.

Locale
:   Type: mandatory, Text.  
    [Deprecated]

Data
:   Type: mandatory, Text.  
    [Deprecated]

_Outputs_

Html
:   Type: Text.  
    The JavaScript code for the Taskbox and its current content.

### API_GetNewOpenActivity {#API_GetNewOpenActivity}

Returns the activity that is currently open by the user and has the indicated activity as one of the previous activities in the process flow.

_Inputs_

UserId
:   Type: mandatory, User Identifier.  
    The identifier of the user.

PreviousActivityId
:   Type: mandatory, Activity Identifier.  
    The identifier of one of the previous activities in the process flow.

_Outputs_

ActivityId
:   Type: Activity Identifier.  
    The activity that is currently open by the user.

### API_GetStaticHtml {#API_GetStaticHtml}

[Deprecated] Returns the HTML of the Taskbox with absolute URLs, i.e., starting with &quot;http://&lt;Server Name&gt;/&quot;.

_Inputs_

EspaceId
:   Type: mandatory, Espace Identifier.  
    The identifier of the module/eSpace.

UserId
:   Type: mandatory, User Identifier.  
    The identifier of the user.

Locale
:   Type: mandatory, Text.  
    The language locale.

Data
:   Type: mandatory, Text.  
    [Deprecated]

_Outputs_

Html
:   Type: Text.  
    The HTML of the Taskbox with absolute URLs, i.e., starting with &quot;http://&lt;Server Name&gt;/&quot;.

### API_MarkActivitiesAsSeen {#API_MarkActivitiesAsSeen}

Displays all Taskbox activities for the user as already seen, i.e., only new activities will be displayed as not seen in the Taskbox.

_Inputs_

UserId
:   Type: mandatory, User Identifier.  
    The identifier of the user.

### API_SetActivityVisualization {#API_SetActivityVisualization}

Sets how an open activity is displayed in the Taskbox.

_Inputs_

ActivityId
:   Type: mandatory, Activity Identifier.  
    The identifier of the activity.

HideDone
:   Type: optional, Boolean.  
    If True, the 'Done' button is not available when the activity is open in the Taskbox.

HideRelease
:   Type: optional, Boolean.  
    If True, the 'Release' button is not available when the activity is open in the Taskbox.

CustomInstructions
:   Type: optional, Text.  
    The text/HTML for custom instructions displayed below the normal activity instructions when the activity is open in the Taskbox.  
    The custom instructions have a maximum length of 500 characters.

### Inbox_DisableInServer {#Inbox_DisableInServer}

Disables the Taskbox in the environment.

### Inbox_EnableInServer {#Inbox_EnableInServer}

Enables the Taskbox in the environment.

## Structures

### Inbox_FilterCriteria {#Structure_Inbox_FilterCriteria}

_Attributes_

ActivityLabel
:   Type: Text (50).  

### Inbox_PaginationCriteria {#Structure_Inbox_PaginationCriteria}

_Attributes_

StartIndex
:   Type: Integer.  

LineCount
:   Type: Integer.  

### Activity {#Structure_Activity}

The structure with the information of an activity in the TaskBox.

_Attributes_

Id
:   Type: EntityReference.
    The identifier of the Activity.

Label
:   Type: Text (50).
    The label of the Activity.

LabelLang
:   Type: Text (50).
    The code of the language locale of the label.

Details
:   Type: Text (50).
    The details of the Activity.

DueDate
:   Type: DateTime.
    The due date of the Activity.

IsOpened
:   Type: Boolean.
    Is True if the activity is already open by a user.

IsSeen
:   Type: Boolean.
    Is False if the activity is not visible in the TaskBox due to pagination.

### PaginationInfo {#Structure_PaginationInfo}

The structure with information of the number of activities in the TaskBox.

_Attributes_

Total
:   Type: Integer.
    The total number of activities in the TaskBox.

Unseen
:   Type: Integer.
    The number of unseen activities due to pagination.
