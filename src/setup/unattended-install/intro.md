---
summary: Learn the unattended or automated processes of installing or updating OutSystems Platform Server, and adding a new front-end server.
tags: article-page; support-Installation_Configuration; support-Installation_Configuration-overview
---

# Unattended Installation and Upgrade

<pre class="script-css">
/* HIDE H2, H3, H4 AND H5 FROM TOC */
#mt-toc-container li li {
    display:none;
}
</pre>

<div class="info" markdown="1">

This article applies to: **OutSystems 11**&#8195;&#8195;Other versions available: [10](https://success.outsystems.com/Documentation/10/Setting_Up_OutSystems/Unattended_Installation_and_Upgrade)

</div>

The goal of this document is to describe the unattended or automated processes of installing or upgrading OutSystems Platform Server in application environments, and adding a new front-end server.

## Overview

OutSystems allows performing silent or automated Platform Server installations and upgrades, as well as adding a new front-end server.

The process for installing or upgrading OutSystems Platform Server in unattended mode involves the following high-level steps:

1. Install the OutSystems platform prerequisites
1. Install the Development Environment binaries
1. Install or upgrade the Platform Server binaries
1. Only for Oracle on first install: create the database users
1. Update the `server.hsconf` configuration file
1. Run the Configuration Tool
1. Upload the license file (requires manual intervention)
1. Only for upgrades: republish the entire factory

The following sections present detailed instructions on how to install, upgrade, and add front-end servers in unattended mode.

## Before you start

* Download the [Installation Checklist](http://www.outsystems.com/goto/checklist-11) from OutSystems website.

* The default paths used in the procedures below are the following:

    * `<development_environment_path>`= C:\Program Files\OutSystems\Development Environment 11
    * `<platform_path>`= C:\Program Files\OutSystems\Platform Server
    * `<outsystems_common_path>`= C:\Program Files\Common Files\OutSystems\11.0

    Adjust them if necessary.

## First install

### 1. Install the OutSystems platform prerequisites

The OutSystems Platform Server installation package can automatically [install most of the prerequisites](../intro.md#prerequisites) if you provide the optional `/InstallPrerequisites=True` switch.

If you prefer to install the prerequisites manually, follow the instructions in the **Pre-installation checklist** section of the Installation Checklist before running the installation package.

<div class="info" markdown="1">

**Notes**

When performing automatic prerequisites installation, the installation package will download the required binaries from the official Microsoft sources by default. However, you can also perform a fully [offline installation](<../intro.md#offline-installation>).

The automatic prerequisites installation has a timeout of 15 minutes. This ensures that any unexpected occurrences during this process (e.g. downloading the prerequisites binaries taking a very long time) do not lock an automated unattended installation indefinitely.

</div>

### 2. Install the Development Environment binaries

Run the OutSystems Development Environment installation package as follows:

```
DevelopmentEnvironment-<version>.exe /S [/D=<development_environment_path>]
```

The optional `/D` switch specifies the path where the Development Environment is installed. If this switch is provided, it must be the last one in the command line and the provided path must not contain quotes (`""`) even if the path contains spaces.

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

## Upgrade

### 1. Install the OutSystems platform prerequisites

The OutSystems Platform Server installation package can automatically [install most of the prerequisites](../intro.md#prerequisites) if you provide the optional `/InstallPrerequisites=True` switch.

If you prefer to install the prerequisites manually, follow the instructions in the **Pre-installation checklist** section of the Installation Checklist before running the installation package.

<div class="info" markdown="1">

**Notes**

The installation package, by default, automatically downloads the required binaries for installing the prerequisites from the official Microsoft sources. However, you can also perform a fully [offline installation](<../intro.md#offline-installation>).

The automatic prerequisites installation has a timeout of 15 minutes. This ensures that any unexpected occurrences during this process (e.g. downloading the prerequisites binaries taking a very long time) do not lock an automated unattended installation indefinitely.

</div>

### 2. Install the Development Environment binaries

If your Development Environment is no longer compatible with the Platform Server you are about to install, run the OutSystems Development Environment installation package as follows:

```
DevelopmentEnvironment-<version>.exe /S [/D=<development_environment_path>]
```

The optional `/D` switch specifies the path where the Development Environment is installed. If this switch is provided, it must be the last one in the command line and the provided path must not contain quotes (`""`) even if the path contains spaces.

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

## Exit Codes and Logging

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
