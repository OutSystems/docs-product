# ExBuilder_UserAuth_CS

Module with some user extended Entites and Actions, to be used on the remaining Modules and includes authentication methods.

## Summary

Action | Description
---|---
[Get_UserMobileDevice_ByUserDeviceIds](<#Get_UserMobileDevice_ByUserDeviceIds>) | Server action to get the UserMobile information for a specific user and device.
[Remove_UserExtended](<#Remove_UserExtended>) | Server action to delete the UserExtended for given user identifier.
[Remove_UserMobileDevice](<#Remove_UserMobileDevice>) | Server action to delete the UserMobile for a given user and device UUID.
[Save_UserMobileDevice](<#Save_UserMobileDevice>) | Server action to save the user extra information in the context of the sample mobile application for Banking.
[Set_PasscodeValue](<#Set_PasscodeValue>) | Server action to set a given passcode for a given user.
[Set_PatternValue](<#Set_PatternValue>) | Server action to set a given pattern for a given user.
[User_CheckUsernameAvailability](<#User_CheckUsernameAvailability>) | Server action to check if the received username is available in the system.
[User_CreateWithExtendedAttributes](<#User_CreateWithExtendedAttributes>) | Server action to create a user with extended attributes.
[User_GetByEmail](<#User_GetByEmail>) | Server action to get a user identifier  associated with an email.
[User_GetByPhoneNumber](<#User_GetByPhoneNumber>) | Server action to get a user identifier  associated with a phone number.
[User_LoginOTP](<#User_LoginOTP>) | Server action to authenticate the user in the system, by using an OTP that is sent.<br/>If successful, returns the user information.<br/>For demo purposes we'll expect the code to be always 123456.
[User_LoginPasscode](<#User_LoginPasscode>) | Server action to authenticate the user in the system, by using the passcode.<br/>If successful, returns the user information.
[User_LoginPattern](<#User_LoginPattern>) | Server action to authenticate the user in the system, by using the pattern.<br/>If successful, returns the user information.
[User_LoginWithUsernamePassword](<#User_LoginWithUsernamePassword>) | Server action to authenticate the user in the system, by using the username and password.<br/>If successful, returns the user information.
[User_SaveLastValidLogin](<#User_SaveLastValidLogin>) | Server action to set the last login date to the current date.
[User_SetupRegistration](<#User_SetupRegistration>) | Server action to setup a user account registration.
[User_ValidateBasicInformation](<#User_ValidateBasicInformation>) | Server action to validate all the user data for the setup registration.
[User_ValidateBasicPersonalDetails](<#User_ValidateBasicPersonalDetails>) | Server action to validate the basic personal details of a user.
[User_ValidatePasscode](<#User_ValidatePasscode>) | Server action to validate a given passcode according to the business rules.
[User_ValidatePasswordComplexity](<#User_ValidatePasswordComplexity>) | Server action to validate a given password according to the business rules.
[User_ValidatePhoneNumber](<#User_ValidatePhoneNumber>) | Server action to validate a phone number for the setup registration.
[UserDevice_RegistrationStatus](<#UserDevice_RegistrationStatus>) | Server action to get the account registration status for a specific user.

Structure | Description
---|---
[Result](<#Structure_Result>) | Structure to handle a result.
[UserSessionInfo](<#Structure_UserSessionInfo>) | Structure to handle the user information in his session.
[ValidationResult](<#Structure_ValidationResult>) | Structure to handle a validation result.

Static Entity | Description
---|---
[UserAccountStatus](<#StaticEntity_UserAccountStatus>) | Static entity to enumerate the available customer account status.

## Actions

### Get_UserMobileDevice_ByUserDeviceIds { #Get_UserMobileDevice_ByUserDeviceIds }

Server action to get the UserMobile information for a specific user and device.

*Inputs*

UserId
:   Type: mandatory, User Identifier.  
    Input variable with the identifier of the user from which we'll get the information.

DeviceId
:   Type: mandatory, Text.  
    Input variable with the mobile device's Universally Unique Identifier (UUID).

*Outputs*

LastUpdate
:   Type: Date Time.  
    Returns a timestamp of the last update in the UserMobileDevice record.

UserSessionInfoRec
:   Type: [UserSessionInfo](<#Structure_UserSessionInfo>).  
    Record with the logged user information.

HasPasscodeDefined
:   Type: Boolean.  
    Returns true if the user has a passcode defined.

HasPatternDefined
:   Type: Boolean.  
    Returns true if the user has a pattern defined.

HasBiometricsDefined
:   Type: Boolean.  
    Returns true if the user defined a biometric authentication.

IsBiometricsActivated
:   Type: Boolean.  
    Returns true if the user has the biometric authentication setting activated.

UserMobileDeviceId
:   Type: UserMobileDevice Identifier.  
    Returns the user mobile device identifier.

PasscodeValue
:   Type: Text.  
    Returns encrypted passcode value.

PatternValue
:   Type: Text.  
    Returns encrypted pattern value.

Exists
:   Type: Boolean.  
    Returns a flag to indicate if the user device pair exists in the system.

### Remove_UserExtended { #Remove_UserExtended }

Server action to delete the UserExtended for given user identifier.

*Inputs*

UserId
:   Type: mandatory, User Identifier.  
    Input variable with user's identifier to delete the entry.

DoLogout
:   Type: optional, Boolean.  
    Input variable to indicate if we also want to logout the user.

### Remove_UserMobileDevice { #Remove_UserMobileDevice }

Server action to delete the UserMobile for a given user and device UUID.

*Inputs*

UserId
:   Type: mandatory, User Identifier.  
    Input variable with user's identifier to delete the entry.

DoLogout
:   Type: optional, Boolean.  
    Input variable to indicate if we also want to logout the user.

### Save_UserMobileDevice { #Save_UserMobileDevice }

Server action to save the user extra information in the context of the sample mobile application for Banking.

*Inputs*

UserMobileDeviceRec
:   Type: mandatory.  
    Input record with the information about the UserMobileDevice.

*Outputs*

UserMobileDeviceId
:   Type: UserMobileDevice Identifier.  
    Returned UserMobileDevice Identifier.

### Set_PasscodeValue { #Set_PasscodeValue }

Server action to set a given passcode for a given user.

*Inputs*

UserId
:   Type: mandatory, User Identifier.  
    Input variable with the Identifier of the user to set the new passcode.

DeviceId
:   Type: mandatory, Text.  
    Input variable with the mobile device's Universally Unique Identifier (UUID).

PasscodeValue_NewValue
:   Type: mandatory, Text.  
    Input variable with the value of the new passcode to be set.

*Outputs*

UserMobileDeviceId
:   Type: UserMobileDevice Identifier.  
    Returned UserMobileDevice Identifier.

ResultStructRec
:   Type: [Result](<#Structure_Result>).  
    Returned record with information to indicate if the passcode was set successfully.

UserSessionInfoRec
:   Type: [UserSessionInfo](<#Structure_UserSessionInfo>).  
    Returned record with information about current user's session.

### Set_PatternValue { #Set_PatternValue }

Server action to set a given pattern for a given user.

*Inputs*

UserId
:   Type: mandatory, User Identifier.  
    Input variable with the Identifier of the user to set the new passcode.

DeviceId
:   Type: mandatory, Text.  
    Input variable with the mobile device's Universally Unique Identifier (UUID).

PatternValue_NewValue
:   Type: mandatory, Text.  
    Input variable with the value of the new pattern to be set.

*Outputs*

UserMobileDeviceId
:   Type: UserMobileDevice Identifier.  
    Returned UserMobileDevice Identifier.

ResultStructRec
:   Type: [Result](<#Structure_Result>).  
    Returned record with information to indicate if the passcode was set successfully.

UserSessionInfoRec
:   Type: [UserSessionInfo](<#Structure_UserSessionInfo>).  
    Returned record with information about current user's session.

### User_CheckUsernameAvailability { #User_CheckUsernameAvailability }

Server action to check if the received username is available in the system.

*Inputs*

Username
:   Type: mandatory, Text.  
    Input variable with the username to be checked.

*Outputs*

IsAvailable
:   Type: Boolean.  
    Returned value indicating if the username is available.

### User_CreateWithExtendedAttributes { #User_CreateWithExtendedAttributes }

Server action to create a user with extended attributes.

*Inputs*

User
:   Type: mandatory.  
    Input record with user information.

UserExtended
:   Type: mandatory.  
    Input record with extended user information.

ImpersonateUserManagmentUser
:   Type: optional, Boolean.  
    Input variable that indicates if we want to impersonate or not the system user.

IsSignupPhoneNumber
:   Type: optional, Boolean.  
    Input variable with a flag to indicate if we're executing a signup with phone number, where the password validation will be different and will be the passcode.

*Outputs*

UserSessionInfoRec
:   Type: [UserSessionInfo](<#Structure_UserSessionInfo>).  
    Returned record with the created user information.

### User_GetByEmail { #User_GetByEmail }

Server action to get a user identifier  associated with an email.

*Inputs*

Email
:   Type: mandatory, Email.  
    Email to look for.

*Outputs*

UserId
:   Type: User Identifier.  
    Returned user identifier associated with a provided email, NullIdentifier() in case of a user not found.

ErrorMessage
:   Type: Text.  
    Error Message if any occurs.

### User_GetByPhoneNumber { #User_GetByPhoneNumber }

Server action to get a user identifier  associated with a phone number.

*Inputs*

PhoneNumber
:   Type: mandatory, Text.  
    Phone number to look for.

*Outputs*

UserId
:   Type: User Identifier.  
    Returned user identifier associated with a provided phone number, NullIdentifier() in case of a user not found.

ErrorMessage
:   Type: Text.  
    Error Message if any occurs.

### User_LoginOTP { #User_LoginOTP }

Server action to authenticate the user in the system, by using an OTP that is sent.  
If successful, returns the user information.  
For demo purposes we'll expect the code to be always 123456.

*Inputs*

UserId
:   Type: mandatory, User Identifier.  
    Input variable with the Identifier of the user to be logged in.

DeviceId
:   Type: mandatory, Text.  
    nput variable with the mobile device's Universally Unique Identifier (UUID).

OTPCode
:   Type: mandatory, Text.  
    Input variable with the OTP code for login.

*Outputs*

ResultRec
:   Type: [Result](<#Structure_Result>).  
    Returned record with information to indicate if the login with passcode was successfull.

UserSessionInfoRec
:   Type: [UserSessionInfo](<#Structure_UserSessionInfo>).  
    Returned record with information about current user's session.

### User_LoginPasscode { #User_LoginPasscode }

Server action to authenticate the user in the system, by using the passcode.  
If successful, returns the user information.

*Inputs*

UserId
:   Type: mandatory, User Identifier.  
    Input variable with the Identifier of the user to be logged in.

Passcode
:   Type: mandatory, Text.  
    Input variable with the passcode for login.

DeviceId
:   Type: mandatory, Text.  
    nput variable with the mobile device's Universally Unique Identifier (UUID).

*Outputs*

ResultRec
:   Type: [Result](<#Structure_Result>).  
    Returned record with information to indicate if the login with passcode was successfull.

UserSessionInfoRec
:   Type: [UserSessionInfo](<#Structure_UserSessionInfo>).  
    Returned record with information about current user's session.

### User_LoginPattern { #User_LoginPattern }

Server action to authenticate the user in the system, by using the pattern.  
If successful, returns the user information.

*Inputs*

UserId
:   Type: mandatory, User Identifier.  
    Input variable with the Identifier of the user to be logged in.

Pattern
:   Type: mandatory, Text.  
    Input variable with the pattern for login.

DeviceId
:   Type: mandatory, Text.  
    nput variable with the mobile device's Universally Unique Identifier (UUID).

*Outputs*

ResultRec
:   Type: [Result](<#Structure_Result>).  
    Returned record with information to indicate if the login with passcode was successfull.

UserSessionInfoRec
:   Type: [UserSessionInfo](<#Structure_UserSessionInfo>).  
    Returned record with information about current user's session.

### User_LoginWithUsernamePassword { #User_LoginWithUsernamePassword }

Server action to authenticate the user in the system, by using the username and password.  
If successful, returns the user information.

*Inputs*

Username
:   Type: mandatory, Text.  
    Input variable with the username of the user to be logged in.

Password
:   Type: mandatory, Text.  
    Input variable with the password to be used for login.

DeviceId
:   Type: mandatory, Text.  
    Input variable with the mobile device's Universally Unique Identifier (UUID).

*Outputs*

ResultRec
:   Type: [Result](<#Structure_Result>).  
    Returned record with information to indicate if the login with password was successfull.

UserSessionInfoRec
:   Type: [UserSessionInfo](<#Structure_UserSessionInfo>).  
    Returned record with information about current user's session.

IsNewInDevice
:   Type: Boolean.  
    Returned value to indicate if the user is new in the Device.

### User_SaveLastValidLogin { #User_SaveLastValidLogin }

Server action to set the last login date to the current date.

*Inputs*

UserId
:   Type: mandatory, User Identifier.  
    Input variable with the identifier of the user.

### User_SetupRegistration { #User_SetupRegistration }

Server action to setup a user account registration.

*Inputs*

Username
:   Type: mandatory, Text.  
    Input variable with user's username.

DeviceId
:   Type: mandatory, Text.  
    Input variable with the mobile device's Universally Unique Identifier (UUID).

Password
:   Type: mandatory, Text.  
    Input variable with user's password.

MobilePhone
:   Type: mandatory, Phone Number.  
    Input variable with user's mobile phone number.

AccountNumber
:   Type: mandatory, Integer.  
    Input variable with user's account number.

SocialSecurityNumber
:   Type: mandatory, Integer.  
    Input variable with user's social security number.

Name
:   Type: mandatory, Text.  
    Input variable with the name of the user.

BirthDate
:   Type: optional, Date.  
    Input variable with the user birth date.

Email
:   Type: optional, Email.  
    Input variable with user's email.

IsSignupPhoneNumber
:   Type: optional, Boolean.  
    Input variable with a flag to indicate if we're executing a signup with phone number, where the password validation will be different and will be the passcode.

PasscodeLength
:   Type: optional, Integer.  
    Input variable with length of the pin code. If &quot;0-1&quot; we'll not validate this. Only applicable for IsSignupPhoneNumber.

*Outputs*

ResultRec
:   Type: [Result](<#Structure_Result>).  
    Returned record with information to indicate if the account registration was successfull.

UserSessionInfoRec
:   Type: [UserSessionInfo](<#Structure_UserSessionInfo>).  
    Returned record with information about current user's session.

### User_ValidateBasicInformation { #User_ValidateBasicInformation }

Server action to validate all the user data for the setup registration.

*Inputs*

Name
:   Type: mandatory, Text.  
    Input variable with the name of the user.

Username
:   Type: mandatory, Text.  
    Input variable with user's username.

MobilePhone
:   Type: optional, Phone Number.  
    Input variable with user's mobile phone number.

IsSignupPhoneNumber
:   Type: optional, Boolean.  
    Input variable with a flag to indicate if we're executing a signup with phone number, where the password validation will be different and will be the passcode.

*Outputs*

Result
:   Type: Boolean, Text.  
    Returned record with information to indicate if the password was validated successfully.

### User_ValidateBasicPersonalDetails { #User_ValidateBasicPersonalDetails }

Server action to validate the basic personal details of a user.

*Inputs*

FirstName
:   Type: mandatory, Text.  
    Input variable with the first legal name of the user.

LastName
:   Type: mandatory, Text.  
    Input variable with the last legalname of the user.

BirthDate
:   Type: mandatory, Date.  
    Input variable with the user birth date.

*Outputs*

Result
:   Type: [ValidationResult](<#Structure_ValidationResult>), [ValidationResult](<#Structure_ValidationResult>), [ValidationResult](<#Structure_ValidationResult>).  
    Returned record with information to indicate if the password was validated successfully.

### User_ValidatePasscode { #User_ValidatePasscode }

Server action to validate a given passcode according to the business rules.

*Inputs*

Passcode
:   Type: mandatory, Text.  
    Input variable with the passcode to be validated.

Length
:   Type: mandatory, Integer.  
    Input variable with length of the pin code. If &quot;-1&quot; we'll not validate this.

*Outputs*

Result
:   Type: Boolean, Text.  
    Returned record with information to indicate if the password was validated successfully.

### User_ValidatePasswordComplexity { #User_ValidatePasswordComplexity }

Server action to validate a given password according to the business rules.

*Inputs*

Password
:   Type: mandatory, Text.  
    Input variable with the password to be validated.

Username
:   Type: mandatory, Text.  
    Input variable with user's username.

*Outputs*

Result
:   Type: Boolean, Text.  
    Returned record with information to indicate if the password was validated successfully.

### User_ValidatePhoneNumber { #User_ValidatePhoneNumber }

Server action to validate a phone number for the setup registration.

*Inputs*

MobilePhone
:   Type: mandatory, Phone Number.  
    Input variable with user's mobile phone number.

*Outputs*

Result
:   Type: Boolean, Text.  
    Returned record with information to indicate if the password was validated successfully.

### UserDevice_RegistrationStatus { #UserDevice_RegistrationStatus }

Server action to get the account registration status for a specific user.

*Inputs*

UserId
:   Type: mandatory, User Identifier.  
    Input variable with user identifier.

DeviceId
:   Type: mandatory, Text.  
    Input variable with the mobile device's Universally Unique Identifier (UUID).

*Outputs*

UserAccountStatusId
:   Type: UserAccountStatus Identifier.  
    Returned UserAccountStatus Identifier.

HasPasscodeDefined
:   Type: Boolean.  
    Returned flag indicating if there's a passcode defined.

HasPatternDefined
:   Type: Boolean.  
    Returned flag indicating if there's a pattern defined.

HasBiometricsDefined
:   Type: Boolean.  
    Returned flag indicating if the user defined a biometric authentication.

Exists
:   Type: Boolean.  
    Returns if given user exists in the device.


## Structures

### Result { #Structure_Result }

Structure to handle a result.

*Attributes*

Success
:   Type: Boolean.  
    If success.

ErrorMessage
:   Type: Text.  
    Error Message if any occurs.

### UserSessionInfo { #Structure_UserSessionInfo }

Structure to handle the user information in his session.

*Attributes*

UserId
:   Type: User Identifier.  
    User Identifier.

DisplayName
:   Type: Text.  
    Name of the user.

Email
:   Type: Email.  
    Email

MobileNumber
:   Type: Text.  
    Mobile Number of the user

Username
:   Type: Text.  
    Username of the user.

### ValidationResult { #Structure_ValidationResult }

Structure to handle a validation result.

*Attributes*

IsValid
:   Type: Boolean.  
    If is valid.

ValidationMessage
:   Type: Text.  
    Validation Message if any occurs.


## Static Entities

### UserAccountStatus { #StaticEntity_UserAccountStatus }

Static entity to enumerate the available customer account status.

*Attributes*

Id
:   Type: Integer.  
    Identifier of the customer account status.

Label
:   Type: Text (50).  
    Label of the customer account status.

Is_Active
:   Type: Boolean.  
    Indicates if the customer account status is active or not.

*Records*

* RegisteredDeactivated
* RegisteredWithoutPasscode
* NotRegistered
* Registered
