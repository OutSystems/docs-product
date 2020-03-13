# LifeTime API v1

## Summary

API | Base URL | Security
---|---|---
[v1](<#v1>) | /lifetimeapi/rest/v1 | SSL/TLS

## v1

API Method | Description
---|---
[GET /applications/](<#Applications_List>) | Returns a list of applications that exist in the infrastructure.
[GET /applications/{ApplicationKey}/](<#Applications_Get>) | Returns the details of a given application.
[GET /applications/{ApplicationKey}/versions/](<#Applications_Versions_List>) | Returns a list of versions of a given application.
[GET /applications/{ApplicationKey}/versions/{VersionKey}/](<#Applications_Versions_Get>) | Returns the details of a given version of the specified application.
[GET /deployments/](<#Deployments_List>) | Returns a list of deployments ordered by creation date, from newest to oldest.
[POST /deployments/](<#Deployments_Create>) | Creates a deployment to a target environment. An optional list of applications to include in the deployment can be specified. The input is a subset of a Deployment object.
[GET /deployments/{DeploymentKey}/](<#Deployments_Get>) | Returns the details of a given deployment. The returned information contains the included applications and the possible conflicts that can arise from the deployment of the current applications.
[PUT /deployments/{DeploymentKey}/](<#Deployments_Update>) | Updates a given deployment. An optional list of applications to include in the deployment can be specified. The input is a subset of a Deployment object.
[DELETE /deployments/{DeploymentKey}/](<#Deployments_Delete>) | Discards a deployment, if possible. Only deployments whose state is “saved” can be deleted.
[POST /deployments/{DeploymentKey}/{Command}/](<#Deployments_ExecuteCommand>) | Executes the given command in a specified deployment. The allowed commands are “start”, “continue” and “abort”.
[GET /deployments/{DeploymentKey}/status/](<#Deployments_GetStatus>) | Returns the details of a given deployment execution, including the deployment status and messages.
[GET /environments/](<#Environments_List>) | Lists all the environments in the infrastructure.
[GET /environments/{EnvironmentKey}/](<#Environments_Get>) | Returns the details of a given environment.
[GET /environments/{EnvironmentKey}/applications/](<#Environments_GetRunningApps>) | Returns information about the running versions of all applications in a given environment.
[GET /environments/{EnvironmentKey}/applications/{ApplicationKey}/](<#Environments_GetRunningApp>) | Returns information about the running version of the specified application in a given environment.
[GET /environments/{EnvironmentKey}/applications/{ApplicationKey}/content/](<#Environments_DownloadRunningApp>) | Returns a link where the binary file for a given application can be downloaded. The link will expire in 60 minutes.
[POST /environments/{EnvironmentKey}/applications/{ApplicationKey}/versions/](<#Environments_Applications_Versions_Create>) | Creates a new version of the application based on the current running application.
[GET /modules/](<#Modules_List>) | Returns a list of modules that exist in the infrastructure.
[GET /modules/{ModuleKey}/](<#Modules_Get>) | Returns the details of a given module.
[GET /modules/{ModuleKey}/versions/](<#ModuleVersions_List>) | Returns a list of versions of a given module.
[GET /modules/{ModuleKey}/versions/{ModuleVersionKey}/](<#ModuleVersion_Get>) | Returns the details of a given module version.

# Actions

## /applications

### GET /applications/ { #Applications_List }

Returns a list of applications that exist in the infrastructure.

*Full URL*

`GET /lifetimeapi/rest/v1/applications/`

*Inputs*

IncludeModules
:   Type: optional, Boolean.  
    Located in: URL.  
    When set to true, the modules are also returned. The default value is false.

IncludeEnvStatus
:   Type: optional, Boolean.  
    Located in: URL.  
    When set to true, the application status per environment is also returned. The default value is false.

*Outputs*

Applications
:   Type: [Application](<#Structure_Application>) List.  
    Located in: Body.  
    A list of Application records including AppStatusInEnv sub-lists, if requested.

*Return Codes*

200
:   Application list successfully retrieved.

204
:   No applications available in the infrastructure.
    In the Java stack, code 200 is returned instead of 204.

400
:   Failed to retrieve applications because IncludeModules was requested but IncludeEnvStatus was not, or invalid request when listing all applications.


### GET /applications/{ApplicationKey}/ { #Applications_Get }

Returns the details of a given application.

*Full URL*

`GET /lifetimeapi/rest/v1/applications/{ApplicationKey}/`

*Inputs*

ApplicationKey
:   Type: mandatory, Text.  
    Located in: URL.  
    The key of the desired application.

IncludeModules
:   Type: optional, Boolean.  
    Located in: URL.  
    When set to true, the modules details are also retrieved. The default value is false.

IncludeEnvStatus
:   Type: optional, Boolean.  
    Located in: URL.  
    When set to true, the application status per environment is also returned. The default value is false.

*Outputs*

Application
:   Type: [Application](<#Structure_Application>).  
    Located in: Body.  
    An Application record including an AppStatusInEnv sub-list, if requested.

*Return Codes*

200
:   Application details successfully retrieved.

400
:   Failed to retrieve applications because IncludeModules and IncludeEnvStatus parameters were incorrect.

403
:   Failed listing all applications because the user has insufficient permissions.

404
:   Failed getting running applications because one of the environments was not found.

### GET /applications/{ApplicationKey}/versions/ { #Applications_Versions_List }

Returns a list of versions of a given application.

*Full URL*

`GET /lifetimeapi/rest/v1/applications/{ApplicationKey}/versions/`

*Inputs*

ApplicationKey
:   Type: mandatory, Text.  
    Located in: URL.  
    The key of the desired application.

MaximumVersionsToReturn
:   Type: optional, Integer.  
    Located in: URL.  
    The maximum number of versions to return. The default value is 5.

*Outputs*

ApplicationVersions
:   Type: [ApplicationVersion](<#Structure_ApplicationVersion>) List.  
    Located in: Body.  
    A list of ApplicationVersion records.

*Return Codes*

200
:   List of application versions successfully retrieved.

400
:   Invalid request due to invalid max versions to return (less than 0).

403
:   Failed to retrieve the application with key `<ApplicationKey>`. The user does not have the required permissions.

404
:   Failed to retrieve the application with key `<ApplicationKey>`.

### GET /applications/{ApplicationKey}/versions/{VersionKey}/ { #Applications_Versions_Get }

Returns the details of a given version of the specified application.

*Full URL*

`GET /lifetimeapi/rest/v1/applications/{ApplicationKey}/versions/{VersionKey}/`

*Inputs*

ApplicationKey
:   Type: mandatory, Text.  
    Located in: URL.  
    The key of the application whose version is being requested.

VersionKey
:   Type: mandatory, Text.  
    Located in: URL.  
    The key of the desired application version.

IncludeModules
:   Type: mandatory, Boolean.  
    Located in: URL.  
    When set to true, the modules details are also retrieved. The default value is false.

*Outputs*

ApplicationVersion
:   Type: [ApplicationVersion](<#Structure_ApplicationVersion>).  
    Located in: Body.  
    An ApplicationVersion record.

*Return Codes*

200
:   Application version details successfully retrieved.

403
:   Failed to retrieve the application with key `<ApplicationKey>`. The user does not have the required permissions.

404
:   Failed to retrieve the application with key `<ApplicationKey>`.

## /deployments

### GET /deployments/ { #Deployments_List }

Returns a list of deployments ordered by creation date, from newest to oldest.

*Full URL*

`GET /lifetimeapi/rest/v1/deployments/`

*Inputs*

MinDate
:   Type: optional, Date.  
    Located in: URL.  
    The minimum creation date of the deployments to return. The default value is 1 week before the current date.

MaxDate
:   Type: optional, Date.  
    Located in: URL.  
    The maximum creation date of the deployments to return. The default value is the current date.

*Outputs*

Deployments
:   Type: [Deployment](<#Structure_Deployment>) List.  
    Located in: Body.  
    A list of Deployment records.

*Return Codes*

200
:   Deployments list successfully retrieved.

204
:   There are no deployments created between `<MinDate>` and `<MaxDate>`.
    In the Java stack, code 200 is returned instead of 204.

400
:   Invalid request for list of deployments created between `<MinDate>` and `<MaxDate>`.

403
:   User doesn't have access to any application or environment involved in the deployments created between `<MinDate>` and `<MaxDate>`.

### POST /deployments/ { #Deployments_Create }

Creates a deployment to a target environment. An optional list of applications to include in the deployment can be specified. The input is a subset of a Deployment object.

*Full URL*

`POST /lifetimeapi/rest/v1/deployments/`

*Inputs*

ApplicationVersionKeys
:   Type: Optional, Text List.  
    Located in: Body.  
    List of keys of the application versions included in the deployment.

Notes
:   Type: optional, Text.  
    Located in: Body.  
    Deployment notes.

SourceEnvironmentKey
:   Type: optional, Text.  
    Located in: Body.  
    Source environment unique identifier.

TargetEnvironmentKey
:   Type: optional, Text.  
    Located in: Body.  
    Target environment unique identifier.

*Outputs*

DeploymentKey
:   Type: Text.  
    Located in: Body.  
    The key of the newly created deployment.

*Return Codes*

201
:   Deployment successfully created.

400
:   Invalid request.

403
:   Invalid user permissions.

404
:   Source or target environment not found.

**Example Request Body**

```javascript
{
  "ApplicationVersionKeys": [
    "22dcc061-8767-46dd-8a6e-7991ee8112c7"
  ],
  "Notes": "WebPortal 1.1 - QA to PRD Deployment",
  "SourceEnvironmentKey": "10061715-16bb-491a-86bc-595b465eaffb",
  "TargetEnvironmentKey": "55c430ee-4783-43e6-a2d4-6eecfed1d90f"
}
```

### GET /deployments/{DeploymentKey}/ { #Deployments_Get }

Returns the details of a given deployment. The returned information contains the included applications and the possible conflicts that can arise from the deployment of the current applications.

*Full URL*

`GET /lifetimeapi/rest/v1/deployments/{DeploymentKey}/`

*Inputs*

DeploymentKey
:   Type: mandatory, Text.  
    Located in: URL.  
    The key of the desired deployment.

*Outputs*

ApplicationConflicts
:   Type: [ApplicationConflict](<#Structure_ApplicationConflict>) List.  
    Located in: Body.  
    List of conflicts between applications in the deployment.

Deployment
:   Type: [Deployment](<#Structure_Deployment>).  
    Located in: Body.  
    The deployment details.

*Return Codes*

200
:   Deployment details successfully retrieved.

403
:   User doesn't have permissions to the deployment with key `<DeploymentKey>`.

404
:   Deployment with key `<DeploymentKey>` not found.

### PUT /deployments/{DeploymentKey}/ { #Deployments_Update }

Updates a given deployment. An optional list of applications to include in the deployment can be specified. The input is a subset of a Deployment object.

*Full URL*

`PUT /lifetimeapi/rest/v1/deployments/{DeploymentKey}/`

*Inputs*

DeploymentKey
:   Type: mandatory, Text.  
    Located in: URL.  
    The key of the deployment to update.

ApplicationVersionKeys
:   Type: optional, Text List.  
    Located in: Body.  
    List of keys of the application versions to include in the deployment.

Notes
:   Type: optional, Text.  
    Located in: Body.  
    Deployment notes.

SourceEnvironmentKey
:   Type: optional, Text.  
    Located in: Body.  
    Source environment unique identifier.

TargetEnvironmentKey
:   Type: optional, Text.  
    Located in: Body.  
    Target environment unique identifier.

*Outputs*

Deployment
:   Type: [Deployment](<#Structure_Deployment>).  
    Located in: Body.  
    A Deployment record containing the updated information.

*Return Codes*

200
:   Deployment successfully updated.

400
:   Invalid request.

403
:   Invalid user permissions.

404
:   Deployment plan not found.


**Example Request Body**

```javascript
{
  "ApplicationVersionKeys": [
    "73b2a7a6-d893-42de-bd94-90276eac8374"
  ],
  "Notes": "WebPortal 1.1 - QA to PRD Deployment",
  "SourceEnvironmentKey": "10061715-16bb-491a-86bc-595b465eaffb",
  "TargetEnvironmentKey": "55c430ee-4783-43e6-a2d4-6eecfed1d90f"
}
```

### DELETE /deployments/{DeploymentKey}/ { #Deployments_Delete }

Discards a deployment, if possible. Only deployments whose state is “saved” can be deleted.

*Full URL*

`DELETE /lifetimeapi/rest/v1/deployments/{DeploymentKey}/`

*Inputs*

DeploymentKey
:   Type: mandatory, Text.  
    Located in: URL.  
    The key of the deployment to delete.

*Return Codes*

204
:   Deployment successfully deleted.
    In the Java stack, code 200 is returned instead of 204.

400
:   Deployment with key `<DeploymentKey>` cannot be deleted.

403
:   Could not access the deployment with key `<DeploymentKey>`. The user does not have the required permissions.

404
:   Deployment with key `<DeploymentKey>` not found.


### POST /deployments/{DeploymentKey}/{Command}/ { #Deployments_ExecuteCommand }

Executes the given command in a specified deployment. The allowed commands are "start", "continue" and "abort".

*Full URL*

`POST /lifetimeapi/rest/v1/deployments/{DeploymentKey}/{Command}/`

*Inputs*

DeploymentKey
:   Type: mandatory, Text.  
    Located in: URL.  
    The key of the deployment where the command will be executed.

Command
:   Type: mandatory, Text.  
    Located in: URL.  
    The command to execute. One of “start”, “continue” or “abort”.

*Return Codes*

202
:   Command `<Command>` executed successfully for deployment `<DeploymentKey>`.

400
:   Command `<Command>` can't be executed for deployment `<DeploymentKey>`.

403
:   User doesn't have permissions to access the deployment with key `<DeploymentKey>`.

404
:   Deployment with key `<DeploymentKey>` not found, or command not found.


### GET /deployments/{DeploymentKey}/status/ { #Deployments_GetStatus }

Returns the details of a given deployment execution, including the deployment status and messages.

*Full URL*

`GET /lifetimeapi/rest/v1/deployments/{DeploymentKey}/status/`

*Inputs*

DeploymentKey
:   Type: mandatory, Text.  
    Located in: URL.  
    The key of the deployment whose status is being requested.

*Outputs*

DeploymentLog
:   Type: [DeploymentMessage](<#Structure_DeploymentMessage>) List.  
    Located in: Body.  
    List of deployment messages.

DeploymentStatus
:   Type: Text.  
    Located in: Body.  
    Status of the deployment. [saved | running | needs_user_intervention | aborted | aborting | finished_successful | finished_with_warnings | finished_with_errors]

*Return Codes*

200
:   Deployment status successfully retrieved.

403
:   User doesn't have permissions to the deployment with key `<DeploymentKey>`.

404
:   Deployment with key `<DeploymentKey>` not found.


## /environments

### GET /environments/ { #Environments_List }

Lists all the environments in the infrastructure.

*Full URL*

`GET /lifetimeapi/rest/v1/environments/`

*Outputs*

Environments
:   Type: [Environment](<#Structure_Environment>) List.  
    Located in: Body.  
    A list of Environment records.

*Return Codes*

200
:   Environments list successfully retrieved.

204
:   No environments found.
    In the Java stack, code 200 is returned instead of 204.

### GET /environments/{EnvironmentKey}/ { #Environments_Get }

Returns the details of a given environment.

*Full URL*

`GET /lifetimeapi/rest/v1/environments/{EnvironmentKey}/`

*Inputs*

EnvironmentKey
:   Type: mandatory, Text.  
    Located in: URL.  
    The key of the desired environment.

*Outputs*

Environment
:   Type: [Environment](<#Structure_Environment>).  
    Located in: Body.  
    An Environment record.

*Return Codes*

200
:   Environment details successfully retrieved.

403
:   Failed to retrieve the environment with key: `<EnvironmentKey>`. The user does not have the required permissions.

404
:   An environment with key `<EnvironmentKey>` was not found.


### GET /environments/{EnvironmentKey}/applications/ { #Environments_GetRunningApps }

Returns information about the running versions of all applications in a given environment.

*Full URL*

`GET /lifetimeapi/rest/v1/environments/{EnvironmentKey}/applications/`

*Inputs*

EnvironmentKey
:   Type: mandatory, Text.  
    Located in: URL.  
    The key of the environment whose list of running applications is being requested.

IncludeModules
:   Type: optional, Boolean.  
    Located in: URL.  
    When set to true, the modules details are also retrieved. The default value is false.

IncludeEnvStatus
:   Type: optional, Boolean.  
    Located in: URL.  
    When set to true, the applications’ status information in the environment is included in the result. The default value is false.

*Outputs*

Applications
:   Type: [Application](<#Structure_Application>) List.  
    Located in: Body.  
    A list of Application records.

*Return Codes*

200
:   Applications list for the given environment successfully retrieved

204
:   No applications found in environment with key `<EnvironmentKey>`.
    In the Java stack, code 200 is returned instead of 204.
400
:   Failed to retrieve applications published in environment because IncludeModules and IncludeEnvStatus parameters were incorrect, or invalid request when getting running applications for environment with key `<EnvironmentKey>`.

403
:   Failed to retrieve the running applications for environment with key `<EnvironmentKey>` because user has insufficient permissions.

404
:   Failed to retrieve running applications for environment with key `<EnvironmentKey>` because it was not found.


### GET /environments/{EnvironmentKey}/applications/{ApplicationKey}/ { #Environments_GetRunningApp }

Returns information about the running version of the specified application in a given environment.

*Full URL*

`GET /lifetimeapi/rest/v1/environments/{EnvironmentKey}/applications/{ApplicationKey}/`

*Inputs*

EnvironmentKey
:   Type: mandatory, Text.  
    Located in: URL.  
    The key of the environment from which to get the running application details.

ApplicationKey
:   Type: mandatory, Text.  
    Located in: URL.  
    The key of the application whose details are being requested.

IncludeEnvStatus
:   Type: optional, Boolean.  
    Located in: URL.  
    When set to true, the applications’ status information in the environment is included in the result. The default value is false.

IncludeModules
:   Type: optional, Boolean.  
    Located in: URL.  
    When set to true, the modules details are also retrieved. The default value is false.

*Outputs*

Application
:   Type: [Application](<#Structure_Application>).  
    Located in: Body.  
    An Application record.

*Return Codes*

200
:   Application information successfully retrieved.

400
:   Request asked for Modules but not for Status.

403
:   User doesn’t have permissions for the given keys (EnvironmentKey:`<EnvironmentKey>`; Application:`<ApplicationKey>`).

404
:   Failed to retrieve the environment with key `<EnvironmentKey>` or the application with key `<ApplicationKey>`.

### GET /environments/{EnvironmentKey}/applications/{ApplicationKey}/content/ { #Environments_DownloadRunningApp }

Returns a link where the binary file for a given application can be downloaded. The link will expire in 60 minutes.

*Full URL*

`GET /lifetimeapi/rest/v1/environments/{EnvironmentKey}/applications/{ApplicationKey}/content/`

*Inputs*

EnvironmentKey
:   Type: mandatory, Text.  
    Located in: URL.  
    The key of the environment from which to get the application binary file link.

ApplicationKey
:   Type: mandatory, Text.  
    Located in: URL.  
    The key of the application for which to get the binary file link.

Type
:   Type: optional, Text.  
    Located in: URL.  
    The type of binary file to return, when applicable. [oap | apk | ipa]

*Outputs*

DownloadLink
:   Type: [DownloadLink](<#Structure_DownloadLink>).  
    Located in: Body.  
    The link for the application binary file.

Expires
:   Type: Date Time.  
    Located in: Header.  
    The expiration date and time of the returned link.

*Return Codes*

200
:   Binary file download link successfully retrieved.

204
:   No binary available for given type and keys.
    In the Java stack, code 200 is returned instead of 204.

400
:   The required type `<Type>` is invalid for the given keys (EnvironmentKey:`<EnvironmentKey>`; Application:`<ApplicationKey>`).

403
:   User doesn’t have permissions for the given keys (EnvironmentKey:`<EnvironmentKey>`; Application:`<ApplicationKey>`).

404
:   Failed to retrieve the environment with key `<EnvironmentKey>` or the application with key `<ApplicationKey>`.

### POST /environments/{EnvironmentKey}/applications/{ApplicationKey}/versions/ { #Environments_Applications_Versions_Create }

Creates a new version of the application based on the current running application.

*Full URL*

`POST /lifetimeapi/rest/v1/environments/{EnvironmentKey}/applications/{ApplicationKey}/versions/`

*Inputs*

EnvironmentKey
:   Type: mandatory, Text.  
    Located in: URL.  
    The key of the environment from which to get the application.

ApplicationKey
:   Type: mandatory, Text.  
    Located in: URL.  
    The key of the application for which to generate a new version.

ApplicationVersionCreate
:   Type: mandatory, [ApplicationVersionCreate](<#Structure_ApplicationVersionCreate>).  
    Located in: Body.  
    A structure holding the new version name for the application and for its native applications, if applicable.

*Outputs*

ApplicationVersionKey
:   Type: Text.  
    Located in: Body.  
    The key of the newly created application version.

*Return Codes*

201
:   Application version successfully created.

400
:   Invalid request.

403
:   Invalid user permissions.

404
:   Environment or application not found.


**Example Request Body**

```javascript
{
  "ChangeLog": "First release of iOS mobile app",
  "Version": "1.0.0",
  "MobileVersions": [
    {
      "NativePlatform": "iOS",
      "VersionNumber": "1.0.0",
      "VersionDescription": "First release"
    }
  ],
  "ModuleVersionKeys": [
    "63146a06-06d3-4f9e-a4ca-abc7bb6950e5"
  ]
}
```


## /modules

### GET /modules/ { #Modules_List }

Returns a list of modules that exist in the infrastructure.

*Full URL*

`GET /lifetimeapi/rest/v1/modules/`

*Inputs*

IncludeEnvStatus
:   Type: optional, Boolean.  
    Located in: URL.  
    When set to true, the module status per environment is also returned. The default value is false.

*Outputs*

ModuleList
:   Type: [Module](<#Structure_Module>) List.  
    Located in: Body.  
    List of Module records.

*Return Codes*

200
:   Modules list successfully retrieved.

204
:   No modules found in the infrastructure.
    In the Java stack, code 200 is returned instead of 204.

### GET /modules/{ModuleKey}/ { #Modules_Get }

Returns the details of a given module.

*Full URL*

`GET /lifetimeapi/rest/v1/modules/{ModuleKey}/`

*Inputs*

ModuleKey
:   Type: mandatory, Text.  
    Located in: URL.  
    Key of the module to list the details from.

IncludeEnvStatus
:   Type: optional, Boolean.  
    Located in: URL.  
    When set to true, the module status per environment is also returned. The default value is false.

*Outputs*

Module
:   Type: [Module](<#Structure_Module>).  
    Located in: Body.  
    Module record.

*Return Codes*

200
:   Module details successfully retrieved.

403
:   Failed to retrieve the module with key: `<ModuleKey>`. The user does not have the required permissions.

404
:   Failed to retrieve the module with key: `<ModuleKey>`.

### GET /modules/{ModuleKey}/versions/ { #ModuleVersions_List }

Returns a list of versions of a given module.

*Full URL*

`GET /lifetimeapi/rest/v1/modules/{ModuleKey}/versions/`

*Inputs*

ModuleKey
:   Type: mandatory, Text.  
    Located in: URL.  
    The module from where to retrieve the versions from.

IncludePublicElements
:   Type: optional, Boolean.  
    Located in: URL.  
    Boolean to indicate if public elements should be returned. Default is false.

IncludeConsumedElements
:   Type: optional, Boolean.  
    Located in: URL.  
    Boolean to indicate if consumed elements should be returned. Default is false.

MaximumVersionsToReturn
:   Type: optional, Integer.  
    Located in: URL.  
    Maximum number of versions to return. Default is 5.

*Outputs*

ModuleVersionList
:   Type: [ModuleVersion](<#Structure_ModuleVersion>) List.  
    Located in: Body.  
    List of ModuleVersion records.

*Return Codes*

200
:   List of module versions successfully retrieved.

400
:   Invalid request due to invalid max versions to return (less than 0).

403
:   Failed to retrieve the module with key: `<ModuleKey>`. The user does not have the required permissions.

404
:   Failed to retrieve the module with key: `<ModuleKey>`.

### GET /modules/{ModuleKey}/versions/{ModuleVersionKey}/ { #ModuleVersion_Get }

Returns the details of a given module version.

*Full URL*

`GET /lifetimeapi/rest/v1/modules/{ModuleKey}/versions/{ModuleVersionKey}/`

*Inputs*

ModuleKey
:   Type: mandatory, Text.  
    Located in: URL.  
    The module from where to retrieve the versions from.

ModuleVersionKey
:   Type: mandatory, Text.  
    Located in: URL.  
    Key of the module version to return.

IncludePublicElements
:   Type: optional, Boolean.  
    Located in: URL.  
    Boolean to indicate if public elements should be returned. Default is false.

IncludeConsumedElements
:   Type: optional, Boolean.  
    Located in: URL.  
    Boolean to indicate if consumed elements should be returned. Default is false.

*Outputs*

ModuleVersion
:   Type: [ModuleVersion](<#Structure_ModuleVersion>)  
    Located in: Body.  
    Record of ModuleVersion.

*Return Codes*

200
:   Module version details successfully retrieved.

403
:   Failed to retrieve the module with key: `<ModuleKey>`. The user does not have the required permissions.

404
:   Failed to retrieve the module with key: `<ModuleKey>`, or failed to retrieve the module version with key: `<ModuleKey>`.


## Structures

### Application { #Structure_Application }

An application with its details and its status in the environments were it is running.

*Attributes*

Key
:   Type: Text.  
    Application unique identifier.

Name
:   Type: Text (50).  
    Name of the application.

Kind
:   Type: RuntimeKind Identifier.  
    Identifies the kind of application. [Mobile | WebResponsive]

Team
:   Type: Text (50).  
    The team that owns the application.

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

IsSystem
:   Type: Boolean.  
    Indicates if the application is a built-in component of the OutSystems platform (e.g. Service Center, LifeTime, ...).

AppStatusInEnvs
:   Type: [AppStatusInEnv](<#Structure_AppStatusInEnv>) List.  
    Information about the status of the application in each environment it is running.

### ApplicationConflict { #Structure_ApplicationConflict }

A deployment conflict.

*Attributes*

Message
:   Type: Text.  
    Description of the conflict.

ProducerApplicationOperation
:   Type: [ApplicationOperation](<#Structure_ApplicationOperation>).  
    Operation executed over producer application.

ConsumerApplicationOperation
:   Type: [ApplicationOperation](<#Structure_ApplicationOperation>).  
    Operation executed over consumed application.

ModuleConflict
:   Type: [ModuleConflict](<#Structure_ModuleConflict>).  
    Details of the module conflict.

### ApplicationOperation { #Structure_ApplicationOperation }

Operation executed in the deployment over the application.

*Attributes*

ApplicationKey
:   Type: Text.  
    Application unique identifier.

ApplicationVersionKey
:   Type: Text.  
    Application Version unique identifier.

DeploymentOperation
:   Type: Text.  
    Label of the operation to be performed. Example: Deploy 1.5.

### ApplicationVersion { #Structure_ApplicationVersion }

Information about a specific version of an application and the versions of its modules.

*Attributes*

Key
:   Type: Text.  
    Application version unique identifier.

ApplicationKey
:   Type: Text.  
    Application unique identifier.

Version
:   Type: Text (50).  
    Version of the application.

MobileVersions
:   Type: [MobileVersion](<#Structure_MobileVersion>) List.  
    List of mobile versions.

PrimaryColor
:   Type: Text (50).  
    The primary color of the application interface.

NativeHash
:   Type: Text (50).  
    The native hash relative to the mobile platform.

ModuleVersions
:   Type: [ModuleVersion](<#Structure_ModuleVersion>) List.  
    List of module versions.

### ApplicationVersionCreate { #Structure_ApplicationVersionCreate }

A structure holding the new version name for the application and for its native applications, if applicable.

*Attributes*

ChangeLog
:   Type: Text.  
    Change log of the version to be created.

Version
:   Type: Text (50).  
    Version of the application.

MobileVersions
:   Type: [MobileVersion](<#Structure_MobileVersion>) List.  
    List of mobile versions.

ModuleVersionKeys
:   Type: Text List.  
    List of module version keys to validate if the current state of the application is still the expected one.

### AppStatusInEnv { #Structure_AppStatusInEnv }

Status of application in a given environment.

*Attributes*

EnvironmentKey
:   Type: Text.  
    Environment unique identifier.

BaseApplicationVersionKey
:   Type: Text.  
    Base application version unique identifier. If app is not modified in environment, this is the application version deployed.

IsModified
:   Type: Boolean.  
    True if the application has been changed since the last tag, false otherwise.

IsModifiedReason
:   Type: Text.  
    Indicates the application status.

IsModifiedMessage
:   Type: Text.  
    Indicates the application status.

ConsistencyStatus
:   Type: Text (50).  
    Indicates the application consistency status.

ConsistencyStatusMessages
:   Type: Text (2000).  
    Messages regarding the consistency status of the application.

MobileAppsStatus
:   Type: [MobileAppStatusInEnv](<#Structure_MobileAppStatusInEnv>) List.  
    Status of mobile apps in environment.

ModuleStatusInEnvs
:   Type: [ModuleStatusInEnv](<#Structure_ModuleStatusInEnv>) List.  
    Status of modules in environment.

### Deployment { #Structure_Deployment }

Deployment information with the operations executed.

*Attributes*

Key
:   Type: Text.  
    Deployment unique identifier.

SourceEnvironmentKey
:   Type: Text.  
    Source environment unique identifier.

TargetEnvironmentKey
:   Type: Text.  
    Target environment unique identifier.

Notes
:   Type: Text.  
    Deployment notes.

CreatedOn
:   Type: Date Time.  
    Date and time when the deployment plan was created.

CreatedBy
:   Type: Text.  
    Name of the user who created the deployment plan.

CreatedByUsername
:   Type: Text.  
    Username of the user who created the deployment plan.

SavedOn
:   Type: Date Time.  
    The date and time when the deployment plan was saved.

SavedBy
:   Type: Text.  
    Name of the user who last saved the deployment plan.

SavedByUsername
:   Type: Text.  
    Username of the user who last saved the deployment plan.

StartedOn
:   Type: Date Time.  
    The date and time when the deployment started.

StartedBy
:   Type: Text.  
    Name of the user who started the deployment.

StartedByUsername
:   Type: Text.  
    Username of the user who started the deployment.

AbortedOn
:   Type: Date Time.  
    The date and time when the deployment was aborted.

AbortedBy
:   Type: Text.  
    Name of the user who aborted the deployment.

AbortedByUsername
:   Type: Text.  
    Username of the user who aborted the deployment.

ApplicationsVersionKeys
:   Type: Text List.  
    List of Application Versions included in the deployment.

### DeploymentMessage { #Structure_DeploymentMessage }

Message from a deployment operation log.

*Attributes*

Instant
:   Type: Date Time.  
    Date and time when the message was logged.

Message
:   Type: Text.  
    Details of the message.

### DownloadLink { #Structure_DownloadLink }

The link for the application binary file.

*Attributes*

url
:   Type: Text.  
    The link for the application binary file.  

expires
:   Type: Date Time.  
    The expiration date and time of the returned link.

### Environment { #Structure_Environment }

An environment and its information.

*Attributes*

Key
:   Type: Text.  
    Unique identifier of the environment.

Name
:   Type: Text (50).  
    Name of the environment.

OSVersion
:   Type: Text (50).  
    Platform Server version. [X.X.X.X]

Order
:   Type: Integer.  
    The order of the environment as registered in Lifetime.

HostName
:   Type: Text (50).  
    Hostname of the environment as registered.

UseHTTPS
:   Type: Boolean.  
    Indicates if connections to the environment are made using HTTPS.

EnvironmentType
:   Type: Text.  
    Indicates the type of the environment. [Development | Test | Production]

NumberOfFrontEnds
:   Type: Integer.  
    Number of front-end servers in the environment.

ApplicationServerType
:   Type: Text (50).  
    Stack of the application server. [.NET | JAVA]

ApplicationServer
:   Type: Text (50).  
    Application server in use. [IIS | JBoss | WebLogic]

DatabaseProvider
:   Type: Text (50).  
    Type of database provider. [SqlServer | Oracle]

IsCloudEnvironment
:   Type: Boolean.  
    Indicates if the environment is running on a cloud service.

### MobileAppStatusInEnv { #Structure_MobileAppStatusInEnv }

Status of mobile application in a given environment.

*Attributes*

EnvironmentKey
:   Type: Text.  
    Environment unique identifier.

NativePlatform
:   Type: Text.  
    Name of native platform. [Android | iOS]

VersionNumber
:   Type: Text.  
    The version number, like for example 1.5.4, of the native build. It is used to be able to map the version to the version in the Android or iOS store.

HasBinaryAvailable
:   Type: Boolean.  
    True if the binary of the application is available for the current configuration.

IsConfigured
:   Type: Boolean.  
    True if the application is configured.

IsConfigurationChanged
:   Type: Boolean.  
    True if the configuration of the Mobile Application has changed in the environment.

IsModified
:   Type: Boolean.  
    True if the Native Hash of the Mobile Application does not match the one in the AppVersionNativeBuild baseline.

### MobileVersion { #Structure_MobileVersion }

A mobile version and its information.

*Attributes*

NativePlatform
:   Type: Text.  
    Name of native platform. [Android | iOS]

VersionNumber
:   Type: Text (50).  
    The version number, like for example 1.5.4, of the native build. It is used to be able to map the version to the version in the Android or iOS store.

VersionDescription
:   Type: Text.  
    The description of the mobile version.

### Module { #Structure_Module }

Module information and the status in the environments where the modules are running.

*Attributes*

Key
:   Type: Text.  
    Module unique identifier.

Name
:   Type: Text (50).  
    Name of the module.

Description
:   Type: Text (50).  
    Description of the module.

Kind
:   Type: Text (50).  
    Module type (eSpace or Extension).

ModuleStatusInEnv
:   Type: [ModuleStatusInEnv](<#Structure_ModuleStatusInEnv>) List.  
    Status of the module in environments.

### ModuleConflict { #Structure_ModuleConflict }

A module conflict.

*Attributes*

ProducerModuleKey
:   Type: Text.  
    Producer Module unique identifier.

ConsumerModuleKey
:   Type: Text.  
    Consumer Module unique identifier.

TotalRequiredElements
:   Type: Integer.  
    Total number of required elements.

ConflictType
:   Type: Text.  
    Type of conflict. [Producer Module Missing | Producer Element Missing | Producer Element Incompatible | Consumer Module Outdated | Newer Producer Module Available | IncompatiblePlatformServer | ConsumerModuleMoved | ProducerModuleMoved | NameColision]

### ModuleElement { #Structure_ModuleElement }

Element version information, such as action, entity, structure, among others.

*Attributes*

Key
:   Type: Text.  
    Module element unique identifier.

Name
:   Type: Text (50).  
    Name of the element as specified by the developer.

ElementType
:   Type: Text.  
    Type of the element, such as action, entity, structure.

CompatibilitySignatureHash
:   Type: Text (50).  
    Hash of the element signature. Can be used to validate if the element version is compatible with another version, not producing a broken reference.

FullSignatureHash
:   Type: Text (50).  
    Hash of the element. Can be used to uniquely identify an element version.

ModuleKey
:   Type: Text.  
    Unique identifier of the module where the element is publicly supplied, among others.

### ModuleStatusInEnv { #Structure_ModuleStatusInEnv }

Status of module in a given environment.

*Attributes*

EnvironmentKey
:   Type: Text.  
    Environment unique identifier.

ModuleVersionKey
:   Type: Text.  
    Module version unique identifier.

ConsistencyStatus
:   Type: Text (50).  
    Indicates the module consistency status.

ConsistencyStatusMessages
:   Type: Text (2000).  
    Messages regarding the consistency status of the module.

### ModuleVersion { #Structure_ModuleVersion }

A module version and its information.

*Attributes*

Key
:   Type: Text.  
    Module version unique identifier.

ModuleKey
:   Type: Text.  
    Module unique identifier.

PublicElements
:   Type: [ModuleElement](<#Structure_ModuleElement>) List.  
    List of module elements exposed by module version.

ConsumedElements
:   Type: [ModuleElement](<#Structure_ModuleElement>) List.  
    List of module elements consumed by module version.
