---
summary: Check OutSystems network requirements before installing it on an environment.
tags: requirements; support-installation
---

# OutSystems network requirements

<div class="info" markdown="1">

This article applies to: **OutSystems 11 cross-platform Service Studio**<br/>
Other versions available:&#8195;[11](https://success.outsystems.com/Documentation/11/Setting_Up_OutSystems/OutSystems_network_requirements)&#8195;[10](https://success.outsystems.com/Documentation/10/Setting_Up_OutSystems/OutSystems_network_requirements)&#8195;[9.1](https://success.outsystems.com/Support/Archive/9.1/OutSystems_Platform_network_requirements)&#8195;[9.0](https://success.outsystems.com/Support/Archive/9.0/OutSystems_Platform_network_requirements)

</div>

## Network environment requirements

### Open ports

The table below details the ports that need to be accessible in each server of an OutSystems environment for **publication and runtime connectivity**. If a server has both roles (Controller and Front-End), then consider the ports for both profiles on that server.

|Source|Destination|Port|Protocol|Notes|
|------|-----------|----|--------|-----|
|End Users|Front-End|80|TCP|Applications HTTP access|
|End Users|Front-End|443|TCP|Applications HTTPS access (always required for Mobile and Reactive Web apps)|
|Front-End|SQL Server / Oracle|1433 / 1521|TCP|Database connection|
|Controller|SQL Server / Oracle|1433 / 1521|TCP|Database connection|

### Development tools

The following table lists the necessary connectivity between the developers workstations and the several endpoints that support the full experience of Service Studio and Integration Studio.

|Source|Destination|Port|Protocol|Notes|
|------|-----------|----|--------|-----|
|Service Studio and Integration Studio|Front-End|80|TCP|<ul>Deploy applications to the environment</ul>|
|Service Studio and Integration Studio|Front-End|443|TCP|<ul>Deploy applications to the environment</ul>|
|Service Studio|\*.outsystems.com<br/>outsystems.com|443|TCP| Service Studio connects to `outsystems.com` and several sub-domains to achieve the following: <ul><li>[AI-Assisted Development](../develop/logic/ai-assisted-dev.md) </li><li> What's New! - The What's New dialog shows you the latest features added.</li> <li>Update Service Studio automatically</li><li>Telemetry</li><li>Submit feedback and errors via Service Studio</li> <li>Forge - The Forge bell icon lets you know if there are updates for installed components. </li><li>Application creation when creating from an existing sample app</li><li>Shows related documentation links when using help.</li></ul>|
|Service Studio|s3.amazonaws.com |443|TCP|<ul><li>Forge components - To install Forge components from the Forge tab or from the Forge website.</li><li>Access app templates while creating apps from scratch.</li></ul>|
|Service Studio| fonts.googleapis.com |443|TCP|<ul>Used when changing the theme when using the Theme Editor both at development and runtime.</ul>
|Service Studio| outsystems.drift.click |443|TCP|<ul>Help Chatbot. This applies when connecting to a personal environment only and to free editions.</ul>|
|Service Studio| outsystems.eu.qualtrics.com|443|TCP|<ul>Used to run surveys inside Service Studio. This applies when connecting to a personal environment only and to free editions.</ul>|

### Network latency

Even though OutSystems is built to scale horizontally, you need to consider the network latency between the database server, the Platform Server, and the front-end servers. For this reason, it’s advisable to have all servers that make up an environment, running under the same provider.
