---
summary: To install and run OutSystems, you need permissions to change files in the file system, run services, listen to specific ports, and make changes to the database.
tags: support-devOps; support-installation; support-Installation_Configuration; support-Integrations_Extensions
locale: en-us
guid: e7fb04c6-9cb6-48d9-a4e7-8d4ad3702613
app_type: traditional web apps, mobile apps, reactive web apps
---

# Default Platform Server and database configurations

<div class="info" markdown="1">

This article applies to: **OutSystems 11**&#8195;&#8195;Other versions available: [10](https://success.outsystems.com/Documentation/10/Setting_Up_OutSystems/Default_Platform_Server_and_database_configurations)

</div>

To install and run OutSystems, you need permissions to change files in the file system, run services, listen to specific ports, and make changes to the database. Learn what permissions are needed.

## Server configurations

### Hardware

The Platform Server must run on a server deployed on bare metal or hardware virtualization technologies (e.g. VMware, KVM) with a fixed MAC address. Changing the MAC address (either by physically changing the network card, of through virtualization software) results in an invalid license.

Note: If your infrastructure is hosted in a cloud environment, changing the MAC address may not result in an invalid license since licensing may also be attached to the instance identifier.

### Software

All software required for installing the Platform Server is listed in the [Platform Server installation checklist](http://www.outsystems.com/goto/checklist-11).

### File system

All OutSystems components are installed by default at `C:\Program Files\OutSystems\`. If you install the development tools (Service Studio and Integration Studio), their preferences are stored at `C:\Users\<user name>\AppData\Roaming\OutSystems`.

Also, the OutSystems installers creates registry entries to store some configurations. These are stored at `HKEY_LOCAL_MACHINE > SOFTWARE > OutSystems`.

### Services

During the installation, OutSystems registers a set of services on the server. You can start and stop these services using the Windows Management Console.

|Service|Executable C:\Program Files\OutSystems\Platform Server|Configuration C:\Program Files\OutSystems\Platform Server|
|-------|-------|-------|
|SMS Connector|SmsConnector.exe|SmsConnector.exe.config|
|Compiler|CompilerService.exe|CompilerService.exe.config|
|DeployService|DeployService.exe|DeployService.exe.config|
|Log|LogServer.exe|LogServer.exe.config|
|Scheduler|Scheduler.exe|Scheduler.exe.config|

_Note:_ All OutSystems services must run with the **Local System account**.

The logs of these services are stored in Windows Event Viewer.


## Database configurations

### SQL Server

The SQL Server database must comply with the following requirements:

* If you are using SQL Server authentication, the authentication mode needs to be set to "Mixed Mode".

* When using Windows Authentication, all front-ends and controller must use the same domain as the database server.

* The collation of the SQL Server instance must be case-insensitive (CI_*).

* The collation of the database catalog must be Case Insensitive and should also be Accent Insensitive.

### Azure SQL Database

The Azure SQL Database catalog and database must comply with the following collation requirements:

* The database instance must be Case Insensitive.

* The database catalog must be Case Insensitive and should also be Accent Insensitive.

* Connecting to the Azure SQL Database using Windows Authentication is not supported.

### Oracle

To integrate with an Oracle database, the **NLS_CHARACTERSET** must be set to **WE8MSWIN1252** or **AL32UTF8**. Additionally, names of tables and columns you want to integrate must use uppercase letters only.

### DB2

To integrate with DB2 database for iSeries, the installation of the IBM iAccess software is required in all Front-End and Deployment Controller server machines.

## Application Server

The IIS needs to be set to [IIS6 compatibility mode](http://technet.microsoft.com/en-us/library/bb397374(v=exchg.80).aspx). To configure your IIS, simply use the Windows Server Manager console.

OutSystems applications are always deployed to the Default Web Site (identifier 1). For this reason, the Default Web Site cannot be renamed, and must listen to 127.0.0.1 on port 80 without any host headers.

In case of having multiple address entries in Default Web Site, the configuration 127.0.0.1:80 with no host headers must be on top of all other entries.

The Server.API component of the platform exposes REST endpoints that are consumed by other components like the Development Environment and LifeTime. Some of these endpoints expect PATCH requests, i.e. HTTP requests using the PATCH method. 
Make sure that any proxies and the IIS running in front-end servers are configured to allow the HTTP 'PATCH' method. Some OutSystems components will not work properly without it.

## Deployed applications

When an application is deployed, the OutSystems Deployment Service compiles the model developed using the development environment into valid .NET code.

### Applications source code

The server with the deployment controller role stores the application source code at: `C:\Program Files\OutSystems\Platform Server\share\<application name>\full`

### Compiled applications

During the deployment of an application, the Deployment Controller ensures the front-end servers have the compiled applications stored in the OutSystems installation folder, and proceeds to change the virtual directories in ISS to point to the new application folder.

The compiled applications are stored at:

* **Shared Libraries** - C:\Program Files\OutSystems\Platform Server\repository

* **Applications** - C:\Program Files\OutSystems\Platform Server\running

### Logging

OutSystems has built-in logic capabilities to monitor the applications during runtime. To ensure the performance of the applications is not compromised, the logs are performed asynchronously, using a message queue. For this, the OutSystems installer creates several queues in the Microsoft Message Queue, and configures them to not be persisted in secondary memory.

The LogServer process is then responsible to consume the messages in these queues and insert them in the OutSystems' Log tables. You can then use Service Center (the environment monitoring console) to consult the logs.
