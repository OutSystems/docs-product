# ExBuilder_PluginsWrapper_MLib

Module that contains several common objects and functions used across the mobile application related with plugins. This includes wrappers for methods that we use at the components level or some methods where we added some extra logic.

## Summary

Client Action | Description
---|---
[Biometrics_IsAvailable](<#Client_Biometrics_IsAvailable>) | Client action that checks if touch ID plugin is available (also set in the keystore).
[Biometrics_Launch](<#Client_Biometrics_Launch>) | Client action to launch Native Biometrics Reader.
[Camera_ChooseGalleryPhoto](<#Client_Camera_ChooseGalleryPhoto>) | Client action to open the device's photo gallery to choose a photo.
[Camera_IsAvailable](<#Client_Camera_IsAvailable>) | Client action that validates if the camera plugin is currently available. Useful to verify if the current application has the plugin installed.
[Camera_TakePicture](<#Client_Camera_TakePicture>) | Client action to trigger the device's camera to take a picture.
[Dialog_CheckPlugin](<#Client_Dialog_CheckPlugin>) | Client action to check if plugin is available on the device.
[Dialog_ConfirmMany](<#Client_Dialog_ConfirmMany>) | Client action to call the native dialogs with more than one buttons.
[GetDistanceBetweenTwoPoints](<#Client_GetDistanceBetweenTwoPoints>) | Client action to calculate distance value between two given points.
[GetFilePath](<#Client_GetFilePath>) | Client action that returns the file transfer path for a mobile device.
[Keystore_GetValue](<#Client_Keystore_GetValue>) | Client action to get a value from device keystore according to its key.
[Keystore_IsAvailable](<#Client_Keystore_IsAvailable>) | Client action to check if keystore plugin is available on the device.
[Keystore_Remove](<#Client_Keystore_Remove>) | Client action to remove a value from device keystore according to it key.
[Keystore_SetValue](<#Client_Keystore_SetValue>) | Client action to sets a value from device keystore according to it key.
[SetCenter](<#Client_SetCenter>) | Client action that triggers the map to be centered arround the given latitude and longitude.
[SpeechRecognition_IsAvailable](<#Client_SpeechRecognition_IsAvailable>) | Client action to check whether the Speech Recognition is available or not.
[SpeechRecognition_RequestPermission](<#Client_SpeechRecognition_RequestPermission>) | Client action to request access permission to system resources if it was not granted before.
[SpeechRecognition_StartListening](<#Client_SpeechRecognition_StartListening>) | Client action to start listening.<br/>There is a difference between Android and iOS platforms. On Android speech recognition stops when the speaker finishes speaking (at end of sentence). On iOS the user has to stop manually the recognition process by calling stopListening() method.
[SpeechRecognition_StopListening](<#Client_SpeechRecognition_StopListening>) | Client action to stop listening. iOS only method. Stop the recognition process.

Structure | Description
---|---
[BiometricAuthSignature](<#Structure_BiometricAuthSignature>) | Structure used to store the users touch id configuration in keystore.
[DeviceInfo](<#Structure_DeviceInfo>) | Structure to handle the device information.
[Error](<#Structure_Error>) | Contains a code and description of a Plugin error.

## Client Actions

### Biometrics_IsAvailable { #Client_Biometrics_IsAvailable }

Client action that checks if touch ID plugin is available (also set in the keystore).

*Outputs*

IsAvailable
:   Type: Boolean.  
    Returns true if the plugin is available to use.

BiometryType
:   Type: Integer.  
    Returns the available biometry type:  
    1 - TouchID  
    2 - FaceID (iOS only)  
    -1 - no Biometry

Error
:   Type: TouchIdErrorMessage Identifier.  
    Returns the error information

### Biometrics_Launch { #Client_Biometrics_Launch }

Client action to launch Native Biometrics Reader.

*Inputs*

Title
:   Type: optional, Text.  
    (Android only) Input variable with the localized text to be displayed on the title of the modal dialog.

Message
:   Type: mandatory, Text.  
    Input variable with localized text explaining why the app needs authentication.

Hint
:   Type: optional, Text.  
    (Android only) Input variable with localized text to be displayed in the scanning result area before the fingerprint is scanned.

DisableBackup
:   Type: optional, Boolean.  
    (Android only) Input variable to disable the possibility to use a backup credential like pin, pattern or password

MaxAttempts
:   Type: optional, Integer.  
    (Android only) Input variable with maximum number of attempts before the scanning is cancelled

Locale
:   Type: optional, Text.  
    (Android only) Input variable with the locale to be used for native text field translation.  
    Supported translations are:  
    English: &quot;en_US&quot;  
    Spanish: &quot;es&quot;  
    Russian: &quot;ru&quot;  
    French: &quot;fr&quot;  
    Chinese (Simplified): &quot;zh_CN&quot;, &quot;zh_SG&quot;  
    Chinese (Traditional): &quot;zh&quot;, &quot;zh_HK&quot;, &quot;zh_TW&quot;, &quot;zh_MO&quot;  
    Norwegian: &quot;no&quot;

*Outputs*

Error
:   Type: TouchIdErrorMessage Identifier.  
    Returns the error information.

Success
:   Type: Boolean.  
    Returns true if everything goes as expected, false if there is an error.

BiometryType
:   Type: Integer.  
    Returns the available biometry type:  
    1 - TouchID  
    2 - FaceID (iOS only)  
    -1 - no Biometry

### Camera_ChooseGalleryPhoto { #Client_Camera_ChooseGalleryPhoto }

Client action to open the device's photo gallery to choose a photo.

*Outputs*

ImageCaptured
:   Type: Binary Data.  
    Returns the binary content of the image that was captured by the plugin.

Error
:   Type: [Error](<#Structure_Error>).  
    Returns additional information in case any error occurs while saving the file.

Success
:   Type: Boolean.  
    Returns true if everything goes as expected, false if there is an error.

### Camera_IsAvailable { #Client_Camera_IsAvailable }

Client action that validates if the camera plugin is currently available. Useful to verify if the current application has the plugin installed.

*Outputs*

IsAvailable
:   Type: Boolean.  
    Returns true if the plugin is available to use.

Error
:   Type: [Error](<#Structure_Error>).  
    Returns additional information in case any error occurs while saving the file.

### Camera_TakePicture { #Client_Camera_TakePicture }

Client action to trigger the device's camera to take a picture.

*Outputs*

ImageCaptured
:   Type: Binary Data.  
    Returned binary of the captured image.

Success
:   Type: Boolean.  
    Returns true if everything goes as expected, false if there is an error.

Error
:   Type: [Error](<#Structure_Error>).  
    Returns additional information in case any error occurs while saving the file.

### Dialog_CheckPlugin { #Client_Dialog_CheckPlugin }

Client action to check if plugin is available on the device.

*Outputs*

IsAvailable
:   Type: Boolean.  
    Returns true if the plugin is available to use, false otherwise

### Dialog_ConfirmMany { #Client_Dialog_ConfirmMany }

Client action to call the native dialogs with more than one buttons.

*Inputs*

Message
:   Type: mandatory, Text.  
    Input variable with the dialog message.

Title
:   Type: mandatory, Text.  
    Input variable with the dialog title.

ButtonsNames
:   Type: mandatory, Text List.  
    Input variable with the list of buttons.

*Outputs*

Success
:   Type: Boolean.  
    Returns a flag to indicate if the action was successfully executed.

ErrorMessage
:   Type: Text.  
    Returns a message with details about any error that might have occurred. Only set when Success output parameter is false.

Button
:   Type: Text.  
    Returns the name of the button selected.

### GetDistanceBetweenTwoPoints { #Client_GetDistanceBetweenTwoPoints }

Client action to calculate distance value between two given points.

*Inputs*

FromLatitude
:   Type: mandatory, Decimal.  
    Input variable with initial latitude decimal value.

FromLongitude
:   Type: mandatory, Decimal.  
    Input variable with initial longitude decimal value.

DestinationLatitude
:   Type: mandatory, Decimal.  
    Input variable with destination latitude decimal value.

DestinationLongitude
:   Type: mandatory, Decimal.  
    Input variable with destination longitude decimal value.

*Outputs*

Distance
:   Type: Decimal.  
    Returned distance (mi) between two given points.

### GetFilePath { #Client_GetFilePath }

Client action that returns the file transfer path for a mobile device.

*Outputs*

FilePathURL
:   Type: Text.  
    Returns the device's file path.

### Keystore_GetValue { #Client_Keystore_GetValue }

Client action to get a value from device keystore according to its key.

*Inputs*

KeystoreKeysId
:   Type: mandatory, KeystoreKeys Identifier.  
    Input variable with the keystore identifier.

*Outputs*

Value
:   Type: Text.  
    Returned value of given keystore.

Error
:   Type: [Error](<#Structure_Error>).  
    Returns error information, in case there is one.  
    An ErrorCode of &quot;0&quot; means that no error occured. Any other ErrorCode represents an error. See the ErrorMessage field for details.

### Keystore_IsAvailable { #Client_Keystore_IsAvailable }

Client action to check if keystore plugin is available on the device.

*Outputs*

IsAvailable
:   Type: Boolean.  
    Returns if touch id is available.

### Keystore_Remove { #Client_Keystore_Remove }

Client action to remove a value from device keystore according to it key.

*Inputs*

KeystoreKeysId
:   Type: mandatory, KeystoreKeys Identifier.  
    Input variable with the identifier of the keystore.

*Outputs*

Error
:   Type: [Error](<#Structure_Error>).  
    Returns error information, in case there is one.  
    An ErrorCode of &quot;0&quot; means that no error occured. Any other ErrorCode represents an error. See the ErrorMessage field for details.

### Keystore_SetValue { #Client_Keystore_SetValue }

Client action to sets a value from device keystore according to it key.

*Inputs*

KeystoreKeysId
:   Type: mandatory, KeystoreKeys Identifier.  
    Input variable with the identifier of the keystore.

Value
:   Type: mandatory, Text.  
    Input variable with the value to be set.

*Outputs*

Error
:   Type: [Error](<#Structure_Error>).  
    Returns error information, in case there is one.  
    An ErrorCode of &quot;0&quot; means that no error occured. Any other ErrorCode represents an error. See the ErrorMessage field for details.

### SetCenter { #Client_SetCenter }

Client action that triggers the map to be centered arround the given latitude and longitude.

*Inputs*

MapId
:   Type: mandatory, Text.  
    Input variable with the identifier of the map element.

Latitude
:   Type: mandatory, Text.  
    Input variable with latitude value to center the map.

Longitude
:   Type: mandatory, Text.  
    Input variable with longitude value to center the map.

### SpeechRecognition_IsAvailable { #Client_SpeechRecognition_IsAvailable }

Client action to check whether the Speech Recognition is available or not.

*Outputs*

IsAvailable
:   Type: Boolean.  
    Returns if the plugin is available or not.

Error
:   Type: [Error](<#Structure_Error>).  
    Returns detailed information of the error, in case there is one.

### SpeechRecognition_RequestPermission { #Client_SpeechRecognition_RequestPermission }

Client action to request access permission to system resources if it was not granted before.

*Outputs*

Success
:   Type: Boolean.  
    Returns if it was a success or not.

Error
:   Type: [Error](<#Structure_Error>).  
    Returns information of the error, in case there is one.

### SpeechRecognition_StartListening { #Client_SpeechRecognition_StartListening }

Client action to start listening.  
There is a difference between Android and iOS platforms. On Android speech recognition stops when the speaker finishes speaking (at end of sentence). On iOS the user has to stop manually the recognition process by calling stopListening() method.

*Inputs*

language
:   Type: optional, Text.  
    Input variable with used language for recognition (default &quot;en-US&quot;).

matches
:   Type: optional, Integer.  
    Input variable with the number of return matches (default 5, on iOS: maximum number of matches).

prompt
:   Type: optional, Text.  
    Input variable with the displayed prompt of listener popup window (default &quot;&quot;, Android only).

showPopup
:   Type: optional, Boolean.  
    Input variable to determine if listener popup window with prompt will be displayed (default true, Android only).

showPartial
:   Type: optional, Boolean.  
    Input variable to allow partial results to be returned (default false, iOS only).

*Outputs*

RecognizedTerms
:   Type: Text List.  
    Returns recognized terms.

Success
:   Type: Boolean.  
    Returns a flag that indicates if the scan was successful.

Error
:   Type: [Error](<#Structure_Error>).  
    Returns an error if the barcode scan was not successful.

### SpeechRecognition_StopListening { #Client_SpeechRecognition_StopListening }

Client action to stop listening. iOS only method. Stop the recognition process.

*Outputs*

Success
:   Type: Boolean.  
    Returns a flag that indicates if the scan was successful.

Error
:   Type: [Error](<#Structure_Error>).  
    Returns an error if the barcode scan was not successful.


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

### DeviceInfo { #Structure_DeviceInfo }

Structure to handle the device information.

*Attributes*

CordovaVersion
:   Type: Text.  
    Represents the version of Cordova running on the device.

Model
:   Type: Text.  
    Returns the name of the device's model or product.

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

### Error { #Structure_Error }

Contains a code and description of a Plugin error.

*Attributes*

ErrorCode
:   Type: Text.  
    

ErrorMessage
:   Type: Text.  
    