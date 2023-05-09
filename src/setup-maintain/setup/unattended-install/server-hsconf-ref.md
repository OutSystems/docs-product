---
summary: Complete reference for the server.hsconf configuration file.
tags: support-Installation_Configuration; support-Installation_Configuration-overview
locale: en-us
guid: dcc55c5d-8cd5-4850-9e88-fa385badc663
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# server.hsconf Configuration File Reference

<div class="info" markdown="1">

This article applies to: **OutSystems 11**&#8195;&#8195;Other versions available: [10](https://success.outsystems.com/Documentation/10/Setting_Up_OutSystems/Unattended_Installation_and_Upgrade/server.hsconf_Configuration_File_Reference)

</div>

The `server.hsconf` is an XML file with all necessary configurations for the OutSystems platform. The settings in the `server.hsconf` configuration file correspond to the settings that are available on the [user interface of the Configuration Tool](../../../ref/configuration-tool/intro.md).

To generate templates for the `server.hsconf` configuration file use the following [Configuration Tool command line](config-tool-ref.md) and choose the template that corresponds to your database management system:

```
ConfigurationTool.com /GenerateTemplates
```

The `server.hsconf` configuration file defines the settings in key-value pairs organized in categories, according to the following syntax:

```
<EnvironmentConfiguration>
<CATEGORY [ProviderKey="[SqlServer|Oracle]"]>
    <KEY [encrypted="[false|true]"]>VALUE</KEY>
    ...
</CATEGORY>
    ...
</EnvironmentConfiguration>
```

The following sections describe in detail the configurations that are available in each category of the configuration file.

## Platform Database Configuration

The following XML element defines the configurations in the Platform Database Configuration category:

```
<PlatformDatabaseConfiguration ProviderKey="[SqlServer|Oracle]">
    <KEY [encrypted="[false|true]"]>VALUE</KEY>
    ...
</PlatformDatabaseConfiguration>
```

The attribute `ProviderKey` specifies the database management system that the configurations apply to.

### Common Configurations

The following are the configurations that do not depend on the database management system:

|Key|Value|Description|
|---|-----|-----------|
|AdminUser|Name of the owner of the OutSystems metamodel tables.||
|AdminPassword*|Password of the owner of the OutSystems metamodel tables.|Configuration Tool will read the clear text password and save an encrypted version.|
|RuntimeUser|Name of the owner of the tables created in the Development Environment.||
|RuntimePassword*|Password of the owner of the tables created in the Development Environment.|Configuration Tool will read the clear text password and save an encrypted version.|
|RuntimeAdvancedSettings|Settings in ADO.NET format to be appended to the connection string for OutSystems services.|Allows you to use a specific connection string for the OutSystems applications.|
|ServicesAdvancedSettings|Settings in ADO.NET format to be appended to the connection string for OutSystems services.|Allows you to use a specific connection string for the OutSystems services.|

(*) Ignored for systems configured with SQL Server as the platform database, when using Windows Authentication.

### SQL Server/Azure SQL Database

The following are the configurations that are specific to SQL Server and Azure SQL Database:

|Key|Value|Description|
|---|-----|-----------|
|Unicode|"true" or "false".<br/>**Do not customize this field.** OutSystems only supports non-Unicode in legacy systems.|Defines if the database supports unicode or not.|
|UsedAuthenticationMode|"Database Authentication" (SQL Server and Azure SQL) or "Windows Authentication" (only SQL Server).|Authentication protocol to be used.|
|Server|Hostname or IP address of the database server.||
|Catalog|Database catalog to be used by OutSystems.||

### Oracle

The following are the configurations that are specific to Oracle:

|Key|Value|Description|
|---|-----|-----------|
|IntrospectionMethod|**Internal**, do not customize.||
|CI_AI|"true" or "false".<br/>**Internal**, do not customize.|Case insensitive and accent insensitive mode.|
|DateFunction|Function used to get date.<br/>**Internal**, do not customize.||
|DDLLockTimeout|Numeric value.<br/>**Internal**, do not customize.|Timeout used in DDL lock operations.|
|NamingType|"Service Name" or "TNS Name".|Connection mode used.|
|TNSName|Address name defined in the `tnsnames.ora` configuration file.|This option is only available when NamingType is set to "TNS Name".<br/>More information [here](http://www.outsystems.com/goto/oracle-tns-configuration).|
|Host|Hostname or IP address of the database server.|This option is only available when NamingType is set to "Service Name".<br/>More information [here](http://www.outsystems.com/goto/oracle-tns-configuration).|
|Port|Port where the database service listens.|This option is only available when NamingType is set to "Service Name".<br/>More information [here](http://www.outsystems.com/goto/oracle-tns-configuration).|
|ServiceName|Oracle database service name.|This option is only available when NamingType is set to "Service Name".<br/>More information [here](http://www.outsystems.com/goto/oracle-tns-configuration).|
|NLS_Language|NLS_LANG Language Oracle environment parameter.|Changes the locale of the messages returned by the Oracle driver.|
|NLS_Territory|NLS_LANG Territory Oracle environment parameter.|Changes the locale of the messages returned by the Oracle driver.|
|AdminTablespace|Table space where the system tables are stored.||
|IndexTablespace|Table space where all the indexes of the platform are stored.||
|RuntimeTablespace|Table space where the tables created in the Development Environment are stored.|

## Logging Database Configuration

The following XML element defines the configurations in the Logging Database Configuration category:

```
<LoggingDatabaseConfiguration ProviderKey="[SqlServer|Oracle]">
    <KEY [encrypted="[false|true]"]>VALUE</KEY>
    ...
</LoggingDatabaseConfiguration>
```

The attribute `ProviderKey` needs to match the `ProviderKey` value set in the Platform Database Configuration; this attribute specifies the database management system that the configurations apply to and it

### Common Configurations

The following are the configurations that do not depend on the database management system:

|Key|Value|Description|
|---|-----|-----------|
|AdminUser|Name of the owner of the OutSystems Logging metamodel tables.||
|AdminPassword*|Password of the owner of the OutSystems Logging metamodel tables.|Configuration Tool will read the clear text password and save an encrypted version.|
|RuntimeUser|Name of the user used to access logs at applications runtime.||
|RuntimePassword*|Password of the user used to access logs at applications runtime.|Configuration Tool will read the clear text password and save an encrypted version.|
|RuntimeAdvancedSettings|Settings in ADO.NET format to be appended to the connection string for OutSystems services.|Allows you to use a specific connection string for the OutSystems applications.|

(*) Ignored for systems configured with SQL Server as the platform database, when using Windows Authentication.

### SQL Server/Azure SQL Database

The following are the configurations that are specific to SQL Server and Azure SQL Database:

|Key|Value|Description|
|---|-----|-----------|
|Unicode|"true" or "false".<br/>**Do not customize this field.** OutSystems only supports non-Unicode in legacy systems.|Defines if the database supports unicode or not.|
|UsedAuthenticationMode|"Database Authentication" or "Windows Authentication".|Authentication protocol to be used. **Needs to match Platform Database Configuration.**|
|Server|Hostname or IP address of the database server.||
|Catalog|Database catalog to be used by Logging.||

### Oracle

The following are the configurations that are specific to Oracle:

|Key|Value|Description|
|---|-----|-----------|
|IntrospectionMethod|**Internal**, do not customize.||
|CI_AI|"true" or "false".<br/>**Internal**, do not customize.|Case insensitive and accent insensitive mode.|
|DateFunction|Function used to get date.<br/>**Internal**, do not customize.||
|DDLLockTimeout|Numeric value.<br/>**Internal**, do not customize.|Timeout used in DDL lock operations.|
|NamingType|"Service Name" or "TNS Name".|Connection mode used.|
|TNSName|Address name defined in the `tnsnames.ora` configuration file.|This option is only available when NamingType is set to "TNS Name".<br/>More information [here](http://www.outsystems.com/goto/oracle-tns-configuration).|
|Host|Hostname or IP address of the database server.|This option is only available when NamingType is set to "Service Name".<br/>More information [here](http://www.outsystems.com/goto/oracle-tns-configuration).|
|Port|Port where the database service listens.|This option is only available when NamingType is set to "Service Name".<br/>More information [here](http://www.outsystems.com/goto/oracle-tns-configuration).|
|ServiceName|Oracle database service name.|This option is only available when NamingType is set to "Service Name".<br/>More information [here](http://www.outsystems.com/goto/oracle-tns-configuration).|
|NLS_Language|NLS_LANG Language Oracle environment parameter.|Changes the locale of the messages returned by the Oracle driver.|
|NLS_Territory|NLS_LANG Territory Oracle environment parameter.|Changes the locale of the messages returned by the Oracle driver.|
|AdminTablespace|Table space where the system tables are stored.||
|IndexTablespace|Table space where all the indexes of the platform are stored.||
|RuntimeTablespace|Table space where the tables created in the Development Environment are stored.|
|LogTablespace|Table space where the logging tables are stored.||

## Session Database Configuration

The following XML element defines the configurations in the Session Database Configuration category:

```
<SessionDatabaseConfiguration ProviderKey="[SqlServer|Oracle]">
    <KEY [encrypted="[false|true]"]>VALUE</KEY>
    ...
</SessionDatabaseConfiguration>
```

The attribute `ProviderKey` needs to match the `ProviderKey` value set in the Platform Database Configuration; this attribute specifies the database management system that the configurations apply to.

### Common Configurations

The following are the configurations that do not depend on the database management system:

|Key|Value|Description|
|---|-----|-----------|
|SessionUser|Name of the owner of the OutSystems session metamodel tables.||
|SessionPassword*|Password of the owner of the OutSystems session metamodel tables.|Configuration Tool will read the clear text password and save an encrypted version.|
|SessionAdvancedSettings|Settings in ADO.NET format to be appended to the connection string for OutSystems services.|Allows you to use a specific connection string for the OutSystems applications.|
|DeleteExpiredSessionsAvoidLockRowCount|Numeric value.<br/>**Internal**, do not customize.|

(*) Ignored for systems configured with SQL Server as the platform database, when using Windows Authentication.

### SQL Server/Azure SQL Database 
The following are the configurations that are specific to SQL Server and Azure SQL Database:

|Key|Value|Description|
|---|-----|-----------|
|UsedAuthenticationMode|"Database Authentication" or "Windows Authentication".|Authentication protocol to be used.<br/>**Needs to match Platform Database Configuration.**|
|Server|Hostname or IP address to the database server.||
|Catalog|Database catalog to be used by OutSystems.||

### Oracle

The following are the configurations that are specific to Oracle:

|Key|Value|Description|
|---|-----|-----------|
|IntrospectionMethod|**Internal**, do not customize.||
|CI_AI|"true" or "false".<br/>**Internal**, do not customize.|Case insensitive and accent insensitive mode.|
|DateFunction|Function used to get date.<br/>**Internal**, do not customize.||
|DDLLockTimeout|Numeric value.<br/>**Internal**, do not customize.|Timeout used in DDL lock operations.|
|IdType|"Service Name" or "TNS Name".|Connection mode used.|
|TNSName|Address name defined in the `tnsnames.ora` configuration file.|This option is only available when IdType is set to "TNS Name".<br/>More information [here](http://www.outsystems.com/goto/oracle-tns-configuration).|
|Host|Hostname or IP address of the database server.|This option is only available when IdType is set to "Service Name".<br/>More information [here](http://www.outsystems.com/goto/oracle-tns-configuration).|
|Port|Port where the database service listens.|This option is only available when IdType is set to "Service Name".<br/>More information [here](http://www.outsystems.com/goto/oracle-tns-configuration).|
|ServiceName|Oracle database service name.|This option is only available when IdType is set to "Service Name".<br/>More information [here](http://www.outsystems.com/goto/oracle-tns-configuration).|
|NLS_Language|NLS_LANG Language Oracle environment parameter.|Changes the locale of the messages returned by the Oracle driver.|
|NLS_Territory|NLS_LANG Territory Oracle environment parameter.|Changes the locale of the messages returned by the Oracle driver.|
|SessionTablespace|Table space where the session tables are stored.||

## Service Configuration

The following XML element defines the configurations in the Service Configuration category:

```
<ServiceConfiguration>
    <KEY>VALUE</KEY>
    ...
</ServiceConfiguration>
```

The following are the available configurations:

|Key|Value|Description|
|---|-----|-----------|
|CompilerServerHostname|Hostname or IP address of the Deployment Controller Server.|To make it easier to add a front-end server later, we do not recommend using the value localhost as the hostname.|
|CompilerServerPort|Numeric value.|Port used by the Deployment Controller Service, in the Deployment Controller Server.|
|DeploymentServerPort|Numeric value.|Port used by the Deployment Service, in the Front-End Servers.|
|SchedulerServerPort|Numeric value.|Port used by the Scheduler Service, in the Front-End Servers.|
|SchedulerRESTPort|Numeric value.|Port used by the Scheduler Service, in the Front-End Servers when using the REST communication protocol.|
|SupportAsynchronousLog|"true" or "false".<br/>**Internal**, do not customize.||
|ServiceInitializationTimeoutInSeconds|Numeric value.|Timeout for services to restart. The default value is 180 seconds.|

## Server Configuration

The following XML element defines the configurations in the Server Configuration category:

```
<ServerConfiguration>
    <KEY>VALUE</KEY>
    ...
</ServerConfiguration>
```

The following are the available configurations:

| Key | Value | Description |
|-----|-------|-------------|
| ApplicationServerPort | **Internal**, do not customize. | The default port is 80. |
| ApplicationServerSecurePort | **Internal**, do not customize. | The default port is 443. |
| MaxConcurrentTimers | Numeric value. | Maximum number of Timers (asynchronous jobs) that can be executed at the same time in each Front-End Server. |
| PlatformServerAdminPassword | Password of the Platform Server Admin user. | The Configuration Tool will read the clear text password in this key and save an encrypted version in the database, setting it as the password for the Platform Server admin user. It will also remove this key from the file.<br/><br/>When the password is written directly in this file, the Configuration Tool will not enforce any validations, i.e. it will accept any value for the password.<br/>On the other hand, when defining this password using the Configuration Tool run in the command-line, the password must be at least 6 characters long and must not include the username. |
| WeeksToKeep | Numeric value. | Indicates for how long the log files are kept. After this time, the log tables are rotated and the information is lost. |

## Network Configuration

The following XML element defines the configurations in the Network Configuration category:

```
<NetworkConfiguration>
    <KEY>VALUE</KEY>
    ...
</NetworkConfiguration>
```

The following are the available configurations:

|Key|Value|Description|
|---|-----|-----------|
|ApplicationServerVersion|**Internal**, do not customize.||
|OutgoingIPAddress|IP address that the Front-End server will register in the Deployment Controller Service. Leave empty for automatic.||
|RequiresSoapHeadersSlowRetrieval|**Internal**, do not customize.||
|ServerKind|**Internal**, do not customize.||

## Cache Invalidation Configuration

The following XML element defines the configurations in the Cache Invalidation Configuration category:

```
<CacheInvalidationConfiguration>
    <KEY [encrypted="[false|true]"]>VALUE</KEY>
    ...
</CacheInvalidationConfiguration>
```

It’s used to configure communications to Cache Invalidation Service (for example RabbitMQ) by applications and OutSystems Services.

The following are the available configurations:

|Key|Value|Description|
|---|-----|-----------|
|ServiceHost|Hostname or IP address of the Cache Invalidation Service.|To make it easier to add a front-end server later, we do not recommend using the value localhost as the hostname.|
|ServicePort|Numeric value.|Port used by the Applications and Services to communicate with Cache Invalidation Service.|
|ServiceUsername|Name of the user of Invalidation Service used by OutSystems Platform.||
|ServicePassword|Password of the user of Invalidation Service used by OutSystems Platform.|Configuration Tool will read the clear text password and save an encrypted version.|
|VirtualHost|Name of virtual host of Invalidation Service used by OutSystems Platform. For example "/outsystems"|Enables you to reuse the Cache Invalidation Service for other purposes not connected to OutSystems logic.|
|TlsEnabled|Boolean|Enables the use of secure connections between application and the cache invalidation service.|
|TlsServerCanonicalName|The canonical name of the certificate being used by the cache invalidation service.||

## Other Configurations

The following XML element defines the configurations in the Other Configurations category:

```
<OtherConfigurations>
    <KEY>VALUE</KEY>
    ...
</OtherConfigurations>
```

The following are the available configurations:

|Key|Value|Description|
|---|-----|-----------|
|DBIntrospectionTimeout|Numeric value.|Default timeout for database queries that do metamodel introspection.|
|DBTimeout|Numeric value.|Default timeout for database queries to complete. The value can be overridden for each query in the Development Environment.|
|DBUpdateTimeout|Numeric value.|Default timeout for database updates to run when 1-Click Publishing an application.|
|InstallationDir|Path of the OutSystems platform installation.|Leave this setting as is, there is no need to configure.|
|InstanceName|**Internal**, do not customize.|Leave this setting as is, there is no need to configure.|
|PlatformVersion|Version of the OutSystems platform.|Leave this setting as is, there is no need to configure.|
|QueuesAvailable|"true" or "false".|Indicates if the messages queues are installed.|
