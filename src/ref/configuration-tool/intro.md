---
tags: configuration management, server setup, platform server configuration, installation procedures, environment management
summary: Explore the Configuration Tool in OutSystems 11 (O11) for server setup and management in complex environments.
locale: en-us
guid: 3ccedde9-7f7c-4d04-8992-703b00953c15
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - platform administrators
  - infrastructure managers
outsystems-tools:
  - platform server
coverage-type:
  - remember
---

# Configuration Tool

Use Configuration Tool to configure your Platform Server. You can use the tool in basic installations, but it's particularly useful in more complex environments. Configuration Tool enables you to export the configuration scripts and inspect them.

This tool is only available in infrastructures managed by customers, such as self-managed installations.

To launch this tool, on the Windows desktop of the server go to: **Start Menu** > **All Programs** > **OutSystems** > **Administration Tools** > **Configuration Tool**. You'll need to be connected to the server for example, via remote desktop.

When you have more than one front-end server, make sure that the configuration is the same in each front-end server, except for the [Scheduler](<tabs/scheduler.md>) configuration.
