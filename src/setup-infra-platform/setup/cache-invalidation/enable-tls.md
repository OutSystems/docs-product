---
summary: How to enable TLS communication between the Cache Invalidation Service (RabbitMQ) and running OutSystems applications.
tags: version-11; support-Installation_Configuration
helpids: 30177
locale: en-us
guid: 2027cfb9-111f-43f5-a3fb-cf1581beece6
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
---

# Enable TLS communication in RabbitMQ

To enable TLS you must manually configure the port used by the TLS listener as well as its certificate and corresponding key.

**Note:** To generate certificates and keys, follow the recommendations provided in the [TLS Support](https://www.rabbitmq.com/ssl.html) page of the official RabbitMQ documentation.

To enable TLS communication do the following:

1. Open the `%ALLUSERSPROFILE%\RabbitMQ\rabbitmq.conf` configuration file.  
**Note**: If they do not exist, create the `RabbitMQ` folder and the `rabbitmq.conf` file.
 
1. Add the following lines:

        ## Disable non-TLS listeners for AMQP connections
        listeners.tcp = none
        
        ## Enable TLS for AMQP connections
        listeners.ssl.default = 5671
        ssl_options.cacertfile = C:\\path\\to\\server\\cacert.pem
        ssl_options.certfile = C:\\path\\to\\server\\cert.pem
        ssl_options.keyfile = C:\\path\\to\\server\\key.pem

This configuration does the following: 

1. Disables all non-TLS listeners (`listeners.tcp`)

   **Note**: You must also ensure that the `RABBITMQ_NODE_PORT` environment variable is **not set** for this configuration to be effective.

1. Creates an TLS listener on port 5671 (`listeners.ssl.default`)

1. Configures the certificate and its key, as well as a bundle of their root and intermediate certificates, to be used by the TLS listener (`ssl_options`)

To apply these settings do the following:

1. In the Configuration Tool, open the **Cache** tab.

1. Set the Port parameter to the same port as in the configuration file (in the example above, the Port value would be `5671`).

1. Activate the option **Enable TLS**.

1. Click **Create/Upgrade Service**.

Alternatively, check [Install and configure RabbitMQ using the command-line](<installation.md>) for more information on how to apply the settings using the command-line.

## Configuring the certificate canonical name

If the canonical name used in the certificate does not match the host name of the machine running the RabbitMQ service, you must manually configure a parameter in the `server.hsconf` file.

Do the following:

1. Open the `server.hsconf` file and check if there's a section named `CacheInvalidationConfiguration` in the file.  
    If the section **does not** exist, you can add it automatically by doing the following:
    
    1. Open Configuration Tool.
    1. Open the **Cache** tab and fill in the configuration values for the RabbitMQ service.
    1. Close the Configuration Tool and, in the **Configuration changed** dialog box, confirm that you wish to save your changes by clicking **Yes**.
    
    The `CacheInvalidationConfiguration` section should now exist in `server.hsconf`.

1. In `server.hsconf`, set the value of the `TlsServerCanonicalName` parameter in the `CacheInvalidationConfiguration` section to the certificate canonical name.

1. Open Configuration Tool and click **Apply and Exit** to apply the new setting.
