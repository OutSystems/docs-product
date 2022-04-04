---
summary: The Embedded Process Automation (EPA) shows automatically a floating taskbox in the browser, with all pending activities.
tags: runtime-traditionalweb
---

# EPA Taskbox API


The Embedded Process Automation (EPA) shows automatically a floating taskbox in the browser, with all pending activities. Each item includes instructions and a link that opens the activity page, so the user can work on the activity. Mobile apps require a custom UI solution.

<div class="info" markdown="1">

See [Using Taskbox in Reactive Web Apps](https://success.outsystems.com/Documentation/How-to_Guides/Processes/Using_Taskbox_in_Reactive_Web_Apps) for  more information about a sample Forge component for a taskbox in Reactive Web Apps, and the instructions how to use the component. The focus of this article is the taskbox in Traditional Web Apps.

</div>


## Summary

Action | Description
---|---
[API_GetActivities](<#API_GetActivities>) | Returns the activities of a user.%%Activity filtering and pagination are allowed.
[API_GetActivityGuidanceHtml](<#API_GetActivityGuidanceHtml>) | Encodes the activity guidance instructions in HTML format.
[API_GetActivityPagination](<#API_GetActivityPagination>) | Returns the pagination information of all activities currently displayed in the Taskbox of the user.
[API_GetActivityVisualization](<#API_GetActivityVisualization>) | Returns information on how an open activity is displayed in the Taskbox.
[API_GetDynamicHtml](<#API_GetDynamicHtml>) | [Deprecated] Returns the JavaScript code for the Taskbox and its current content.
[API_GetNewOpenActivity](<#API_GetNewOpenActivity>) | Returns the activity that is currently open by the user and has the indicated activity as one of the previous activities in the process flow.
[API_GetStaticHtml](<#API_GetStaticHtml>) | [Deprecated] Returns the HTML of the Taskbox with absolute URLs, i.e., starting with &quot;http://&lt;Server Name&gt;/&quot;.
[API_MarkActivitiesAsSeen](<#API_MarkActivitiesAsSeen>) | Displays all Taskbox activities for the user as already seen, i.e., only new activities will be displayed as not seen in the Taskbox.
[API_SetActivityVisualization](<#API_SetActivityVisualization>) | Sets how an open activity is displayed in the Taskbox.
[Inbox_DisableInServer](<#Inbox_DisableInServer>) | Disables the Taskbox in the environment.
[Inbox_EnableInServer](<#Inbox_EnableInServer>) | Enables the Taskbox in the environment.

Structure | Description
---|---
[Inbox_FilterCriteria](<#Structure_Inbox_FilterCriteria>) | 
[Inbox_PaginationCriteria](<#Structure_Inbox_PaginationCriteria>) | 
[Activity](<#Structure_Activity>) | The structure with the information of an activity in the TaskBox.
[PaginationInfo](#Structure_PaginationInfo) | The structure with information of the number of activities in the TaskBox.


## Actions

### API_GetActivities { #API_GetActivities }

Returns the activities of a user.  
Activity filtering and pagination are allowed.

*Inputs*

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

*Outputs*

ActivityList
:   Type: [Activity](#Structure_Activity) Record List.  
    The list of activities.

PaginationInfo
:   Type: [PaginationInfo](#Structure_PaginationInfo).  
    The definite pagination information for displaying the activities in the Taskbox of the user.

### API_GetActivityGuidanceHtml { #API_GetActivityGuidanceHtml }

Encodes the activity guidance instructions in HTML format.

*Inputs*

Guidance
:   Type: mandatory, Text.  
    The activity guidance instructions.

*Outputs*

GuidanceHtml
:   Type: Text.  
    The activity guidance instructions encoded in HTML format.

### API_GetActivityPagination { #API_GetActivityPagination }

Returns the pagination information of all activities currently displayed in the Taskbox of the user.

*Inputs*

UserId
:   Type: mandatory, User Identifier.  
    The identifier of the user.

FilterCriteria
:   Type: optional, [Inbox_FilterCriteria](<#Structure_Inbox_FilterCriteria>).  
    The criteria for filtering activities.  
    Leave it empty for no filtering.

*Outputs*

PaginationInfo
:   Type: [PaginationInfo](#Structure_PaginationInfo).  
    The pagination information of all activities currently displayed in the Taskbox of the user.

### API_GetActivityVisualization { #API_GetActivityVisualization }

Returns information on how an open activity is displayed in the Taskbox.

*Inputs*

ActivityId
:   Type: mandatory, Activity Identifier.  
    The identifier of the activity.

*Outputs*

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

### API_GetDynamicHtml { #API_GetDynamicHtml }

[Deprecated] Returns the JavaScript code for the Taskbox and its current content.

*Inputs*

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

*Outputs*

Html
:   Type: Text.  
    The JavaScript code for the Taskbox and its current content.

### API_GetNewOpenActivity { #API_GetNewOpenActivity }

Returns the activity that is currently open by the user and has the indicated activity as one of the previous activities in the process flow.

*Inputs*

UserId
:   Type: mandatory, User Identifier.  
    The identifier of the user.

PreviousActivityId
:   Type: mandatory, Activity Identifier.  
    The identifier of one of the previous activities in the process flow.

*Outputs*

ActivityId
:   Type: Activity Identifier.  
    The activity that is currently open by the user.

### API_GetStaticHtml { #API_GetStaticHtml }

[Deprecated] Returns the HTML of the Taskbox with absolute URLs, i.e., starting with &quot;http://&lt;Server Name&gt;/&quot;.

*Inputs*

EspaceId
:   Type: mandatory, Espace Identifier.  
    The identifier of the eSpace.

UserId
:   Type: mandatory, User Identifier.  
    The identifier of the user.

Locale
:   Type: mandatory, Text.  
    The language locale.

Data
:   Type: mandatory, Text.  
    [Deprecated]

*Outputs*

Html
:   Type: Text.  
    The HTML of the Taskbox with absolute URLs, i.e., starting with &quot;http://&lt;Server Name&gt;/&quot;.

### API_MarkActivitiesAsSeen { #API_MarkActivitiesAsSeen }

Displays all Taskbox activities for the user as already seen, i.e., only new activities will be displayed as not seen in the Taskbox.

*Inputs*

UserId
:   Type: mandatory, User Identifier.  
    The identifier of the user.

### API_SetActivityVisualization { #API_SetActivityVisualization }

Sets how an open activity is displayed in the Taskbox.

*Inputs*

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

### Inbox_DisableInServer { #Inbox_DisableInServer }

Disables the Taskbox in the environment.

### Inbox_EnableInServer { #Inbox_EnableInServer }

Enables the Taskbox in the environment.


## Structures

### Inbox_FilterCriteria { #Structure_Inbox_FilterCriteria }


*Attributes*

ActivityLabel
:   Type: Text (50).  
    

### Inbox_PaginationCriteria { #Structure_Inbox_PaginationCriteria }


*Attributes*

StartIndex
:   Type: Integer.  
    

LineCount
:   Type: Integer.  
    

### Activity { #Structure_Activity }

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
 

### PaginationInfo { #Structure_PaginationInfo }

The structure with information of the number of activities in the TaskBox.

_Attributes_

Total
:   Type: Integer.
    The total number of activities in the TaskBox.

Unseen
:   Type: Integer.
    The number of unseen activities due to pagination.

