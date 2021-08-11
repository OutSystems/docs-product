---
summary: Check the hardware and software requirements to install OutSystems on-premises.
tags: requirements; support-Application_Troubleshooting; support-installation; support-Installation_Configuration; support-Installation_Configuration-overview
---

# OutSystems system requirements

<div class="info" markdown="1">

This article applies to: **OutSystems 11 cross-platform Service Studio**<br/>
Other versions available:&#8195;[11](https://success.outsystems.com/Documentation/11/Setting_Up_OutSystems/OutSystems_system_requirements)&#8195;[10](https://success.outsystems.com/Documentation/10/Setting_Up_OutSystems/OutSystems_system_requirements)&#8195;[9.1](https://success.outsystems.com/Support/Archive/9.1/OutSystems_Platform_system_requirements)&#8195;[9.0](https://success.outsystems.com/Support/Archive/9.0/OutSystems_Platform_system_requirements)

</div>


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

From OutSystems 11 Platform Server Release Oct.2019 onwards you cannot have integrations with Oracle databases earlier than 11g R2. 

</div>

### MySQL Database

* MySQL 5.6 (5.6.5 or later within the 5.6 version, all editions)
* MySQL 5.7 (5.7.22 or later within the 5.7 version, all editions)

### IBM Database

* DB2 for iSeries V6R1 or higher

<div class="info" markdown="1">

The installation of the IBM i Access Client Solutions - Windows Application Package software is required in all Front-End and Deployment Controller server machines.

The use of double-byte characters with DB2 databases is not supported.

</div>


## Development tools

To develop your applications using OutSystems, developers need to install Service Studio and Integration Studio development tools on their desktops.

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

**macOS:**

* macOS Catalina
* macOS Big Sur

**Windows:**

* Windows 10 (64-bit)
* Windows 8 (64-bit)
* Microsoft Windows Server 2019
* Microsoft Windows Server 2016

#### Required Software

* To perform client-side debugging in Service Studio using a desktop browser:  
    Google Chrome version 54 or later.

* To perform client-side debugging on an Android mobile device:  
    Android device drivers, if the device is not recognized automatically.

* To perform client-side debugging on an iOS mobile device:  
    iTunes 12.1.3 or later.

#### Network

You need an internet connection to install Service Studio with a minimum speed of 1 Mbps for both downloading and uploading. You need an internet connection even when installing Service Studio on a virtual machine.

### Integration Studio

Installation requirements for these tools are as follows.

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

#### Required Network Connection

Minimum speed of 1 Mbps for both downloading and uploading.

These requirements apply, even when installing the development tools on a virtual machine.

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

The minimum requirements depend on the [Mobile Apps Build Service (MABS) version](https://success.outsystems.com/Support/Release_Notes/Mobile_Apps_Build_Service_Versions) used to generate your Mobile Apps.
