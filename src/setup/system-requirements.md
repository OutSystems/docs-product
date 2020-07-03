---
summary: Check the hardware and software requirements to install OutSystems on-premises.
tags: requirements; support-Application_Troubleshooting; support-installation; support-Installation_Configuration; support-Installation_Configuration-overview
---

# OutSystems system requirements

<div class="info" markdown="1">

This article applies to: **OutSystems 11**&#8195;&#8195;Other versions available: [10](https://success.outsystems.com/Documentation/10/Setting_Up_OutSystems/OutSystems_system_requirements)&#8195;[9.1](https://success.outsystems.com/Support/Archive/9.1/OutSystems_Platform_system_requirements)&#8195;[9.0](https://success.outsystems.com/Support/Archive/9.0/OutSystems_Platform_system_requirements)

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

The supported Operating System configurations need to be deployed on bare metal or hardware virtualization technologies (e.g. VMware, KVM).

Future revisions of OutSystems may require the installation of an update within the major versions mentioned in the previous list.

### Application Server

* Microsoft Internet Information Services (IIS) 10.0 or higher configured with a valid SSL certificate emitted by a public Certificate Authority

### Database Management System

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
* .NET Core 2.1 Runtime & Hosting Bundle for Windows

Future revisions of OutSystems may require the installation of an update within the major versions mentioned in the previous list.

## Cache Invalidation Service

OutSystems Cache Invalidation Service requires a RabbitMQ Server version 3.7.x with Erlang version 20.x.

While installing the OutSystems Platform Server you will be provided with a script that simplifies the local installation of these two components. Alternatively, you can use an existing RabbitMQ Server and Erlang installation as long as it fulfills the same version requirements.

## Amazon EC2 considerations

OutSystems can run on Amazon EC2 instances. Each instance must fulfill the following requirements:

* The EC2Config service must be running

For more information on how to enable this service check Amazon's [EC2Config service documentation](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2config-service.html).

## Amazon RDS considerations 

OutSystems supports Microsoft SQL Server 2016, Microsoft SQL Server 2017, Oracle 12c, Oracle 18c, and Oracle 19c on Amazon RDS. The database instance class must fulfill the following requirements:

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

* The MDC (Multiple Database Catalogs) feature is not supported.
* Connecting to Azure SQL using Windows Authentication is not supported.
* The database service tier must be at least "S3".
* Currently, Azure SQL does not support customizing the timezone from UTC.

OutSystems also supports SQL Server running on an Azure Virtual Machine.

## Integration with external systems

The following systems are certified to integrate with OutSystems.

### SQL Server Database

* Microsoft SQL Server 2017
* Microsoft SQL Server 2016
* Microsoft SQL Server 2014
* Microsoft SQL Server 2012
* Microsoft SQL Server 2008 R2
* Microsoft SQL Server 2008

### Azure SQL Database

* Azure SQL available in the cloud

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

The installation of the IBM iAccess software is required in all Front-End and Deployment Controller server machines.

The use of double-byte characters with DB2 databases is not supported.

</div>

### SAP

* SAP ERP R/3 4.6 or higher
* SAP ECC 5.0 or higher
* SAP S/4HANA

## Development tools

To develop your applications using OutSystems, developers need to install Service Studio and Integration Studio development tools on their desktops.

Installation requirements for these tools are as follows.

### Hardware (minimum requirements)

* 1.8 GHz dual-core processor (or better)
* 2 GB of RAM (4 GB recommended)
* 1 GB of free disk space

Limitations:

* The touch feature of touch screen devices is not supported, however, you can use touch screen devices with keyboard and mouse.

### Supported Operating Systems

* Windows 10 (64-bit)
* Windows 8 (64-bit)
* Windows 7 (64-bit)
* Microsoft Windows Server 2019, since Development Environment 11.6.5
* Microsoft Windows Server 2016

For the versions above, OutSystems only supports Windows editions that are [supported by Microsoft](https://support.microsoft.com/en-us/lifecycle/search).

<div class="info" markdown="1">

The 32-bit versions of Windows 10, Windows 8, and Windows 7 are supported up to Development Environment 11.6.7.

Microsoft Windows Server 2008 and Microsoft Windows Server 2012 are supported up to Development Environment 11.6.5.

</div>

### Required Software

* Microsoft .NET Framework 4.7.2 (or higher).

* To integrate with external systems using Integration Studio to edit the source code of Extension Actions:  
    Visual Studio 2015, Visual Studio 2017, or Visual Studio 2019 (since Development Environment 11.6.7).

* To perform client-side debugging in Service Studio using a desktop browser:  
    Google Chrome version 54 or later.

* To perform client-side debugging on an Android mobile device:  
    Android device drivers, if the device is not recognized automatically.

* To perform client-side debugging on an iOS mobile device:  
    iTunes 12.1.3 or later.

### Required Network Connection

Minimum speed of 1 Mbps for both downloading and uploading.

These requirements apply, even when installing the development tools on a virtual machine.

## End User Requirements

Running an OutSystems app on a browser continues to be supported for 6 months after the end-of-support date announced by OutSystems for that browser.

### Reactive Web Apps

* Edge (latest stable version)
* Firefox (latest stable version)
* Google Chrome (latest stable version)
* Safari (latest stable version)

### Progressive Web Apps (Early Access feature)

<div class="info" markdown="1">

Learn more about this Early Access feature by checking out the [Progressive Web Apps documentation page](../deliver-mobile/distribute-pwa/intro.md).

</div>

* Default browser for latest stable version of Android
* Default browser for latest stable version of iOS

### Mobile App packages

The minimum requirements depend on the [Mobile Apps Build Service (MABS) version](https://success.outsystems.com/Support/Release_Notes/Mobile_Apps_Build_Service_Versions) used to generate your Mobile Apps.

Note: Only official Android and iOS ROMs are supported.

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

## Containers considerations

Containers only expose HTTP port 80. HTTPS connections must be ensured by the load balancer, following an SSL offload scenario.

Follow the instructions in [End-to-end SSL and SSL Offloading](https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Using_OutSystems_in_Reverse_Proxy_Scenarios/03_OutSystems_configurations_in_reverse_proxy_scenarios#C_-_End-to-end_SSL_and_SSL_Offloading): you **do not** need to follow the step instructing you to insert a record in the `OSSYS_PARAMETER` table, since the platform already performs this task when deploying an application to containers.

### Docker Containers

To deploy OutSystems applications to Docker containers you will need a Docker infrastructure able to run standard Docker Windows Server containers, i.e. Windows Server containers that only use the functionality provided by default in a Docker installation.
 
#### Infrastructure

The minimum required Docker infrastructure consists of a Docker Engine installation, i.e. the client-server technology that builds and runs containers using Docker components and services. The engine must support and be able to run Windows Server containers.

The minimum recommended Docker version is the following:

* Docker client/server version 17.10

The machine running Docker must fulfill the following OS requirement:

* Windows Server 2016 (version 1709 or later)

OutSystems also supports the following Docker-based hosting technologies:

* Amazon ECS (Elastic Container Service)
* Azure Container Service (ACS)

If you are using Amazon please read the [Amazon Elastic Container Service documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_GetStarted.html). If you are using Azure please read the documentation on [Azure for Containers documentation](https://docs.microsoft.com/en-us/azure/containers/).

The Docker Secrets functionality is not supported, since its support on Windows containers is not yet ready for production use.

#### Docker Registries

While having a Docker registry is not mandatory, it is highly recommended. You can use any Docker registry as long as it supports storing and retrieving images for Windows Server containers.

For example, you can use one of the following docker registries (either on-premises or in the cloud):

* Docker Hub
* Docker Trusted Registry

#### Container Cluster Orchestrators

When deploying an OutSystems application in a Docker container it's necessary to map port 80 exposed by the container to an available port in the container host (usually a high-numbered port selected by the container runtime).

Since this port in the container host may change and each container needs at least port 80 mapped in the container host machine, the recommended approach is to set up a **container cluster**, together with a container cluster manager/orchestrator, that seamlessly handles all the routing to the right container and port.

You can use OutSystems with the following container cluster orchestrators:

* Docker Swarm
* Google Kubernetes
* Amazon Elastic Container Service

If you are using Docker Swarm, please read the official [Docker Swarm documentation](https://docs.docker.com/engine/swarm/). If you are using Kubernetes, please read the official Kubernetes documentation that includes detailed instructions on [using Kubernetes with a cluster](https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster/).

The container cluster manager/orchestrator can be installed anywhere as long as it allows you to manage the Docker engine on which you will be running the containers with OutSystems applications.
 
#### Base Image Availability

Ensure that all machines that will build/run the application images have the `microsoft/dotnet-framework:4.7.2-runtime` base image present in the machine. If the base image is not in the machine, the first build/run may timeout while the base image is downloaded.

### Pivotal Cloud Foundry

To deploy your OutSystems applications to Pivotal Cloud Foundry (PCF) you will need to have access to a PCF infrastructure. It must be able to run Windows stemcells, i.e. you will need to install a Windows tile in your infrastructure.

#### Infrastructure

The PCF infrastructure must have a Pivotal Application Service for Windows tile installed. To install a Windows tile, follow the instructions provided by Pivotal for the Windows 2016 tile.

Note: The Windows 2012r2 tile is **not supported**.
 
#### PCF Internal Routing

You will need to ensure that your PCF internal router can route requests to OutSystems applications both when these come from your internal network, as well as when coming from the outside.

We recommend adding **two domains** to your Pivotal Apps Manager's "org" (organization):

* A subdomain of your main shared domain that will be used as the PCF's deployment zone address. All the modules of each OutSystems application deployed to this zone will be mapped here. Example: If your main shared domain is `apps.pcf.example.com`, add a new domain called `os.apps.pcf.example.com`.

* A domain equal to the public address of your main load balancer and reverse proxy. This lets the PCF internally route requests coming from outside your internal network. Example: If your main load balancer and reverse proxy is publicly accessible using `site.example.com`, add exactly this value as a new domain.

#### Command-line Tools (cf CLI)

The deployment instructions provided by OutSystems use the Cloud Foundry Command Line Interface ("cf CLI") tool provided by Pivotal.

You must [install "cf CLI"](https://docs.cloudfoundry.org/cf-cli/install-go-cli.html) on the machine executing the deployment to PCF to be able to run the `cf` command-line executable.

You will also need to [log in to Cloud Foundry using "cf CLI"](https://docs.cloudfoundry.org/cf-cli/install-go-cli.html), specifying an API endpoint and an "org" (organization), before you are able to run commands like `cf push` successfully.
