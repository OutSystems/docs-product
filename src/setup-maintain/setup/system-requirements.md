---
summary: Check the hardware and software requirements to install OutSystems on-premises.
tags: support-Application_Troubleshooting; support-installation; support-Installation_Configuration; support-Installation_Configuration-overview
locale: en-us
guid: 244db17a-7a98-4cb0-93c0-db91f1c91fd8
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# OutSystems system requirements

<div class="info" markdown="1">

This article applies to: **OutSystems 11**&#8195;&#8195;Other versions available: [10](https://success.outsystems.com/Documentation/10/Setting_Up_OutSystems/OutSystems_system_requirements)&#8195;[9.1](https://www.outsystems.com/Downloads/ScreenDetails.aspx?MajorVersion=9&ReleaseId=18346&ComponentName=Platform+Server)&#8195;[9.0](https://www.outsystems.com/Downloads/ScreenDetails.aspx?MajorVersion=9&ReleaseId=19270&ComponentName=Platform+Server)

</div>

Before installing OutSystems on-premises, check its hardware and software requirements. Once you're ready to start the installation, head to [Setting Up OutSystems](intro.md).

## Platform Server

This section summarizes the requirements for installing the Platform Server in your data center.

### Hardware (minimum requirements)

* Dual-core processor
* 4 GB of RAM
* 80 GB of free disk space

### Operating System

* Microsoft Windows Server 2019 (Standard Edition or higher edition), since Platform Server Release Jul.2019
* Microsoft Windows Server 2016 (Standard Edition or higher edition)

For these Operating System versions, OutSystems only supports Windows editions that are [supported by Microsoft](https://support.microsoft.com/en-us/lifecycle/search).

The supported Operating System configurations must be deployed on bare metal or hardware virtualization technologies (for example, VMware or KVM).

Future revisions of OutSystems may require the installation of an update within the major versions mentioned in the previous list.

### Application Server

* Microsoft Internet Information Services (IIS) 10.0 or higher configured with a valid SSL certificate emitted by a public Certificate Authority

### Database Management System

Keep in mind that you must use the same flavor of database engine for the 3 databases used by the platform (platform and apps, logs, session). Combinations of database engines, for example, using SQL Server for the platform database and Azure SQL database for the logs and or session databases (or any other combination), are not supported.

* Microsoft SQL Server 2019 and compatibility level 150, since Platform Server 11.12.0 <sup>1</sup>
* Microsoft SQL Server 2017 (Web Edition or higher edition)<sup>1</sup>
* Microsoft SQL Server 2016 (Web Edition or higher edition)<sup>1</sup>
* Microsoft SQL Server 2014 (Web Edition or higher edition)<sup>1</sup>
* Azure SQL Database V12
* Oracle 19c (Standard Edition or Enterprise Edition), since Platform Server 11 – Release Oct.2019 CP3
* Oracle 18c (Standard Edition or Enterprise Edition), since Platform Server 11 – Release Oct.2019 CP2
* Oracle 12c (12.1 or 12.2, Standard Edition or Enterprise Edition)

<sup>1</sup> Developer and Express editions of Microsoft SQL Server (any version) are not supported.

Future revisions of OutSystems may require the installation of an update within the major versions mentioned in the previous list.

Apart from standard Oracle Database setups, OutSystems Platform 8.0 and onwards works with [Oracle Exadata Database Machines](http://www.oracle.com/us/products/database/exadata/overview/index.html) running with Oracle Linux 5.5 or higher.

### Additional Software Requirements

* Microsoft .NET Framework 4.8 (supported since Platform Server 11 – Release Oct.2019 CP2) or Microsoft .NET Framework 4.7.2
* Microsoft Build Tools 2015
* .NET 6.0 Runtime & Hosting Bundle for Windows

Future revisions of OutSystems may require the installation of an update within the major versions mentioned in the previous list.

## Cache Invalidation Service

OutSystems Cache Invalidation Service requires the following minimum version of RabbitMQ Server:

* RabbitMQ Server 3.10.14 with Erlang version 25.1.2, since Platform Server 11.19.0
* RabbitMQ Server 3.9.11 with Erlang version 24.2, from Platform Server 11.15.0 to 11.18.1
* RabbitMQ Server 3.8.21 with Erlang version 23.2, from Platform Server 11.13.2 to 11.14.1
* RabbitMQ Server 3.8.3 with Erlang version 22.3, from Platform Server 11.9.0 to 11.13.1
* RabbitMQ Server 3.7.7 with Erlang version 20.3, for earlier versions of Platform Server

These versions can be upgraded to the latest minor version compliant with the [official documentation](https://www.rabbitmq.com/which-erlang.html).

During Platform Server installation, OutSystems provides you with a script that simplifies the local installation of these two components (RabbitMQ Server and Erlang). Alternatively, you can use an existing RabbitMQ Server and Erlang installation, as long as it fulfills the same version requirements.

## Amazon EC2 considerations

OutSystems can run on Amazon EC2 instances. Each instance must fulfill the following requirements:

* The EC2Config service must be running

For more information on how to enable this service check Amazon's [EC2Config service documentation](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2config-service.html).

## Amazon RDS considerations

OutSystems supports Microsoft SQL Server 2019 and compatibility level 150 (since Platform Server 11.12.0), Microsoft SQL Server 2016, Microsoft SQL Server 2017, Oracle 12c, Oracle 18c, and Oracle 19c on Amazon RDS. The database instance class must fulfill the following requirements:

* 1 vCPU (virtual central processing unit) or higher
* 1 ECU (EC2 Compute Unit) or higher
* 3.75 GiB of memory or higher
* "Moderate" network performance or higher

Example of a DB instance class fulfilling these requirements: "db.t2.medium".

Oracle 18c on Amazon RDS is supported since Platform Server 11 – Release Oct.2019 CP2.
Oracle 19c on Amazon RDS is supported since Platform Server 11 – Release Oct.2019 CP3.

Check [Amazon's DB Instance Class](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html) topic for more information on the available DB instance classes. Be sure to also check [Amazon RDS System Requirements](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) to learn about Amazon RDS limitations.

## Microsoft Azure considerations

OutSystems supports Microsoft Azure SQL Database V12 with the following considerations:

* The database service tier must be at least "S3".
* The MDC (Multiple Database Catalogs) feature is not supported.
* Connecting to Azure SQL Database using Windows Authentication is not supported.
* Private endpoints are not supported, due to a limitation on how Microsoft implements them.
* Currently, Azure SQL Database does not support customizing the timezone from UTC.

OutSystems also supports SQL Server running on an Azure Virtual Machine.

## Integration with external systems

The following systems are certified to integrate with OutSystems.

### SQL Server Database

* Microsoft SQL Server 2019 and compatibility level 150, since Platform Server 11.12.0
* Microsoft SQL Server 2017
* Microsoft SQL Server 2016
* Microsoft SQL Server 2014
* Microsoft SQL Server 2012
* Microsoft SQL Server 2008 R2
* Microsoft SQL Server 2008

### Azure SQL Database

* Azure SQL Database available in the cloud

### Oracle Database

* Oracle 19c (Standard Edition or Enterprise Edition), since Platform Server 11 – Release Oct.2019 CP3
* Oracle 18c (Standard Edition or Enterprise Edition), since Platform Server 11 – Release Oct.2019 CP2
* Oracle 12c (12.1 and 12.2, Standard Edition or Enterprise Edition)
* Oracle 11g R2 (Standard Edition or Enterprise Edition)

The **NLS_CHARACTERSET** must be set to **WE8MSWIN1252** or **AL32UTF8**.

<div class="info" markdown="1">

From OutSystems 11 Platform Server Release Oct.2019 onwards you can't have integrations with Oracle databases earlier than 11g R2.

</div>

### MySQL Database

* MySQL 5.6 (5.6.5 or later within the 5.6 version, all editions)
* MySQL 5.7 (5.7.22 or later within the 5.7 version, all editions)
* MySQL 8.0 (8.0.28 or later within the 8.0 version, all editions), since Platform Server 11.19.0

### PostgreSQL Database

* PostgreSQL 12.x.x
* PostgreSQL 13.x.x

### Aurora PostgreSQL Database

* Aurora PostgreSQL Database available in the cloud running a version compatible with a [supported PostgreSQL database](#postgresql-database)

### IBM Database

* DB2 for iSeries V6R1 or higher
* **OutSystems** supports integration with DB2 databases hosted in iSeries machines only. It does not support integration with DB2 databases hosted in Unix, Linux, or Windows.

<div class="info" markdown="1">

The installation of the IBM i Access Client Solutions - Windows Application Package software is required in all Front-End and Deployment Controller server machines.

The use of double-byte characters with DB2 databases is not supported.

</div>

### MongoDB Database

* MongoDB Atlas and on-premises
* MongoDB 4.X
* MongoDB 5.X

### SAP

* SAP ERP R/3 4.6 or higher
* SAP ECC 5.0 or higher
* SAP S/4HANA

## Development tools

To develop your applications using OutSystems, developers need to install **Service Studio** and **Integration Studio** development tools on their desktops.
The latest version of the development tools are available in the [OutSystems downloads page](https://www.outsystems.com/Downloads/search/Development+Environment/11/).

### Service Studio

Before setting up Service Studio make sure that your computer meets the following requirements:

### Hardware (minimum requirements)

* 1.8 GHz dual-core processor or better.
* 2 GB of RAM (4 GB recommended).
* 1 GB of free disk space

<div class="info" markdown="1">

In Apple devices using Apple Silicon M1 processor, Service Studio runs under the Rosetta 2 emulation.

</div>

#### Operating System

**macOS (cross-platform Service Studio only):**

* macOS Big Sur
* macOS Monterrey

**Windows:**

* Windows 10 (64-bit)
* Windows 8 (64-bit)
* Microsoft Windows Server 2019
* Microsoft Windows Server 2016

For these Operating System versions, OutSystems only supports Windows and macOS editions that are supported by [Microsoft](https://support.microsoft.com/en-us/lifecycle/search) and Apple respectively.

#### Required Software

* To perform client-side debugging in Service Studio using a desktop browser:
    Google Chrome version 54 or later.

* To perform client-side debugging on an Android mobile device:
    Android device drivers, if the device is not recognized automatically.

* To perform client-side debugging on an iOS mobile device:
    iTunes 12.1.3 or later.

### Integration Studio

Installation requirements are as follows.

#### Hardware (minimum requirements)

* 1.8 GHz dual-core processor (or better)
* 2 GB of RAM (4 GB recommended)
* 1 GB of free disk space

Limitations:

* The touch feature of touch screen devices is not supported, however, you can use touch screen devices with keyboard and mouse.

#### Operating System

* Windows 10 (64-bit)
* Windows 8 (64-bit)
* Windows 7 (64-bit)
* Microsoft Windows Server 2019, since Development Environment 11.6.5
* Microsoft Windows Server 2016

For the versions above, OutSystems only supports Windows editions that are [supported by Microsoft](https://support.microsoft.com/en-us/lifecycle/search).

#### Required Software

* Microsoft .NET Framework 4.7.2 (or higher).

* To integrate with external systems using Integration Studio to edit the source code of Extension Actions:
    Visual Studio 2015, Visual Studio 2017, or Visual Studio 2019 (since Development Environment 11.6.7).

## End User Requirements

Running an OutSystems app on a browser continues to be supported for 6 months after the end-of-support date announced by OutSystems for that browser.

### Reactive Web Apps

* Edge (latest stable version)
* Firefox (latest stable version)
* Google Chrome (latest stable version)
* Safari (latest stable version)

### Progressive Web Apps

* Default browser for latest stable version of Android
* Default browser for latest stable version of iOS

### Mobile App packages

See [Mobile Apps Build Service (MABS)](https://success.outsystems.com/Support/Release_Notes/Mobile_Apps_Build_Service_Versions) for the latest supported Android and iOS platform versions and the minimum requirements to generate your Mobile Apps.

### Traditional Web Apps

**Desktop Browsers**

* Internet Explorer 11 (latest stable version)
* Edge (latest stable version)
* Firefox (latest stable version)
* Google Chrome (latest stable version)
* Safari (latest stable version)

**Mobile Device Browsers**

* Default browser for iOS 7 or higher
* Default browser for Android 4.1 or higher
* Default browser for Windows Phone 8 or higher
