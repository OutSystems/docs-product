---
summary: In the Cache tab you define the configuration settings of the Cache Invalidation Service.
locale: en-us
guid: f224026f-76d6-4b2b-b750-a0d2f52f609a
app_type: traditional web apps, mobile apps, reactive web apps
---

# Cache Tab

In the **Cache** tab you define the basic settings for connecting to the Cache Invalidation Service (RabbitMQ) from applications and OutSystems services.

## Cache Invalidation Service section

This section contains configuration parameters for the cache invalidation service.

Configuration | Description  | Default value
--------------|--------------|---------------
Host | Hostname or IP address of the Cache Invalidation Service.<br/>_Note:_ To make it easier to add a front-end server later, OutSystems doesn't recommend using `localhost` as the hostname. | `localhost`
Port | Port used by applications and OutSystems services to communicate with the cache invalidation service. | `5672`
Virtual Host | Name of RabbitMQ virtual host.<br/>Virtual hosts allow you to reuse the service to other purposes having a separation from OutSystems logic. | `/outsystems`
Username | User of the cache invalidation service used by the OutSystems platform. | `admin`
Password | Password of the user of the cache invalidation service used by the platform.<br/>_Note:_ Currently this password can't contain special characters (for example, `?`, `&`, `^`, `"`, `'`, `*`, `(`, `)`). |
Enable TLS | When checked, enables the usage of secure connections between applications and the cache invalidation service | Unchecked

## Create/Upgrade Service button

To install or upgrade the cache invalidation service, click **Create/Upgrade Service**.

This button installs RabbitMQ and Erlang, the components used by the OutSystems platform to implement the cache invalidation service, using the configurations supplied in the Cache Invalidation Service section.

If these components were already installed by the OutSystems platform, the Configuration Tool updates their configuration according to the supplied values.

## Test Connection button

To verify that it's possible to connect to the cache invalidation service with the supplied configuration, click **Test Connection**.
