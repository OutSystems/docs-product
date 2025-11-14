---
summary: Explore how to install and configure RabbitMQ via command-line for OutSystems 11 (O11) by modifying server configurations and running specific commands.
tags: installation, configuration, command-line tools, rabbitmq, server administration
locale: en-us
guid: 7f15fedf-010b-4271-8630-86ab785d618a
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - platform administrators
  - full stack developers
  - backend developers
outsystems-tools:
  - platform server
coverage-type:
  - apply
---

# Install and configure RabbitMQ using the command-line

You can install and configure RabbitMQ via command-line instead of using Configuration Tool.

Do the following:

1. Ensure that your `server.hsconf` has a valid `CacheInvalidationConfiguration` section;

1. _(Optional)_ If you are installing RabbitMQ for the first time, you can create the `%ALLUSERSPROFILE%\RabbitMQ\advanced.config` configuration file before proceeding with the service installation in the next step. This is useful if you want to [enable TLS communications](<enable-tls.md>).

1. Open a command-line console (run as Administrator) and change to the OutSystems platform installation folder (by default, `C:\Program Files\OutSystems\Platform Server`).

1. Run the following command:  
    `ConfigurationTool.exe /CreateUpgradeCacheInvalidationService`
