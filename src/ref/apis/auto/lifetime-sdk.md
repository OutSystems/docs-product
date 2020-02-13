# LifeTime SDK

For version 10.0.902.100. Core layout components and APIs used by LifeTime and its plugins.

## Summary

Widget | Description
---|---
[Internal_Layout_LifeTime](<#Internal_Layout_LifeTime>) | The LifeTime layout.
[Internal_Layout_Popup](<#Internal_Layout_Popup>) | The Popup Layout to be used in a LifeTime plugin. Pressing the popup buttons triggers the OnNotify action containing a LayoutPopupButtonClicked identifier.
[Layout_LifeTimeSDK](<#Layout_LifeTimeSDK>) | The Web Block to be used as the base layout for a LifeTime plugin. The layout allows you to easily create screens with the look and feel of LifeTime, since it contains LifeTime header and footer.%%%%The layout also contains a stamp for you to customize with the developer or company name, when you register the plugin.

Action | Description
---|---
[Application_Get](<#Application_Get>) | Returns the information of an application in an environment.%%If the environment is not specified, information of the application across all infrastructure is returned.
[Application_List](<#Application_List>) | Returns a list of the applications in the specified environment that are visible within LifeTime, with their information, such as name, description, url. If no environment is specified, information of all visible applications across all environments is returned.
[ApplicationVersion_Get](<#ApplicationVersion_Get>) | Returns information of an application on a specified date.
[ApplicationVersion_List](<#ApplicationVersion_List>) | Returns the information of all tagged application versions for the specified application.
[Deployment_Get](<#Deployment_Get>) | Returns information of the specified deployment.
[Deployment_List](<#Deployment_List>) | Returns information of all deployments made between two environments.
[Environment_Get](<#Environment_Get>) | Returns the information of an environment, such as name, version of the Platform, Application Server.
[Environment_List](<#Environment_List>) | Returns a list of environments with their information, such as name, version of the Platform, Application Server.
[GetUserSessionToken](<#GetUserSessionToken>) | Returns an authentication token that is valid for 5 minutes, for the session user.
[ModuleVersion_Get](<#ModuleVersion_Get>) | Returns the information of a module version for the specified module and version.
[ModuleVersion_List](<#ModuleVersion_List>) | Returns the information of all module versions for the specified module.
[Plugin_Register](<#Plugin_Register>) | Registers the caller eSpace as a LifeTime plugin: in the LifeTime 'More' menu a new link is created with the specified name that redirects to the entry point provided, or the default entry point if none is provided. All web screens of the plugin are displayed with their owner name.%%Each eSpace can only register a single plugin.%%
[Plugin_Unregister](<#Plugin_Unregister>) | Unregisters the caller eSpace as a LifeTime plugin: in the LifeTime 'More' menu there is no longer a link to the plugin.
[Security_CheckApplicationPermission](<#Security_CheckApplicationPermission>) | Checks if a user has a permission for a specific application running on an environment.%%If no user is specified, the current user is used.
[Security_CheckEnvironmentPermission](<#Security_CheckEnvironmentPermission>) | Checks if a user has a permission for a specific environment. If no user is specified, the current user is used.
[Security_CheckInfrastructurePermission](<#Security_CheckInfrastructurePermission>) | Checks if a user has the 'Configure Infrastructure' permission. If no user is specified, the current user is used.
[Security_GetApplicationsPermissions](<#Security_GetApplicationsPermissions>) | Returns the permissions the specified user has for each application in the environment. If no user is specified, the current user is used.
[Security_GetEnvironmentsPermissions](<#Security_GetEnvironmentsPermissions>) | Returns the permissions the specified user has for each environment. If no user is specified, the current user is used.
[SetLoginRedirectURL](<#SetLoginRedirectURL>) | 

Structure | Description
---|---
[ApplicationInfo](<#Structure_ApplicationInfo>) | Application details and environment specific information where the application is running.
[ApplicationVersionInfo](<#Structure_ApplicationVersionInfo>) | Information of a specific version of an application, and the versions of its modules.
[DeploymentInfo](<#Structure_DeploymentInfo>) | Deployment information with the operations executed.
[DeploymentMessage](<#Structure_DeploymentMessage>) | Message from a deployment operation log.
[DeploymentOperationInfo](<#Structure_DeploymentOperationInfo>) | A deployment operation as specified in the deployment plan.
[EnvironmentApplicationInfo](<#Structure_EnvironmentApplicationInfo>) | Application information for a specific environment.
[EnvironmentApplicationPermission](<#Structure_EnvironmentApplicationPermission>) | A user's permission to an application in an environment.
[EnvironmentInfo](<#Structure_EnvironmentInfo>) | An environment and its information.
[EnvironmentModuleInfo](<#Structure_EnvironmentModuleInfo>) | Information of a module in a specific environment.
[EnvironmentPermission](<#Structure_EnvironmentPermission>) | A user's permission to an environment.
[ModuleInfo](<#Structure_ModuleInfo>) | Module information and the status in the environments where the modules are running.
[ModuleVersionInfo](<#Structure_ModuleVersionInfo>) | Information about a module version.

Static Entity | Description
---|---
[ApplicationPermissionLevel](<#StaticEntity_ApplicationPermissionLevel>) | Permission level that a user has over an application.
[DeploymentMessageType](<#StaticEntity_DeploymentMessageType>) | The type of a deployment message.
[DeploymentOperationType](<#StaticEntity_DeploymentOperationType>) | The type of a deployment operation.
[DeploymentStatus](<#StaticEntity_DeploymentStatus>) | The status of a deployment operation.
[DialogBoxIcon](<#StaticEntity_DialogBoxIcon>) | Internal only. Icon of a Dialog Box.
[ElementType](<#StaticEntity_ElementType>) | The types of elements a module references or exposes as public.
[EnvironmentPermissionLevel](<#StaticEntity_EnvironmentPermissionLevel>) | Permission level that a user has over an epplication.
[LayoutPopupButtonClicked](<#StaticEntity_LayoutPopupButtonClicked>) | The message of an OnNotify action when a button is pressed in a popup.

## Widgets

### Internal_Layout_LifeTime { #Internal_Layout_LifeTime }

The LifeTime layout.

*Inputs*

HelpURL
:   Type: optional, Text.  
    

ForceFixedContentOnTop
:   Type: optional, Boolean.  
    

### Internal_Layout_Popup { #Internal_Layout_Popup }

The Popup Layout to be used in a LifeTime plugin. Pressing the popup buttons triggers the OnNotify action containing a LayoutPopupButtonClicked identifier.

*Inputs*

Title
:   Type: mandatory, Text.  
    The Title of the Popup.

Subtitle
:   Type: optional, Text.  
    The Subtitle of the Popup.

ConfirmButtonLabel
:   Type: optional, Text.  
    The label of the confirmation button.

CancelButtonLabel
:   Type: optional, Text.  
    The label of the cancel button.

HideConfirmButton
:   Type: optional, Boolean.  
    If True, the confirmation button is hidden.

HideCancelButton
:   Type: optional, Boolean.  
    If True, the cancel button is hidden.

AlignTitleToCenter
:   Type: optional, Boolean.  
    If True, the Title is aligned to the center of the popup.

IgnoreNotifyOnCancel
:   Type: optional, Boolean.  
    If True, pressing the cancel button does not trigger the OnNotify action.

WrapTitle
:   Type: optional, Boolean.  
    If True, the Title is wrapped.

HideScrollbars
:   Type: optional, Boolean.  
    If True, no scrollbars are shown when necessary.

JustifyContent
:   Type: optional, Boolean.  
    If True, the content of the popup is justified.

Icon
:   Type: optional, DialogBoxIcon Identifier.  
    The icon to appear in the Popup.

### Layout_LifeTimeSDK { #Layout_LifeTimeSDK }

The Web Block to be used as the base layout for a LifeTime plugin. The layout allows you to easily create screens with the look and feel of LifeTime, since it contains LifeTime header and footer.  
  
The layout also contains a stamp for you to customize with the developer or company name, when you register the plugin.


## Actions

### Application_Get { #Application_Get }

Returns the information of an application in an environment.  
If the environment is not specified, information of the application across all infrastructure is returned.

*Inputs*

ApplicationKey
:   Type: mandatory, Text.  
    The application unique identifier.

EnvironmentKey
:   Type: optional, Text.  
    The environment unique identifier. If the environment is not specified, information of the application across all infrastructure is returned.

IncludeModules
:   Type: mandatory, Boolean.  
    True returns information about the modules of the application, false only returns information of the application.

*Outputs*

Application
:   Type: [ApplicationInfo](<#Structure_ApplicationInfo>).  
    Application with its information, such as name, description, url.

Modules
:   Type: [ModuleInfo](<#Structure_ModuleInfo>) List.  
    List of modules with their information, such as name, description, status.

### Application_List { #Application_List }

Returns a list of the applications in the specified environment that are visible within LifeTime, with their information, such as name, description, url. If no environment is specified, information of all visible applications across all environments is returned.

*Inputs*

EnvironmentKey
:   Type: optional, Text.  
    The environment unique identifier. If no environment is specified, information of all visible applications across all environments is returned.

IncludeHiddenApplications
:   Type: optional, Boolean.  
    If set to True, the result includes applications that are not visible within LifeTime.

*Outputs*

Applications
:   Type: [ApplicationInfo](<#Structure_ApplicationInfo>) List.  
    List of applications with their information, such as name, description, url.

### ApplicationVersion_Get { #ApplicationVersion_Get }

Returns information of an application on a specified date.

*Inputs*

ApplicationKey
:   Type: mandatory, Text.  
    The application unique identifier.

Version
:   Type: mandatory, Text.  
    The version number.

*Outputs*

ApplicationVersion
:   Type: [ApplicationVersionInfo](<#Structure_ApplicationVersionInfo>).  
    Application with its information, such as version, description and modules.

### ApplicationVersion_List { #ApplicationVersion_List }

Returns the information of all tagged application versions for the specified application.

*Inputs*

ApplicationKey
:   Type: mandatory, Text.  
    The application unique identifier.

CreatedOnEnvironmentKey
:   Type: optional, Text.  
    The environment unique identifier from where the versions are to be retrieved. If the environment is not specified, information of the application versions across all infrastructure is returned.

*Outputs*

ApplicationVersions
:   Type: [ApplicationVersionInfo](<#Structure_ApplicationVersionInfo>) List.  
    List of application versions with their information, such as version, description and its modules.

### Deployment_Get { #Deployment_Get }

Returns information of the specified deployment.

*Inputs*

DeploymentKey
:   Type: mandatory, Text.  
    The deployment unique identifier.

IncludeLog
:   Type: mandatory, Boolean.  
    If true, returns the deployment log information.

*Outputs*

Deployment
:   Type: [DeploymentInfo](<#Structure_DeploymentInfo>).  
    The deployment with its information, such as source environment, target environment, and operations executed.

DeploymentLog
:   Type: [DeploymentMessage](<#Structure_DeploymentMessage>) List.  
    The log of the operations executed during the deployment.

### Deployment_List { #Deployment_List }

Returns information of all deployments made between two environments.

*Inputs*

SourceEnvironmentKey
:   Type: optional, Text.  
    The environment unique identifier. If not specified, returns deployments from all environments.

TargetEnvironmentKey
:   Type: optional, Text.  
    The environment unique identifier. If not specified, returns deployments to all environments.

DeploymentStatus
:   Type: optional, DeploymentStatus Identifier.  
    The deployment status. If not specified, returns deployments finished with any status.

IgnoreUnchangedApplications
:   Type: mandatory, Boolean.  
    If true, ignores the applications that were not changed in the deployments.

*Outputs*

Deployments
:   Type: [DeploymentInfo](<#Structure_DeploymentInfo>) List.  
    The list of deployments with their information, such as source environment, target environment, and operations executed.

### Environment_Get { #Environment_Get }

Returns the information of an environment, such as name, version of the Platform, Application Server.

*Inputs*

EnvironmentKey
:   Type: mandatory, Text.  
    The environment unique identifier.

*Outputs*

Environment
:   Type: [EnvironmentInfo](<#Structure_EnvironmentInfo>).  
    Information of an environment, such as name, version of the Platform, Application Server.

### Environment_List { #Environment_List }

Returns a list of environments with their information, such as name, version of the Platform, Application Server.

*Outputs*

Environments
:   Type: [EnvironmentInfo](<#Structure_EnvironmentInfo>) List.  
    List of environments with their information, such as name, version of the Platform, Application Server...

### GetUserSessionToken { #GetUserSessionToken }

Returns an authentication token that is valid for 5 minutes, for the session user.

*Inputs*

Username
:   Type: mandatory, Text.  
    A LifeTime username.

*Outputs*

Token
:   Type: Text.  
    A session token. This token expires 5 minutes after it has been created.

ResponseMessage
:   Type: Text.  
    A human readable message that explains why the call to the API failed.

ResponseAdditionalInfo
:   Type: Text.  
    More information about why the call to the API failed.

### ModuleVersion_Get { #ModuleVersion_Get }

Returns the information of a module version for the specified module and version.

*Inputs*

ModuleKey
:   Type: mandatory, Text.  
    The module unique identifier.

ModuleVersionKey
:   Type: mandatory, Text.  
    The module version unique identifier.

*Outputs*

ModuleVersion
:   Type: [ModuleVersionInfo](<#Structure_ModuleVersionInfo>).  
    Module version with its information, such as key, when it was created and by whom.

### ModuleVersion_List { #ModuleVersion_List }

Returns the information of all module versions for the specified module.

*Inputs*

ModuleKey
:   Type: mandatory, Text.  
    The module unique identifier.

*Outputs*

ModuleVersions
:   Type: [ModuleVersionInfo](<#Structure_ModuleVersionInfo>) List.  
    List of module versions with their information, such as key, when it was created and by whom.

### Plugin_Register { #Plugin_Register }

Registers the caller eSpace as a LifeTime plugin: in the LifeTime 'More' menu a new link is created with the specified name that redirects to the entry point provided, or the default entry point if none is provided. All web screens of the plugin are displayed with their owner name.  
Each eSpace can only register a single plugin.  


*Inputs*

PluginName
:   Type: mandatory, Text.  
    The name of the plugin. The name provided will be displayed in LifeTime 'More' menu.

EntryPointName
:   Type: optional, Text.  
    The entry point to use when clicking the link created in Lifetime 'More' menu. If no entry point is provided, the default is used.

DeveloperName
:   Type: optional, Text.  
    The developers of the plugin. The name is displayed in all web screens of the plugin.

### Plugin_Unregister { #Plugin_Unregister }

Unregisters the caller eSpace as a LifeTime plugin: in the LifeTime 'More' menu there is no longer a link to the plugin.

### Security_CheckApplicationPermission { #Security_CheckApplicationPermission }

Checks if a user has a permission for a specific application running on an environment.  
If no user is specified, the current user is used.

*Inputs*

UserId
:   Type: optional, User Identifier.  
    The user to check permissions for. If no user is specified, the current user is used instead.

RequiredPermissionLevel
:   Type: mandatory, ApplicationPermissionLevel Identifier.  
    The permission level to check for.

EnvironmentKey
:   Type: mandatory, Text.  
    The environment unique identifier.

ApplicationKey
:   Type: mandatory, Text.  
    The application unique identifier.

*Outputs*

HasPermission
:   Type: Boolean.  
    True if the user has the specified permission, false otherwise.

### Security_CheckEnvironmentPermission { #Security_CheckEnvironmentPermission }

Checks if a user has a permission for a specific environment. If no user is specified, the current user is used.

*Inputs*

UserId
:   Type: optional, User Identifier.  
    The user to check permissions for. Defaults to the logged in user if not specified.

RequiredPermissionLevel
:   Type: mandatory, EnvironmentPermissionLevel Identifier.  
    The permission level to check for.

EnvironmentKey
:   Type: mandatory, Text.  
    The environment unique identifier.

*Outputs*

HasPermission
:   Type: Boolean.  
    True if the user has the requested permission, false otherwise.

### Security_CheckInfrastructurePermission { #Security_CheckInfrastructurePermission }

Checks if a user has the 'Configure Infrastructure' permission. If no user is specified, the current user is used.

*Inputs*

UserId
:   Type: optional, User Identifier.  
    The user to check permissions for. If no user is specified, the current user is used instead.

*Outputs*

HasPermission
:   Type: Boolean.  
    True if the user has the requested permission, false otherwise.

### Security_GetApplicationsPermissions { #Security_GetApplicationsPermissions }

Returns the permissions the specified user has for each application in the environment. If no user is specified, the current user is used.

*Inputs*

UserId
:   Type: optional, User Identifier.  
    The user to check permissions for. If no user is specified, the current user is used instead.

EnvironmentKey
:   Type: mandatory, Text.  
    The environment unique identifier.

*Outputs*

EnvironmentApplicationsPermissions
:   Type: [EnvironmentApplicationPermission](<#Structure_EnvironmentApplicationPermission>) List.  
    List of the application permissions for each application in the environment.

### Security_GetEnvironmentsPermissions { #Security_GetEnvironmentsPermissions }

Returns the permissions the specified user has for each environment. If no user is specified, the current user is used.

*Inputs*

UserId
:   Type: optional, User Identifier.  
    The user to check permissions for. If no user is specified, the current user is used instead.

*Outputs*

EnvironmentsPermissions
:   Type: [EnvironmentPermission](<#Structure_EnvironmentPermission>) List.  
    List of the permissions for each environment.

### SetLoginRedirectURL { #SetLoginRedirectURL }



*Inputs*

URL
:   Type: mandatory, Text.  
    


## Structures

### ApplicationInfo { #Structure_ApplicationInfo }

Application details and environment specific information where the application is running.

*Attributes*

Key
:   Type: Text (50).  
    Application unique identifier.

Name
:   Type: Text (50).  
    Name of the application.

Description
:   Type: Text (50).  
    Description of the application.

URLPath
:   Type: Text (50).  
    Relative URL path of the application, starting from the hostname.

IconHash
:   Type: Text (50).  
    Hash of the application icon. Can be used to detect changes in the application icon.

IconURL
:   Type: Text (50).  
    The URL for the application icon.

StatusInEnvironments
:   Type: [EnvironmentApplicationInfo](<#Structure_EnvironmentApplicationInfo>) List.  
    Information about the status of the application in each environment it is running.

IsSystem
:   Type: Boolean.  
    Indicates if the application is a built-in component of the AgilePlatform (e.g. ServiceCenter, LifeTime, ...).

IsHidden
:   Type: Boolean.  
    Indicates if the application is not visible within LifeTime.

ApplicationKindId
:   Type: RuntimeKind Identifier.  
    

### ApplicationVersionInfo { #Structure_ApplicationVersionInfo }

Information of a specific version of an application, and the versions of its modules.

*Attributes*

Version
:   Type: Text (50).  
    Version of the application.

Description
:   Type: Text (50).  
    Description of the version.

CreatedOnEnvironmentKey
:   Type: Text (50).  
    Environment unique identifier of the environment where the application was created.

CreatedOn
:   Type: Date Time.  
    Date and time of the application creation.

CreatedBy
:   Type: Text (50).  
    Username of the user that created the application version.

ModuleVersions
:   Type: [ModuleVersionInfo](<#Structure_ModuleVersionInfo>) List.  
    List of module versions that make the application version.

### DeploymentInfo { #Structure_DeploymentInfo }

Deployment information with the operations executed.

*Attributes*

Key
:   Type: Text (50).  
    Deployment unique identifier.

SourceEnvironmentKey
:   Type: Text (50).  
    Source environment unique identifier.

TargetEnvironmentKey
:   Type: Text (50).  
    Target environment unique identifier.

Notes
:   Type: Text (50).  
    Deployment notes.

TwoStepMode
:   Type: Boolean.  
    True if the deployment was executed in two stages, false otherwise.

DeploymentStatusId
:   Type: DeploymentStatus Identifier.  
    Deployment status identifier.

CreatedOn
:   Type: Date Time.  
    Date and time when the deployment plan was created.

CreatedBy
:   Type: Text (50).  
    Username of the user that created deployment plan.

SavedOn
:   Type: Date Time.  
    The date and time when the deployment plan was saved.

StartedOn
:   Type: Date Time.  
    The date and time when the deployment started.

StartedBy
:   Type: Text (50).  
    Username of the user that started the deployment.

NeedsUserIntervention
:   Type: Boolean.  
    True if the deployment needs the user intervention to proceed, false otherwise.

DeploymentFinishedOn
:   Type: Date Time.  
    Date and time when the deployment was completed.

SyncFinishedOn
:   Type: Date Time.  
    Date and time when the synchronization between the target environment and LifeTime was completed.

Operations
:   Type: [DeploymentOperationInfo](<#Structure_DeploymentOperationInfo>) List.  
    List of operations to execute, as specified in the deployment plan.

### DeploymentMessage { #Structure_DeploymentMessage }

Message from a deployment operation log.

*Attributes*

Instant
:   Type: Date Time.  
    Date and time when the message was logged.

Message
:   Type: Text (50).  
    Content of the message. Can be used to group messages.

Detail
:   Type: Text (50).  
    Details of the message.

DeploymentMessageTypeId
:   Type: DeploymentMessageType Identifier.  
    Type of the message. Can be used to identify errors, warnings and other events.

### DeploymentOperationInfo { #Structure_DeploymentOperationInfo }

A deployment operation as specified in the deployment plan.

*Attributes*

ApplicationKey
:   Type: Text (50).  
    Application unique identifier.

SourceApplicationVersion
:   Type: Text (50).  
    Application version in the source environment.

TargetApplicationVersion
:   Type: Text (50).  
    Application version in the target environment.

DeploymentOperationTypeId
:   Type: DeploymentOperationType Identifier.  
    Type of operation to execute, as specified in the deployment plan.

### EnvironmentApplicationInfo { #Structure_EnvironmentApplicationInfo }

Application information for a specific environment.

*Attributes*

EnvironmentKey
:   Type: Text (50).  
    Environment unique identifier.

ExistsInEnvironment
:   Type: Boolean.  
    True if the application exists in the environment, false otherwise.

Version
:   Type: Text (50).  
    Version of the application.

IsModified
:   Type: Boolean.  
    True if the application has been changed since the last tag, false otherwise.

LastPublishedOn
:   Type: Date Time.  
    Date and time of the last publication.

LastPublishedBy
:   Type: Text (50).  
    Username of user that performed the last publication.

### EnvironmentApplicationPermission { #Structure_EnvironmentApplicationPermission }

A user's permission to an application in an environment.

*Attributes*

ApplicationKey
:   Type: Text (50).  
    Application unique identifier.

ApplicationPermissionLevelId
:   Type: ApplicationPermissionLevel Identifier.  
    Application Permission Level identifier.

### EnvironmentInfo { #Structure_EnvironmentInfo }

An environment and its information.

*Attributes*

Key
:   Type: Text (50).  
    Environment unique identifier.

Name
:   Type: Text (50).  
    Name of the environment.

Version
:   Type: Text (50).  
    Platform Server version. [X.X.X.X]

Order
:   Type: Integer.  
    The order of the environment as displayed in Lifetime.

HostName
:   Type: Text (50).  
    Hostname of the environment.

UseHTTPS
:   Type: Boolean.  
    Indicates if connections to the environment are made using HTTPS.

InProductionMode
:   Type: Boolean.  
    Indicates if the environment is running in production mode.

NumberOfFrontEnds
:   Type: Integer.  
    Number of front-end servers in the environment.

ApplicationServerType
:   Type: Text (50).  
    Stack of the application server.

ApplicationServer
:   Type: Text (50).  
    Type of application server. [IIS | JBoss | WebLogic]

DatabaseProvider
:   Type: Text (50).  
    Type of database provider. [SqlServer | Oracle]

IsCloudEnvironment
:   Type: Boolean.  
    Indicates if the environment is running on a cloud service.

### EnvironmentModuleInfo { #Structure_EnvironmentModuleInfo }

Information of a module in a specific environment.

*Attributes*

EnvironmentKey
:   Type: Text (50).  
    Environment unique identifier.

ExistsInEnvironment
:   Type: Boolean.  
    True if the module exists in the environment, false otherwise.

PublishedOn
:   Type: Date Time.  
    Date and time of the publication.

PublishedBy
:   Type: Text (50).  
    Username of the user that published the module.

Status
:   Type: Text (50).  
    Status of the module. Is empty if the module is working correctly, and returns ‘Warning’ if the module has outdated references, or ‘Error’ if the module uses broken references.

StatusMessage
:   Type: Text (50).  
    Verbose status messages. associated with the module, one message per line of text.

ModuleVersionInfoKey
:   Type: Text (50).  
    Module version unique identifier.

### EnvironmentPermission { #Structure_EnvironmentPermission }

A user's permission to an environment.

*Attributes*

EnvironmentKey
:   Type: Text (50).  
    Environment unique identifier.

EnvironmentPermissionLevelId
:   Type: EnvironmentPermissionLevel Identifier.  
    Environment Permission Level identifier.

### ModuleInfo { #Structure_ModuleInfo }

Module information and the status in the environments where the modules are running.

*Attributes*

Key
:   Type: Text (50).  
    Module unique identifier.

Name
:   Type: Text (50).  
    Name of the module.

Kind
:   Type: Text (50).  
    Module type (eSpace or Extension).

Description
:   Type: Text (50).  
    Description of the module.

StatusInEnvironments
:   Type: [EnvironmentModuleInfo](<#Structure_EnvironmentModuleInfo>) List.  
    Status of the module for each environment where the application is running.

### ModuleVersionInfo { #Structure_ModuleVersionInfo }

Information about a module version.

*Attributes*

Key
:   Type: Text (50).  
    Module version unique identifier.

ComparisonHash
:   Type: Text (100).  
    Hash of the module version. Can be used to validate if two module versions have differences.

CreatedOn
:   Type: Date Time.  
    Date and time of the module version creation.

CreatedBy
:   Type: Text (50).  
    Username of the user that created the version.


## Static Entities

### ApplicationPermissionLevel { #StaticEntity_ApplicationPermissionLevel }

Permission level that a user has over an application.

*Attributes*

Id
:   Type: Integer.  
    

Label
:   Type: Text (50).  
    

Description
:   Type: Text (128).  
    

Level
:   Type: Integer.  
    

*Records*

* NoAccess
* List
* OpenReuse
* ChangeDeploy

### DeploymentMessageType { #StaticEntity_DeploymentMessageType }

The type of a deployment message.

*Attributes*

Id
:   Type: Integer.  
    

Label
:   Type: Text (50).  
    

*Records*

* StageAborted
* Info
* PublishStop
* Start
* End
* Error
* Unknown
* Warning
* Step
* StepSub
* AcceptableError

### DeploymentOperationType { #StaticEntity_DeploymentOperationType }

The type of a deployment operation.

*Attributes*

Id
:   Type: Integer.  
    

Label
:   Type: Text (50).  
    

Order
:   Type: Integer.  
    

*Records*

* Unchanged
* Deploy
* Republish

### DeploymentStatus { #StaticEntity_DeploymentStatus }

The status of a deployment operation.

*Attributes*

Id
:   Type: Integer.  
    

Label
:   Type: Text (50).  
    

Order
:   Type: Integer.  
    

*Records*

* NeedsUserIntervention
* InProgress
* Planned
* Synchronized
* Deployed
* Draft

### DialogBoxIcon { #StaticEntity_DialogBoxIcon }

Internal only. Icon of a Dialog Box.

*Attributes*

Id
:   Type: Integer.  
    

Label
:   Type: Text (50).  
    

CssClass
:   Type: Text (50).  
    

*Records*

* None
* Success
* Error
* Feedback
* Warning

### ElementType { #StaticEntity_ElementType }

The types of elements a module references or exposes as public.

*Attributes*

Id
:   Type: Integer.  
    

Label
:   Type: Text (50).  
    

Order
:   Type: Integer.  
    

*Records*

* HumanActivity
* Structure
* HiddenEntity
* WebBlock
* Unknown
* Image
* Action
* WebFlow
* WebScreen
* Theme
* StaticEntity
* Role
* Entity
* Process
* ServiceAPIMethod

### EnvironmentPermissionLevel { #StaticEntity_EnvironmentPermissionLevel }

Permission level that a user has over an epplication.

*Attributes*

Id
:   Type: Integer.  
    

Label
:   Type: Text (50).  
    

Description
:   Type: Text (128).  
    

Level
:   Type: Integer.  
    

ApplicationLevelId
:   Type: ApplicationPermissionLevel Identifier.  
    The application level to which this environment level corresponds.

*Records*

* NoAccess
* FullControl
* ChangeDeploy
* OpenReuse
* List

### LayoutPopupButtonClicked { #StaticEntity_LayoutPopupButtonClicked }

The message of an OnNotify action when a button is pressed in a popup.

*Attributes*

Id
:   Type: Integer.  
    

Label
:   Type: Text (50).  
    

*Records*

* Cancel
* Confirm


