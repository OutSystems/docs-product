---
locale: en-us
guid: bf5a417a-a13c-4dc4-b9c8-4800c7f324b3
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# ExBuilder_Authentication_MCS

Module with the authentication mobile core services.

## Summary

Client Action | Description
---|---
[BiometricSignature_Update](<#Client_BiometricSignature_Update>) | Client variable to update the biometric's signature.
[Change_Passcode](<#Client_Change_Passcode>) | Client action to change the passcode of a given user.
[Change_Pattern](<#Client_Change_Pattern>) | Client action to change the pattern of a given user.
[Get_HasPasscodeDefined](<#Client_Get_HasPasscodeDefined>) | Client action to check if the user has a passcode defined or not.
[Get_UserMobileForUserDevice](<#Client_Get_UserMobileForUserDevice>) | Client action to get the UserMobile information for a specific user and device.
[Remove_UserMobileDevice](<#Client_Remove_UserMobileDevice>) | Client action to delete the UserMobile for a given user and device UUID. Also logs out the user.
[Set_PasscodeValue](<#Client_Set_PasscodeValue>) | Client action to set a given passcode for a given user.
[Set_PatternValue](<#Client_Set_PatternValue>) | Client action to set a given pattern for a given user.
[StoredInformation_DeleteAll](<#Client_StoredInformation_DeleteAll>) | Client action to delete the local settings from the device. Used on the logout process.
[User_AccountRegistration](<#Client_User_AccountRegistration>) | Client action to setup an account registration.
[User_CheckUsernameAvailability](<#Client_User_CheckUsernameAvailability>) | Client action to check if the received username is available in the system.
[User_ClearSessionInfo](<#Client_User_ClearSessionInfo>) | Client action to clear user data from client variables.
[User_GetByEmail](<#Client_User_GetByEmail>) | Client action to get a user identifier associated with a email.
[User_GetByPhoneNumber](<#Client_User_GetByPhoneNumber>) | Client action to get a user identifier associated with a Phone Number.
[User_GetSessionInfo](<#Client_User_GetSessionInfo>) | Client action to get user data from client variables.
[User_GetStatus](<#Client_User_GetStatus>) | Client action to get a resume of the user account status.
[User_LoginOTP](<#Client_User_LoginOTP>) | Client action to authenticate the user in the system, by using an OTP that is sent.<br/>If successful, returns the user information.<br/>For demo purposes we'll expect the code to be always 123456.
[User_LoginWithPasscode](<#Client_User_LoginWithPasscode>) | Client action to authenticate the user in the system, by using the passcode.<br/>If successful, returns the user information.
[User_LoginWithPassword](<#Client_User_LoginWithPassword>) | Client action to login a user by username and password.
[User_LoginWithPattern](<#Client_User_LoginWithPattern>) | Client action to authenticate the user in the system, by using the pattern.<br/>If successful, returns the user information.
[User_SetSessionInfo](<#Client_User_SetSessionInfo>) | Client action to set user info in client variables.
[User_ValidateBasicPersonalDetails](<#Client_User_ValidateBasicPersonalDetails>) | Server action to validate the basic personal details of a user.
[User_ValidatePhoneNumber](<#Client_User_ValidatePhoneNumber>) | Client action to validate phone for the setup registration.

Structure | Description
---|---
[BiometricAuthSignature](<#Structure_BiometricAuthSignature>) | Structure used to store the users touch id configuration in keystore.
[Result](<#Structure_Result>) | Result structure.
[UserSessionInfo](<#Structure_UserSessionInfo>) | Structure to handle the user information in their session.
[ValidationResult](<#Structure_ValidationResult>) | Structure to handle a validation result.

## Client Actions

### BiometricSignature_Update { #Client_BiometricSignature_Update }

Client variable to update the biometric's signature.

*Inputs*

UserId
:   Type: mandatory, Text.  
    Input variable with the Identifier of the current user.

Passcode
:   Type: mandatory, Text.  
    Input variable with user passcode.

Pattern
:   Type: optional, Text.  
    Input variable with user pattern.

BiometryType
:   Type: mandatory, Text.  
    Input variable to set the biometry type:  
    1 - TouchID  
    2 - FaceID (iOS only)  
    -1 - no Biometry

IsBiometricsAvailableInDevice
:   Type: mandatory, Text.  
    Input variable to indicate if biometrics are available on the current device.

IsBiometricsActiveOnApp
:   Type: mandatory, Text.  
    Input variable to indicate if biometrics are active on the app.

*Outputs*

Out_BiometricConfigRec
:   Type: [BiometricAuthSignature](<#Structure_BiometricAuthSignature>).  
    Returned record with the updated biometrics information.

### Change_Passcode { #Client_Change_Passcode }

Client action to change the passcode of a given user.

*Inputs*

PasscodeValue_NewValue
:   Type: mandatory, Text.  
    Input variable with the passcode value encrypted.

UserId
:   Type: mandatory, User Identifier.  
    Input variable with the Identifier of the user to which we'll change the passcode.

### Change_Pattern { #Client_Change_Pattern }

Client action to change the pattern of a given user.

*Inputs*

PatternValue_NewValue
:   Type: mandatory, Text.  
    Input variable with the pattern value encrypted.

UserId
:   Type: mandatory, User Identifier.  
    Input variable with the Identifier of the user to which we'll change the passcode.

### Get_HasPasscodeDefined { #Client_Get_HasPasscodeDefined }

Client action to check if the user has a passcode defined or not.

*Inputs*

UserId
:   Type: mandatory, User Identifier.  
    Input variable with the Identifier of the user to be checked.

*Outputs*

HasPasscodeDefined
:   Type: Boolean.  
    Returns true if the user has a passcode defined.

### Get_UserMobileForUserDevice { #Client_Get_UserMobileForUserDevice }

Client action to get the UserMobile information for a specific user and device.

*Inputs*

UserId
:   Type: mandatory, User Identifier.  
    Input variable with the identifier of the user from which we'll get the information.

DeviceId
:   Type: mandatory, Text.  
    Input variable with the mobile device's Universally Unique Identifier (UUID).

*Outputs*

HasPasscodeDefined
:   Type: Boolean.  
    Returns true if the user has a passcode defined.

HasBiometricsDefined
:   Type: Boolean.  
    Returns true if the user defined a biometric authentication.

IsBiometricsActivated
:   Type: Boolean.  
    Returns true if the user has the biometric authentication setting activated.

### Remove_UserMobileDevice { #Client_Remove_UserMobileDevice }

Client action to delete the UserMobile for a given user and device UUID. Also logs out the user.

*Inputs*

UserId
:   Type: mandatory, User Identifier.  
    Input variable with user's identifier to delete the entry.

### Set_PasscodeValue { #Client_Set_PasscodeValue }

Client action to set a given passcode for a given user.

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

ResultStructRec
:   Type: [Result](<#Structure_Result>).  
    Returned record with information to indicate if the passcode was set successfully.

UserSessionInfoRec
:   Type: [UserSessionInfo](<#Structure_UserSessionInfo>).  
    Returned record with information about current user's session.

### Set_PatternValue { #Client_Set_PatternValue }

Client action to set a given pattern for a given user.

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

ResultStructRec
:   Type: [Result](<#Structure_Result>).  
    Returned record with information to indicate if the passcode was set successfully.

UserSessionInfoRec
:   Type: [UserSessionInfo](<#Structure_UserSessionInfo>).  
    Returned record with information about current user's session.

### StoredInformation_DeleteAll { #Client_StoredInformation_DeleteAll }

Client action to delete the local settings from the device. Used on the logout process.

### User_AccountRegistration { #Client_User_AccountRegistration }

Client action to setup an account registration.

*Inputs*

Username
:   Type: mandatory, Text.  
    Input variable with user's username.

Password
:   Type: mandatory, Text.  
    Input variable with user's password.

Name
:   Type: mandatory, Text.  
    Input variable with the name of the user.

MobilePhone
:   Type: mandatory, Phone Number.  
    Input variable with user's mobile phone number.

AccountNumber
:   Type: mandatory, Integer.  
    Input variable with user's account number.

SocialSecurityNumber
:   Type: mandatory, Integer.  
    Input variable with user's social security number.

BirthDate
:   Type: optional, Date.  
    Input variable with the user birth date.

DeviceId
:   Type: mandatory, Text.  
    Input variable with the mobile device's Universally Unique Identifier (UUID).

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

ResultStructRec
:   Type: [Result](<#Structure_Result>).  
    Returned record with information to indicate if the account registration was successfull.

UserSessionInfo
:   Type: [UserSessionInfo](<#Structure_UserSessionInfo>).  
    Returned record with information about current user's session.

### User_CheckUsernameAvailability { #Client_User_CheckUsernameAvailability }

Client action to check if the received username is available in the system.

*Inputs*

Username
:   Type: mandatory, Text.  
    Input variable with the username to be checked.

*Outputs*

ResultStructRec
:   Type: [Result](<#Structure_Result>).  
    Returned record with information to indicate if the username was checked successfully.

IsAvailable
:   Type: Boolean.  
    Returned value indicating if the username is available.

### User_ClearSessionInfo { #Client_User_ClearSessionInfo }

Client action to clear user data from client variables.

### User_GetByEmail { #Client_User_GetByEmail }

Client action to get a user identifier associated with a email.

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

### User_GetByPhoneNumber { #Client_User_GetByPhoneNumber }

Client action to get a user identifier associated with a Phone Number.

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

### User_GetSessionInfo { #Client_User_GetSessionInfo }

Client action to get user data from client variables.

*Outputs*

UserSessionInfo
:   Type: [UserSessionInfo](<#Structure_UserSessionInfo>).  
    Returned record with current user's session info.

### User_GetStatus { #Client_User_GetStatus }

Client action to get a resume of the user account status.

*Inputs*

UserId
:   Type: mandatory, User Identifier.  
    Input variable with the identifier of the user to get status.

DeviceId
:   Type: mandatory, Text.  
    Input variable with the mobile device's Universally Unique Identifier (UUID).

*Outputs*

IsNotRegistered
:   Type: Boolean.  
    Indicates if the user is not registered.

IsRegistered
:   Type: Boolean.  
    Indicates if the user is registered.

IsRegisteredDeactivated
:   Type: Boolean.  
    Indicates if the user is registered but deactivated.

IsRegisteredWithoutPasscode
:   Type: Boolean.  
    Indicates if the user is registered but without a passcode being set.

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
    Indicates that exists in the device.

### User_LoginOTP { #Client_User_LoginOTP }

Client action to authenticate the user in the system, by using an OTP that is sent.  
If successful, returns the user information.  
For demo purposes we'll expect the code to be always 123456.

*Inputs*

UserId
:   Type: mandatory, User Identifier.  
    Input variable with the Identifier of the user to be logged in.

DeviceId
:   Type: mandatory, Text.  
    Input variable with the mobile device's Universally Unique Identifier (UUID).

OTPCode
:   Type: mandatory, Text.  
    Input variable with the OTP code for login.

*Outputs*

ResultStructRec
:   Type: [Result](<#Structure_Result>).  
    Returned record with information to indicate if the login with passcode was successfull.

UserSessionInfoRec
:   Type: [UserSessionInfo](<#Structure_UserSessionInfo>).  
    Returned record with information about current user's session.

### User_LoginWithPasscode { #Client_User_LoginWithPasscode }

Client action to authenticate the user in the system, by using the passcode.  
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
    Input variable with the mobile device's Universally Unique Identifier (UUID).

*Outputs*

ResultStructRec
:   Type: [Result](<#Structure_Result>).  
    Returned record with information to indicate if the login with passcode was successfull.

UserSessionInfoRec
:   Type: [UserSessionInfo](<#Structure_UserSessionInfo>).  
    Returned record with information about current user's session.

### User_LoginWithPassword { #Client_User_LoginWithPassword }

Client action to login a user by username and password.

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

ResultStructRec
:   Type: [Result](<#Structure_Result>).  
    Returned record with information to indicate if the login with password was successfull.

UserSessionInfoRec
:   Type: [UserSessionInfo](<#Structure_UserSessionInfo>).  
    Returned record with information about current user's session.

IsNewInDevice
:   Type: Boolean.  
    Returned record with information about current user's session.

### User_LoginWithPattern { #Client_User_LoginWithPattern }

Client action to authenticate the user in the system, by using the pattern.  
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
    Input variable with the mobile device's Universally Unique Identifier (UUID).

*Outputs*

ResultStructRec
:   Type: [Result](<#Structure_Result>).  
    Returned record with information to indicate if the login with passcode was successfull.

UserSessionInfoRec
:   Type: [UserSessionInfo](<#Structure_UserSessionInfo>).  
    Returned record with information about current user's session.

### User_SetSessionInfo { #Client_User_SetSessionInfo }

Client action to set user info in client variables.

*Inputs*

UserSessionInfo
:   Type: mandatory, [UserSessionInfo](<#Structure_UserSessionInfo>).  
    Input variable with current user's session info to be set.

### User_ValidateBasicPersonalDetails { #Client_User_ValidateBasicPersonalDetails }

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

### User_ValidatePhoneNumber { #Client_User_ValidatePhoneNumber }

Client action to validate phone for the setup registration.

*Inputs*

MobilePhone
:   Type: mandatory, Phone Number.  
    Input variable with user's mobile phone number.

*Outputs*

Result
:   Type: Boolean, Text.  
    Returned record with information to indicate if the password was validated successfully.


## Structures

### BiometricAuthSignature { #Structure_BiometricAuthSignature }

Structure used to store the users touch id configuration in keystore.

*Attributes*

UserId
:   Type: User Identifier.  
    Represents the User Identifier.

Passcode
:   Type: Text.  
    Represents the user Passcode.

Pattern
:   Type: Text.  
    Represents the user Pattern.

BiometryType
:   Type: Text.  
    Represents the biometrics type available on the device:  
    1 - TouchID  
    2 - FaceID (iOS only)  
    -1 - no Biometry

IsBiometricsActiveOnApp
:   Type: Text.  
    Flag to indicate if the biometrics are activated inside the app settings.

IsBiometricsAvailableInDevice
:   Type: Text.  
    Flag to indicate if the biometrics are available on the current device.

### Result { #Structure_Result }

Result structure.

*Attributes*

Success
:   Type: Boolean.  
    Indicates if the result was a success.

ErrorMessage
:   Type: Text.  
    Error Message if any occurs.

### UserSessionInfo { #Structure_UserSessionInfo }

Structure to handle the user information in their session.

*Attributes*

UserId
:   Type: User Identifier.  
    Identifier of the user.

DisplayName
:   Type: Text.  
    Represents the name of the user.

Email
:   Type: Email.  
    Represents the email of the user.

MobileNumber
:   Type: Text.  
    Represents the mobile number of the user

Username
:   Type: Text.  
    Represents the username of the user.

### ValidationResult { #Structure_ValidationResult }

Structure to handle a validation result.

*Attributes*

IsValid
:   Type: Boolean.  
    If is valid.

ValidationMessage
:   Type: Text.  
    Validation Message if any occurs.
