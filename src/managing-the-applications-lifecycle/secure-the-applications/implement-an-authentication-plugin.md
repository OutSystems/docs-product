---
summary: Learn the requirements an external authentication plugin must implement.
---

# Implement an Authentication Plugin

OutSystems allows you to authenticate IT users (developers, testers operations), using an external authentication provider. It can be done by using or developing an authentication plugin and assigning it as the authentication provider on the platform. This page contains the requirements an external authentication plugin must implement.

## SOAP Web Service Name

An authentication plugin is a module that exposes a SOAP web service. This web service is invoked by OutSystems when activating the plugin and when authenticating users.

The SOAP web service needs to be called 'OSPlatformAuthentication'.

## SOAP Web Service Methods

The 'OSPlatformAuthentication' SOAP web service needs to expose the following methods.  


Name     | Description
---------|------------
[Plugin_GetAllConfigurations](<#plugin_getallconfigurations>)() | Method invoked synchronously to get all configurations needed by the plugin and their current values.
[Plugin_GetCapabilities](<#plugin_getcapabilities>)() | Method invoked synchronously when the platform is changed to use this plugin for authentication. You should use this method to return the capabilities of your plugin.
[Plugin_OnActivation](<#plugin_onactivation>)() | Called synchronously when the OutSystems authentication method is changed to use this plugin for authentication. As an example, you can use this method to execute your tests and validate the plugin.
[Plugin_OnDeactivation](<#plugin_ondeactivation>)() |Method invoked synchronously when the OutSystems authentication method is changed to stop using this plugin for authentication. As an example, you can use this method to disable your users from the platform.
[Plugin_SetConfigurations](<#plugin_setconfigurations>)() | This method is executed synchronously to update the plugin configuration when changing its configurations in the infrastructure management console (LifeTime).
[Plugin_Test](<#plugin_test>)() | Called synchronously when the IT user tests if the plugin is working correctly in the platform. As an example, you can use this method to check if your plugin is valid.
[User_AuthenticateWithCredentials](<#user_authenticatewithcredentials>)(Text, Text) | Executed synchronously when the platform authenticates a username and password against the external system. As an example, you can use this method to validate a user in the Active Directory.
[User_AuthenticateWithUsername](<#user_authenticatewithusername>)(Text) | Method invoked synchronously when the platform authenticates a username against the external system. As an example, you can use this method to validate a user with Integrated Authentication.

## Plugin_GetAllConfigurations

Method invoked synchronously to get all configurations needed by the plugin and their current values.

### Inputs

None.

### Outputs  

Name | Type | Description
---------|----------|---------
 Configuration | [PluginAPIConfigurationParameter](#pluginapiconfigurationparameter) Record List | The list of plugin configuration properties and their values.
 Status | [PluginAPIStatus](#pluginapistatus) | The status of invoking this action. It contains the success value and the response information of the action.


## Plugin_GetCapabilities

Method invoked synchronously when the platform is changed to use this plugin for authentication. You should use this method to return the capabilities of your plugin.

### Inputs

None.

### Outputs  

Name | Type | Description
---------|----------|---------
 SupportedCapabilities | [Capability](#capability) Record List | The list of supported capabilities.
 Status | [PluginAPIStatus](#pluginapistatus) | The status of invoking this action. It contains the success value and the response information of the action.

## Plugin_OnActivation

Called synchronously when the OutSystems authentication method is changed to use this plugin for authentication. As an example, you can use this method to execute your tests and validate the plugin.

### Inputs

None.

### Outputs  

Name | Type | Description
-----|------|------------
Status | [PluginAPIStatus](#pluginapistatus) | The status of invoking this action. It contains the success value and the response information of the action.

## Plugin_OnDeactivation

Method invoked synchronously when the OutSystems authentication method is changed to stop using this plugin for authentication. As an example, you can use this method to disable your users from the platform.

### Inputs

None.

### Outputs

None.




## Plugin_SetConfigurations

This method is executed synchronously to update the plugin configuration when changing its configurations in the infrastructure management console (LifeTime). This method is only invoked if the plugin has the 'ConfigurationAPI.Supported' capability value set to 'True'.

Implementations should validate whether configurations are valid (e.g. values match data types; mandatory setting have values defined) and signal the status of the operation accordingly.


### Inputs

Name | Type | Description
---------|----------|---------
Configuration | [PluginAPIConfigurationParameter](#pluginapiconfigurationparameter) Record List | The list of plugin configuration properties to update and their new values.

### Outputs  

Name | Type | Description
---------|----------|---------
Status | [PluginAPIStatus](#pluginapistatus) | The status of invoking this action. It contains the success value and the response information of the action.


## Plugin_Test

Called synchronously when the IT user tests if the plugin is working correctly in the platform. As an example, you can use this method to check if your plugin is valid.

### Inputs

None.

### Outputs  
 
Name | Type | Description
-----|------|-------------
Status | [PluginAPIStatus](#pluginapistatus) | The status of invoking this action. It contains the success value and the response information of the action.

## User_AuthenticateWithCredentials

Executed synchronously when the platform authenticates a username and password against the external system. As an example, you can use this method to validate a user in the Active Directory.

### Inputs  
  
Name | Type | Description
-----|------|------------
Username | Text | The username of the user to authenticate.
Password | Text | The password of the user to authenticate.

### Outputs  
  
Name | Type | Description
-----|------|------------
UserId | User Identifier | The OutSystems user identifier.
Status | [PluginAPIStatus](#pluginapistatus) | The status of invoking this action. It contains the success value and the response information of the action.

## User_AuthenticateWithUsername

Method invoked synchronously when the platform authenticates a username against the external system. As an example, you can use this method to validate a user with Integrated Authentication.

### Inputs  
  
Name | Type | Description
-----|------|------------
Username | Text | The username of the user to authenticate.

### Outputs  

Name | Type | Description
-----|------|------------
UserId | User Identifier | The OutSystems user identifier.
Status | [PluginAPIStatus](#pluginapistatus) | The status of invoking this action. It contains the success value and the response information of the action.

## Structures

Below are the structures the plugin needs to have.

### PluginAPIStatus  

Name | Type | Description
-----|------|------------
Success | Boolean | True if the operation was successful, False otherwise.
ResponseId | Integer | The response code.
ResponseMessage | Text | The response message.
ResponseAdditionalInfo | Text | The response detailed message.

You can customize the values for the ResponseId, ResponseMessage, and ResponseAdditionalInfo attributes since these attributes are only used to generate logs.

### Capability  

Name | Type | Description
-----|------|------------
Name | Text | The name of the capability.
Value | Text | The value of the capability.

__Supported Values__

Your plugin can expose specific values for the following capabilities (if a capability is not specified, the default value will be 'False'):

Name | Possible Values | Description
-----|------|----
'UserPassword.Supported' | 'True' or 'False' | Indicates if the plugin supports user credentials validation (i.e. it implements the [User_AuthenticateWithCredentials](<#user_authenticatewithcredentials>) method).
'IntegratedAuthentication.Supported' | 'True' or 'False' | Indicates if the plugin supports authentication through a username (i.e. if it implements the [User_AuthenticateWithUsername](<#user_authenticatewithusername>) method).
'ConfigurationAPI.Supported' | 'True' or 'False' | Indicates if the plugin supports the configuration API methods ([Plugin_GetAllConfigurations](<#plugin_getallconfigurations>) and [Plugin_SetConfigurations](<#plugin_setconfigurations>)).
'Cloud.Supported' | 'True' or 'False' | Indicates if the plugin is supported in OutSystems Cloud.

### PluginAPIConfigurationParameter  

Name | Type | Description
-----|------|------------
Name | Text | Name of the configuration parameter.
Value | Text | Value of the parameter.
