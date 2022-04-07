---
tags: 
summary: Learn how to use a forward proxy while connecting from the Architecture Dashboard plugin to the Architecture Dashboard Software as a Service (SaaS).
locale: en-us
guid: 06af3d66-f6c3-4827-aa17-36b1124f321b
---


# How to use a proxy to connect to Architecture Dashboard

The Architecture Dashboard plugin can use a forward proxy while connecting to the Architecture Dashboard Software as a Service (SaaS).

## Prerequisites

Before configuring the proxy in Architecture Dashboard, make sure that the following requirements are met:

* Your infrastructure uses **version 4.0 or higher** of the **Architecture Dashboard probes**.

## Configure the forward proxy

To configure the proxy, follow these steps:

1. Go to the Architecture Dashboard LifeTime plugin (`https://<lifetime_environment>/ArchitectureDashboardProbe/`) and select **Configuration**.

    ![Go to the plugin configuration](images/proxy-config-ad.png)

1. In the **Configuration** screen, turn on the **Proxy authentication** toggle.

    ![Turn on the Proxy authentication](images/proxy-auth-toggle-ad.png)

1. In the **Proxy configuration** section, enter the proxy URL and the credentials.

1. Select **Save and update**.

    ![Enter proxy information and save changes](images/proxy-info-ad.png)

After these steps the Architecture Dashboard plugin uses the proxy you configured when connecting to the Architecture Dashboard SaaS.
