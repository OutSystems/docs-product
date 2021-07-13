---
summary: Learn the several components that are part of OutSystems, and how to set up OutSystems on the cloud or on-premises.
tags: article-page; support-installation; support-Installation_Configuration-overview; support-Integrations_Extensions
---

# Setting Up OutSystems

<div class="info" markdown="1">

This article applies to: **OutSystems 11**&#8195;&#8195;Other versions available: [10](https://success.outsystems.com/Documentation/10/Setting_Up_OutSystems)&#8195;[9.1](https://success.outsystems.com/Support/Archive/9.1/01_Install_and_set_up_OutSystems_Platform)&#8195;[9.0](https://success.outsystems.com/Support/Archive/9.0/01_Install_and_set_up_OutSystems_Platform)

</div>

This article explains the several components of OutSystems. It also explains how to set up OutSystems on the cloud or on-premises.

## OutSystems Overview

### Components

OutSystems has the following components:

* **Platform Server:** The component that orchestrates all runtime, deployment, and management activities for all applications. This tool is installed in each environment.

* **LifeTime:** This is the centralized console for managing the infrastructure, environments, applications, IT users, and security.

* **Service Center:** The administration console for an environment of the infrastructure.

* **Service Studio:** The visual development tool to create, change, and deploy your applications. This tool is installed in the developers desktop.

* **Integration Studio:** The development tool to create connectors to integrate OutSystems applications with other enterprise systems. This tool is installed in the developers desktop.

![](images/intro-1.png)

### Typical infrastructure

OutSystems covers the full application lifecycle, from development to deployment. For this reason, a typical OutSystems infrastructure has four environments:

* **Development Environment:** The environment where applications are initially developed and tested.

* **Quality Environment:** The environment where testers and business users experiment applications to perform quality assurance. This environment usually has few scalability and redundancy requirements.

* **Production Environment:** The environment that hosts the application version end users are interacting with. Usually, this environment is only accessible by the operations team.

* **Management Environment:** The environment that hosts LifeTime application, which is the infrastructure management console. Given its requirements, LifeTime application must run in a **dedicated** environment. **Installing LifeTime in an existing environment is not a supported scenario.** Learn how to [size an environment for the infrastructure management console](https://success.outsystems.com/Support/Enterprise_Customers/Installation/Size_an_environment_to_run_the_infrastructure_management_console).

You can have your infrastructure on the cloud or on-premises. [Learn more about the possible OutSystems infrastructure configurations.](https://success.outsystems.com/Documentation/11/Setting_Up_OutSystems/Possible_setups_for_an_OutSystems_infrastructure)

### Licensing

If you're using OutSystems Cloud, you don't need to worry about installing or licensing your infrastructure. Once you receive your OutSystems Cloud, it is ready for you to develop your apps.


## Installation alternatives

### Cloud

If you selected to setup OutSystems infrastructure using our Cloud offering you do not have to do any of the initial platform setup yourself. Your servers will be automatically set up for you and you will receive an email with access details such as address and usernames.

Nevertheless, when managing a single environment or infrastructure on the OutSystems cloud, you should take into account the following considerations:

* Currently, our cloud provider (Amazon) does not support customizing the time zone for SQL Server. Conversions need to be done programmatically from UTC to the desired time zone.

* Custom database objects such as stored procedures are not supported. You can either implement the same logic using "Advanced Queries" (standard SQL) or through Extensions (by implementing your own C# code).

* The Multiple Database Catalogs and Schema feature is not available. This means that all applications store their data in the same database Catalog/Schema.

* The Zones feature is not available. All applications running on an environment are available in all front-end servers of that environment. However, applications can be set up to only be accessible from the internal network.

* Using the built-in SMS mechanism is not supported. You can send SMS’s by using Extensions available in OutSystems Forge.


## Installation prerequisites

Before installing any component of OutSystems, make sure your hardware and software comply with the minimum requirements. For this, be sure to check:

* [System requirements](https://success.outsystems.com/Documentation/11/Setting_Up_OutSystems/OutSystems_system_requirements): the supported hardware and software for installing OutSystems.

* [Network requirements](https://success.outsystems.com/Documentation/11/Setting_Up_OutSystems/OutSystems_network_requirements): the network requirements for an environment where OutSystems is installed.

## Installation steps

To install OutSystems in your infrastructure:

1. Download the Platform Server installation binaries.
1. Install the Platform Server in each environment that will host your applications (eg. Development, Quality and Production).
1. Download the infrastructure management console (LifeTime) installation binaries.
1. Install the infrastructure management console in a dedicated environment.
1. Configure the infrastructure management console.
1. Install and configure the development tools.



### 6. Install and configure the development tools

OutSystems is now ready for you to start developing. The only thing missing is to [install the development tools](http://www.outsystems.com/home/downloads/) on your developers' desktops. Be sure to install a version of the development tools that is compatible with the version of the Platform Server installed in your environments.

After installing the development tools, [configure them for developing your own extensions](http://www.outsystems.com/goto/howto-configure-integration-studio).


## More Information

If you are having trouble installing or setting up OutSystems, check the [OutSystems Community](http://www.outsystems.com/forums/) for help, or reach out to the [OutSystems technical support](https://success.outsystems.com/Support/Enterprise_Customers/OutSystems_Support/01_Contact_OutSystems_technical_support).
