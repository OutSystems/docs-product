---
summary: How to install and configure the Cache Invalidation Service using the command-line.
tags: version-11; support-Installation_Configuration
---

# Install and configure RabbitMQ using the command-line

You can install and configure RabbitMQ via command-line instead of using Configuration Tool.

Do the following:

1. Ensure that your `server.hsconf` has a valid `CacheInvalidationConfiguration` section;

1. _(Optional)_ If you are installing RabbitMQ for the first time, you can create the `%ALLUSERSPROFILE%\RabbitMQ\advanced.config` configuration file before proceeding with the service installation in the next step. This is useful if you want to [enable TLS communications](<enable-tls.md>).

1. Open a command-line console (run as Administrator) and change to the OutSystems platform installation folder (by default, `C:\Program Files\OutSystems\Platform Server`).

1. Run the following command:  
    `ConfigurationTool.exe /CreateUpgradeCacheInvalidationService`


