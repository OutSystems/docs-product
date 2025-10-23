---
summary: Explore the KeyStore Plugin functionalities in OutSystems 11 (O11), including client actions, and error handling.
locale: en-us
guid: 962724cd-01a8-4655-b8bf-9a0147387e77
app_type: mobile apps
platform-version: o11
figma:
coverage-type:
  - remember
tags: keystore plugin, error handling, client actions, outsystems 11, mobile apps
audience:
  - mobile developers
outsystems-tools:
  - none
---
# KeyStore Plugin reference

## Client Actions

### CheckKeyStorePlugin

Verifies if the KeyStore Plugin is available or properly installed in the application.

| Parameter|Type|Data Type|Description |
| -|-|-|- |
| IsAvailable|Output|Boolean|Indicates if the plugin is available ('True') or not ('False'). |
| Error|Output|Error|Displays detailed information of an error, if applicable. |

### GetValue

Returns the value from the store, associated with the given key .

| Parameter|Type|Data Type|Description |
| -|-|-|- |
| Store|Input|Text|The name of the store where to set the value. |
| Key|Input|Text|The key that identifies the desired value. |
| Value|Output|Text|The value associated to the key in the store. |
| Success|Output|Boolean|Indicates if the action was successful ('True') or not ('False'). |
| Error|Output|Error|Displays detailed information of an error, if applicable. |

### SetValue

Creates or updates a key-value pair in the store.

| Parameter|Type|Data Type|Description |
| -|-|-|- |
| Store|Input|Text|The name of the store where to set the value. |
| Key|Input|Text|The key that will identify the value. |
| Value|Input|Text|The value to be set. |
| KeyAuthentication|Input|Boolean|The authentication value for a specific key-value pair. By default, no authentication is required to access the pair ('False'). If ('True'), the access to the pair will require an authentication method. |
| Success|Output|Boolean|Indicates if the action was successful ('True') or not ('False'). |
| Error|Output|Error|Displays detailed information of an error, if applicable. |

### RemoveKey

Removes the key-value pair from the store.

| Parameter|Type|Data Type|Description |
| -|-|-|- |
| Store|Input|Text|The name of the store that contains the key to be removed. |
| Key|Input|Text|The key to be removed. |
| Success|Output|Boolean|Indicates if the action was successful ('True') or not ('False'). |
| Error|Output|Error|Displays detailed information of an error, if applicable. |

## Error Codes

| Code|Platform|Message |
| -|-|- |
| OS-PLUG-KSTR-0001|iOS|Some of the arguments are not valid. |
| OS-PLUG-KSTR-0002|iOS|Function or operation not implemented. |
| OS-PLUG-KSTR-0003|iOS|One or more parameters passed to a function are not valid. |
| OS-PLUG-KSTR-0004|iOS|Failed to allocate memory. |
| OS-PLUG-KSTR-0005|iOS|No Keychain is available. A restart may be needed. |
| OS-PLUG-KSTR-0006|iOS|The specified item already exists in the Keychain. |
| OS-PLUG-KSTR-0007|iOS|The specified item could not be found in the Keychain. |
| OS-PLUG-KSTR-0008|iOS|User interaction is currently not allowed. |
| OS-PLUG-KSTR-0009|iOS|Unable to decode the provided data. |
| OS-PLUG-KSTR-0010|iOS|The user name or passphrase you entered is not correct. |
| OS-PLUG-KSTR-0011|iOS|An error just occurred. |
| OS-PLUG-KSTR-00012|Android|Key does not exist. |
| OS-PLUG-KSTR-0013|Android|Failed to authenticate user. |
| OS-PLUG-KSTR-0014|Android|Device is not secure. |
| OS-PLUG-KSTR-0015|Android|There was an error accessing the KeyStore. |
| OS-PLUG-KSTR-0016|Web|Cordova is not defined. |
| OS-PLUG-KSTR-0017|iOS, Android|Key Store Plugin is unavailable. |
| OS-PLUG-KSTR-0018|Web|Not running on device. Will fallback to browser local storage but unencrypted. |
