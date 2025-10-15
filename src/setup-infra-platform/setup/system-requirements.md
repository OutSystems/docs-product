---
summary: Explore the comprehensive system requirements for deploying OutSystems 11 (O11) across various platforms and configurations.
tags: system requirements, on-premises installation, windows server, hardware requirements, software compatibility
locale: en-us
guid: 244db17a-7a98-4cb0-93c0-db91f1c91fd8
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - platform administrators
  - infrastructure managers
  - tech leads
outsystems-tools:
  - platform server
coverage-type:
  - understand
topic:
  - download-and-set-up
---

# OutSystems system requirements

<div class="info" markdown="1">

This article applies to: **OutSystems 11**&#8195;&#8195;Other version available: [10](https://success.outsystems.com/Documentation/10/Setting_Up_OutSystems/OutSystems_system_requirements)
</div>

Before installing OutSystems on-premises, verify that your setup meets the hardware and software requirements outlined in this article. To start the installation, refer to [Setting Up OutSystems](intro.md).

## Platform server

The following are the requirements for installing the Platform Server in your data center.

### Hardware (minimum requirements)

* Dual-core processor
* 4 GB of RAM
* 80 GB of free disk space

### Operating system

* Microsoft Windows Server 2025 (Standard Edition or higher edition), since Platform Server 11.35.0<sup>1</sup>
* Microsoft Windows Server 2022 (Standard Edition or higher edition), since Platform Server 11.20.0<sup>1</sup>
* Microsoft Windows Server 2019 (Standard Edition or higher edition), since Platform Server Release Jul.2019
* Microsoft Windows Server 2016 (Standard Edition or higher edition)

<div class="info" markdown="1">

<sup>1</sup> When using the Platform Server on Windows Server 2022/2025, consider increasing the CPU and memory of the machines, as the operating system itself requires more resources.
<br/>
<br/>
OutSystems only supports Windows editions that are [supported by Microsoft](https://support.microsoft.com/en-us/lifecycle/search).

</div>

The supported Operating System configurations must be deployed on bare metal or hardware virtualization technologies (for example, VMware or KVM).

Future revisions of OutSystems may require the installation of an update within the major versions mentioned in the previous list.

### Application server

* Microsoft Internet Information Services (IIS) 10.0 or higher configured with a valid SSL certificate issued by a public certificate authority. The SSL Certificate can alternatively be installed at a load balancer or reverse proxy level in [end-to-end SSL and SSL offloading](https://success.outsystems.com/documentation/how_to_guides/infrastructure/using_outsystems_in_reverse_proxy_scenarios/outsystems_configurations_in_reverse_proxy_scenarios/#ssl-offloading) configurations.

### Database management system

Use the same type of database engine for all three 3 databases in Platform Server (platform and apps, logs, and session). OutSystems does not support a combination of database engines. For example, you can't use SQL Server for the platform database and Azure SQL database for the logs/session databases (or any other combination).

* Microsoft SQL Server supported versions<sup>1, 2</sup> and respective supported compatibility levels:

    |  2016                |  2017                 |  2019                 |  2022                   |
    |----------------------|-----------------------|-----------------------|-------------------------|
    |  130                 |  130, 140             |  130, 140, 150        |  130, 140, 150          |

* Azure SQL Database, with compatibility level between 130 and 150
* Oracle<sup>3, 4</sup> 19c (Standard Edition or Enterprise Edition), since Platform Server 11 – Release Oct.2019 CP3

<div class="info" markdown="1">

<sup>1</sup> Requires Web Edition or higher. Developer and Express editions of Microsoft SQL Server (any version) aren't supported.
<br/>
<br/>
<sup>2</sup> SQL Server 2014 stopped being supported from Platform Server version 11.33 onwards.
<br/>
<br/>
<sup>3</sup> Oracle 18c stopped being supported from Platform Server version 11.33 onwards. It was initially supported from Platform Server 11 – Release Oct.2019 CP2.
<br/>
<br/>
<sup>4</sup> Oracle 12c stopped being supported from Platform Server version 11.33 onwards.
<br/>
<br/>
 OutSystems only supports Database versions that are supported by their respective vendor.
<br/>
<br/>

Future revisions of OutSystems may require the installation of an update within the major versions mentioned in the previous list.

</div>

### Additional software requirements

* Microsoft .NET Framework, one of the following, depending on the Platform Server version:
    * 4.8.1<sup>1</sup> : supported since Platform Server 11.35.0
    * 4.8<sup>2</sup> : supported since Platform Server 11 – Release Oct.2019 CP2
    * 4.7.2: supported by all Platform Server 11 versions
* Microsoft Build Tools 2015<sup>3</sup>
* .NET Runtime & Hosting Bundle for Windows in the following versions, depending on the Platform Server version:
    * .NET 8.0 Runtime & Hosting Bundle for Windows for Platform Server version 11.27.0 or newer
    * .NET 6.0 Runtime & Hosting Bundle for Windows for Platform Server versions between 11.17.1 and 11.26.0
    * .NET 3.1 Runtime & Hosting Bundle for Windows for Platform Server versions between 11.12.2 and 11.17.0
    * .NET 2.1 Runtime & Hosting Bundle for Windows for Platform Server versions between 11.12.1 and 11.0.539.0 (Release Jul.2019 CP1)
    * .NET 2.0 Runtime & Hosting Bundle for Windows for Platform Server version 11.0.528.0 (Release Jul.2019) and older
* Microsoft Visual C++ 2015-2022 Redistributable (x64) (only for Platform Server version 11.21.0 or above)

Future revisions of OutSystems may require the installation of an update within the major versions mentioned in the previous list.

<div class="info" markdown="1">

<sup>1</sup> Using Microsoft .NET Framework 4.8.1 implies a slightly higher memory usage for OutSystems apps, consider increasing the memory of Frontends.
<br/>
<br/>
<sup>2</sup> This version of .NET or later is required to ensure a FIPS-compliant environment.
<br/>
<br/>
<sup>3</sup> Microsoft Build Tools is no longer required starting from Platform Server versions 11.35.0.

</div>

### FIPS-compliance

From version 11.38.0 onwards, the Platform Server can be installed on FIPS-compliant systems.

To be able to achieve FIPS-compliance, customers must:

- Install Platform Server 11.38.0 or higher
- Use .NET 4.8 Framework or higher
- Purchase and install the commercial version of RabbitMQ<sup>1</sup>

<div class="info" markdown="1">

<sup>1</sup> Platform Server includes the Open Source version of RabbitMQ, which is not FIPS-compliant.

</div>

## Cache invalidation service

RabbitMQ Server and Erlang version numbers follow the format: Major.Minor.Patch. OutSystems Platform Server versions require minimum Patch versions of RabbitMQ Server and Erlang.

You can upgrade to the latest Patch of RabbitMQ Server provided that:


* The Patch RabbitMQ Server is higher than the one listed for the Platform Server version. For example, you can upgrade to RabbitMQ Server 3.10.25 for environments using Platform Server 11.19.0
* The Minor version of Erlang is higher than the one listed for the Platform Server version. For example, you can upgrade Erlang version to 25.2 for environments using Platform Server 11.19.0
* You keep the combination with the Erlang compliant with the [official documentation](https://www.rabbitmq.com/which-erlang.html). For example, when upgrading for RabbitMQ Server 3.10.25 you can upgrade Erlang to 25.2
* The Patch RabbitMQ Server is higher than the one listed for the Platform Server version. For example, you can upgrade to RabbitMQ Server 4.1.5 for environments using Platform Server 11.38.0.

Depending on the RabbitMQ used by the Platform Server, you can upgrade to either the latest Minor or Patch of Erlang provided that:

* The Minor/Patch version of Erlang is higher than the one listed for the Platform Server version. For example, you can upgrade Erlang:
    * to 27.4 (Minor) for environments using Platform Server 11.38.0.
    * to 26.2.5 (Patch) for environments using Platform Server 11.37.0.
* You keep the combination with the Erlang compliant with the [official documentation](https://www.rabbitmq.com/which-erlang.html).


The following are the minimum Patch versions of RabbitMQ Server and Erlang per Platform Server version:

* For Platform Server 11.38.0 and higher: RabbitMQ Server 4.1.2 and Erlang version 27.3.4
* From Platform Server 11.27.0 to 11.37.0: RabbitMQ Server 3.13.0 and Erlang version 26.2.2
* From Platform Server 11.19.0 to 11.26.0: RabbitMQ Server 3.10.14 and Erlang version 25.1.2
* From Platform Server 11.15.0 to 11.18.1: RabbitMQ Server 3.9.11 and Erlang version 24.2
* From Platform Server 11.13.2 to 11.14.1: RabbitMQ Server 3.8.21 and Erlang version 23.2
* From Platform Server 11.9.0 to 11.13.1: RabbitMQ Server 3.8.3 and Erlang version 22.3
* For Platform Server 11.8.2 and lower: RabbitMQ Server 3.7.7 and Erlang version 20.3

During Platform Server installation, OutSystems provides a script that simplifies the local installation of these two components (RabbitMQ Server and Erlang). Platform Server includes the open-source version of RabbitMQ. The commercial version of RabbitMQ is required for full FIPS compliance.

Alternatively, you can use an existing RabbitMQ Server and Erlang installation if it fulfills the same version requirements.

## Amazon EC2 considerations

OutSystems can run on Amazon EC2 instances. Each instance must fulfill one of the following requirements:

* The `Amazon EC2Launch` service must be running, available from Amazon EC2Launch v2 (starting with Platform Server 11.32.0)

* Or, the `EC2Config` service must be running

For more information on how to enable `Amazon EC2Launch` service, refer to [Amazon EC2Launch v2 service documentation](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2launch-v2.html).

For more information on how to enable `EC2Config` service, refer to [Amazon EC2Config service documentation](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2config-service.html).

## Amazon RDS considerations

OutSystems supports Microsoft SQL Server 2019 or higher and compatibility level 150 (since Platform Server 11.12.0), Microsoft SQL Server 2016, Microsoft SQL Server 2017 and Oracle 19c on Amazon RDS.

The database instance class must fulfill the following requirements:

* 1 vCPU (virtual central processing unit) or higher
* 1 ECU (EC2 Compute Unit) or higher
* 3.75 GiB of memory or higher
* "Moderate" network performance or higher

Example of a DB instance class fulfilling these requirements: "db.t2.medium".

Oracle 19c on Amazon RDS is supported since Platform Server 11 – Release Oct.2019 CP3.

<div class="info" markdown="1">

* Oracle 18c stopped being supported from Platform Server version 11.33 onwards. It was initially supported from Platform Server 11 – Release Oct.2019 CP2.

* Oracle 12c stopped being supported from Platform Server version 11.33 onwards.

</div>

For more information on the available DB instance classes, refer to [Amazon's DB Instance Class](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html).To learn more about Amazon RDS limitations, refer to [Amazon RDS System Requirements](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html).

## Microsoft Azure considerations

OutSystems supports Microsoft Azure SQL Database with the following considerations:

* The compatibility level must be between 130 and 150.
* The database service tier must be at least "S3".
* The MDC (Multiple Database Catalogs) feature isn't supported.
* Connecting to Azure SQL database using Windows authentication isn't supported.
* Private endpoints aren't supported, due to a limitation on how Microsoft implements them.
* Customizing the timezone from UTC isn't supported in Azure SQL database.

OutSystems also supports SQL Server running on an Azure virtual machine.

## Integration with external systems

The following systems are certified to integrate with OutSystems.

### SQL Server database

* Supported versions<sup>1</sup> and respective supported compatibility levels:

    |  2016    |  2017       |  2019           |  2022            |
    |----------|-------------|-----------------|------------------|
    |  130     |  130, 140   |  130, 140, 150  |  130, 140, 150   |

<sup>1</sup> Versions 2008 to 2014 stopped being supported from Platform Server version 11.33 onwards.

### Azure SQL database

* Azure SQL Database with compatibility level between 130 and 150

### Oracle database

* Oracle 19c (Standard Edition or Enterprise Edition), since Platform Server 11 – Release Oct.2019 CP3

The **NLS_CHARACTERSET** must be set to **WE8MSWIN1252** or **AL32UTF8**.

<div class="info" markdown="1">

* Oracle 18c stopped being supported from Platform Server version 11.33 onwards. It was initially supported from Platform Server 11 – Release Oct.2019 CP2.

* Oracle 12c stopped being supported from Platform Server version 11.33 onwards.

* Oracle 11g R2 stopped being supported from Platform Server version 11.25 onwards.

* Oracle versions earlier than 11g R2 stopped being supported from OutSystems 11 Platform Server Release Oct.2019 onwards.

</div>

### MySQL database

* MySQL 5.6 (5.6.5 or later within the 5.6 version, all editions)<sup>1</sup>
* MySQL 5.7 (5.7.22 or later within the 5.7 version, all editions)<sup>1</sup>
* MySQL 8.0 (8.0.28 or later within the 8.0 version, all editions), since Platform Server 11.19.0
* MySQL 8.4 (8.4.3 or later within the 8.3 version, all editions), since Platform Server 11.38.0


<sup>1</sup> This version is no longer supported by MySQL and isn't supported by OutSystems starting with Platform Server version 11.32.0.

### PostgreSQL database

* PostgreSQL 12.x.x, since Platform Server 11.15.0<sup>1</sup>
* PostgreSQL 13.x.x, since Platform Server 11.15.0
* PostgreSQL 17.x.x, since Platform Server 11.38.0

<sup>1</sup> This version is no longer supported by PostgreSQL and isn't supported by OutSystems starting with Platform Server version 11.38.0.

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

* 1.8 GHz dual-core processor or better
* 2 GB of RAM (4 GB recommended)
* 1 GB of free disk space

#### Operating System

**macOS (cross-platform Service Studio only):**

* macOS Ventura since Service Studio 11.54.60
* macOS Sonoma since Service Studio 11.54.60
* macOS Sequoia since Service Studio 11.55.0

**Windows:**

* Windows 11 (64-bit) since Service Studio 11.54.45
* Windows 10 (64-bit)
* Microsoft Windows Server 2019
* Microsoft Windows Server 2016

 OutSystems only supports Windows and macOS editions that are supported by [Microsoft](https://support.microsoft.com/en-us/lifecycle/search) and Apple, respectively.

#### Required software

* Google Chrome version 54 or later, or Microsoft Edge (Edge is only available for Service Studio running on Windows)
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

* The touch feature of touch screen devices isn't supported. However, you can use touch screen devices with a keyboard and mouse.

#### Operating System

* Windows 11 (64-bit) since Integration Studio 11.14.23
* Windows 10 (64-bit)
* Microsoft Windows Server 2019, since Development Environment 11.6.5
* Microsoft Windows Server 2016

OutSystems only supports Windows editions that are [supported by Microsoft](https://support.microsoft.com/en-us/lifecycle/search).

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

* Default browser for the latest stable version of Android
* Default browser for the latest stable version of iOS

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
