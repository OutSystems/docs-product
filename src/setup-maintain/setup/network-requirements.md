---
summary: Check OutSystems network requirements before installing it on an environment.
tags: support-installation
locale: en-us
guid: 6238ecb9-6eaf-4406-a421-f4b01322052d
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# OutSystems network requirements

<div class="info" markdown="1">

This article applies to: **OutSystems 11**&#8195;&#8195;Other versions available: [10](https://success.outsystems.com/Documentation/10/Setting_Up_OutSystems/OutSystems_network_requirements)&#8195;[9.1](https://success.outsystems.com/Support/Archive/9.1/OutSystems_Platform_network_requirements)&#8195;[9.0](https://success.outsystems.com/Support/Archive/9.0/OutSystems_Platform_network_requirements)

</div>

## Network environment requirements

### Open ports

For each server of an OutSystems environment, `localhost`:

* must resolve to 127.0.0.1 (IPv4)
* must be accessible by HTTP on 127.0.0.1

<div class="info" markdown="1">

It's possible to configure some of the ports used. Check the [Configuration Tool documentation](../../ref/configuration-tool/intro.md) to learn more.

</div>

The following table lists the ports that should be open to make your applications to be accessible **outside** of your local network (WAN) or **inside** of your local network (LAN).

|Source|Destination|Port|Protocol|Notes|
|------|-----------|----|--------|-----|
|End Users/Internet|Front-End|80|TCP|Applications HTTP access|
|End Users/Internet|Front-End|443|TCP|Applications HTTPS access (always required for Mobile and Reactive Web apps)|

The table below details the ports that need to be accessible in each server of an OutSystems environment for **publication and runtime connectivity**. If a server has both roles (Controller and Front-End), then consider the ports for both profiles on that server.

<div class="info" markdown="1">

Security Tip: TCP Ports 12000,12001 and 12002 shouldn't be open to the internet.

</div>

|Source|Destination|Port|Protocol|Notes|
|------|-----------|----|--------|-----|
|SysOps|Server|22/3389|TCP|Access the server through SSH or Remote Desktop|
|Front-End|nativebuilder.api.outsystems.com|443|TCP|Generate Mobile apps ([more info](https://success.outsystems.com/Support/Enterprise_Customers/Installation/Mobile_App_Builder_Service_connectivity_requirements))|
|Front-End|Controller (by default)<br/>— Depends on where the Cache Invalidation Service/RabbitMQ is installed.|5672|TCP|Cache Invalidation Service connection|
|Front-End|Controller|12000|TCP|OutSystems Deployment Controller Service connection|
|Front-End|SQL Server / Oracle|1433 / 1521|TCP|Database connection|
|Controller|Front-End|12001|TCP|OutSystems Deployment Service connection|
|Controller|SQL Server / Oracle|1433 / 1521|TCP|Database connection|

The following table lists the ports that should be open to correctly **monitor** OutSystems. A failure on opening these ports may result in warnings and error messages.

|Source|Destination|Port|Protocol|Notes|
|------|-----------|----|--------|-----|
|Front-End|Front-End|80|TCP|IIS Monitoring|
|Front-End|Controller|12000|TCP|OutSystems Deployment Controller Service Monitoring|
|Front-End|Front-End|12001|TCP|OutSystems Deployment Service Monitoring|
|Front-End|Front-End|12002|TCP|OutSystems Scheduler Service Monitoring|
|Controller|Front-End|80|TCP|IIS Monitoring|
|Controller|Front-End|12001|TCP|OutSystems Deployment Service Monitoring|
|Controller|Front-End|12002|TCP|OutSystems Scheduler Service Monitoring|
|Front-End and Controller|\*.outsystems.com<br/>outsystems.com|443|TCP|Telemetry|

In case you are using a hybrid infrastructure where some part is in OutSystems Cloud and another is managed by yourself, it's possible to create a VPN connection between the environments (hybrid configuration is only supported in OutSystems licenses purchased before January 2020). Learn more in the [Amazon documentation](http://aws.amazon.com/vpc/faqs/#C1).

### Development tools

The following table lists the necessary connectivity between the developers workstations and the several endpoints that support the full experience of Service Studio and Integration Studio.

|Source|Destination|Port|Protocol|Notes|
|------|-----------|----|--------|-----|
|Service Studio and Integration Studio|Front-End|443|TCP|<ul>Deploy applications to the environment</ul>|
|Service Studio|\*.outsystems.com<br/>outsystems.com|443|TCP| Service Studio connects to `outsystems.com` and several sub-domains to achieve the following: <ul><li>[AI-Assisted Development](../../develop/logic/ai-assisted-dev.md) </li><li> What's New! - The What's New dialog shows you the latest features added.</li> <li>Update Service Studio automatically</li><li>Telemetry</li><li>Submit feedback and errors via Service Studio</li> <li>Forge - The Forge bell icon lets you know if there are updates for installed components. </li><li>Application creation when creating from an existing sample app</li><li>Shows related documentation links when using help.</li></ul>|
|Service Studio|s3.amazonaws.com |443|TCP|<ul><li>Forge components - To install Forge components from the Forge tab or from the Forge website.</li><li>Access app templates while creating apps from scratch.</li></ul>|
|Service Studio| fonts.googleapis.com |443|TCP|<ul>Used when changing the theme when using the Theme Editor both at development and runtime.</ul>
|Service Studio| outsystems.drift.click |443|TCP|<ul>Help Chatbot. This applies when connecting to a personal environment only and to free editions.</ul>|
|Service Studio| outsystems.eu.qualtrics.com|443|TCP|<ul>Used to run surveys inside Service Studio. This applies when connecting to a personal environment only and to free editions.</ul>|

### Network latency

Even though OutSystems is built to scale horizontally, you need to consider the network latency between the database server, the Platform Server, and the front-end servers. For this reason, it’s advisable to have all servers that make up an environment, running under the same provider.

As an example, if you are using Amazon RDS as your database server and running the Platform Server on your own infrastructure, the application’s performance will be degraded.

### Experience Builder

[Experience Builder](https://experiencebuilder.outsystems.com/) must be able to connect to the environment where you want Experience Builder to publish apps. Ensure that the front ends of that environment accept inbound connections from the **Source** address.

Alternatively, ensure that the front ends of the environment used with Experience Builder accepts connections from the IP addresses in the **Notes**. These IP addresses are subject to change.

The Experience Builder uses the environment's public DNS hostname to communicate.

Source|Destination|Port|Protocol|Notes
---|---|---|---|---
experiencebuilder.outsystems.com|Environment Front-End<br/>(public DNS hostname)|443|TCP|52.51.203.1<br/>108.128.2.246<br/>54.228.47.100<br/>63.33.151.194<br/>34.241.56.16<br/>54.75.124.221

### Integration Builder

[Integration Builder](https://integrationbuilder.outsystems.com/) should be able to connect to the environments where you deploy integrations*. When connecting Integration Builder to all your environments, ensure that the front ends of the environments accept inbound connections from the **Source** address. For example, for a standard infrastructure, Integration Builder should be able to connect to the development, quality assurance, and production environments but doesn't need to connect to LifeTime.

Alternatively, ensure that the front ends of the environments used with Integration Builder accept connections from the IP addresses in the **Notes**. These IP addresses are subject to change.

The Integration Builder uses the environments' public DNS hostname to communicate.

Source|Destination|Port|Protocol|Notes
---|---|---|---|---
integrationbuilder.outsystems.com|Environment Front-End<br/>(public DNS hostname)|443|HTTPS|52.51.203.1<br/>108.128.2.246<br/>54.228.47.100<br/>63.33.151.194<br/>34.241.56.16<br/>54.75.124.221
Environment Front-End|integrationbuilder.outsystems.com|443|HTTPS|52.51.203.1<br/>108.128.2.246<br/>54.228.47.100<br/>63.33.151.194<br/>34.241.56.16<br/>54.75.124.221

It's not mandatory to have Integration Builder connected to **all your environments**. Only a development environment is mandatory. However, there are a few limitations on environments that are not connected to Integration Builder:

* Development Connections (created automatically by Integration Builder in a
  Dev environment for testing purposes) won't work. It's necessary to define
  your own connection.

* Sending emails through Integration Manager to administrators to request new
  connections or assistants won't work.

* Automatic creation of connections in Integration Manager won't work. Manual
  creation is still possible.

### Workflow Builder

[Workflow Builder](http://workflowbuilder.outsystems.com/) must be able to connect to the environment where you want Workflow Builder to publish apps. Ensure that the front ends of that environment accept inbound connections from the **Source** address.

Alternatively, ensure that the front ends of the environment used with Workflow Builder accepts connections from the IP addresses in the **Notes**. These IP addresses are subject to change.

The Workflow Builder uses the environment's public DNS hostname to communicate.

Source|Destination|Port|Protocol|Notes
---|---|---|---|---
workflowbuilder.outsystems.com|Environment Front-End<br/>(public DNS hostname)|443|TCP|52.51.203.1<br/>108.128.2.246<br/>54.228.47.100<br/>63.33.151.194<br/>34.241.56.16<br/>54.75.124.221

To use [IT user governance based on LifeTime teams](https://success.outsystems.com/Documentation/Workflow_Builder/How_to_set_up_Workflow_Builder/How_to_set_up_the_users_governance_model), Workflow Builder needs to be able to connect directly to LifeTime via TCP using HTTPS, port 443.

## Network infrastructure requirements

### LifeTime

You need to have bidirectional secure communication between the front-end of the LifeTime environment, and all other servers (front-ends and deployment controllers) of your OutSystems Infrastructure. When the environments have load balancers, you can establish the connectivity between LifeTime and the load balancers of the environments it manages.

|Source|Destination|Port|Protocol|
|------|-----------|----|--------|
|LifeTime Front-End|Environment Front-End|443|TCP|
|Environment Front-End|LifeTime Front-End|443|TCP|

### AI Mentor Studio

To use [AI Mentor Studio](https://aimentorstudio.outsystems.com/), the AI Mentor Studio LifeTime plugin must be able to communicate with the AI Mentor Studio SaaS. Check out [how AI Mentor Studio works](https://success.outsystems.com/Documentation/Architecture_Dashboard/How_does_Architecture_Dashboard_work). 

#### Version 4.3 of the AI Mentor Studio LifeTime probes

From version 4.3 of the AI Mentor Studio LifeTime probes, [AI Mentor Studio](https://aimentorstudio.outsystems.com/) must be able to connect to the environment where you want to perform code analysis. Hence, besides ensuring the destination endpoint (LifeTime Front-End) is reachable, you also need to ensure that the front ends of the environment where you want to perform code analysis accept inbound connections from `aimentorstudio.outsystems.com`.

Alternatively, ensure that the front ends of the environment used with AI Mentor Studio accept connections from the IP addresses in the **Notes**. These IP addresses are subject to change.

Source|Destination|Port|Protocol|Notes
---|---|---|---|---
LifeTime Front-End|aimentorstudio.outsystems.com/Probe_API/rest/Synchronization/|443|TCP| **Outbound communication** 
aimentorstudio.outsystems.com|Environment Front-End (public DNS hostname)|443|TCP|**Inbound communication**<br/>IP addresses:<br/>52.51.203.1<br/>108.128.2.246<br/>54.228.47.100<br/>63.33.151.194<br/>34.241.56.16<br/>54.75.124.221

#### Version 4.2 of the AI Mentor Studio LifeTime probes

Ensure the following destination endpoint is reachable:

Source|Destination|Port|Protocol|Notes
---|---|---|---|---
LifeTime Front-End|aimentorstudio.outsystems.com/Probe_API/rest/Synchronization/|443|TCP|

#### Versions 4.0 and 4.1 of the AI Mentor Studio LifeTime probes

Ensure the following destination endpoint is reachable:

Source|Destination|Port|Protocol|Notes
---|---|---|---|---
LifeTime Front-End|architecture.outsystems.com/Broker_API/rest/ArchitectureDashboard|443|TCP|

