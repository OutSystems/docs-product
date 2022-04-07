---
summary: Allows manipulating runtime configurations for the environment.
tags: 
locale: en-us
guid: 66bc7e5d-11fc-4670-a85e-4ac5e0defd1c
---

# PlatformRuntime API


The OutSystems PlatformRuntime API provides actions to:

* switch the database connection in runtime
* retrieve the GUID that uniquely identifies the current request

To use this API, add a dependency to your application on the PlatformRuntime_API module.

## Summary

Action | Description
---|---
[Audit_CreateAuditLog](<#Audit_CreateAuditLog>) | Creates an audit log record in a secure auditing storage. This action waits until the audit log is successfully stored, otherwise an exception is raised.<br/>If the secure auditing storage is unsupported or not configured in the current environment, the creation of the audit log record is skipped.
[Database_WriteInParallelTransaction](<#Database_WriteInParallelTransaction>) | Write a record converted to an object using other transaction besides the main transaction of the request.
[DatabaseConnection_SetConnectionStringForSession](<#DatabaseConnection_SetConnectionStringForSession>) | Switches a Database Connection from one database to another at runtime and in the current Session.<br/>There are some conditions to which you have to pay attention to when using this action:<br/>\- The Connection String must connect to a database with the same type (e.g. Oracle, SQL Server, MySQL) as the one configured in Service Center for the Database Connection.<br/>\- For Traditional Web apps, if you run any Aggregate or SQL using the Database Connection with the previous database before executing this action, the switch to the new database becomes effective only in the next request.<br/>\- For Mobile and Reactive Web apps, you need to execute this action in the beginning of a Data Action, before running any Aggregate or SQL to fetch the records. As the session is not persistent between server requests, this needs to be done for each server request that you need to switch the database connection string.<br/>\- Your license must include the Platform Extensibility APIs feature.
[Request_GetKey](<#Request_GetKey>) | Provides the RequestKey that uniquely identifies the current request.<br/>If there is no RequestKey available in the current context, an empty string is returned.
[Session_GetMobileAppLoginId](<#Session_GetMobileAppLoginId>) | Gets the token that uniquely identifies the authenticated session for a Mobile Application.<br/>This method can be used in when managing server side session stores where you need to uniquely identify a user authenticated session.
[Session_GetMobileAppLoginInfo](<#Session_GetMobileAppLoginInfo>) | Gets User information of the authenticated user for a Mobile Application.<br/>This method is designed for interoperability scenarios where you need to embed a Responsive screen in your mobile application.
[Session_GetWebAppLoginInfo](<#Session_GetWebAppLoginInfo>) | Gets User information of the authenticated user for a Web Application.<br/>This method is designed for interoperability scenarios where you need to access session information in sessionless endpoints like REST methods.

## Actions

### Audit_CreateAuditLog { #Audit_CreateAuditLog }

Creates an audit log record in a secure auditing storage. This action waits until the audit log is successfully stored, otherwise an exception is raised.  
If the secure auditing storage is unsupported or not configured in the current environment, the creation of the audit log record is skipped.

*Inputs*

Operation
:   Type: Text. Mandatory.  
    Name of the operation being logged.

Message
:   Type: Text. Mandatory.  
    Message of the audit log.

Extra
:   Type: Text.  
    String in JSON format including extra information relevant to the audit log.

### Database_WriteInParallelTransaction { #Database_WriteInParallelTransaction }

Write a record converted to an object using other transaction besides the main transaction of the request.

*Inputs*

Record
:   Type: Object. Mandatory.  
    Record to write using the a parallel transaction

### DatabaseConnection_SetConnectionStringForSession { #DatabaseConnection_SetConnectionStringForSession }

Switches a Database Connection from one database to another at runtime and in the current Session.  
There are some conditions to which you have to pay attention to when using this action:  
\- The Connection String must connect to a database with the same type (e.g. Oracle, SQL Server, MySQL) as the one configured in Service Center for the Database Connection.  
\- For Traditional Web apps, if you run any Aggregate or SQL using the Database Connection with the previous database before executing this action, the switch to the new database becomes effective only in the next request.  
\- For Mobile and Reactive Web apps, you need to execute this action in the beginning of a Data Action, before running any Aggregate or SQL to fetch the records. As the session is not persistent between server requests, this needs to be done for each server request that you need to switch the database connection string.  
\- Your license must include the Platform Extensibility APIs feature.


*Inputs*

connectionName
:   Type: Text. Mandatory.  
    Name of the Database Connection, as defined in Service Center.

connectionString
:   Type: Text. Mandatory.  
    The Connection String to be used by the Database Connection to connect to the new database.

databaseIdentifier
:   Type: Text.  
    The initial database to use (effective only for Oracle databases, indicating the schema to be initialy used).

### Request_GetKey { #Request_GetKey }

Provides the RequestKey that uniquely identifies the current request.  
If there is no RequestKey available in the current context, an empty string is returned.

*Outputs*

RequestKey
:   Type: Text.  
    

### Session_GetMobileAppLoginId { #Session_GetMobileAppLoginId }

Gets the token that uniquely identifies the authenticated session for a Mobile Application.  
This method can be used in when managing server side session stores where you need to uniquely identify a user authenticated session.

*Outputs*

loginId
:   Type: Text.  
    Returns the session identifier or NullTextIdentifier() if no user is logged in.

### Session_GetMobileAppLoginInfo { #Session_GetMobileAppLoginInfo }

Gets User information of the authenticated user for a Mobile Application.  
This method is designed for interoperability scenarios where you need to embed a Responsive screen in your mobile application.

*Outputs*

userId
:   Type: Integer.  
    Returns the user identifier, or NullIdentifier() (userId = 0) if user is not logged in.

isPersistent
:   Type: Boolean.  
    True if the login is persistent.


### Session_GetWebAppLoginInfo { #Session_GetWebAppLoginInfo }

Gets User information of the authenticated user for a Web Application.  
This method is designed for interoperability scenarios where you need to access session information in sessionless endpoints like REST methods.

*Outputs*

userId
:   Type: Integer.  
    Returns the user identifier, or NullIdentifier() (userId = 0) if user is not logged in.

