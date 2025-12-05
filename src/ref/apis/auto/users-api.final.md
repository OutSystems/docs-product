---
summary: Explore user and group management functionalities in OutSystems 11 (O11) through its comprehensive Users API.
tags: api documentation, user management, security, group management, dependency management
locale: en-us
guid: ce2ac90a-1911-4fcf-8c8d-016110b3f8e2
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - full stack developers
  - backend developers
  - platform administrators
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Users API

This API provides access to a subset of functionality made available by the Users application, allowing you to manage End Users and Groups.

Users API manages the system entities User and Group but include additional logic to them.

To use this API, use the **Manage Dependencies** window in Service Studio to add a dependency to the API elements you want to use.

## Summary

| Widget | Description |
| ---|--- |
| [ChangePassword](<#ChangePassword>) | Allows changing the user password. |
| [EditMyInfo](<#EditMyInfo>) | |

| Action | Description |
| ---|--- |
| [EncryptPassword](<#EncryptPassword>) | Returns the encrypted password for a specific username and password. This is the value kept in the Password attribute of the User system entity. |
| [GetEffectiveUserProviderEspaceId](<#GetEffectiveUserProviderEspaceId>) | Returns the module/eSpace identifier of the effective user provider. Normally it returns the Users eSpaceId, in upgrade scenarios it returns the EnterpriseManager eSpaceId. |
| [Group_CreateNew](<#Group_CreateNew>) | Create a new system group. Requires the UserManager role to be invoked. |
| [Group_Delete](<#Group_Delete>) | Delete a system group. Requires the UserManager role to be invoked. |
| [Group_Update](<#Group_Update>) | Updates a system group. Requires the UserManager role to be invoked. |
| [IPAddress_GetBlockedStatus](<#IPAddress_GetBlockedStatus>) | Returns the blocking state of the IP address. |
| [IPAddress_GetBlocks](<#IPAddress_GetBlocks>) | Returns the blocking state of the IP address. If there are no blocks for this address, the list will be empty. If no IP address is given, information on all blocked IP addresses will be returned. |
| [IPAddress_Unblock](<#IPAddress_Unblock>) | Ends the blocking period for the specified IP address, allowing any user to login in that address. |
| [UseActiveDirectoryAuthentication](<#UseActiveDirectoryAuthentication>) | Returns the Users configuration that determines if the Active Directory is used for authentication |
| [UseIntegratedAuthentication](<#UseIntegratedAuthentication>) | Returns the Users configuration that determines if the Integrated Authentication is used to login. |
| [UseLDAPAuthentication](<#UseLDAPAuthentication>) | Returns the Users configuration that determines if the Active Directory is used for authentication |
| [User_CanChangePassword](<#User_CanChangePassword>) | Checks if the User is allowed to change a password. It is false for Active Directory users. |
| [User_Create](<#User_Create>) | Create a new user. Requires UserManager role to be invoked.<br/>Fails when the username is repeated. |
| [User_CreateOrUpdate](<#User_CreateOrUpdate>) | Create or updates a user. Requires UserManager role to be invoked. |
| [User_DeleteIfNoRoles](<#User_DeleteIfNoRoles>) | Deletes the User if there are no roles assigned to it. |
| [User_GetBlockedStatus](<#User_GetBlockedStatus>) | Returns information regarding the blocking state of the user and the blocking reason, in the specified IP address. If no IP address is given, checks the last IP address from where the user attempted to login. |
| [User_GetIdByUsername](<#User_GetIdByUsername>) | Returns the user identifier for a specific user given the username |
| [User_GetLastFailedLoginAttempts](<#User_GetLastFailedLoginAttempts>) | Returns a list of last failed login attempts (one record for each IP address). This information can be used to invoke User_Unblock or IPaddress_Unblock. |
| [User_GetName](<#User_GetName>) | Returns the name of the logged user. |
| [User_GetUnifiedLoginUrl](<#User_GetUnifiedLoginUrl>) | Returns the Url used for custom unified login patterns. Includes Windows Integrated Authentication pattern. |
| [User_GetUnifiedLogoutUrl](<#User_GetUnifiedLogoutUrl>) | Returns the Url used for custom unified logout patterns. Includes Windows Integrated Authentication pattern. |
| [User_IsExternalUser](<#User_IsExternalUser>) | Checks if the user was synched from an external system. |
| [User_Login](<#User_Login>) | Action to login using username and password as credentials. |
| [User_Logout](<#User_Logout>) | Logs out the current user. Session variables are cleared during the logout process. |
| [User_Unblock](<#User_Unblock>) | Ends the blocking period for the specified user, allowing the user to login in all IP addresses where the user was blocked. |
| [User_Update](<#User_Update>) | Updates a specific user. |

| Structure | Description |
| ---|--- |
| [LoginAttemptPublic](<#Structure_LoginAttemptPublic>) | Represents the Login attempt record structure that is exposed |

| Static Entity | Description |
| ---|--- |
| [LoginAttemptResult](<#StaticEntity_LoginAttemptResult>) | The alternative values that may appear in the LoginAttempt record Result column. |
| [MenuItem](<#StaticEntity_MenuItem>) | Menu item to be used in menu web block parameters. |

| Role | Description |
| ---|--- |
| UserManager | |

## Widgets

### ChangePassword {#ChangePassword}

Allows changing the user password.

_Inputs_

UserId
:   Type: optional, User Identifier.  

### EditMyInfo {#EditMyInfo}

## Actions

### EncryptPassword {#EncryptPassword}

Returns the encrypted password for a specific username and password. This is the value kept in the Password attribute of the User system entity.

_Inputs_

Username
:   Type: mandatory, Text.  

Password
:   Type: mandatory, Text.  

_Outputs_

EncryptedPassword
:   Type: Text.  

### GetEffectiveUserProviderEspaceId {#GetEffectiveUserProviderEspaceId}

Returns the module/eSpace identifier of the effective user provider. Normally it returns the Users eSpaceId, in upgrade scenarios it returns the EnterpriseManager eSpaceId.  

_Outputs_

EspaceId
:   Type: Espace Identifier.  

### Group_CreateNew {#Group_CreateNew}

Create a new system group. Requires the UserManager role to be invoked.

_Inputs_

Group
:   Type: mandatory, Group.  

_Outputs_

GroupId
:   Type: Group Identifier.  

### Group_Delete {#Group_Delete}

Delete a system group. Requires the UserManager role to be invoked.

_Inputs_

GroupId
:   Type: mandatory, Group Identifier.  

### Group_Update {#Group_Update}

Updates a system group. Requires the UserManager role to be invoked.

_Inputs_

Group
:   Type: mandatory, Group.  

### IPAddress_GetBlockedStatus {#IPAddress_GetBlockedStatus}

Returns the blocking state of the IP address.

_Inputs_

IPAddress
:   Type: mandatory, Text.  
    IP address for which the blocking state should be evaluated.

_Outputs_

LoginAttemptResult
:   Type: [LoginAttemptResult](<#Structure_LoginAttemptResult>).  
    Blocking state for the given IP address.

### IPAddress_GetBlocks {#IPAddress_GetBlocks}

Returns the blocking state of the IP address. If there are no blocks for this address, the list will be empty. If no IP address is given, information on all blocked IP addresses will be returned.

_Inputs_

IPAddress
:   Type: optional, Text.  
    IP Address for which the current block information should be given.

_Outputs_

BlockedAddresses
:   Type: [LoginAttemptPublic](<#Structure_LoginAttemptPublic>) List.  
    Blocked login attempts associated to the given IP address, or all IP addresses, if no input is given.

### IPAddress_Unblock {#IPAddress_Unblock}

Ends the blocking period for the specified IP address, allowing any user to login in that address.

_Inputs_

IPAddress
:   Type: mandatory, Text.  
    The IP address to be unblocked.

### UseActiveDirectoryAuthentication {#UseActiveDirectoryAuthentication}

Returns the Users configuration that determines if the Active Directory is used for authentication

_Outputs_

IsActive
:   Type: Boolean.  

### UseIntegratedAuthentication {#UseIntegratedAuthentication}

Returns the Users configuration that determines if the Integrated Authentication is used to login.

_Outputs_

IsActive
:   Type: Boolean.  

### UseLDAPAuthentication {#UseLDAPAuthentication}

Returns the Users configuration that determines if the Active Directory is used for authentication

_Outputs_

IsActive
:   Type: Boolean.  

### User_CanChangePassword {#User_CanChangePassword}

Checks if the User is allowed to change a password. It is false for Active Directory users.

_Inputs_

UserId
:   Type: mandatory, User Identifier.  

_Outputs_

IsAllowed
:   Type: Boolean.  

### User_Create {#User_Create}

Create a new user. Requires UserManager role to be invoked.  
Fails when the username is repeated.

_Inputs_

User
:   Type: mandatory, User.  

_Outputs_

UserId
:   Type: User Identifier.  

### User_CreateOrUpdate {#User_CreateOrUpdate}

Create or updates a user. Requires UserManager role to be invoked.

_Inputs_

User
:   Type: mandatory, User.  

_Outputs_

UserId
:   Type: User Identifier.  

### User_DeleteIfNoRoles {#User_DeleteIfNoRoles}

Deletes the User if there are no roles assigned to it.

_Inputs_

UserId
:   Type: mandatory, User Identifier.  

### User_GetBlockedStatus {#User_GetBlockedStatus}

Returns information regarding the blocking state of the user and the blocking reason, in the specified IP address. If no IP address is given, checks the last IP address from where the user attempted to login.

_Inputs_

Username
:   Type: mandatory, Text.  
    The username of the user whose information regarding the blocked/unblocked state will be retrieved.

IPAddress
:   Type: optional, Text.  
    The IP address for which the information regarding the blocked/unblocked user state will be retrieved.

_Outputs_

LoginAttemptResult
:   Type: [LoginAttemptResult](<#Structure_LoginAttemptResult>).  
    Blocking state and reason for the given username.

### User_GetIdByUsername {#User_GetIdByUsername}

Returns the user identifier for a specific user given the username

_Inputs_

Username
:   Type: mandatory, Text.  

_Outputs_

UserId
:   Type: User Identifier.  

### User_GetLastFailedLoginAttempts {#User_GetLastFailedLoginAttempts}

Returns a list of last failed login attempts (one record for each IP address). This information can be used to invoke User_Unblock or IPaddress_Unblock.

_Inputs_

Username
:   Type: mandatory, Text.  
    The username of the user whose failed login attempts are retrieved.

Since
:   Type: optional, Date Time.  
    Only the login attempts after this datetime are retrieved.

_Outputs_

LoginAttempt
:   Type: [LoginAttemptPublic](<#Structure_LoginAttemptPublic>) List.  
    List of last failed login attempts for the given username.

### User_GetName {#User_GetName}

Returns the name of the logged user.

_Outputs_

Name
:   Type: Text.  

### User_GetUnifiedLoginUrl {#User_GetUnifiedLoginUrl}

Returns the Url used for custom unified login patterns. Includes Windows Integrated Authentication pattern.

_Inputs_

OriginalUrl
:   Type: mandatory, Text.  

_Outputs_

Url
:   Type: Text.  

### User_GetUnifiedLogoutUrl {#User_GetUnifiedLogoutUrl}

Returns the Url used for custom unified logout patterns. Includes Windows Integrated Authentication pattern.

_Inputs_

OriginalUrl
:   Type: optional, Text.  

_Outputs_

Url
:   Type: Text.  

### User_IsExternalUser {#User_IsExternalUser}

Checks if the user was synched from an external system.

_Inputs_

UserId
:   Type: mandatory, User Identifier.  

_Outputs_

IsExternal
:   Type: Boolean.  

### User_Login {#User_Login}

Action to login using username and password as credentials.

_Inputs_

Username
:   Type: mandatory, Text.  
    User's username.

Password
:   Type: mandatory, Text.  
    User's password (should not be encrypted).

RememberLogin
:   Type: mandatory, Boolean.  
    If true, the login will be persistent for 10 days.

### User_Logout {#User_Logout}

Logs out the current user. Session variables are cleared during the logout process.

### User_Unblock {#User_Unblock}

Ends the blocking period for the specified user, allowing the user to login in all IP addresses where the user was blocked.

_Inputs_

Username
:   Type: mandatory, Text.  
    The username of the user that is being unblocked and that will be allowed to login again from the specified IP address.

IPAddress
:   Type: optional, Text.  
    The IP address that is being unblocked and from where the specified user will be allowed to login again.

### User_Update {#User_Update}

Updates a specific user.

_Inputs_

User
:   Type: mandatory, User.  

## Structures

### LoginAttemptPublic {#Structure_LoginAttemptPublic}

Represents the Login attempt record structure that is exposed

_Attributes_

Instant
:   Type: Date Time.  

Success
:   Type: Boolean.  

IPAddress
:   Type: Text (45).  

UsernameFailureCount
:   Type: Integer.  

IPAddressFailureCount
:   Type: Integer.  

RequestKey
:   Type: Text (36).  

UserAgent
:   Type: Text (200).  

Visitor
:   Type: Text (36).  

Result
:   Type: Text.  

## Static Entities

### LoginAttemptResult {#StaticEntity_LoginAttemptResult}

The alternative values that may appear in the LoginAttempt record Result column.

_Attributes_

Id
:   Type: Text (50).  

_Records_

* InvalidLDAPAuthentication
* BlockedIP
* Unblocked
* LoggedIn
* BlockedUser
* InvalidADAuthentication
* InvalidUser
* InvalidPassword

### MenuItem {#StaticEntity_MenuItem}

Menu item to be used in menu web block parameters.

_Attributes_

Id
:   Type: Integer.  

Order
:   Type: Integer.  

Caption
:   Type: Text (50).  

_Records_

* Applications
* Users
* Groups
