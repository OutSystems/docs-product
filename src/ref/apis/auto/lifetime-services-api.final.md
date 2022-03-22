---
summary: A set of SOAP Web Services that allow you to manage the infrastructure made available by OutSystems.
tags: support-application_development; support-Integrations_Extensions
---

# LifeTime Services API


This API, composed of a set of SOAP Web Services, provides functionality to manage the infrastructure made available by OutSystems.

## Summary

Web Service | Description
---|---
[RoleManagementService](<#RoleManagementService>) | The Platform API to manage IT roles: roles created in the platform. The authenticated user needs to have 'Manage Infrastructure' permissions in the platform to use this API.%%To use this API you need to send an authentication argument with username/password, or use the AuthenticationService Web Service API to acquire a session token to send as argument.
[AuthenticationService](<#AuthenticationService>) | The Platform API to acquire an authentication token to be used when invoking other OutSystems APIs. After 5 minutes, the token expires.
[TeamManagementService](<#TeamManagementService>) | The Platform API to manage teams in the platform.%%To use this API you need to send an authentication argument with username/password, or use the AuthenticationService Web Service API to acquire a session token to send as argument.
[SecurityManagementService](<#SecurityManagementService>) | The Platform API for getting security information about users and addresses who login to the platform.%%To use this API you need to send an authentication argument with username/password, or use the AuthenticationService Web Service API to acquire a session token to send as argument.
[DbConnectionManagementService](<#DbConnectionManagementService>) | This API provides methods to create, change, and delete connections to external databases. It also allows managing users permissions.
[UserManagementService](<#UserManagementService>) | The Platform API to manage IT users: users created in the platform. The authenticated user needs to have 'Manage Infrastructure' permissions in the platform to use this API.%%To use this API you need to send an authentication argument with username/password, or use the AuthenticationService Web Service API to acquire a session token to send as argument.

## RoleManagementService

The Platform API to manage IT roles: roles created in the platform. The authenticated user needs to have 'Manage Infrastructure' permissions in the platform to use this API.  
To use this API you need to send an authentication argument with username/password, or use the AuthenticationService Web Service API to acquire a session token to send as argument.

This API is exposed as a Web Service, made available at:  
`http://<InfrastructureManagementEnvironment>/LifeTimeServices/RoleManagementService.asmx?WSDL`

Action | Description
---|---
[Role_ChangeName](<#Role_ChangeName>) | Updates the name of a platform role.
[Role_CreateOrUpdate](<#Role_CreateOrUpdate>) | Creates a new platform role or updates a platform role that already exists.
[Role_Delete](<#Role_Delete>) | Deletes a platform role that already exists. Since the platform requires IT users to have a single platform role, you need to specify a new platform role to grant to the users that are currently set with the role you want to delete.%%
[Role_GetEnvironmentPermissionsLevels](<#Role_GetEnvironmentPermissionsLevels>) | Lists the permission levels that a platform user has over the environments.
[Role_GetPermissions](<#Role_GetPermissions>) | Returns the list of permissions a platform role has in the environments registered in the platform.
[Role_List](<#Role_List>) | Returns all platform roles with their information.
[Role_UpdatePermission](<#Role_UpdatePermission>) | Updates the permissions a platform role has in a specified environment.

### Actions

#### Role_ChangeName { #Role_ChangeName }

Updates the name of a platform role.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the AuthenticationService API to acquire a session token.

OldRoleName
:   Type: mandatory, Text.  
    The name of a platform role that is going to be renamed.

NewRoleName
:   Type: mandatory, Text.  
    The new name of the platform role.

*Outputs*

Success
:   Type: Boolean.  
    True if the method was successful, False otherwise.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.

#### Role_CreateOrUpdate { #Role_CreateOrUpdate }

Creates a new platform role or updates a platform role that already exists.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the AuthenticationService API to acquire a session token.

RoleName
:   Type: mandatory, Text.  
    The name of a platform role. If this role does not exist in the platform it is created, otherwise it is updated.  
    

CanConfigureInfrastructure
:   Type: mandatory, Boolean.  
    Specifies whether the platform role has permissions to configure the infrastructure.

RoleDescription
:   Type: mandatory, Text.  
    The description for the platform role.

*Outputs*

Success
:   Type: Boolean.  
    True if the method was successful, False otherwise.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.

PlatformRole
:   Type: [PlatformRole](<#Structure_PlatformRole>).  
    A platform role with its information.

#### Role_Delete { #Role_Delete }

Deletes a platform role that already exists. Since the platform requires IT users to have a single platform role, you need to specify a new platform role to grant to the users that are currently set with the role you want to delete.  


*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the AuthenticationService API to acquire a session token.

RoleName
:   Type: mandatory, Text.  
    The name of a platform role.

UsersNewRoleName
:   Type: mandatory, Text.  
    A platform role to grant to the users that had the platform role that is going to be deleted.

*Outputs*

Success
:   Type: Boolean.  
    True if the method was successful, False otherwise.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.

AffectedPlatformUsers
:   Type: [PlatformUser](<#Structure_PlatformUser>) List.  
    The list of IT users that had the deleted platform role assigned to them.

#### Role_GetEnvironmentPermissionsLevels { #Role_GetEnvironmentPermissionsLevels }

Lists the permission levels that a platform user has over the environments.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the LoginService API to acquire a session token.

*Outputs*

Success
:   Type: Boolean.  
    True if the method was successful, False otherwise.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.

RolePermissionLevels
:   Type: EnvironmentPermissionLevel List.  
    The permissions an IT user has over an environment, as configured in the platform.

#### Role_GetPermissions { #Role_GetPermissions }

Returns the list of permissions a platform role has in the environments registered in the platform.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the AuthenticationService API to acquire a session token.

RoleName
:   Type: mandatory, Text.  
    The name of a platform role.

*Outputs*

Success
:   Type: Boolean.  
    True if the method was successful, False otherwise.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.

PlatformRolePermissions
:   Type: [EnvironmentPermissionForRole](<#Structure_EnvironmentPermissionForRole>) List.  
    The list of permissions a platform role has over the environments registered in the platform.

#### Role_List { #Role_List }

Returns all platform roles with their information.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the AuthenticationService API to acquire a session token.

*Outputs*

Success
:   Type: Boolean.  
    True if the method was successful, False otherwise.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.  
    

PlatformRoles
:   Type: [PlatformRole](<#Structure_PlatformRole>) List.  
    The list of platform roles.

#### Role_UpdatePermission { #Role_UpdatePermission }

Updates the permissions a platform role has in a specified environment.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the AuthenticationService API to acquire a session token.

RoleName
:   Type: mandatory, Text.  
    The name of a platform role.

EnvironmentKey
:   Type: mandatory, Text.  
    The environment unique identifier.

NewPermissionLevelId
:   Type: mandatory, EnvironmentPermissionLevel Identifier.  
    A reference to the new permission level the platform role will have.

*Outputs*

Success
:   Type: Boolean.  
    True if the method was successful, False otherwise.

Status
:   Type: APIStatus.  
    The status of invoking this API action. In case of error, contains the error code and human-readable error messages.


## AuthenticationService

The Platform API to acquire an authentication token to be used when invoking other OutSystems APIs. After 5 minutes, the token expires.

This API is exposed as a Web Service, made available at:  
`http://<InfrastructureManagementEnvironment>/LifeTimeServices/AuthenticationService.asmx?WSDL`

Action | Description
---|---
[Authentication_GetToken](<#Authentication_GetToken>) | Returns an authentication token that is valid for 5 minutes.

### Actions

#### Authentication_GetToken { #Authentication_GetToken }

Returns an authentication token that is valid for 5 minutes.

*Inputs*

Username
:   Type: mandatory, Text.  
    A platform username.

Password
:   Type: mandatory, Text.  
    A platform password.

*Outputs*

Success
:   Type: Boolean.  
    True if the method was successful, False otherwise.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.  
    

Token
:   Type: Text.  
    A session token. This token expires 5 minutes after it has been created.


## TeamManagementService

The Platform API to manage teams in the platform.  
To use this API you need to send an authentication argument with username/password, or use the AuthenticationService Web Service API to acquire a session token to send as argument.

This API is exposed as a Web Service, made available at:  
`http://<InfrastructureManagementEnvironment>/LifeTimeServices/TeamManagementService.asmx?WSDL`

Action | Description
---|---
[Team_AddUser](<#Team_AddUser>) | Adds a user to a team with a specified role.
[Team_AssignApplication](<#Team_AssignApplication>) | Assigns an application to a team, replacing a previous assignment, if any. An application can only be assigned to a team a time.
[Team_CreateOrUpdate](<#Team_CreateOrUpdate>) | Creates a new team or updates an already existent team.
[Team_Delete](<#Team_Delete>) | Deletes a team.
[Team_GetDetails](<#Team_GetDetails>) | Returns the details of a team, with its users and applications.
[Team_List](<#Team_List>) | Returns a list of the teams.
[Team_RemoveApplication](<#Team_RemoveApplication>) | Removes an application from a team.
[Team_RemoveUser](<#Team_RemoveUser>) | Removes a user from a team.

### Actions

#### Team_AddUser { #Team_AddUser }

Adds a user to a team with a specified role.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid username and password, or use the AuthenticationService API to acquire a session token.

TeamName
:   Type: mandatory, Text.  
    The name of the team.

Username
:   Type: mandatory, Text.  
    The username of the user.

RoleName
:   Type: mandatory, Text.  
    The name of the role to assign to the user.

*Outputs*

Success
:   Type: Boolean.  
    True if the method was successful, False otherwise.

Status
:   Type: APIStatus.  
    The status of invoking this API action. In case of error, contains the error code and human-readable error messages.

#### Team_AssignApplication { #Team_AssignApplication }

Assigns an application to a team, replacing a previous assignment, if any. An application can only be assigned to a team a time.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid username and password, or use the AuthenticationService API to acquire a session token.

TeamName
:   Type: mandatory, Text.  
    The name of the team.

ApplicationKey
:   Type: mandatory, Text.  
    The application unique identifier.

*Outputs*

Success
:   Type: Boolean.  
    True if the method was successful, False otherwise.

Status
:   Type: APIStatus.  
    The status of invoking this API action. In case of error, contains the error code and human-readable error messages.

#### Team_CreateOrUpdate { #Team_CreateOrUpdate }

Creates a new team or updates an already existent team.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid username and password, or use the AuthenticationService API to acquire a session token.

TeamName
:   Type: mandatory, Text.  
    The name of the team.

Description
:   Type: mandatory, Text.  
    The description of the team.

*Outputs*

Success
:   Type: Boolean.  
    True if the method was successful, False otherwise.

Status
:   Type: APIStatus.  
    The status of invoking this API action. In case of error, contains the error code and human-readable error messages.

PlatformTeam
:   Type: [PlatformTeam](<#Structure_PlatformTeam>).  
    The team created or updated.

#### Team_Delete { #Team_Delete }

Deletes a team.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid username and password, or use the AuthenticationService API to acquire a session token.

TeamName
:   Type: mandatory, Text.  
    The name of the team.

*Outputs*

Success
:   Type: Boolean.  
    True if the method was successful, False otherwise.

Status
:   Type: APIStatus.  
    The status of invoking this API action. In case of error, contains the error code and human-readable error messages.

#### Team_GetDetails { #Team_GetDetails }

Returns the details of a team, with its users and applications.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid username and password, or use the AuthenticationService API to acquire a session token.

TeamName
:   Type: mandatory, Text.  
    The name of the team.

*Outputs*

Success
:   Type: Boolean.  
    True if the method was successful, False otherwise.

Status
:   Type: APIStatus.  
    The status of invoking this API action. In case of error, contains the error code and human-readable error messages.

PlatformTeam
:   Type: [PlatformTeam](<#Structure_PlatformTeam>).  
    The team details.

#### Team_List { #Team_List }

Returns a list of the teams.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid username and password, or use the AuthenticationService API to acquire a session token.

*Outputs*

Success
:   Type: Boolean.  
    True if the method was successful, False otherwise.

Status
:   Type: APIStatus.  
    The status of invoking this API action. In case of error, contains the error code and human-readable error messages.

PlatformTeams
:   Type: [PlatformTeam](<#Structure_PlatformTeam>) List.  
    The list with the teams. The returned ApplicationList and UserList attributes of each team will be empty; call the Team_GetDetails action to obtain the application and user list of a team.

#### Team_RemoveApplication { #Team_RemoveApplication }

Removes an application from a team.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid username and password, or use the AuthenticationService API to acquire a session token.

TeamName
:   Type: mandatory, Text.  
    The name of the team.

ApplicationKey
:   Type: mandatory, Text.  
    The application unique identifier.

*Outputs*

Success
:   Type: Boolean.  
    True if the method was successful, False otherwise.

Status
:   Type: APIStatus.  
    The status of invoking this API action. In case of error, contains the error code and human-readable error messages.

#### Team_RemoveUser { #Team_RemoveUser }

Removes a user from a team.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid username and password, or use the AuthenticationService API to acquire a session token.

TeamName
:   Type: mandatory, Text.  
    The name of the team.

Username
:   Type: mandatory, Text.  
    The username of the user.

*Outputs*

Success
:   Type: Boolean.  
    True if the method was successful, False otherwise.

Status
:   Type: APIStatus.  
    The status of invoking this API action. In case of error, contains the error code and human-readable error messages.


## SecurityManagementService

The Platform API for getting security information about users and addresses who login to the platform.  
To use this API you need to send an authentication argument with username/password, or use the AuthenticationService Web Service API to acquire a session token to send as argument.

This API is exposed as a Web Service, made available at:  
`http://<InfrastructureManagementEnvironment>/LifeTimeServices/SecurityManagementService.asmx?WSDL`

Action | Description
---|---
[IPAddress_GetLockedStatus](<#IPAddress_GetLockedStatus>) | 
[IPAddress_Unlock](<#IPAddress_Unlock>) | 
[User_GetLockedStatus](<#User_GetLockedStatus>) | 
[User_Unlock](<#User_Unlock>) | 

### Actions

#### IPAddress_GetLockedStatus { #IPAddress_GetLockedStatus }



*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the AuthenticationService API to acquire a session token.

IPAddress
:   Type: optional, Text.  
    IP Address to which the lock information, should it exist, belongs to. If this parameter is empty, information on all IP locked addresses is returned.

EnvironmentKey
:   Type: optional, Text.  
    The environment unique identifier in which the lock information should be searched. If the parameter is empty, it returns the pertaining information regarding all active environments.

*Outputs*

Success
:   Type: Boolean.  
    True if the method was successful, False otherwise.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.

PlatformLoginAttempts
:   Type: [PlatformLoginAttempt](<#Structure_PlatformLoginAttempt>) List.  
    List of login attempts with respect to the given IP address (or all IP addresses) in the given environment (or all active environments).

#### IPAddress_Unlock { #IPAddress_Unlock }



*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the AuthenticationService API to acquire a session token.

IPAddress
:   Type: mandatory, Text.  
    IP Address to be unlocked in the given environment.

EnvironmentKey
:   Type: optional, Text.  
    The environment unique identifier in which the IP address should be unlocked.

*Outputs*

Success
:   Type: Boolean.  
    True if the method was successful, False otherwise.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.

#### User_GetLockedStatus { #User_GetLockedStatus }



*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the AuthenticationService API to acquire a session token.

Username
:   Type: mandatory, Text.  
    Username to which the lock information, should it exist, belongs to.

EnvironmentKey
:   Type: optional, Text.  
    The environment unique identifier in which the lock information should be searched. If the parameter is empty, it returns the pertaining information regarding all active environments.

*Outputs*

Success
:   Type: Boolean.  
    True if the method was successful, False otherwise.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.

PlatformLoginAttempts
:   Type: [PlatformLoginAttempt](<#Structure_PlatformLoginAttempt>) List.  
    List of login attempts with respect to the given Username in the given environment (or all active environments).

#### User_Unlock { #User_Unlock }



*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the AuthenticationService API to acquire a session token.

Username
:   Type: mandatory, Text.  
    Username to be unlocked in the given environment (or all environments).

IPAddress
:   Type: optional, Text.  
    IP address from which the specified Username is to be unlocked.

EnvironmentKey
:   Type: optional, Text.  
    The environment unique identifier in which the Username should be unlocked.

*Outputs*

Success
:   Type: Boolean.  
    True if the method was successful, False otherwise.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.


## DbConnectionManagementService

This API provides methods to create, change, and delete connections to external databases. It also allows managing users permissions.

This API is exposed as a Web Service, made available at:  
`http://<InfrastructureManagementEnvironment>/LifeTimeServices/DbConnectionManagementService.asmx?WSDL`

Action | Description
---|---
[DbConnection_Create](<#DbConnection_Create>) | Creates a new database connection.
[DbConnection_Delete](<#DbConnection_Delete>) | Deletes the database connection given by the name.
[DbConnection_Edit](<#DbConnection_Edit>) | Updates the configuration of the database connection.
[DbConnection_Get](<#DbConnection_Get>) | Returns the database connection.
[DbConnection_GetRoleAccess](<#DbConnection_GetRoleAccess>) | Returns the role permissions to use a database connection.
[DbConnection_GetUserAccess](<#DbConnection_GetUserAccess>) | Returns the user permissions to use a database connection.
[DbConnection_GrantRoleAccess](<#DbConnection_GrantRoleAccess>) | Grants a role with a permission level to use the database connection.
[DbConnection_GrantUserAccess](<#DbConnection_GrantUserAccess>) | Grants a user with a permission level to use the database connection.
[DbConnection_ListAll](<#DbConnection_ListAll>) | Returns a list with all database connections.
[DbConnection_ListProviders](<#DbConnection_ListProviders>) | The list of database providers that a user can associate to a database connection.
[DbConnection_PermissionLevel_List](<#DbConnection_PermissionLevel_List>) | Returns the list of permission levels.
[DbConnection_Rename](<#DbConnection_Rename>) | Renames an database connection. This may have impact on all running application that use this database connection.
[DbConnection_RevokeRoleAccess](<#DbConnection_RevokeRoleAccess>) | Revokes the role permissions to use the database connection.
[DbConnection_RevokeUserAccess](<#DbConnection_RevokeUserAccess>) | Revokes the user permissions to use the database connection.
[DbConnection_TestConnection](<#DbConnection_TestConnection>) | Tests a database connection with the given parameters.

### Actions

#### DbConnection_Create { #DbConnection_Create }

Creates a new database connection.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid Platform username and password, or use the LoginService API to acquire a session token.

EnvironmentKey
:   Type: mandatory, Text.  
    The environment unique identifier.

Name
:   Type: mandatory, Text.  
    The name of the new database connection.

ProviderKey
:   Type: mandatory, Text.  
    The key of the database provider associated with the new database connection. See method DBConnection_ListProviders.

Description
:   Type: mandatory, Text.  
    The description of the new database connection.

DBUsername
:   Type: mandatory, Text.  
    The username to log in to the external database.

DBPassword
:   Type: mandatory, Text.  
    The password to log in to the external database.

DBConfigParams
:   Type: mandatory, Text.  
    Parameters for the connection string. Separate them using ';'.

TestConnection
:   Type: mandatory, Boolean.  
    If True, the database connection is only created after being tested with success.

*Outputs*

DbConnection
:   Type: .  
    The database connection that was created.

Success
:   Type: Boolean.  
    True if the database connection was created.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.

#### DbConnection_Delete { #DbConnection_Delete }

Deletes the database connection given by the name.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the LoginService API to acquire a session token.

EnvironmentKey
:   Type: mandatory, Text.  
    An environment unique identifier.

DbConnectionName
:   Type: mandatory, Text.  
    The name of the database connection .

*Outputs*

Success
:   Type: Boolean.  
    True if the database connection was deleted.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.

#### DbConnection_Edit { #DbConnection_Edit }

Updates the configuration of the database connection.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the LoginService API to acquire a session token.

EnvironmentKey
:   Type: mandatory, Text.  
    An environment unique identifier.

DbConnectionName
:   Type: mandatory, Text.  
    The name of the database connection.

ProviderKey
:   Type: mandatory, Text.  
    The key of the database provider associated with the new database connection. See method DBConnection_ListProviders.

Description
:   Type: mandatory, Text.  
    The database connection description.

DBUsername
:   Type: mandatory, Text.  
    The username to log in to the external database.

DBPassword
:   Type: mandatory, Text.  
    The password to log in to the external database.

DBConfigParams
:   Type: mandatory, Text.  
    Parameters for the connection string. Separate them using ';'.

TestConnection
:   Type: mandatory, Boolean.  
    If True, the database connection is only updated after being tested with sucess.

*Outputs*

Success
:   Type: Boolean.  
    True if the database connection was changed.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.

#### DbConnection_Get { #DbConnection_Get }

Returns the database connection.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the LoginService API to acquire a session token.

EnvironmentKey
:   Type: mandatory, Text.  
    An environment unique identifier.

DbConnectionName
:   Type: mandatory, Text.  
    The name of the database connection.

*Outputs*

DbConnection
:   Type: .  
    The database connection.

Success
:   Type: Boolean.  
    True if the database connection was got.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.

#### DbConnection_GetRoleAccess { #DbConnection_GetRoleAccess }

Returns the role permissions to use a database connection.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the LoginService API to acquire a session token.

EnvironmentKey
:   Type: mandatory, Text.  
    An environment unique identifier.

DbConnectionName
:   Type: mandatory, Text.  
    The name of the database connection.

RoleName
:   Type: mandatory, Text.  
    The name of the role.

*Outputs*

PermissionLevel
:   Type: .  
    The role's permission level.

Success
:   Type: Boolean.  
    True if the permissions were got.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.

#### DbConnection_GetUserAccess { #DbConnection_GetUserAccess }

Returns the user permissions to use a database connection.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the LoginService API to acquire a session token.

EnvironmentKey
:   Type: mandatory, Text.  
    An environment unique identifier.

DbConnectionName
:   Type: mandatory, Text.  
    The name of the database connection.

Username
:   Type: mandatory, Text.  
    The username of the user.

*Outputs*

PermissionLevel
:   Type: .  
    The user's permission level.

Success
:   Type: Boolean.  
    True if the permissions were got.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.

#### DbConnection_GrantRoleAccess { #DbConnection_GrantRoleAccess }

Grants a role with a permission level to use the database connection.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the LoginService API to acquire a session token.

EnvironmentKey
:   Type: mandatory, Text.  
    An environment unique identifier.

DbConnectionName
:   Type: mandatory, Text.  
    The name of the database connection.

RoleName
:   Type: mandatory, Text.  
    The name of the role of users to grant permissions.

PermissionLevelId
:   Type: mandatory, DbConnectionPermissionLevel Identifier.  
    The permission level to be granted. See method DbConnection_PermissionLevel_List.

*Outputs*

Success
:   Type: Boolean.  
    True if the permissions were granted.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.

#### DbConnection_GrantUserAccess { #DbConnection_GrantUserAccess }

Grants a user with a permission level to use the database connection.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the LoginService API to acquire a session token.

EnvironmentKey
:   Type: mandatory, Text.  
    An environment unique identifier.

DbConnectionName
:   Type: mandatory, Text.  
    The name of the database connection.

Username
:   Type: mandatory, Text.  
    The username of the user to grant permissions.

PermissionLevelId
:   Type: mandatory, DbConnectionPermissionLevel Identifier.  
    The permission level to be granted. See method DbConnection_PermissionLevel_List.

*Outputs*

Success
:   Type: Boolean.  
    True if the permissions were granted.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.

#### DbConnection_ListAll { #DbConnection_ListAll }

Returns a list with all database connections.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the LoginService API to acquire a session token.

EnvironmentKey
:   Type: mandatory, Text.  
    An environment unique identifier.

*Outputs*

DbConnections
:   Type: DatabaseConnection List.  
    The list of all database connections.

Success
:   Type: Boolean.  
    True if the list of database connections is filled.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.

#### DbConnection_ListProviders { #DbConnection_ListProviders }

The list of database providers that a user can associate to a database connection.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid Platform username and password, or use the LoginService API to acquire a session token.

*Outputs*

Providers
:   Type: DbProvider List.  
    The list of allowed database providers.

Success
:   Type: Boolean.  
    True if the authentication succeeds and a list of providers is returned.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error message.

#### DbConnection_PermissionLevel_List { #DbConnection_PermissionLevel_List }

Returns the list of permission levels.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the LoginService API to acquire a session token.

*Outputs*

Success
:   Type: Boolean.  
    True if the authentication succeeds and a list of permission levels is returned.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.

DbConnectionPermissionLevels
:   Type: DbConnectionPermissionLevel List.  
    The list of permission levels.

#### DbConnection_Rename { #DbConnection_Rename }

Renames an database connection. This may have impact on all running application that use this database connection.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the LoginService API to acquire a session token.

EnvironmentKey
:   Type: mandatory, Text.  
    An environment unique identifier.

CurrentName
:   Type: mandatory, Text.  
    The current name of the database connection.

NewName
:   Type: mandatory, Text.  
    The new name for the database connection.

*Outputs*

Success
:   Type: Boolean.  
    True if the database connection was renamed.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.

#### DbConnection_RevokeRoleAccess { #DbConnection_RevokeRoleAccess }

Revokes the role permissions to use the database connection.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the LoginService API to acquire a session token.

EnvironmentKey
:   Type: mandatory, Text.  
    An environment unique identifier.

DbConnectionName
:   Type: mandatory, Text.  
    The name of the database connection.

RoleName
:   Type: mandatory, Text.  
    The name of the role to revoke permissions.

*Outputs*

Success
:   Type: Boolean.  
    True if the permissions were revoked.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.

#### DbConnection_RevokeUserAccess { #DbConnection_RevokeUserAccess }

Revokes the user permissions to use the database connection.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the LoginService API to acquire a session token.

EnvironmentKey
:   Type: mandatory, Text.  
    An environment unique identifier.

DbConnectionName
:   Type: mandatory, Text.  
    The name of the database connection.

Username
:   Type: mandatory, Text.  
    The username of the user to revoke permissions.

*Outputs*

Success
:   Type: Boolean.  
    True if the permissions were revoked.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.

#### DbConnection_TestConnection { #DbConnection_TestConnection }

Tests a database connection with the given parameters.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid Platform username and password, or use the LoginService API to acquire a session token.

EnvironmentKey
:   Type: mandatory, Text.  
    An environment unique identifier.

ProviderKey
:   Type: mandatory, Text.  
    The key of the database provider associated with the new database connection. See method DBConnection_ListProviders.

DBUsername
:   Type: mandatory, Text.  
    The username to log in to the external database.

DBPassword
:   Type: mandatory, Text.  
    The password to log in to the external database.

DBConfigParams
:   Type: mandatory, Text.  
    Parameters for the connection string. Separate them using ';'.

*Outputs*

Success
:   Type: Boolean.  
    True if the connection was successful.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.


## UserManagementService

The Platform API to manage IT users: users created in the platform. The authenticated user needs to have 'Manage Infrastructure' permissions in the platform to use this API.  
To use this API you need to send an authentication argument with username/password, or use the AuthenticationService Web Service API to acquire a session token to send as argument.

This API is exposed as a Web Service, made available at:  
`http://<InfrastructureManagementEnvironment>/LifeTimeServices/UserManagementService.asmx?WSDL`

Action | Description
---|---
[User_ChangePassword](<#User_ChangePassword>) | Changes the password of a platform user.
[User_ChangeUsername](<#User_ChangeUsername>) | Changes the username of a platform user.
[User_CreateOrUpdate](<#User_CreateOrUpdate>) | Creates a new platform user or updates an existing one. The operation activates the user in the platform.
[User_DeleteApplicationPermission](<#User_DeleteApplicationPermission>) | Deletes the permission a platform user has for a specific application. After executing this operation, the user permissions for the application are defined by the platform roles the platform user has.
[User_GetAllPermissions](<#User_GetAllPermissions>) | Returns the permissions a platform user has over each existing application and the permissions of the platform role, in each environment of the infrastructure.
[User_GetApplicationPermissions](<#User_GetApplicationPermissions>) | Returns the permissions a platform user has over an application, in each environment of the infrastructure, or the permissions from the platform role in case of specific permissions for the application were not specified.
[User_List](<#User_List>) | Returns the list of platform users, with their information, such as username, email and platform role.
[User_SetActive](<#User_SetActive>) | Activates a user in the platform, restoring all permissions the platform user has associated.
[User_SetApplicationRole](<#User_SetApplicationRole>) | Updates the role a platform user has for an application with the given key.
[User_SetInactive](<#User_SetInactive>) | Deactivates a user in the platform. The user stops having access to all operations that require authentication.

### Actions

#### User_ChangePassword { #User_ChangePassword }

Changes the password of a platform user.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the AuthenticationService API to acquire a session token.

Username
:   Type: mandatory, Text.  
    The username of a platform user.

NewPassword
:   Type: mandatory, Text.  
    The new password.

EncryptPassword
:   Type: mandatory, Boolean.  
    Specifies if the password of the platform user will be encrypted.

*Outputs*

Success
:   Type: Boolean.  
    True if the method was successful, False otherwise.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.  
    

#### User_ChangeUsername { #User_ChangeUsername }

Changes the username of a platform user.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the AuthenticationService API to acquire a session token.

OldUsername
:   Type: mandatory, Text.  
    The username of a platform user.

NewUsername
:   Type: mandatory, Text.  
    The new username.

*Outputs*

Success
:   Type: Boolean.  
    True if the method was successful, False otherwise.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.

#### User_CreateOrUpdate { #User_CreateOrUpdate }

Creates a new platform user or updates an existing one. The operation activates the user in the platform.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the AuthenticationService API to acquire a session token.

Username
:   Type: mandatory, Text.  
    The username of a platform user.

Password
:   Type: mandatory, Text.  
    The password of a platform user.

EncryptPassword
:   Type: mandatory, Boolean.  
    Specifies if the password of the platform user will be encrypted.

Name
:   Type: mandatory, Text.  
    The name of a platform user.

Email
:   Type: mandatory, Email.  
    The email of a platform user.

RoleName
:   Type: mandatory, Text.  
    The platform role to grant to a platform user.  
    

*Outputs*

Success
:   Type: Boolean.  
    True if the method was successful, False otherwise.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.

PlatformUser
:   Type: [PlatformUser](<#Structure_PlatformUser>).  
    A platform user.

#### User_DeleteApplicationPermission { #User_DeleteApplicationPermission }

Deletes the permission a platform user has for a specific application. After executing this operation, the user permissions for the application are defined by the platform roles the platform user has.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the AuthenticationService API to acquire a session token.

Username
:   Type: mandatory, Text.  
    The username of a platform user.

ApplicationKey
:   Type: mandatory, Text.  
    An application unique identifier.

*Outputs*

Success
:   Type: Boolean.  
    True if the method was successful, False otherwise.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.

#### User_GetAllPermissions { #User_GetAllPermissions }

Returns the permissions a platform user has over each existing application and the permissions of the platform role, in each environment of the infrastructure.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the AuthenticationService API to acquire a session token.

Username
:   Type: mandatory, Text.  
    The username of a platform user.

*Outputs*

Success
:   Type: Boolean.  
    

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.  
    

ApplicationPermissions
:   Type: [ApplicationPermissions](<#Structure_ApplicationPermissions>), [ApplicationShortInfo](<#Structure_ApplicationShortInfo>) List.  
    The list of permissions a platform user has over each application in each environment registered in platform.  
    

PlatformRolePermissions
:   Type: [ApplicationPermissions](<#Structure_ApplicationPermissions>).  
    The list of permissions a platform user has considering the platform role in each environment registered in platform.

#### User_GetApplicationPermissions { #User_GetApplicationPermissions }

Returns the permissions a platform user has over an application, in each environment of the infrastructure, or the permissions from the platform role in case of specific permissions for the application were not specified.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the AuthenticationService API to acquire a session token.

Username
:   Type: mandatory, Text.  
    The username of a platform user.

ApplicationKey
:   Type: mandatory, Text.  
    An application unique identifier.

*Outputs*

Success
:   Type: Boolean.  
    True if the method was successful, False otherwise.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.  
    

ArePlatformRolePermissions
:   Type: Boolean.  
    Specifies whether the permissions are granted from the user's role or if the user has permissions configured for the application.

ApplicationPermissions
:   Type: [ApplicationPermissions](<#Structure_ApplicationPermissions>).  
    The list of permissions a platform user has over the application in each environment registered in platform.

#### User_List { #User_List }

Returns the list of platform users, with their information, such as username, email and platform role.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the AuthenticationService API to acquire a session token.  
    

ShowInactive
:   Type: mandatory, Boolean.  
    If True returns users that are set to inactive. If False, only returns active users.  
    

*Outputs*

Success
:   Type: Boolean.  
    True if the method was successful, False otherwise.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.

PlatformUsers
:   Type: [PlatformUser](<#Structure_PlatformUser>) List.  
    The list of platform users.

#### User_SetActive { #User_SetActive }

Activates a user in the platform, restoring all permissions the platform user has associated.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the AuthenticationService API to acquire a session token.

Username
:   Type: mandatory, Text.  
    The username of a platform user.

*Outputs*

Success
:   Type: Boolean.  
    True if the method was successful, False otherwise.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.  
    

#### User_SetApplicationRole { #User_SetApplicationRole }

Updates the role a platform user has for an application with the given key.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the AuthenticationService API to acquire a session token.

Username
:   Type: mandatory, Text.  
    The username of a platform user.

ApplicationKey
:   Type: mandatory, Text.  
    An application unique identifier.

RoleName
:   Type: mandatory, Text.  
    The role name.

*Outputs*

Success
:   Type: Boolean.  
    True if the method was successful, False otherwise.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.

#### User_SetInactive { #User_SetInactive }

Deactivates a user in the platform. The user stops having access to all operations that require authentication.

*Inputs*

Authentication
:   Type: mandatory, [WebServiceSimpleAuthentication](<#Structure_WebServiceSimpleAuthentication>).  
    The authentication required to use this API. Specify a valid platform username and password, or use the AuthenticationService API to acquire a session token.

Username
:   Type: mandatory, Text.  
    The username of a platform user.

*Outputs*

Success
:   Type: Boolean.  
    True if the method was successful, False otherwise.

Status
:   Type: APIStatus.  
    The status of invoking this API. This status contains an error code and human-readable error messages.


## Structures

### ApplicationPermissions { #Structure_ApplicationPermissions }

Represents a set of permissions of an application with respect each one of the available environments.

*Attributes*

ApplicationPermissions
:   Type: [EnvironmentPermissionForApplication](<#Structure_EnvironmentPermissionForApplication>) List.  
    The permissions list where each permission corresponds to an environment.

### ApplicationShortInfo { #Structure_ApplicationShortInfo }

Few details about an application managed by the platform.

*Attributes*

Name
:   Type: Text (50).  
    Name of the application.

Key
:   Type: Text (50).  
    Application unique identifier.

Description
:   Type: Text (50).  
    Description of the application.

### EnvironmentPermissionForApplication { #Structure_EnvironmentPermissionForApplication }

Permissions an IT user or role has over an application running on a specified environment.

*Attributes*

EnvironmentKey
:   Type: Text (50).  
    Environment unique identifier.

EnvironmentName
:   Type: Text (50).  
    Name of the environment.

EnvironmentHost
:   Type: Text (50).  
    The environment host which is represented by a relative URL path, starting from the hostname.

EnvironmentType
:   Type: Text (50).  
    Type of the environment. [Development | Test | Production]

ApplicationPermissionLevelId
:   Type: ApplicationPermissionLevel Identifier.  
    The Application Permission Level ID with respect to the environment.

### EnvironmentPermissionForRole { #Structure_EnvironmentPermissionForRole }

Permissions an IT role has over an environment.

*Attributes*

EnvironmentKey
:   Type: Text (50).  
    Environment unique identifier.

EnvironmentName
:   Type: Text (50).  
    Name of the environment.

EnvironmentHost
:   Type: Text (50).  
    The environment host which is represented by a relative URL path, starting from the hostname.

EnvironmentType
:   Type: Text (50).  
    Type of the environment. [Development | Test | Production]

EnvironmentPermissionLevelId
:   Type: EnvironmentPermissionLevel Identifier.  
    The Environment Permission Level ID with respect to the environment.

### PlatformLoginAttempt { #Structure_PlatformLoginAttempt }



*Attributes*

Id
:   Type: Long Integer.  
    

UserId
:   Type: Integer.  
    

Username
:   Type: Text (250).  
    

Success
:   Type: Boolean.  
    

Instant
:   Type: Date Time.  
    

IPAddress
:   Type: Text (45).  
    

UsernameFailureCount
:   Type: Integer.  
    

OriginAddressFailureCount
:   Type: Integer.  
    

UserAgent
:   Type: Text (200).  
    

Visitor
:   Type: Text (36).  
    

RequestKey
:   Type: Text (36).  
    

Result
:   Type: Text (50).  
    

EnvironmentId
:   Type: Environment Identifier.  
    

EnvironmentName
:   Type: Text.  
    

### PlatformRole { #Structure_PlatformRole }

Details about a role.

*Attributes*

Id
:   Type: InfrastructureRole Identifier.  
    Role unique identifier.  


Name
:   Type: Text (50).  
    Name of the role.

Description
:   Type: Text (500).  
    Description of the role.

CanManageInfrastructure
:   Type: Boolean.  
    Specifies whether this role has permissions to configure the infrastructure or not.

IsProtected
:   Type: Boolean.  
    True if the role is protected. False otherwise.

AllowChangePermissions
:   Type: Boolean.  
    True if it is possible to change the role permissions. False otherwise.

PermissionsPerEnvironment
:   Type: [EnvironmentPermissionForRole](<#Structure_EnvironmentPermissionForRole>) List.  
    Role permissions information for each environment.

### PlatformTeam { #Structure_PlatformTeam }

The information about a platform team.

*Attributes*

Id
:   Type: Integer.  
    The team unique identifier.

Name
:   Type: Text (50).  
    The name of the team.

Description
:   Type: Text (50).  
    The description of the team.

ApplicationList
:   Type: [ApplicationShortInfo](<#Structure_ApplicationShortInfo>) List.  
    The list of applications associated with the team.

UserList
:   Type: [PlatformUser](<#Structure_PlatformUser>) List.  
    The list of users associated with the team.

### PlatformUser { #Structure_PlatformUser }

The information about a user.

*Attributes*

Id
:   Type: Integer.  
    User unique identifier.

Username
:   Type: Text (50).  
    Username of an IT user.

Name
:   Type: Text (50).  
    Name of an IT user.

Email
:   Type: Email.  
    Email of an IT user.

RoleName
:   Type: Text (50).  
    Role name the IT user has assigned.  

### WebServiceSimpleAuthentication { #Structure_WebServiceSimpleAuthentication }

Represents the fields to authenticate an OutSystems IT user. Specify a username/password combination to authenticate, or use the AuthenticationService Web Service API to acquire a session token.

*Attributes*

Username
:   Type: Text (50).  
    The username of an IT user.

Password
:   Type: Text.  
    The password of the IT user.

Token
:   Type: Text (50).  
    An authentication token.


