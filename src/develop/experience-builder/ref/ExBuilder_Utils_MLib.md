---
locale: en-us
guid: 61ef3e53-5022-4fa2-be4c-5acd839fc949
---

# ExBuilder_Utils_MLib

Module that contains several common objects and functions used across the mobile application.

## Summary

Client Action | Description
---|---
[AddClassToBody](<#Client_AddClassToBody>) | Client action to add a specific class to the screen body.
[AnimateScreenElement](<#Client_AnimateScreenElement>) | Client action to animate a specific page element.<br/>Ex: Error animation on Login passcode elements or Focus on a specific element.
[BlurActiveElement](<#Client_BlurActiveElement>) | Client action to make the blur on the document active element. Usually useful to close the keyboard.
[ClearSessionStorage](<#Client_ClearSessionStorage>) | Client action to clear the javascript session storage.
[Convert24hTo12hFormat](<#Client_Convert24hTo12hFormat>) | Client action to convert 24h format time in 12h format.
[FeatureNotAvailable](<#Client_FeatureNotAvailable>) | Client action to provide feedback about some plugin not being available on the device.
[FeatureNotImplemented](<#Client_FeatureNotImplemented>) | Client action to provide feedback about something that is not implemented yet.
[FocusActiveElement](<#Client_FocusActiveElement>) | Client action to make the focus on the document active element. Usually usefull to close the keyboard.
[FormatCurrencyVal](<#Client_FormatCurrencyVal>) | Client action to format an inputted currency.<br/>Ex: $100,00.50
[FormatDate](<#Client_FormatDate>) | Client action to format an given date.<br/>Ex:<br/>Jun 07, 2019 (ShowYear=True)<br/>Jun 07       (ShowYear=False)
[GetDeviceInfo](<#Client_GetDeviceInfo>) | Client action to get the available device information via Cordova methods.
[GetFullHostname](<#Client_GetFullHostname>) | Client action that returns the hostname of the current page, including the protocol.
[GetHostName](<#Client_GetHostName>) | Client action to get the hostname of the screen URL.
[HideFeedbackMessages](<#Client_HideFeedbackMessages>) | Client action to hide mobile feedback messages.
[IsNavigatingFromHistory](<#Client_IsNavigatingFromHistory>) | Client action that returns true if the user is navigating from history
[ListToString](<#Client_ListToString>) | Client action that receives a list and joins it with a delimiter text, creating a single Text.
[MaskEmail](<#Client_MaskEmail>) | Client action that masks an Email with * leaving a few digits visible.
[MaskPhone](<#Client_MaskPhone>) | Client action that masks a Phone number with * leaving a few digits visible.
[NotConnectedToScreen](<#Client_NotConnectedToScreen>) | Client action to provide feedback about a link not connected to any screen.
[RegexSearch](<#Client_RegexSearch>) | Client action to execute a regex search with javascript.
[RegexValidator](<#Client_RegexValidator>) | Client action to validate if a given text is valid on a regex pattern.
[Resolve](<#Client_Resolve>) | Client action that implements the protected Resolve method that ensures the DOM is fully loaded (useful to run JavaScript on the DOM after it).
[ScrollToTop](<#Client_ScrollToTop>) | Client action to scroll the screen to the top.
[ShowPassword](<#Client_ShowPassword>) | Client action to be used on the Login screen to enable users to show or hide the password characters.
[StringSplit](<#Client_StringSplit>) | Client action that receives one string and splits it by a delimiter text into a List of Text.
[ValidateEmail](<#Client_ValidateEmail>) | Client action to checks whether the given value is a valid e-mail.
[ValidatePhoneNumber](<#Client_ValidatePhoneNumber>) | Client action to validate a given phone number using RegEx.<br/>Format: XXX-XXX-XXXX

Structure | Description
---|---
[DeviceInfo](<#Structure_DeviceInfo>) | Structure to handle the device information.
[Result](<#Structure_Result>) | Result structure.
[UserSessionInfo](<#Structure_UserSessionInfo>) | Structure to handle the user information in his session.

## Client Actions

### AddClassToBody { #Client_AddClassToBody }

Client action to add a specific class to the screen body.

*Inputs*

Class
:   Type: mandatory, Text.  
    Input variable with the class to add.

### AnimateScreenElement { #Client_AnimateScreenElement }

Client action to animate a specific page element.  
Ex: Error animation on Login passcode elements or Focus on a specific element.

*Inputs*

AnimationType
:   Type: mandatory, Text.  
    Input variable with the type of animation to add to the specified element.  
    Ex: &quot;error&quot; or &quot;focus&quot;

AnimationWrapperId
:   Type: mandatory, Text.  
    Input variable with the id of the wrapper with the element to be animated. Eg. &quot;Passcode.Id&quot;

AnimationRemoveDelay
:   Type: mandatory, Integer.  
    Input variable delay in ms to remove the class that gives the animation to the given element.  
    Ex. &quot;500&quot; that corresponds to 500ms.

### BlurActiveElement { #Client_BlurActiveElement }

Client action to make the blur on the document active element. Usually useful to close the keyboard.

### ClearSessionStorage { #Client_ClearSessionStorage }

Client action to clear the javascript session storage.

### Convert24hTo12hFormat { #Client_Convert24hTo12hFormat }

Client action to convert 24h format time in 12h format.

*Inputs*

TimeValue
:   Type: mandatory, Time.  
    Input variable with time value to be converted to 12h format.

GroupSeparator
:   Type: mandatory, Text.  
    Input variable with separator symbol to be used as a hour, minute and second separator. Default value is &quot;:&quot;.

ShowSecounds
:   Type: mandatory, Boolean.  
    Input variable to determine if seconds will be displayed or not.

*Outputs*

TimeConverted
:   Type: Text.  
    Returned time in 12h format.

### FeatureNotAvailable { #Client_FeatureNotAvailable }

Client action to provide feedback about some plugin not being available on the device.

### FeatureNotImplemented { #Client_FeatureNotImplemented }

Client action to provide feedback about something that is not implemented yet.

### FocusActiveElement { #Client_FocusActiveElement }

Client action to make the focus on the document active element. Usually usefull to close the keyboard.

### FormatCurrencyVal { #Client_FormatCurrencyVal }

Client action to format an inputted currency.  
Ex: $100,00.50

*Inputs*

InputValue
:   Type: mandatory, Currency.  
    Input variable with the currency value to be formatted.

CurrencySymbol
:   Type: optional, Text.  
    Input variable with currency symbol to add to the format. By default it's &quot;$&quot;.

*Outputs*

Currency
:   Type: Text.  
    Returned formatted currency.

### FormatDate { #Client_FormatDate }

Client action to format an given date.  
Ex:  
Jun 07, 2019 (ShowYear=True)  
Jun 07       (ShowYear=False)

*Inputs*

InputDate
:   Type: mandatory, Date Time.  
    Input variable with date value to be formatted.

ShowYear
:   Type: optional, Boolean.  
    Input variable to determine if we want to show the year on the date.

*Outputs*

Date
:   Type: Text.  
    Returned formatted date.

### GetDeviceInfo { #Client_GetDeviceInfo }

Client action to get the available device information via Cordova methods.

*Outputs*

DeviceInfoRec
:   Type: [DeviceInfo](<#Structure_DeviceInfo>).  
    Returned record with the device information.

### GetFullHostname { #Client_GetFullHostname }

Client action that returns the hostname of the current page, including the protocol.

*Outputs*

FullHostname
:   Type: Text.  
    Returns the hostname of the current page, including the protocol.

### GetHostName { #Client_GetHostName }

Client action to get the hostname of the screen URL.

*Outputs*

HostName
:   Type: Text.  
    Returned hostname of the current screen.

### HideFeedbackMessages { #Client_HideFeedbackMessages }

Client action to hide mobile feedback messages.

### IsNavigatingFromHistory { #Client_IsNavigatingFromHistory }

Client action that returns true if the user is navigating from history

*Outputs*

IsFromHistory
:   Type: Boolean.  
    Input variable to indicate if the user is navigating to the current page from history

### ListToString { #Client_ListToString }

Client action that receives a list and joins it with a delimiter text, creating a single Text.

*Inputs*

StrList
:   Type: mandatory, Text List.  
    Input variable with the list of text with all the strings.

Delimiters
:   Type: optional, Text.  
    Input variable containing all the characters that should be considered as delimiters.

*Outputs*

Str
:   Type: Text.  
    Returned joined string.

### MaskEmail { #Client_MaskEmail }

Client action that masks an Email with * leaving a few digits visible.

*Inputs*

Email
:   Type: mandatory, Text.  
    Input variable containing then email to be masked.

*Outputs*

MaskedEmail
:   Type: Text.  
    Returns the email with the mask applied.

### MaskPhone { #Client_MaskPhone }

Client action that masks a Phone number with * leaving a few digits visible.

*Inputs*

PhoneNumber
:   Type: mandatory, Text.  
    Input variable with the phone number to be masked.

*Outputs*

MaskedPhoneNumber
:   Type: Text.  
    Returns the phone number with the mask applied.

### NotConnectedToScreen { #Client_NotConnectedToScreen }

Client action to provide feedback about a link not connected to any screen.

### RegexSearch { #Client_RegexSearch }

Client action to execute a regex search with javascript.

*Inputs*

Text
:   Type: mandatory, Text.  
    Input variable with the text to be searched.

Pattern
:   Type: mandatory, Text.  
    Input variable with the regex pattern to be executed for the search.

*Outputs*

IsFound
:   Type: Boolean.  
    Returns true if the pattern was found on the text.

PatternResult
:   Type: Text.  
    Returned value of the first element matching the pattern.

FirstIndex
:   Type: Integer.  
    Returned index of the first element matching the pattern.

### RegexValidator { #Client_RegexValidator }

Client action to validate if a given text is valid on a regex pattern.

*Inputs*

Text
:   Type: mandatory, Text.  
    Input variable with the text to be validated.

Pattern
:   Type: mandatory, Text.  
    Input variable with the regex pattern for the validation.

*Outputs*

IsValid
:   Type: Boolean.  
    Returns if the text matches the pattern.

### Resolve { #Client_Resolve }

Client action that implements the protected Resolve method that ensures the DOM is fully loaded (useful to run JavaScript on the DOM after it).

### ScrollToTop { #Client_ScrollToTop }

Client action to scroll the screen to the top.

### ShowPassword { #Client_ShowPassword }

Client action to be used on the Login screen to enable users to show or hide the password characters.

*Inputs*

InputId
:   Type: mandatory, Text.  
    Input variable with the identifier of the input html element in order to change the input type.

### StringSplit { #Client_StringSplit }

Client action that receives one string and splits it by a delimiter text into a List of Text.

*Inputs*

Str
:   Type: mandatory, Text.  
    Input variable with the string to be splitted.

Delimiters
:   Type: mandatory, Text.  
    Input variable containing all the characters that should be considered as separators.

*Outputs*

SubStrings
:   Type: Text List.  
    Returned list of text with all the splitted strings.

### ValidateEmail { #Client_ValidateEmail }

Client action to checks whether the given value is a valid e-mail.

*Inputs*

Email
:   Type: mandatory, Text.  
    Input variable with the email to be validated.

*Outputs*

IsValid
:   Type: Boolean.  
    Returns if the given email is valid or not.

### ValidatePhoneNumber { #Client_ValidatePhoneNumber }

Client action to validate a given phone number using RegEx.  
Format: XXX-XXX-XXXX

*Inputs*

PhoneNumber
:   Type: mandatory, Phone Number.  
    Input variable with the phone number to be validated.

*Outputs*

IsValid
:   Type: Boolean.  
    Returned value indicating if the given phone number is valid.


## Structures

### DeviceInfo { #Structure_DeviceInfo }

Structure to handle the device information.

*Attributes*

CordovaVersion
:   Type: Text.  
    Represents the version of Cordova running on the device.

Model
:   Type: Text.  
    Represents the name of the device's model or product.

Platform
:   Type: Text.  
    Represents the device's operating system name.  
    \- Android  
    \- BlackBerry 10  
    \- Browser  
    \- Firefox OS  
    \- iOS  
    \- Tizen  
    \- Windows Phone 7 and 8  
    \- Windows  
    \- OSX

UUID
:   Type: Text.  
    Represents the device's Universally Unique Identifier (UUID).  
    https://en.wikipedia.org/wiki/Universally_unique_identifier

Version
:   Type: Text.  
    Represents the operating system version.

Manufacturer
:   Type: Text.  
    Represents the device's manufacturer.

IsVirtual
:   Type: Boolean.  
    Indicates whether the device is running on a simulator.

Serial
:   Type: Text.  
    Represents the device hardware serial number (SERIAL).  
    https://developer.android.com/reference/android/os/Build.html#SERIAL

IsRunningAsPWA
:   Type: Boolean.  
    Indicates if the application is running as PWA.

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

Structure to handle the user information in his session.

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
