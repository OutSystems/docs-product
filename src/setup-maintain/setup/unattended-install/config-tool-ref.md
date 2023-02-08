---
summary: Complete reference for the Configuration Tool command line.
tags: support-Installation_Configuration; support-Installation_Configuration-overview
locale: en-us
guid: 7c953aae-e0ef-4034-afcf-84960d18ad3b
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Configuration Tool Command Line Reference

<div class="info" markdown="1">

This article applies to: **OutSystems 11**&#8195;&#8195;Other versions available: [10](https://success.outsystems.com/Documentation/10/Setting_Up_OutSystems/Unattended_Installation_and_Upgrade/Configuration_Tool_Command_Line_Reference)

</div>

The Configuration Tool allows you to configure your OutSystems server.

The default path of the Configuration Tool command line is the following:

```
C:\Program Files\OutSystems\Platform Server\ConfigurationTool.com
```

The Configuration Tool command line returns non-zero values when an error occurs.

## Syntax

```
ConfigurationTool.com 
    | /SetupInstall [<platform_db_admin_username> <platform_db_admin_password> <logging_db_admin_username> <logging_db_admin_password>] [/SetPlatformServerAdminPassword <platform_server_admin_password>] 
    | /UpgradeInstall [<integrated_auth_admin_password>] [/SetPlatformServerAdminPassword <platform_server_admin_password>] 
    | /RebuildSession <session_db_admin_username> <session_db_admin_password> 
    | /InstallServiceCenter  
    | /InstallSystemComponents
    | /GenerateTemplates
    | /ClearInternalNetwork
    | /UploadLicense <license_file> <platform_server_admin_user> <platform_server_admin_password>
    | /RegenerateSettingsKey
    | /GetSerial
    | /SetPlatformServerAdminPassword <platform_server_admin_password>
    | /GetDeploymentZones
    | /ModifyDeploymentZone <deployment_zone_name> <deployment_zone_address> [<enable_https>]
    | /CreateUpgradeCacheInvalidationService
    | /UpgradeEnvironment
    | /UpgradePublishedApplications
    | /DeployPreparedApplications
    | /ApplySettingsFactory
```

## Parameters

`/SetupInstall [<platform_db_admin_username> <platform_db_admin_password> <logging_db_admin_username> <logging_db_admin_password>] [/SetPlatformServerAdminPassword <platform_server_admin_password>]`

:   Creates or upgrades the OutSystems platform and logging database model using the `server.hsconf` configuration file.

    For Azure SQL Database or SQL Server databases, you must provide the credentials needed to create or upgrade the platform database. Furthermore, if you specify separate platform and logging databases in `server.hsconf`, you also need to provide the credentials needed to create or upgrade the logging database.

    For Oracle databases, you do not need to provide the admin usernames and passwords.
    
    If you provide the optional `/SetPlatformServerAdminPassword` parameter with a password, sets the password for the Platform Server `admin` user.

`/UpgradeInstall [<integrated_auth_admin_password>] [/SetPlatformServerAdminPassword <platform_server_admin_password>]`

:   Upgrades the OutSystems platform and logging database models, without validating if the database exists or if the permissions are correct.

    The `<integrated_auth_admin_password>` parameter corresponds to the Platform Administrator user password that is configured when enabling Integrated Authentication. This password is optional and is only used for integrated authentication purposes where the password isn't stored in the server configuration file.
    
    If you provide the optional `/SetPlatformServerAdminPassword` parameter with a password, sets the password for the Platform Server `admin` user.

`/RebuildSession <session_db_admin_username> <session_db_admin_password>`

:   Upgrades the session database model. The username and password provided must belong to a user with permissions to execute these operations.

`/InstallServiceCenter `

:   Forces the Service Center installation to run after finishing Configuration Tool.

`/InstallSystemComponents`

:   Forces the System Components installation or upgrade to run after applying the configuration settings.

`/GenerateTemplates`

:   Generates server configuration file (`.hsconf`) templates for each supported database engine in `Platform Server\docs`.

`/ClearInternalNetwork`

:   Resets the internal network settings so that internal applications become accessible from any origin.

`/UploadLicense <license_file> <platform_server_admin_user> <platform_server_admin_password>`

:   Uploads the license file and checks if the license is valid.

    You must provide valid Service Center admin user credentials to execute this operation.  
    The Service Center application must be running.

`/RegenerateSettingsKey`

:   Generates a new private.key file.

`/GetSerial`

:   Prints the serial number of this installation.

`/SetPlatformServerAdminPassword <platform_server_admin_password>`

:   Defines the password for the Platform Server Admin user, if the user is active.  
    Note: This command doesn't work when using Integrated Authentication.
    
`/GetDeploymentZones`

:   Lists the configured deployment zones for the current installation. The data is presented in JSON format, limited to the relevant settings that can be manipulated with `/ModifyDeploymentZone`, namely: the Configuration Name and Address, and it's Enable HTTPS status.

`/ModifyDeploymentZone <deployment_zone_name> <deployment_zone_address> [<enable_https>]`

:   Modifies the Address and/or Enable HTTPS settings of a Deployment Zone.

    `<deployment_zone_name>` is the Deployment Zone that you want to modify; this argument is case insensitive (for example "GLOBAL" will map to "Global").

    `<deployment_zone_address>` is the new address for the target Deployment Zone.

    `[<enable_https>]` is an optional boolean argument; if this argument is not provided the setting will remain unchanged. If the string "true" (case insensitive) is provided, the Enable HTTPS setting is set to "true"; if any other string is provided the setting Enable HTTPS is set to "false". The applied value of the Enable HTTPS setting is displayed.

`/CreateUpgradeCacheInvalidationService`

:   Installs cache invalidation service or reconfigures the service given in the configuration file (`server.hsconf`).
    
`/UpgradeEnvironment`

:   Installs the core components (Service Center and the System Components), and starts [preparing your modules](https://success.outsystems.com/Support/Enterprise_Customers/Upgrading/Modules_preparation_step_during_Platform_Server_upgrade) for the new Platform Server version. Skips any of these steps if they were previously executed.

`/UpgradePublishedApplications`

:   Forces the [preparation of your modules](https://success.outsystems.com/Support/Enterprise_Customers/Upgrading/Modules_preparation_step_during_Platform_Server_upgrade) for the new Platform Server version.

`/DeployPreparedApplications`

:   <div class="warning" markdown="1">

       Due to known issues found in Platform Server 11.18.0, we advise all customers **not to use** the **/DeployPreparedApplications** parameter, which is related to the [Deploy All](../../upgrade/upgrade-platform-module-deploy.md) feature.

    Check [Platform Server 11.18.0 release notes and known issues](https://success.outsystems.com/Support/Release_Notes/11/Platform_Server#platform_server_11.18.0) for more details. In Platform Server 11.18.1 we've turned off this feature. These issues will be fixed in a next release and the feature will be again available for use.

    </div>

    Deploys all the successfully prepared modules from your current Platform Server version to Platform Server 11.18.0 or later, except for those modules already deployed in the latest version. Read more about this feature in [Modules deployment step during Platform Server upgrade](https://success.outsystems.com/Documentation/11/Setup_and_maintain_your_OutSystems_infrastructure/Upgrade_OutSystems_platform/Modules_deployment_step_during_Platform_Server_upgrade).

`/ApplySettingsFactory`

:   Applies the current `server.hsconf` settings to the factory.  
    Note: This command only generates output in case of errors.

## Example

Perform a clean installation for SQL Server or Azure SQL Database:

```
ConfigurationTool.com
    /SetupInstall <platform_db_admin_username> <platform_db_admin_password> <logging_db_admin_username> <logging_db_admin_password>
    /RebuildSession <session_db_admin_username> <session_db_admin_password>
    /CreateUpgradeCacheInvalidationService
    /InstallServiceCenter 
```

Perform a clean installation for Oracle:

```
ConfigurationTool.com
    /SetupInstall
    /RebuildSession <session_db_admin_username> <session_db_admin_password>
    /CreateUpgradeCacheInvalidationService
    /InstallServiceCenter 
```

Perform an upgrade from OutSystems 10 (or lower):

```
ConfigurationTool.com
    /UpgradeInstall <integrated_auth_admin_password>
    /RebuildSession <session_db_admin_username> <session_db_admin_password>
    /CreateUpgradeCacheInvalidationService
    /UpgradeEnvironment  
```

Perform an upgrade from OutSystems 11:

```
ConfigurationTool.com
    /UpgradeInstall <integrated_auth_admin_password>
    /RebuildSession <session_db_admin_username> <session_db_admin_password>
    /UpgradeEnvironment  
```

Upgrade to Platform Server 11.18.0 or later and deploy all modules after completing the upgrade installation:

```
ConfigurationTool.com
    /UpgradeInstall <integrated_auth_admin_password>
    /RebuildSession <session_db_admin_username> <session_db_admin_password>
    /UpgradeEnvironment  
    /DeployPreparedApplications
```

Modify the Address and/or Enable HTTPS settings of the "Global" deployment zone:

```
ConfigurationTool.com
    /ModifyDeploymentZone "Global" <deployment_zone_address> [<enable_https>]
```

## Logging

By default, the Configuration Tool has logging enabled with log level `4` (Verbose), and the predefined log file is defined as `C:\Windows\Temp\ConfigurationTool.log`.

For more information on configuring logs check the [Change OutSystems Platform logging levels (OSTrace)](https://success.outsystems.com/Support/Enterprise_Customers/Troubleshooting/Change_OutSystems_Platform_logging_levels_(OSTrace)) topic.
