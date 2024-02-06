---
summary: Check the hardware and software requirements to install OutSystems on-premises.
tags: 
locale: en-us
guid: 244db17a-7a98-4cb0-93c0-db91f1c91fd8
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: 
---

# OutSystems system requirements

<div class="info" markdown="1">

This article applies to: **OutSystems 11**&#8195;&#8195;Other versions available: [10](https://success.outsystems.com/Documentation/10/Setting_Up_OutSystems/OutSystems_system_requirements)&#8195;[9.1](https://www.outsystems.com/Downloads/ScreenDetails.aspx?MajorVersion=9&ReleaseId=18346&ComponentName=Platform+Server)&#8195;[9.0](https://www.outsystems.com/Downloads/ScreenDetails.aspx?MajorVersion=9&ReleaseId=19270&ComponentName=Platform+Server)

</div>

Before installing OutSystems on-premises, check if your set up meets the hardware and software requirements listed in this article. To start the installation, refer to [Setting Up OutSystems](intro.md).

## Platform server

The following are the requirements for installing the Platform Server in your data center.

### Hardware (minimum requirements)

* Dual-core processor
* 4 GB of RAM
* 80 GB of free disk space

### Operating system

* Microsoft Windows Server 2022 (Standard Edition or higher edition), since Platform Server 11.20.0<sup>1</sup>
* Microsoft Windows Server 2019 (Standard Edition or higher edition), since Platform Server Release Jul.2019
* Microsoft Windows Server 2016 (Standard Edition or higher edition)

OutSystems only supports Windows editions that are [supported by Microsoft](https://support.microsoft.com/en-us/lifecycle/search).

<sup>1</sup> When installing the Platform Server on Windows Server 2022, or upgrading an existing installation to Windows Server 2022, consider increasing the CPU and memory of the machines as the Operating System itself requires more resources.


The supported Operating System configurations must be deployed on bare metal or hardware virtualization technologies (for example, VMware or KVM).

Future revisions of OutSystems may require the installation of an update within the major versions mentioned in the previous list.

### Application server

* Microsoft Internet Information Services (IIS) 10.0 or higher configured with a valid SSL certificate emitted by a public certificate authority. The SSL Certificate can alternatively be installed at a load balancer or reverse proxy level in [end-to-end SSL and SSL offloading](https://success.outsystems.com/documentation/how_to_guides/infrastructure/using_outsystems_in_reverse_proxy_scenarios/outsystems_configurations_in_reverse_proxy_scenarios/#ssl-offloading) configurations.

### Database management system

Use the same type of database engine for all the 3 databases in Platform Server (platform and apps, logs, session). OutSystems does not support a combination of database engines. For example, you can't use SQL Server for the platform database and Azure SQL database for the logs/session databases (or any other combination).

* Microsoft SQL Server 2019 or higher, with compatibility level 150, since Platform Server 11.12.0 <sup>1</sup>
* Microsoft SQL Server 2017 (Web Edition or higher edition)<sup>1</sup>
* Microsoft SQL Server 2016 (Web Edition or higher edition)<sup>1</sup>
* Microsoft SQL Server 2014 (Web Edition or higher edition)<sup>1</sup>
* Azure SQL Database V12
* Oracle 19c (Standard Edition or Enterprise Edition), since Platform Server 11 – Release Oct.2019 CP3
* Oracle 18c (Standard Edition or Enterprise Edition), since Platform Server 11 – Release Oct.2019 CP2
* Oracle 12c (12.1 or 12.2, Standard Edition or Enterprise Edition)

<sup>1</sup> Developer and Express editions of Microsoft SQL Server (any version) aren't supported.

Future revisions of OutSystems may require the installation of an update within the major versions mentioned in the previous list.

Apart from standard Oracle Database setups, OutSystems platform 8.0 and onwards works with [Oracle Exadata Database Machines](http://www.oracle.com/us/products/database/exadata/overview/index.html) running with Oracle Linux 5.5 or higher.

### Additional software requirements

* Microsoft .NET Framework 4.8 (supported since Platform Server 11 – Release Oct.2019 CP2) or Microsoft .NET Framework 4.7.2
* Microsoft Build Tools 2015
* .NET 6.0 Runtime & Hosting Bundle for Windows
* Microsoft Visual C++ 2015-2022 Redistributable (x64) (only for Platform Server version 11.21.0 or above)

Future revisions of OutSystems may require the installation of an update within the major versions mentioned in the previous list.

## Cache invalidation service

The cache invalidation service requires the following minimum version of RabbitMQ Server:

* RabbitMQ Server 3.10.14 with Erlang version 25.1.2, since Platform Server 11.19.0
* RabbitMQ Server 3.9.11 with Erlang version 24.2, from Platform Server 11.15.0 to 11.18.1
* RabbitMQ Server 3.8.21 with Erlang version 23.2, from Platform Server 11.13.2 to 11.14.1
* RabbitMQ Server 3.8.3 with Erlang version 22.3, from Platform Server 11.9.0 to 11.13.1
* RabbitMQ Server 3.7.7 with Erlang version 20.3, for earlier versions of Platform Server

These versions can be upgraded to the latest minor version compliant with the [official documentation](https://www.rabbitmq.com/which-erlang.html).

During Platform Server installation, OutSystems provides you with a script that simplifies the local installation of these two components (RabbitMQ Server and Erlang). Alternatively, you can use an existing RabbitMQ Server and Erlang installation, if it fulfills the same version requirements.

## Amazon EC2 considerations

OutSystems can run on Amazon EC2 instances. Each instance must fulfill the following requirements:

* The EC2Config service must be running

For more information on how to enable this service, refer to [Amazon EC2Config service documentation](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2config-service.html).

## Amazon RDS considerations

OutSystems supports Microsoft SQL Server 2019 and compatibility level 150 (since Platform Server 11.12.0), Microsoft SQL Server 2016, Microsoft SQL Server 2017, Oracle 12c, Oracle 18c, and Oracle 19c on Amazon RDS. The database instance class must fulfill the following requirements:

* 1 vCPU (virtual central processing unit) or higher
* 1 ECU (EC2 Compute Unit) or higher
* 3.75 GiB of memory or higher
* "Moderate" network performance or higher

Example of a DB instance class fulfilling these requirements: "db.t2.medium".

Oracle 18c on Amazon RDS is supported since Platform Server 11 – Release Oct.2019 CP2.
Oracle 19c on Amazon RDS is supported since Platform Server 11 – Release Oct.2019 CP3.

For more information on the available DB instance classes, refer to [Amazon's DB Instance Class](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html).To learn more about Amazon RDS limitations, refer to [Amazon RDS System Requirements](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html).

## Microsoft Azure considerations

OutSystems supports Microsoft Azure SQL Database V12 with the following considerations:

* The database service tier must be at least "S3".
* The MDC (Multiple Database Catalogs) feature isn't supported.
* Connecting to Azure SQL database using Windows authentication isn't supported.
* Private endpoints aren't supported, due to a limitation on how Microsoft implements them.
* Customizing the timezone from UTC isn't supported in Azure SQL database.

OutSystems also supports SQL Server running on an Azure virtual machine.

## Integration with external systems

The following systems are certified to integrate with OutSystems.

### SQL Server Database

* Microsoft SQL Server 2019 or higher, with compatibility level 150, since Platform Server 11.12.0
* Microsoft SQL Server 2017
* Microsoft SQL Server 2016
* Microsoft SQL Server 2014
* Microsoft SQL Server 2012
* Microsoft SQL Server 2008 R2
* Microsoft SQL Server 2008

### Azure SQL database

* Azure SQL Database available in the cloud

### Oracle database

* Oracle 19c (Standard Edition or Enterprise Edition), since Platform Server 11 – Release Oct.2019 CP3
* Oracle 18c (Standard Edition or Enterprise Edition), since Platform Server 11 – Release Oct.2019 CP2
* Oracle 12c (12.1 and 12.2, Standard Edition or Enterprise Edition)
* Oracle 11g R2 (Standard Edition or Enterprise Edition). From Platform Server 11.25.0, Oracle 11g R2 is no longer supported.

The **NLS_CHARACTERSET** must be set to **WE8MSWIN1252** or **AL32UTF8**.

<div class="info" markdown="1">

From OutSystems 11 Platform Server Release Oct.2019 onwards you can't have integrations with Oracle databases earlier than 11g R2.

</div>

### MySQL database

* MySQL 5.6 (5.6.5 or later within the 5.6 version, all editions)
* MySQL 5.7 (5.7.22 or later within the 5.7 version, all editions)
* MySQL 8.0 (8.0.28 or later within the 8.0 version, all editions), since Platform Server 11.19.0

### PostgreSQL database

* PostgreSQL 12.x.x, since Platform Server 11.15.0
* PostgreSQL 13.x.x, since Platform Server 11.15.0

### Aurora PostgreSQL database

* Aurora PostgreSQL database available in the cloud running a version compatible with a [supported PostgreSQL database](#postgresql-database), since Platform Server 11.15.0

### IBM database

* DB2 for iSeries V6R1 or higher
* **OutSystems** supports integration with DB2 databases hosted in iSeries machines only. It doesn't support integration with DB2 databases hosted in Unix, Linux, or Windows.

<div class="info" markdown="1">

The installation of the IBM i Access Client Solutions - Windows Application Package software is required in all Front-End and Deployment Controller server machines.

The use of double-byte characters with DB2 databases isn't supported.

</div>

### MongoDB database

* MongoDB Atlas and on-premises
* MongoDB 4.X
* MongoDB 5.X
* MongoDB 6.X
* MongoDB 7.0

### SAP

* SAP ERP R/3 4.6 or higher
* SAP ECC 5.0 or higher
* SAP S/4HANA

## Development tools

To develop your applications using OutSystems, you must install **Service Studio** and **Integration Studio** development tools on your desktop.
You can download the latest version of development tools from the [OutSystems downloads page](https://www.outsystems.com/Downloads/).

### Service Studio

Before setting up Service Studio make sure that your computer meets the following requirements:

### Hardware (minimum requirements)

* 1.8 GHz dual-core processor or better.
* 2 GB of RAM (4 GB recommended).
* 1 GB of free disk space

#### Operating System

**macOS (cross-platform Service Studio only):**

* macOS Big Sur
* macOS Monterrey

**Windows:**

* Windows 11 (64-bit) since Service Studio 11.54.45
* Windows 10 (64-bit)
* Microsoft Windows Server 2019
* Microsoft Windows Server 2016

 OutSystems only supports Windows and macOS editions that are supported by [Microsoft](https://support.microsoft.com/en-us/lifecycle/search) and Apple respectively.

#### Required software

* Google Chrome version 54 or later, or Microsoft Edge
:   To perform client-side debugging in Service Studio using a  desktop browser 
* Android device drivers
:   To perform client-side debugging on an Android mobile device if the device isn't recognized automatically
* iTunes 12.1.3 or later
:   To perform client-side debugging on an iOS mobile device

### Integration Studio

The installation requirements for Integration Studio are as follows:

#### Hardware (minimum requirements)

* 1.8 GHz dual-core processor (or better)
* 2 GB of RAM (4 GB recommended)
* 1 GB of free disk space

Limitations:

* The touch feature of touch screen devices isn't supported, however, you can use touch screen devices with keyboard and mouse.

#### Operating System

* Windows 10 (64-bit)
* Microsoft Windows Server 2019, since Development Environment 11.6.5
* Microsoft Windows Server 2016

OutSystems only supports Windows editions that are [supported by Microsoft](https:mm//support.microsoft.com/en-us/lifecycle/search).

#### Required software

* Microsoft .NET Framework 4.7.2 (or higher)
* Visual Studio 2015, Visual Studio 2017, or Visual Studio 2019 (since development environment 11.6.7)
:   To integrate with external systems using Integration Studio and to edit source code extension actions

## End user requirements

Running an OutSystems app on a browser is supported for 6 months after the end-of-support date announced by OutSystems for that browser.

### Reactive Web apps

Use the most current stable version of the following browsers:

* Edge 
* Firefox 
* Google Chrome 
* Safari 

### Progressive Web Apps

* Default browser for latest stable version of Android
* Default browser for latest stable version of iOS

### Mobile App packages

For more information on the supported Android and iOS platform versions, refer to [Mobile Apps Build Service (MABS)](https://success.outsystems.com/Support/Release_Notes/Mobile_Apps_Build_Service_Versions)

### Traditional Web apps

**Desktop browsers**

Use the most current stable version of the following browsers:

* Internet Explorer 
* Edge 
* Firefox 
* Google Chrome
* Safari

**Mobile device browsers**

* Default browser for iOS 7 or higher
* Default browser for Android 4.1 or higher
* Default browser for Windows Phone 8 or higher
