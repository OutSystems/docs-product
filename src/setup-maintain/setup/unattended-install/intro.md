---
summary: Learn the unattended or automated processes of installing or updating OutSystems Platform Server, and adding a new front-end server.
tags: article-page; support-Installation_Configuration; support-Installation_Configuration-overview
locale: en-us
guid: 4f39d91e-bc2f-4eac-a4ca-b8c660d97d0e
app_type: traditional web apps, mobile apps, reactive web apps
---

# Unattended Installation and Upgrade

<div class="info" markdown="1">

This article applies to: **OutSystems 11**&#8195;&#8195;Other versions available: [10](https://success.outsystems.com/Documentation/10/Setting_Up_OutSystems/Unattended_Installation_and_Upgrade)

</div>

This document describes the unattended or automated process of installing or upgrading the OutSystems Platform Server in application environments and adding a new front-end server.

Additionally, it describes how to perform the unattended installation or upgrade of the LifeTime Management Console.

## Overview

OutSystems allows performing silent or automated installations and upgrades of the Platform Server component, as well as adding a new front-end server.

The process for installing or upgrading the OutSystems Platform Server component in unattended mode involves the following high-level steps:

1. Install the OutSystems platform prerequisites
1. Install Service Studio and Integration Studio binaries
1. Install or upgrade the Platform Server binaries
1. Only for Oracle on first install: create the database users
1. Update the `server.hsconf` configuration file
1. Run the Configuration Tool
1. Upload the license file (requires manual intervention)
1. Only for upgrades: republish the entire factory

The following sections present detailed instructions on how to install or upgrade the OutSystems Platform Server component of your application environments in unattended mode, and add front-end servers.

The [LifeTime unattended installation and upgrade](#lifetime) explains how to use a similar process to execute the unattended installation or upgrade of the LifeTime Management Console environment.

## Before you start

* Make sure you are aware of the general process to [upgrade an OutSystems environment](https://success.outsystems.com/Support/Enterprise_Customers/Upgrading/01_Upgrade_OutSystems_Platform).

* Download the [Installation Checklist](http://www.outsystems.com/goto/checklist-11) from OutSystems website.

* If you are installing or upgrading to OutSystems Platform Server 11.7.1, use the following default paths:

    * ``<service_studio_path>= C:\Program Files\OutSystems\Service Studio 11``
    * ``<integration_studio_path>= C:\Program Files\OutSystems\Integration Studio``
    * ``<platform_path>= C:\Program Files\OutSystems\Platform Serve``
    * ``<outsystems_common_path>= C:\Program Files\Common Files\OutSystems\11.0``

    **Note** :If you previously had a Development Environment installed (in C:\Program Files\OutSystems\Development Environment 11), uninstall it to avoid installing Service Studio and Integration under the ``development_environment_path``.

* If you are installing or upgrading to  OutSystems Platform Server earlier than version 11.17.0, use the following default paths:

    * ``<development_environment_path>= C:\Program Files\OutSystems\Development Environment 11``
    * ``<platform_path>= C:\Program Files\OutSystems\Platform Server``
    * ``<outsystems_common_path>= C:\Program Files\Common Files\OutSystems\11.0``

## First install { #first-install }

### 1. Install the OutSystems platform prerequisites

The OutSystems Platform Server installation package can automatically [install most of the prerequisites](../intro.md#prerequisites) if you provide the optional `/InstallPrerequisites=True` switch.

If you prefer to install the prerequisites manually, follow the instructions in the **Pre-installation checklist** section of the Installation Checklist before running the installation package.

<div class="info" markdown="1">

**Notes**

When performing automatic prerequisites installation, the installation package will download the required binaries from the official Microsoft sources by default. However, you can also perform a fully [offline installation](<../intro.md#offline-installation>).

The automatic prerequisites installation has a timeout of 15 minutes. This ensures that any unexpected occurrences during this process (e.g. downloading the prerequisites binaries taking a very long time) do not lock an automated unattended installation indefinitely.

</div>

### 2. Install the Service Studio and Integration Studio binaries

* If you are installing or upgrading to OutSystems Platform Server 11.17.1 or later:

    * Run the OutSystems Service Studio installation executable as follows: ``ServiceStudio-<version>.exe /S [/D=<Service_Studio_path>]``

    * Run the OutSystems Integration Studio installation executable as follows: ``IntegrationStudio-<version>.exe/S[/D=<Integration_Studio_path>]``

* If you are installing or upgrading to OutSystems Platform Server 11.7.0 or earlier,  run the OutSystems Development Environment installation package as follows:

    * ``DevelopmentEnvironment-<version>.exe /S [/D=<development_environment_path>]``

The optional `/D` switch specifies the path where the Service Studio and Integration Studio is installed. If this switch is provided, it must be the last one in the command line and the provided path must not contain quotes (`""`) even if the path contains spaces.

### 3. Install the Platform Server binaries

Run the OutSystems Platform Server installation package as follows:

```
PlatformServer-<version>.exe /S [/InstallPrerequisites=True] [/DoTuning=<factory_size>] [/D=<platform_path>]
```

The optional `/InstallPrerequisites=True` switch specifies if the prerequisites will be automatically installed.  
The optional `/DoTuning=<factory_size>` switch specifies if the tuning should be automatically performed.  
The optional `/D` switch specifies the path where the OutSystems Platform Server is installed. If this switch is provided, it must be the last one in the command line and the provided path must not contain quotes (`""`) even if the path contains spaces.

For more information check the [Automatic Prerequisites Installation and Configuration Tuning](../intro.md#prerequisites).

### 4. Only for Oracle: create the database users

Follow the instructions in the **Database** section of the Installation Checklist.

### 5. Update the server.hsconf configuration file

Replace the default `<platform_path>\server.hsconf` file with a customized template containing your specific configurations.

To help create specific server configuration files, Configuration Tool can automatically generate different configuration file templates for each database engine on which OutSystems can run on. The templates refer to the operating system and application server where the Configuration Tool is running. You can check the [description of each parameter in the `server.hsconf` file](server-hsconf-ref.md).

Templates can be automatically generated before proceeding with the configuration steps of the unattended installation process (or even before the installation of the platform in the new machine, if you already have another machine where the platform is already installed), by using the following command line which will save them to the directory `<platform_path>\docs`:

```
<platform_path>\ConfigurationTool.com /GenerateTemplates
```

Keep in mind that configuration settings differ between OutSystems platform database.

To easily add a front-end later, the `CompilerServerHostname` parameter must include the name or IP of the machine and not `localhost`. The same applies to other parameters that refer hostnames.

Ensure that usernames and passwords are stored with the correct casing.

### 6. Run the Configuration Tool

This step configures the platform, installs Service Center and installs the System Components.

For SQL Server and Azure SQL Database:

```
<platform_path>\ConfigurationTool.com /SetupInstall <platform_db_admin_username> <platform_db_admin_password> [<logging_db_admin_username> <logging_db_admin_password>]
    /SetPlatformServerAdminPassword <platform_server_admin_password>
    /RebuildSession <session_db_admin_username> <session_db_admin_password>
    /CreateUpgradeCacheInvalidationService
    /InstallServiceCenter
    /InstallSystemComponents
```

For Oracle:

```
<platform_path>\ConfigurationTool.com /SetupInstall
    /SetPlatformServerAdminPassword <platform_server_admin_password>
    /RebuildSession <session_db_admin_username> <session_db_admin_password>
    /CreateUpgradeCacheInvalidationService
    /InstallServiceCenter
    /InstallSystemComponents
```

### 7. Upload license file (requires manual intervention)

Manually obtain a valid OutSystems platform license from [www.outsystems.com/licensing](http://www.outsystems.com/licensing) using the environment activation code.

```
<platform_path>\ConfigurationTool.com /UploadLicense <license_file.lic>
```

## Upgrade { #upgrade }

### 1. Install the OutSystems platform prerequisites

The OutSystems Platform Server installation package can automatically [install most of the prerequisites](../intro.md#prerequisites) if you provide the optional `/InstallPrerequisites=True` switch.

If you prefer to install the prerequisites manually, follow the instructions in the **Pre-installation checklist** section of the Installation Checklist before running the installation package.

<div class="info" markdown="1">

**Notes**

The installation package, by default, automatically downloads the required binaries for installing the prerequisites from the official Microsoft sources. However, you can also perform a fully [offline installation](<../intro.md#offline-installation>).

The automatic prerequisites installation has a timeout of 15 minutes. This ensures that any unexpected occurrences during this process (for example, downloading the prerequisites binaries taking a very long time) do not lock an automated unattended installation indefinitely.

</div>

### 2. Install Service Studio and Integration Studio binaries

* If you are installing or upgrading to OutSystems Platform Server 11.17.1 or later:

    * Run the OutSystems Service Studio installation executable as follows: ``ServiceStudio-<version>.exe /S [/D=<Service_Studio_path>]``
    * Run the OutSystems Integration Studio installation executable as follows: ``IntegrationStudio-<version>.exe /S [/D=<Integration_Studio_path>``

    **Note**: If you previously had a Development Environment installed (in C:\Program Files\OutSystems\Development Environment 11),  uninstall it to avoid installing Service Studio and Integration under the ``development_environment_path``.

* If you are installing or upgrading to OutSystems Platform Server 11.17.0 or earlier, run the OutSystems Development Environment installation package as follows:


    * ``DevelopmentEnvironment-<version>.exe /S [/D=<development_environment_path>]``

    The optional `/D` switch specifies the path where the  Service Studio and Integration Studio is installed. If this switch is provided, it must be the last one in the command line and the provided path must not contain quotes (`""`) even if the path contains spaces.

### 3. Upgrade the Platform Server binaries

Run the OutSystems Platform Server installation package as follows:

```
PlatformServer-<version>.exe /S [/InstallPrerequisites=True] [/DoTuning=<factory_size>] [/D=<platform_path>]
```

The optional `/InstallPrerequisites=True` switch specifies if the prerequisites will be automatically installed.  
The optional `/DoTuning=<factory_size>` switch specifies if the tuning should be automatically performed.  
The optional `/D` switch is ignored in an upgrade scenario.

For more information check the [Automatic Prerequisites Installation and Configuration Tuning](../intro.md#prerequisites).

### 4. Update the server.hsconf configuration file

Skip this step if no changes are necessary to the running configuration and that configuration file templates haven't changed.

### 5. Run the Configuration Tool { #upgrade-step-5 }

This step configures the platform, installs Service Center, and installs the System Components. Depending on your upgrade scenario, this step also starts [preparing your modules](https://success.outsystems.com/Support/Enterprise_Customers/Upgrading/Modules_preparation_step_during_Platform_Server_upgrade) for the new Platform Server version.

#### 5.1 Minor upgrades

If you are upgrading from **Platform Server 11.x** to **Platform Server 11.12 or later**, after the Platform Server is upgraded, you can publish your applications gradually, following your teams' pace. You can also opt to republish all your applications right after the upgrade, but it's not a mandatory step.

If you plan to **publish your applications gradually**, run the Configuration Tool as follows:

```
<platform_path>\ConfigurationTool.com /UpgradeInstall [<admin_password>]
    [/SetPlatformServerAdminPassword <platform_server_admin_password>]
    [/RebuildSession <session_db_admin_username> <session_db_admin_password>]
    [/CreateUpgradeCacheInvalidationService]
    /UpgradeEnvironment
```

The above command sets the Configuration Tool to start [preparing your modules](https://success.outsystems.com/Support/Enterprise_Customers/Upgrading/01_Upgrade_OutSystems_Platform) for the new Platform Server version, without deploying them. In this scenario, you won't execute [Step 7](#upgrade-step-7) to republish all applications.

If you plan to **republish all your applications right after the upgrade**, use the following instead:

```
<platform_path>\ConfigurationTool.com /UpgradeInstall [<admin_password>]
    [/SetPlatformServerAdminPassword <platform_server_admin_password>]
    [/RebuildSession <session_db_admin_username> <session_db_admin_password>]
    [/CreateUpgradeCacheInvalidationService]
    /InstallServiceCenter
    /InstallSystemComponents
```

The above command skips the modules preparation step. In this scenario, you need to execute [Step 7](#upgrade-step-7) to republish all applications right after the upgrade.

**Note:** In both cases, you need to include the `/SetPlatformServerAdminPassword <platform_server_admin_password>` argument if the Admin user of Platform Server is active and its password is still defined as 'admin'.

#### 5.2 Major upgrades

If you are upgrading from **Platform Server 10 or previous** to **Platform Server 11**, run the Configuration Tool as follows:

```
<platform_path>\ConfigurationTool.com /UpgradeInstall [<admin_password>]
    [/SetPlatformServerAdminPassword <platform_server_admin_password>]
    [/RebuildSession <session_db_admin_username> <session_db_admin_password>]
    [/CreateUpgradeCacheInvalidationService]
    /UpgradeEnvironment
```

**Note:** You need to include the `/SetPlatformServerAdminPassword <platform_server_admin_password>` argument if the Admin user of Platform Server is active and its password is still defined as 'admin'.

In major upgrades, the module preparation is skipped, thus you are required to republish all applications right after the upgrade ([Step 7](#upgrade-step-7)).

### 6. Upload the license file (requires manual intervention)

Skip this step if the existing license is valid for the OutSystems version you're upgrading to.

Manually obtain a valid OutSystems platform license from [www.outsystems.com/licensing](http://www.outsystems.com/licensing) using the environment activation code.

```
<platform_path>\ConfigurationTool.com /UploadLicense <license_file.lic>
```

### 7. Only for upgrades: republish the entire factory { #upgrade-step-7 }

<div class="info" markdown="1">

This step is not mandatory for minor upgrades. Don't run this step if you are doing a **minor upgrade** and you plan to **publish your applications gradually**. For this case, you must run the Configuration Tool in [Step 5](#upgrade-step-5) to start preparing your modules for the new Platform Server version, without deploying them.

</div>

Execute this step only if you are:

* Doing a major upgrade (from **Platform Server 10 or previous** to **Platform Server 11**)
* Doing a minor upgrade, and you opt to **republish all your applications** right after the upgrade

Run the following:

```
<outsystems_common_path>\OSPTool.com /PublishFactory <hostname> <username> <password>
```

## Adding a Front-End

<div class="info" markdown="1">

When adding a new front-end server to your environment, make sure that:

* There are no ongoing deployments or solution publishes, and also no prepared deployments to continue, in case you have [two-stage deployments](../../../managing-the-applications-lifecycle/deploy-applications/deploy-in-a-short-deployment-window.md) enabled in the environment. Having ongoing or prepared deployments when adding a new front-end server might prevent the correct deployment of the modules.

* The new front-end server is a clean installation, it doesn't contain settings or deployed applications from a previous OutSystems installation. Otherwise, you might need to republish all the environment modules or the deployment of new applications might fail.

</div>

### 1. Install the Platform Server binaries

Implies execution of the steps described in the **Pre-installation Checklist** (e.g. server roles and features, services options). The OutSystems Platform Server installation package can [automatically install most of the prerequisites](../intro.md#prerequisites).

Run the OutSystems Platform Server installation package as follows:

```
PlatformServer-<version>.exe /S [/InstallPrerequisites=True] [/DoTuning=<factory_size>] [/D=<platform_path>]
```

The optional `/InstallPrerequisites=True` switch specifies if the prerequisites will be automatically installed.  
The optional `/DoTuning=<factory_size>` switch specifies if the tuning should be automatically performed.  
The optional `/D` switch specifies the path where the OutSystems Platform Server is installed. If this switch is provided, it must be the last one in the command line and the provided path must not contain quotes (`""`) even if the path contains spaces.

For more information check the [Automatic Prerequisites Installation and Configuration Tuning](../intro.md#prerequisites).

### 2. Copy the configuration files from the controller node to the front-end

In order for this step to be successful, the `server.hsconf` file in the deployment controller machine **must not** refer to `localhost` in any hostname parameter, namely the deployment controller hostname and cache service hostname. If that is not true, you will need to run the Configuration Tool on the controller machine and change that address, before continuing with this step.

Copy the following files from the **controller** machine to the **front-end** machine, keeping the same path:

* `<platform_path>\private.key`

* `<platform_path>\server.hsconf`

### 3. Run the Configuration Tool

For SQL Server and Azure SQL Database:

```
<platform_path>\ConfigurationTool.com /UpgradeInstall
```

For Oracle:

```
<platform_path>\ConfigurationTool.com /UpgradeInstall
```

## Exit codes and logging

The OutSystems Platform Server installation package will return different exit codes depending on the install status:

* **0** = successful install  
* **1** = system reboot is required to finalize prerequisite installation (only detected when the Platform Server installation package is automatically installing the prerequisites)  
* **2** = install failure

Capturing these exit codes requires that the installer package is executed inside the context of its own command shell.

You can check the logs generated by the installer package for detailed information. They are located in the following folder:

* `%LocalAppData%\OutSystems\PlatformInstaller`  
(the default path is `C:\Users\<current_user>\AppData\Local\OutSystems\PlatformInstaller`)

Where `<current_user>` is the user installing the platform. The available log files are the following:

`PrerequisitesCheck.log`
:   Lists all the steps done to check what prerequisites are installed and/or missing.

`PrerequisitesInstall.log`
:   Lists all the steps done when installing  missing prerequisites (if applicable).

`PerformanceTuningCheck.log`
:   Lists all the steps done to check which tuning optimizations can be performed.

`PerformanceTuning.log`
:   Lists all the steps done to perform tuning optimizations (if applicable).

## LifeTime unattended installation and upgrade { #lifetime }

The LifeTime Management Console comprises the following parts:

* Platform Server component (the version can be different from your application environments)
* LifeTime application

Therefore, the unattended installation and upgrade process for the LifeTime environment is very similar to the process described above for your application environments.

Before you start:

* Make sure you are aware of the general process to [upgrade your LifeTime management console](https://success.outsystems.com/Support/Enterprise_Customers/Upgrading/Upgrade_LifeTime_management_console).

* LifeTime unattended installation and upgrade process doesn't apply to major upgrades (for example, from Platform Server 10 or previous to Platform Server 11).

To perform the unattended installation or upgrade of your LifeTime Management Console, do the following:

1. Execute all the steps described in the [First install](#first-install) section, for installing LifeTime, or in the [Upgrade](#upgrade) section, for upgrading LifeTime, **using the LifeTime installation package**, `LifeTimeWithPlatformServer-<version>.exe`, instead of the Platform Server package, `PlatformServer-<version>.exe`. All the options apply to both installation packages.

1. Run the following command to install the LifeTime application solution:

    ```
    <outsystems_common_path>\OSPTool.com /Publish "LifeTime.osp" <hostname> <username> <password>
    ```
