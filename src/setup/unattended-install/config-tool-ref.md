---
summary: Complete reference for the Configuration Tool command line.
tags: support-Installation_Configuration; support-Installation_Configuration-overview
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
    | /SCInstall 
    | /UpgradeSystemComponents
    | /UpgradePublishedApplications
    | /GenerateTemplates
    | /ClearInternalNetwork
    | /UploadLicense <license_file> <platform_server_admin_user> <platform_server_admin_password>
    | /RegenerateSettingsKey
    | /GetSerial
    | /SetPlatformServerAdminPassword <platform_server_admin_password>
    | /GetDeploymentZones
    | /ModifyDeploymentZone <deployment_zone_name> <deployment_zone_address> [<enable_https>]
    | /CreateUpgradeCacheInvalidationService
    | /EnableServerAPI
    | /DisableServerAPI
    | /UpgradeEnvironment
```

## Parameters

`/SetupInstall [<platform_db_admin_username> <platform_db_admin_password> <logging_db_admin_username> <logging_db_admin_password>] [/SetPlatformServerAdminPassword platform_server_admin_password]`

:   Creates or upgrades the OutSystems platform and logging database model using the `server.hsconf` configuration file.

    For SQL Server of Azure SQL databases, you must provide the credentials needed to create or upgrade the platform database. Furthermore, if you specify separate platform and logging databases in `server.hsconf`, you also need to provide the credentials needed to create or upgrade the logging database.

    For Oracle databases, you do not need to provide the admin usernames and passwords.
    
    If you provide the optional `/SetPlatformServerAdminPassword` parameter with a password, sets the password for the Platform Server `admin` user.

`/UpgradeInstall [<integrated_auth_admin_password>] [/SetPlatformServerAdminPassword <platform_server_admin_password>]`

:   Upgrades the OutSystems platform and logging database models, without validating if the database exists or if the permissions are correct.

    The admin password is optional and is only used for integrated authentication purposes where the password isn’t stored in the server configuration file.
    
    If you provide the optional `/SetPlatformServerAdminPassword` parameter with a password, sets the password for the Platform Server `admin` user.

`/RebuildSession <session_db_admin_username> <session_db_admin_password>`

:   Upgrades the session database model. The username and password provided must belong to a user with permissions to execute these operations.

`/SCInstall`

:   Forces the Service Center installation to run after finishing Configuration Tool.

`/UpgradeSystemComponents`

:   Forces the System Components installation or upgrade to run after applying the configuration settings.

`/UpgradePublishedApplications`

:   Forces the published applications upgrade to run after applying the configuration settings.

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
    Note: This command does not work when using Integrated Authentication.
    
`/GetDeploymentZones`

:   Lists the configured deployment zones for the current installation. The data is presented in JSON format, limited to the relevant settings that can be manipulated with `/ModifyDeploymentZone`, namely: the Configuration Name and Address, and it's Enable HTTPS status.

`/ModifyDeploymentZone <deployment_zone_name> <deployment_zone_address> [<enable_https>]`

:   Modifies the Address and/or Enable HTTPS settings of a Deployment Zone.

    `<deployment_zone_name>` is the Deployment Zone that you want to modify; this argument is case insensitive (for example "GLOBAL" will map to "Global").

    `<deployment_zone_address>` is the new address for the target Deployment Zone.

    `[<enable_https>]` is an optional boolean argument; if this argument is not provided the setting will remain unchanged. If the string "true" (case insensitive) is provided, the Enable HTTPS setting is set to "true"; if any other string is provided the setting Enable HTTPS is set to "false". The applied value of the Enable HTTPS setting is displayed.

`/CreateUpgradeCacheInvalidationService`

:   Installs cache invalidation service or reconfigures the service given in the configuration file (`server.hsconf`).
    
`/EnableServerAPI`

:   Enables Server.API and Server.Identity on this machine. (Server.API and Server.Identity are enabled by default)

`/DisableServerAPI`

:   Disables Server.API and Server.Identity on this machine. Beware, Service Center will not work without them.

`/UpgradeEnvironment`

:   Installs Service Center and System Components, and upgrades published applications. Skips any of these steps if they were previously executed.

## Example

Perform a clean installation for SQL Server or Azure SQL:

```
ConfigurationTool.com
    /SetupInstall <platform_db_admin_username> <platform_db_admin_password> <logging_db_admin_username> <logging_db_admin_password>
    /RebuildSession <session_db_admin_username> <session_db_admin_password>
    /CreateUpgradeCacheInvalidationService
    /SCInstall
```

Perform a clean installation for Oracle:

```
ConfigurationTool.com
    /SetupInstall
    /RebuildSession <session_db_admin_username> <session_db_admin_password>
    /CreateUpgradeCacheInvalidationService
    /SCInstall
```

Perform an upgrade from OutSystems 10 (or lower):

```
ConfigurationTool.com
    /UpgradeInstall <integrated_auth_admin_password>
    /RebuildSession <session_db_admin_username> <session_db_admin_password>
    /CreateUpgradeCacheInvalidationService
    /SCInstall
```

Perform an upgrade from OutSystems 11:

```
ConfigurationTool.com
    /UpgradeInstall <integrated_auth_admin_password>
    /RebuildSession <session_db_admin_username> <session_db_admin_password>
    /SCInstall
```

Modify the Address and/or Enable HTTPS settings of the "Global" deployment zone:

```
ConfigurationTool.com
    /ModifyDeploymentZone "Global" <zone_address> [<enable_https>]
```

Disable Server.API and Server.Identity:

```
ConfigurationTool.com
    /DisableServerAPI
```

Enable Server.API and Server.Identity:

```
ConfigurationTool.com
    /EnabelServerAPI
```

## Logging

By default, the Configuration Tool has logging enabled with log level `4` (Verbose), and the predefined log file is defined as `C:\Windows\Temp\ConfigurationTool.log`.

For more information on configuring logs check the [Change OutSystems Platform logging levels (OSTrace)](https://success.outsystems.com/Support/Enterprise_Customers/Troubleshooting/Change_OutSystems_Platform_logging_levels_(OSTrace)) topic.
