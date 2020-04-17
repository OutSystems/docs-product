# System Actions



## Summary

Server Action | Description | Is Function?
---|---|---
[AbortTransaction](<#AbortTransaction>) | Issues a database ROLLBACK command that undoes all changes performed on the database since the last commit. | 
[ActivityClose](<#ActivityClose>) | Explicitly closes a Human Activity or a Wait Activity ending the execution.%%The the id of the next Human Activity in sequence is returned, if determined. | 
[ActivityGetUrl](<#ActivityGetUrl>) | Returns the URL of the web screen where an activity will be carried out, once opened. | Yes
[ActivityOpen](<#ActivityOpen>) | Explicitly forces a Human Activity instance to be opened in an end user's Taskbox. | 
[ActivityReset](<#ActivityReset>) | Releases the Human Activity leaving it to be opened and carried out by another end user. | 
[ActivitySchedule](<#ActivitySchedule>) | Schedules a date for the Human Activity to be available in the Taskbox. | 
[ActivitySetGroup](<#ActivitySetGroup>) | Limit a Human Activity visibility and handling to end users who belong to a specific group. | 
[ActivitySkip](<#ActivitySkip>) | Explicitly skips the execution of a Human Activity or a Wait Activity.%%The the id of the next Human Activity in sequence is returned, if determined. | 
[ActivityStart](<#ActivityStart>) | Explicitly starts the execution of a ConditionalStart Activity. | 
[ClientCertificateGetDetails](<#ClientCertificateGetDetails>) | Gets the relevant information for the current request client certificate from the .NET framework. | 
[ClientCertificateValue](<#ClientCertificateValue>) | Gets the value of a specific property of the client certificate in the .NET framework. | 
[CommitTransaction](<#CommitTransaction>) | Issues a database COMMIT command that makes effective all changes done on the database since the last commit. | 
[Deprecated_Notify](<#Deprecated_Notify>) | DEPRECATED: This action is deprecated because Events are now available for Web Blocks. Use Events in Web Blocks to propagate changes from a Web Block to the parent block.%%%%The way a web block has to notify a screen or web block using it. They handle the notification through the action set in their On Notify property. To retrieve a message sent with the notification, use the NotifyGetMessage function. | 
[Deprecated_NotifyGetMessage](<#Deprecated_NotifyGetMessage>) | DEPRECATED: This action is deprecated because Events are now available for Web Blocks. Use Input Parameters in block Events to send information to the parent block when the Event is triggered.%%%%Returns the notification message sent by the Notify action. | Yes
[Deprecated_NotifyWidget](<#Deprecated_NotifyWidget>) | The way a web block has to notify a screen or web block using it. They handle the notification through the action set in their On Notify property. To retrieve a message sent with the notification, use the NotifyGetMessage function. | 
[EspaceInvalidateCache](<#EspaceInvalidateCache>) | Invalidates eSpace's specific caches across all Front-end servers and consumer eSpaces. Limit the invalidation to a single tenant by setting the tenant identifier. | 
[GenerateGuid](<#GenerateGuid>) | Generates and returns a new GUID. | Yes
[InboundSmsGetDetails](<#InboundSmsGetDetails>) | DEPRECATED: This action is deprecated because the SMS features are no longer available. Returns information about the inbound SMS that is currently being processed. | 
[IntegratedSecurityCheckRole](<#IntegratedSecurityCheckRole>) | Verifies whether the current Windows user has access to a specific role. | Yes
[IntegratedSecurityGetDetails](<#IntegratedSecurityGetDetails>) | Gets information about the current Windows user that made the request. | 
[ListAll](<#ListAll>) | Determines if all the elements in the list satisfy the given condition. | 
[ListAny](<#ListAny>) | Determines if any of the elements in the list satisfies the given condition. | 
[ListAppend](<#ListAppend>) | Adds an element to the end of a list. | 
[ListAppendAll](<#ListAppendAll>) | Adds the elements of the source list to the end of the destination list. | 
[ListClear](<#ListClear>) | Removes all elements from a list. | 
[ListDistinct](<#ListDistinct>) | Filters duplicate elements from a list. | Yes
[ListDuplicate](<#ListDuplicate>) | Duplicates the elements of a list into another list. | Yes
[ListFilter](<#ListFilter>) | Returns a new list with the elements from the List parameter satisfying the given condition. | 
[ListIndexOf](<#ListIndexOf>) | Returns the position of the first element of the List parameter that satisfies the given condition, or -1 if no element satisfying the condition was found. | 
[ListInsert](<#ListInsert>) | Inserts an element in a specific position of a list. | 
[ListRemove](<#ListRemove>) | Removes an element from a specific position of a list. | 
[ListSort](<#ListSort>) | Sorts the elements of the List parameter by the given criteria. Note that ListSort is different from the dynamic sorting in Aggregates. Multiple attributes having different data types (such as Text and Integer) in the criteria may not sort the list correctly. | 
[Login](<#Login>) | Logs a specified user in the application.%%In case of success, 'UserId' and 'Username' session variables are filled with the user data. | 
[LoginPassword](<#LoginPassword>) | Logs a specified user in the application using a password.%%In case of success, 'UserId' and 'Username' session variables are filled with the user data. | 
[LogMessage](<#LogMessage>) | Registers information that can be presented in Service Center in the module general log. | 
[Logout](<#Logout>) | Logs out a specific user from the application.%%The 'UserId' and 'Username' session variables are cleared. | 
[ProcessTerminate](<#ProcessTerminate>) | Explicitly forces a Process to terminate its execution. | 
[SetCurrentLocale](<#SetCurrentLocale>) | Sets the language locale of the user session to change the application presentation language. | 
[TenantCreate](<#TenantCreate>) | Creates a new tenant and associates it with the provisioning site. | 
[TenantInvalidateCache](<#TenantInvalidateCache>) | Invalidates tenant's specific caches across all Front-end servers and eSpaces. This action is now available for compatibility purposes only. Please use the EspaceInvalidateCache action instead and invalidate tenant's specific caches by eSpace to narrow the invalidation scope | 
[TenantSwitch](<#TenantSwitch>) | Change the context to the given tenant identifier. When switching tenant, the session is cleared (equivalent to an implicit logout, before changing the tenant), the OnSessionStart actions are executed, and the current transaction is committed. | 

Client Action | Description | Is Function?
---|---|---
[ListAll](<#Client_ListAll>) | Determines if all the elements in the list satisfy the given condition. | 
[ListAny](<#Client_ListAny>) | Determines if any of the elements in the list satisfies the given condition. | 
[ListAppend](<#Client_ListAppend>) | Adds an element to the end of a list. | 
[ListAppendAll](<#Client_ListAppendAll>) | Adds the elements of the source list to the end of the destination list. | 
[ListClear](<#Client_ListClear>) | Removes all elements from a list. | 
[ListDistinct](<#Client_ListDistinct>) | Filters duplicate elements from a list. | Yes
[ListDuplicate](<#Client_ListDuplicate>) | Duplicates the elements of a list into another list. | Yes
[ListFilter](<#Client_ListFilter>) | Returns a new list with the elements from the List parameter satisfying the given condition. | 
[ListIndexOf](<#Client_ListIndexOf>) | Returns the position of the first element of the List parameter that satisfies the given condition, or -1 if no element satisfying the condition was found. | 
[ListInsert](<#Client_ListInsert>) | Inserts an element in a specific position of a list. | 
[ListRemove](<#Client_ListRemove>) | Removes an element from a specific position of a list. | 
[ListSort](<#Client_ListSort>) | Sorts the elements of the List parameter by the given criteria. Note that ListSort is different from the dynamic sorting in Aggregates. Multiple attributes having different data types (such as Text and Integer) in the criteria may not sort the list correctly. | 
[LogMessage](<#Client_LogMessage>) | Registers information that can be presented in Service Center in the module general log. | 
[RequireScript](<#Client_RequireScript>) | Add a Javascript to the html header. Multiple calls for the same Javascript will only add it once. Action flow will proceed after the Javascript has been successfully loaded. | 

## Server Actions

### AbortTransaction { #AbortTransaction }

Issues a database ROLLBACK command that undoes all changes performed on the database since the last commit.

### ActivityClose { #ActivityClose }

Explicitly closes a Human Activity or a Wait Activity ending the execution.  
The the id of the next Human Activity in sequence is returned, if determined.

*Inputs*

ActivityId
:   Type: mandatory, Activity Identifier.  
    

*Outputs*

NextHumanActivityId
:   Type: Activity Identifier.  
    

### ActivityGetUrl { #ActivityGetUrl }

Returns the URL of the web screen where an activity will be carried out, once opened.

*Inputs*

ActivityId
:   Type: mandatory, Activity Identifier.  
    

*Outputs*

HandlingUrl
:   Type: Text.  
    

### ActivityOpen { #ActivityOpen }

Explicitly forces a Human Activity instance to be opened in an end user's Taskbox.

*Inputs*

ActivityId
:   Type: mandatory, Activity Identifier.  
    

*Outputs*

HandlingUrl
:   Type: Text.  
    

### ActivityReset { #ActivityReset }

Releases the Human Activity leaving it to be opened and carried out by another end user.

*Inputs*

ActivityId
:   Type: mandatory, Activity Identifier.  
    

ResetActivityUser
:   Type: mandatory, Boolean.  
    

### ActivitySchedule { #ActivitySchedule }

Schedules a date for the Human Activity to be available in the Taskbox.

*Inputs*

ActivityId
:   Type: mandatory, Activity Identifier.  
    

StartDate
:   Type: mandatory, Date Time.  
    

### ActivitySetGroup { #ActivitySetGroup }

Limit a Human Activity visibility and handling to end users who belong to a specific group.

*Inputs*

ActivityId
:   Type: mandatory, Activity Identifier.  
    

GroupId
:   Type: mandatory, Group Identifier.  
    

### ActivitySkip { #ActivitySkip }

Explicitly skips the execution of a Human Activity or a Wait Activity.  
The the id of the next Human Activity in sequence is returned, if determined.

*Inputs*

ActivityId
:   Type: mandatory, Activity Identifier.  
    

*Outputs*

NextHumanActivityId
:   Type: Activity Identifier.  
    

### ActivityStart { #ActivityStart }

Explicitly starts the execution of a ConditionalStart Activity.

*Inputs*

ActivityId
:   Type: mandatory, Activity Identifier.  
    

*Outputs*

NextHumanActivityId
:   Type: Activity Identifier.  
    

### ClientCertificateGetDetails { #ClientCertificateGetDetails }

Gets the relevant information for the current request client certificate from the .NET framework.

*Outputs*

cookie
:   Type: Text.  
    Gets the unique Id for the client certificate, if provided.

flags
:   Type: Integer.  
    A set of flags that provide additional client certificate information. Bit0 is set to 1 if the client certificate is present. Bit1 is set to 1 if the Certificate Authority (CA) of the client certificate is not in the list of recognized CAs on the server.

isPresent
:   Type: Boolean.  
    Gets a value that indicates whether the client certificate is present.

issuer
:   Type: Text.  
    A string that contains a list of subfield values containing information about the certificate issuer.

isValid
:   Type: Boolean.  
    Gets a value that indicates whether the client certificate is valid.

serialNumber
:   Type: Text.  
    Provides the certificate serial number as an ASCII representation of hexadecimal bytes separated by hyphens. For example, 04-67-F3-02.

serverIssuer
:   Type: Text.  
    Gets the issuer field of the server certificate.

serverSubject
:   Type: Text.  
    Gets the subject field of the server certificate.

subject
:   Type: Text.  
    Gets the subject field of the client certificate.

validFrom
:   Type: Date Time.  
    Gets the date when the certificate becomes valid. The date varies with international settings.

validUntil
:   Type: Date Time.  
    Gets the certificate expiration date

### ClientCertificateValue { #ClientCertificateValue }

Gets the value of a specific property of the client certificate in the .NET framework.

*Inputs*

key
:   Type: mandatory, Text.  
    

*Outputs*

value
:   Type: Text.  
    

### CommitTransaction { #CommitTransaction }

Issues a database COMMIT command that makes effective all changes done on the database since the last commit.

### Deprecated_Notify { #Deprecated_Notify }

DEPRECATED: This action is deprecated because Events are now available for Web Blocks. Use Events in Web Blocks to propagate changes from a Web Block to the parent block.  
  
The way a web block has to notify a screen or web block using it. They handle the notification through the action set in their On Notify property. To retrieve a message sent with the notification, use the NotifyGetMessage function.

*Inputs*

Message
:   Type: optional, Text.  
    

### Deprecated_NotifyGetMessage { #Deprecated_NotifyGetMessage }

DEPRECATED: This action is deprecated because Events are now available for Web Blocks. Use Input Parameters in block Events to send information to the parent block when the Event is triggered.  
  
Returns the notification message sent by the Notify action.

*Outputs*

Message
:   Type: Text.  
    

### Deprecated_NotifyWidget { #Deprecated_NotifyWidget }

The way a web block has to notify a screen or web block using it. They handle the notification through the action set in their On Notify property. To retrieve a message sent with the notification, use the NotifyGetMessage function.

*Inputs*

Message
:   Type: optional, Text.  
    

### EspaceInvalidateCache { #EspaceInvalidateCache }

Invalidates eSpace's specific caches across all Front-end servers and consumer eSpaces. Limit the invalidation to a single tenant by setting the tenant identifier.

*Inputs*

EspaceId
:   Type: optional, Espace Identifier.  
    Identifier of the eSpace to invalidate. If not specificed, the identifier of caller eSpace is used.

TenantId
:   Type: optional, Tenant Identifier.  
    Optional tenant identifier to limit the cache invalidation to a specific tenant.

### GenerateGuid { #GenerateGuid }

Generates and returns a new GUID.

*Outputs*

Guid
:   Type: Text.  
    

### InboundSmsGetDetails { #InboundSmsGetDetails }

DEPRECATED: This action is deprecated because the SMS features are no longer available. Returns information about the inbound SMS that is currently being processed.

*Outputs*

MSISDN
:   Type: Phone Number.  
    

LargeAccount
:   Type: Phone Number.  
    

Message
:   Type: Text.  
    

BinaryMessage
:   Type: Text.  
    

UDH
:   Type: Text.  
    

MessageId
:   Type: Text.  
    

Priority
:   Type: Integer.  
    

Encoding
:   Type: Text.  
    

Connection
:   Type: Text.  
    

OperatorCode
:   Type: Text.  
    

Sent
:   Type: Date Time.  
    

Custom1
:   Type: Text.  
    

Custom2
:   Type: Text.  
    

Custom3
:   Type: Text.  
    

### IntegratedSecurityCheckRole { #IntegratedSecurityCheckRole }

Verifies whether the current Windows user has access to a specific role.

*Inputs*

RoleName
:   Type: mandatory, Text.  
    

*Outputs*

Belongs
:   Type: Boolean.  
    

### IntegratedSecurityGetDetails { #IntegratedSecurityGetDetails }

Gets information about the current Windows user that made the request.

*Outputs*

Username
:   Type: Text.  
    

isGuest
:   Type: Boolean.  
    

isSystem
:   Type: Boolean.  
    

isAnonymous
:   Type: Boolean.  
    

isAuthenticated
:   Type: Boolean.  
    

### ListAll { #ListAll }

Determines if all the elements in the list satisfy the given condition.

*Inputs*

List
:   Type: mandatory, Generic Record List.  
    The list that contains the elements to which to apply the condition.

Condition
:   Type: mandatory, Boolean.  
    The boolean expression to check for on each element of the list.

*Outputs*

Result
:   Type: Boolean.  
    True if every element of the List satisfies the condition; otherwise, False.

### ListAny { #ListAny }

Determines if any of the elements in the list satisfies the given condition.

*Inputs*

List
:   Type: mandatory, Generic Record List.  
    The list that contains the elements to which to apply the condition.

Condition
:   Type: mandatory, Boolean.  
    The boolean expression to check for on each element of the list.

*Outputs*

Result
:   Type: Boolean.  
    True if there is an element of the List satisfying the condition; otherwise, False.

### ListAppend { #ListAppend }

Adds an element to the end of a list.

*Inputs*

List
:   Type: mandatory, Generic Record List.  
    The list to add the element to.

Element
:   Type: mandatory, Generic Record.  
    The element to be added to the end of the list.

### ListAppendAll { #ListAppendAll }

Adds the elements of the source list to the end of the destination list.

*Inputs*

List
:   Type: mandatory, Generic Record List.  
    The destination List.

SourceList
:   Type: mandatory, Generic Record List.  
    The list whose elements will be added.

### ListClear { #ListClear }

Removes all elements from a list.

*Inputs*

List
:   Type: mandatory, Generic Record List.  
    The list to remove the elements from.

### ListDistinct { #ListDistinct }

Filters duplicate elements from a list.

*Inputs*

SourceList
:   Type: mandatory, Generic Record List.  
    The list that includes duplicate elements.

*Outputs*

DistinctList
:   Type: Generic Record List.  
    List that only includes the distinct elements of the source list.

### ListDuplicate { #ListDuplicate }

Duplicates the elements of a list into another list.

*Inputs*

SourceList
:   Type: mandatory, Generic Record List.  
    The list to duplicate.

*Outputs*

DuplicatedList
:   Type: Generic Record List.  
    The duplicate list.

### ListFilter { #ListFilter }

Returns a new list with the elements from the List parameter satisfying the given condition.

*Inputs*

SourceList
:   Type: mandatory, Generic Record List.  
    The list that contains the elements to which to apply the condition.

Condition
:   Type: mandatory, Boolean.  
    The boolean expression to check for on each element of the list.

*Outputs*

FilteredList
:   Type: Generic Record List.  
    A new list with the elements that satisfy the condition.

### ListIndexOf { #ListIndexOf }

Returns the position of the first element of the List parameter that satisfies the given condition, or -1 if no element satisfying the condition was found.

**Examples**
```
ListIndexOf(UserList, Is_Active)

Returns the position of the first user in the list of User records satisfying the condition Is_Active = True.
```
```
ListIndexOf(UserList, Name = "James")

Returns the position of the first user in the list of User records satisfying the condition Name = "James".
```
*Inputs*

List
:   Type: mandatory, Generic Record List.  
    The list that contains the elements to which to apply the condition.

Condition
:   Type: mandatory, Boolean.  
    The boolean expression to check for on each element of the list.

*Outputs*

Position
:   Type: Integer.  
    The position of the first element of the list that satisfies the given condition; -1 if no element satisfying the condition was found.

### ListInsert { #ListInsert }

Inserts an element in a specific position of a list.

*Inputs*

List
:   Type: mandatory, Generic Record List.  
    The list to add the element to.

Element
:   Type: mandatory, Generic Record.  
    The element to insert in the list.

Position
:   Type: mandatory, Integer.  
    The position where the element is inserted.

### ListRemove { #ListRemove }

Removes an element from a specific position of a list.

*Inputs*

List
:   Type: mandatory, Generic Record List.  
    The list that the element is removed from.

Position
:   Type: mandatory, Integer.  
    Position of the element to be removed.

### ListSort { #ListSort }

Sorts the elements of the List parameter by the given criteria. Note that ListSort is different from the dynamic sorting in Aggregates. Multiple attributes having different data types (such as Text and Integer) in the criteria may not sort the list correctly.

**Examples**

```
ListSort(UserList, Name)

Sorts UserList (list of User records) by the Name attribute.
```
```
ListSort(TextList, Value, False)

Sorts TextList (a list of text values) by Value in descending order. 
Value is the runtime property that represents the current Text value being sorted.
``` 
```
ListSort(OfficeEmployeesList, Employee.Name + " " + Office.Name)

Sorts OfficeEmployeesList (a list of Employee and Office records) by the employee name and office name. If employees work in multiple offices then this sorted list will have the employee records in the different offices displayed consecutively in ascending order of both their own names and the names of the offices.
```
*Inputs*

List
:   Type: mandatory, Any List.  
    The list that contains the elements to sort by the given criteria.

By
:   Type: mandatory, Any Data Type.  
    The criteria by which to order the elements of the list.

Ascending
:   Type: optional, Boolean.  
    The boolean expression to indicate if the elements are sorted ascending (True) or descending (False) according to the By parameter. The default value is ascending (True).

### Login { #Login }

Logs a specified user in the application.  
In case of success, 'UserId' and 'Username' session variables are filled with the user data.

*Inputs*

UserId
:   Type: mandatory, User Identifier.  
    

Persistent
:   Type: mandatory, Boolean.  
    If true, the login will be persistent for 15 days

### LoginPassword { #LoginPassword }

Logs a specified user in the application using a password.  
In case of success, 'UserId' and 'Username' session variables are filled with the user data.

*Inputs*

UserId
:   Type: mandatory, User Identifier.  
    

Password
:   Type: mandatory, Text.  
    

Persistent
:   Type: mandatory, Boolean.  
    If true, the login will be persistent for 15 days

### LogMessage { #LogMessage }

Registers information that can be presented in Service Center in the module general log.

*Inputs*

Message
:   Type: mandatory, Text.  
    The message to add to the module general log.

ModuleName
:   Type: mandatory, Text.  
    The name of the module to be associated with the log message.

### Logout { #Logout }

Logs out a specific user from the application.  
The 'UserId' and 'Username' session variables are cleared.

### ProcessTerminate { #ProcessTerminate }

Explicitly forces a Process to terminate its execution.

*Inputs*

ProcessId
:   Type: mandatory, Process Identifier.  
    

### SetCurrentLocale { #SetCurrentLocale }

Sets the language locale of the user session to change the application presentation language.

*Inputs*

Locale
:   Type: mandatory, Text.  
    

### TenantCreate { #TenantCreate }

Creates a new tenant and associates it with the provisioning site.

*Inputs*

eSpaceName
:   Type: mandatory, Text.  
    Name of the [User Provider module](../../../develop/security/end-user-manage/end-user-authentication/single-sign-on.md) that will provide the users and sessions to the new tenant. The new tenant will become a User Subscriber to the specified module.

TenantName
:   Type: mandatory, Text.  
    

*Outputs*

TenantId
:   Type: Tenant Identifier.  
    

### TenantInvalidateCache { #TenantInvalidateCache }

Invalidates tenant's specific caches across all Front-end servers and eSpaces. This action is now available for compatibility purposes only. Please use the EspaceInvalidateCache action instead and invalidate tenant's specific caches by eSpace to narrow the invalidation scope

*Inputs*

TenantId
:   Type: mandatory, Tenant Identifier.  
    Identifier of the tenant which will have all of its specific caches invalidated.

### TenantSwitch { #TenantSwitch }

Change the context to the given tenant identifier. When switching tenant, the session is cleared (equivalent to an implicit logout, before changing the tenant), the OnSessionStart actions are executed, and the current transaction is commited.

*Inputs*

TenantId
:   Type: mandatory, Tenant Identifier.  
    


## Client Actions

### ListAll { #Client_ListAll }

Determines if all the elements in the list satisfy the given condition.

*Inputs*

List
:   Type: mandatory, Generic Record List.  
    The list that contains the elements to which to apply the condition.

Condition
:   Type: mandatory, Boolean.  
    The boolean expression to check for on each element of the list.

*Outputs*

Result
:   Type: Boolean.  
    True if every element of the List satisfies the condition; otherwise, False.

### ListAny { #Client_ListAny }

Determines if any of the elements in the list satisfies the given condition.

*Inputs*

List
:   Type: mandatory, Generic Record List.  
    The list that contains the elements to which to apply the condition.

Condition
:   Type: mandatory, Boolean.  
    The boolean expression to check for on each element of the list.

*Outputs*

Result
:   Type: Boolean.  
    True if there is an element of the List satisfying the condition; otherwise, False.

### ListAppend { #Client_ListAppend }

Adds an element to the end of a list.

*Inputs*

List
:   Type: mandatory, Generic Record List.  
    The list to add the element to.

Element
:   Type: mandatory, Generic Record.  
    The element to be added to the end of the list.

### ListAppendAll { #Client_ListAppendAll }

Adds the elements of the source list to the end of the destination list.

*Inputs*

List
:   Type: mandatory, Generic Record List.  
    The list to add the element to.

SourceList
:   Type: mandatory, Generic Record List.  
    The list whose elements will be added.

### ListClear { #Client_ListClear }

Removes all elements from a list.

*Inputs*

List
:   Type: mandatory, Generic Record List.  
    The list to remove the elements from.

### ListDistinct { #Client_ListDistinct }

Filters duplicate elements from a list.

*Inputs*

SourceList
:   Type: mandatory, Generic Record List.  
    The list that includes duplicate elements.

*Outputs*

DistinctList
:   Type: Generic Record List.  
    List that only includes the distinct elements of the source list.

### ListDuplicate { #Client_ListDuplicate }

Duplicates the elements of a list into another list.

*Inputs*

SourceList
:   Type: mandatory, Generic Record List.  
    The list to duplicate.

*Outputs*

DuplicatedList
:   Type: Generic Record List.  
    The duplicate list.

### ListFilter { #Client_ListFilter }

Returns a new list with the elements from the List parameter satisfying the given condition.

*Inputs*

SourceList
:   Type: mandatory, Generic Record List.  
    The list that contains the elements to which to apply the condition.

Condition
:   Type: mandatory, Boolean.  
    The boolean expression to check for on each element of the list.

*Outputs*

FilteredList
:   Type: Generic Record List.  
    A new list with the elements that satisfy the condition.

### ListIndexOf { #Client_ListIndexOf }

Returns the position of the first element of the List parameter that satisfies the given condition, or -1 if no element satisfying the condition was found.

**Examples**
```
ListIndexOf(UserList, Is_Active)

Returns the position of the first user in the list of User records satisfying the condition Is_Active = True.
```
```
ListIndexOf(UserList, Name = "James")

Returns the position of the first user in the list of User records satisfying the condition Name = "James".
```
*Inputs*

List
:   Type: mandatory, Any List.  
    The list that contains the elements to which to apply the condition.

Condition
:   Type: mandatory, Boolean.  
    The boolean expression to check for on each element of the list.

*Outputs*

Position
:   Type: Integer.  
    The position of the first element of the list that satisfies the given condition; -1 if no element satisfying the condition was found.

### ListInsert { #Client_ListInsert }

Inserts an element in a specific position of a list.

*Inputs*

List
:   Type: mandatory, Generic Record List.  
    The list to add the element to.

Element
:   Type: mandatory, Generic Record.  
    The element to insert in the list.

Position
:   Type: mandatory, Integer.  
    The position where the element is inserted.

### ListRemove { #Client_ListRemove }

Removes an element from a specific position of a list.

*Inputs*

List
:   Type: mandatory, Generic Record List.  
    The list that the element is removed from.

Position
:   Type: mandatory, Integer.  
    Position of the element to be removed.

### ListSort { #Client_ListSort }

Sorts the elements of the List parameter by the given criteria. Note that ListSort is different from the dynamic sorting in Aggregates. Multiple attributes having different data types (such as Text and Integer) in the criteria may not sort the list correctly.

**Examples**

```
ListSort(UserList, Name)

Sorts UserList (list of User records) by the Name attribute.
```
```
ListSort(TextList, Value, False)

Sorts TextList (a list of text values) by Value in descending order. 
Value is the runtime property that represents the current Text value being sorted.
``` 
```
ListSort(OfficeEmployeesList, Employee.Name + " " + Office.Name)

Sorts OfficeEmployeesList (a list of Employee and Office records) by the employee name and office name. If employees work in multiple offices then this sorted list will have the employee records in the different offices displayed consecutively in ascending order of both their own names and the names of the offices.
```
*Inputs*

List
:   Type: mandatory, Any List.  
    The list that contains the elements to sort by the given criteria.

By
:   Type: mandatory, Any Data Type.  
    The criteria by which to order the elements of the list.

Ascending
:   Type: optional, Boolean.  
    The boolean expression to indicate if the elements are sorted ascending (True) or descending (False) according to the By parameter. The default value is ascending (True).

### LogMessage { #Client_LogMessage }

Registers information that can be presented in Service Center in the module general log.

*Inputs*

Message
:   Type: mandatory, Text.  
    The message to add to the module general log.

ModuleName
:   Type: mandatory, Text.  
    The name of the module to be associated with the log message.

### RequireScript { #Client_RequireScript }

Add a Javascript to the html header. Multiple calls for the same Javascript will only add it once. Action flow will proceed after the Javascript has been successfully loaded.

*Inputs*

Url
:   Type: mandatory, Text.  
    The Url of the Javascript to add to the header


