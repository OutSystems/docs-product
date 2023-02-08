---
summary: API to manage End Users and Groups.
tags: support-devOps; support-Security
locale: en-us
guid: ce2ac90a-1911-4fcf-8c8d-016110b3f8e2
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Users API


This API provides access to a subset of functionality made available by the Users application, allowing you to manage End Users and Groups.

Users API manages the system entities User and Group but include additional logic to them.

To use this API, use the **Manage Dependencies** window in Service Studio to add a dependency to the API elements you want to use.

## Summary

Widget | Description
---|---
[ChangePassword](<#ChangePassword>) | Allows changing the user password.
[EditMyInfo](<#EditMyInfo>) | 

Action | Description
---|---
[EncryptPassword](<#EncryptPassword>) | Returns the encrypted password for a specific username and password. This is the value kept in the Password attribute of the User system entity.
[GetEffectiveUserProviderEspaceId](<#GetEffectiveUserProviderEspaceId>) | Returns the eSpace identifier of the effective user provider. Normally it returns the Users eSpaceId, in upgrade scenarios it returns the EnterpriseManager eSpaceId.
[Group_CreateNew](<#Group_CreateNew>) | Create a new system group. Requires the UserManager role to be invoked.
[Group_Delete](<#Group_Delete>) | Delete a system group. Requires the UserManager role to be invoked.
[Group_Update](<#Group_Update>) | Updates a system group. Requires the UserManager role to be invoked.
[IPAddress_GetBlockedStatus](<#IPAddress_GetBlockedStatus>) | Returns the blocking state of the IP address.
[IPAddress_GetBlocks](<#IPAddress_GetBlocks>) | Returns the blocking state of the IP address. If there are no blocks for this address, the list will be empty. If no IP address is given, information on all blocked IP addresses will be returned.
[IPAddress_Unblock](<#IPAddress_Unblock>) | Ends the blocking period for the specified IP address, allowing any user to login in that address.
[UseActiveDirectoryAuthentication](<#UseActiveDirectoryAuthentication>) | Returns the Users configuration that determines if the Active Directory is used for authentication
[UseIntegratedAuthentication](<#UseIntegratedAuthentication>) | Returns the Users configuration that determines if the Integrated Authentication is used to login.
[UseLDAPAuthentication](<#UseLDAPAuthentication>) | Returns the Users configuration that determines if the Active Directory is used for authentication
[User_CanChangePassword](<#User_CanChangePassword>) | Checks if the User is allowed to change a password. It is false for Active Directory users.
[User_Create](<#User_Create>) | Create a new user. Requires UserManager role to be invoked.<br/>Fails when the username is repeated.
[User_CreateOrUpdate](<#User_CreateOrUpdate>) | Create or updates a user. Requires UserManager role to be invoked.
[User_DeleteIfNoRoles](<#User_DeleteIfNoRoles>) | Deletes the User if there are no roles assigned to it.
[User_GetBlockedStatus](<#User_GetBlockedStatus>) | Returns information regarding the blocking state of the user and the blocking reason, in the specified IP address. If no IP address is given, checks the last IP address from where the user attempted to login.
[User_GetIdByUsername](<#User_GetIdByUsername>) | Returns the user identifier for a specific user given the username
[User_GetLastFailedLoginAttempts](<#User_GetLastFailedLoginAttempts>) | Returns a list of last failed login attempts (one record for each IP address). This information can be used to invoke User_Unblock or IPaddress_Unblock.
[User_GetName](<#User_GetName>) | Returns the name of the logged user.
[User_GetUnifiedLoginUrl](<#User_GetUnifiedLoginUrl>) | Returns the Url used for custom unified login patterns. Includes Windows Integrated Authentication pattern.
[User_GetUnifiedLogoutUrl](<#User_GetUnifiedLogoutUrl>) | Returns the Url used for custom unified logout patterns. Includes Windows Integrated Authentication pattern.
[User_IsExternalUser](<#User_IsExternalUser>) | Checks if the user was synched from an external system.
[User_Login](<#User_Login>) | Action to login using username and password as credentials.
[User_Logout](<#User_Logout>) | Logs out the current user. Session variables are cleared during the logout process.
[User_Unblock](<#User_Unblock>) | Ends the blocking period for the specified user, allowing the user to login in all IP addresses where the user was blocked.
[User_Update](<#User_Update>) | Updates a specific user.

Structure | Description
---|---
[LoginAttemptPublic](<#Structure_LoginAttemptPublic>) | Represents the Login attempt record structure that is exposed

Static Entity | Description
---|---
[LoginAttemptResult](<#StaticEntity_LoginAttemptResult>) | The alternative values that may appear in the LoginAttempt record Result column.
[MenuItem](<#StaticEntity_MenuItem>) | Menu item to be used in menu web block parameters.

Role | Description
---|---
UserManager | 

## Widgets

### ChangePassword { #ChangePassword }

Allows changing the user password.

*Inputs*

UserId
:   Type: optional, User Identifier.  
    

### EditMyInfo { #EditMyInfo }




## Actions

### EncryptPassword { #EncryptPassword }

Returns the encrypted password for a specific username and password. This is the value kept in the Password attribute of the User system entity.

*Inputs*

Username
:   Type: mandatory, Text.  
    

Password
:   Type: mandatory, Text.  
    

*Outputs*

EncryptedPassword
:   Type: Text.  
    

### GetEffectiveUserProviderEspaceId { #GetEffectiveUserProviderEspaceId }

Returns the eSpace identifier of the effective user provider. Normally it returns the Users eSpaceId, in upgrade scenarios it returns the EnterpriseManager eSpaceId.  


*Outputs*

EspaceId
:   Type: Espace Identifier.  
    

### Group_CreateNew { #Group_CreateNew }

Create a new system group. Requires the UserManager role to be invoked.

*Inputs*

Group
:   Type: mandatory, Group.  
    

*Outputs*

GroupId
:   Type: Group Identifier.  
    

### Group_Delete { #Group_Delete }

Delete a system group. Requires the UserManager role to be invoked.

*Inputs*

GroupId
:   Type: mandatory, Group Identifier.  
    

### Group_Update { #Group_Update }

Updates a system group. Requires the UserManager role to be invoked.

*Inputs*

Group
:   Type: mandatory, Group.  
    

### IPAddress_GetBlockedStatus { #IPAddress_GetBlockedStatus }

Returns the blocking state of the IP address.

*Inputs*

IPAddress
:   Type: mandatory, Text.  
    IP address for which the blocking state should be evaluated.

*Outputs*

LoginAttemptResult
:   Type: [LoginAttemptResult](<#Structure_LoginAttemptResult>).  
    Blocking state for the given IP address.

### IPAddress_GetBlocks { #IPAddress_GetBlocks }

Returns the blocking state of the IP address. If there are no blocks for this address, the list will be empty. If no IP address is given, information on all blocked IP addresses will be returned.

*Inputs*

IPAddress
:   Type: optional, Text.  
    IP Address for which the current block information should be given.

*Outputs*

BlockedAddresses
:   Type: [LoginAttemptPublic](<#Structure_LoginAttemptPublic>) List.  
    Blocked login attempts associated to the given IP address, or all IP addresses, if no input is given.

### IPAddress_Unblock { #IPAddress_Unblock }

Ends the blocking period for the specified IP address, allowing any user to login in that address.

*Inputs*

IPAddress
:   Type: mandatory, Text.  
    The IP address to be unblocked.

### UseActiveDirectoryAuthentication { #UseActiveDirectoryAuthentication }

Returns the Users configuration that determines if the Active Directory is used for authentication

*Outputs*

IsActive
:   Type: Boolean.  
    

### UseIntegratedAuthentication { #UseIntegratedAuthentication }

Returns the Users configuration that determines if the Integrated Authentication is used to login.

*Outputs*

IsActive
:   Type: Boolean.  
    

### UseLDAPAuthentication { #UseLDAPAuthentication }

Returns the Users configuration that determines if the Active Directory is used for authentication

*Outputs*

IsActive
:   Type: Boolean.  
    

### User_CanChangePassword { #User_CanChangePassword }

Checks if the User is allowed to change a password. It is false for Active Directory users.

*Inputs*

UserId
:   Type: mandatory, User Identifier.  
    

*Outputs*

IsAllowed
:   Type: Boolean.  
    

### User_Create { #User_Create }

Create a new user. Requires UserManager role to be invoked.  
Fails when the username is repeated.

*Inputs*

User
:   Type: mandatory, User.  
    

*Outputs*

UserId
:   Type: User Identifier.  
    

### User_CreateOrUpdate { #User_CreateOrUpdate }

Create or updates a user. Requires UserManager role to be invoked.

*Inputs*

User
:   Type: mandatory, User.  
    

*Outputs*

UserId
:   Type: User Identifier.  
    

### User_DeleteIfNoRoles { #User_DeleteIfNoRoles }

Deletes the User if there are no roles assigned to it.

*Inputs*

UserId
:   Type: mandatory, User Identifier.  
    

### User_GetBlockedStatus { #User_GetBlockedStatus }

Returns information regarding the blocking state of the user and the blocking reason, in the specified IP address. If no IP address is given, checks the last IP address from where the user attempted to login.

*Inputs*

Username
:   Type: mandatory, Text.  
    The username of the user whose information regarding the blocked/unblocked state will be retrieved.

IPAddress
:   Type: optional, Text.  
    The IP address for which the information regarding the blocked/unblocked user state will be retrieved.

*Outputs*

LoginAttemptResult
:   Type: [LoginAttemptResult](<#Structure_LoginAttemptResult>).  
    Blocking state and reason for the given username.

### User_GetIdByUsername { #User_GetIdByUsername }

Returns the user identifier for a specific user given the username

*Inputs*

Username
:   Type: mandatory, Text.  
    

*Outputs*

UserId
:   Type: User Identifier.  
    

### User_GetLastFailedLoginAttempts { #User_GetLastFailedLoginAttempts }

Returns a list of last failed login attempts (one record for each IP address). This information can be used to invoke User_Unblock or IPaddress_Unblock.

*Inputs*

Username
:   Type: mandatory, Text.  
    The username of the user whose failed login attempts are retrieved.

Since
:   Type: optional, Date Time.  
    Only the login attempts after this datetime are retrieved.

*Outputs*

LoginAttempt
:   Type: [LoginAttemptPublic](<#Structure_LoginAttemptPublic>) List.  
    List of last failed login attempts for the given username.

### User_GetName { #User_GetName }

Returns the name of the logged user.

*Outputs*

Name
:   Type: Text.  
    

### User_GetUnifiedLoginUrl { #User_GetUnifiedLoginUrl }

Returns the Url used for custom unified login patterns. Includes Windows Integrated Authentication pattern.

*Inputs*

OriginalUrl
:   Type: mandatory, Text.  
    

*Outputs*

Url
:   Type: Text.  
    
### User_GetUnifiedLogoutUrl { #User_GetUnifiedLogoutUrl }

Returns the Url used for custom unified logout patterns. Includes Windows Integrated Authentication pattern.

*Inputs*

OriginalUrl
:   Type: optional, Text.  
    

*Outputs*

Url
:   Type: Text.  

### User_IsExternalUser { #User_IsExternalUser }

Checks if the user was synched from an external system.

*Inputs*

UserId
:   Type: mandatory, User Identifier.  
    

*Outputs*

IsExternal
:   Type: Boolean.  
    

### User_Login { #User_Login }

Action to login using username and password as credentials.

*Inputs*

Username
:   Type: mandatory, Text.  
    User's username.

Password
:   Type: mandatory, Text.  
    User's password (should not be encrypted).

RememberLogin
:   Type: mandatory, Boolean.  
    If true, the login will be persistent for 10 days.

### User_Logout { #User_Logout }

Logs out the current user. Session variables are cleared during the logout process.

### User_Unblock { #User_Unblock }

Ends the blocking period for the specified user, allowing the user to login in all IP addresses where the user was blocked.

*Inputs*

Username
:   Type: mandatory, Text.  
    The username of the user that is being unblocked and that will be allowed to login again from the specified IP address.

IPAddress
:   Type: optional, Text.  
    The IP address that is being unblocked and from where the specified user will be allowed to login again.

### User_Update { #User_Update }

Updates a specific user.

*Inputs*

User
:   Type: mandatory, User.  
    


## Structures

### LoginAttemptPublic { #Structure_LoginAttemptPublic }

Represents the Login attempt record structure that is exposed

*Attributes*

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

### LoginAttemptResult { #StaticEntity_LoginAttemptResult }

The alternative values that may appear in the LoginAttempt record Result column.

*Attributes*

Id
:   Type: Text (50).  
    

*Records*

* InvalidLDAPAuthentication
* BlockedIP
* Unblocked
* LoggedIn
* BlockedUser
* InvalidADAuthentication
* InvalidUser
* InvalidPassword

### MenuItem { #StaticEntity_MenuItem }

Menu item to be used in menu web block parameters.

*Attributes*

Id
:   Type: Integer.  
    

Order
:   Type: Integer.  
    

Caption
:   Type: Text (50).  
    

*Records*

* Applications
* Users
* Groups


