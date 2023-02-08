---
tags: 
summary: Learn how to use a forward proxy while connecting from the AI Mentor Studio plugin to the AI Mentor Studio Software as a Service (SaaS).
locale: en-us
guid: 06af3d66-f6c3-4827-aa17-36b1124f321b
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# How to use a proxy to connect to AI Mentor Studio

<div class="info" markdown="1">

Architecture Dashboard is now AI Mentor Studio.

</div>

The AI Mentor Studio plugin can use a forward proxy while connecting to the AI Mentor Studio Software as a Service (SaaS). 

## Prerequisites

Before configuring the proxy in AI Mentor Studio, make sure that the following requirements are met:

* Your infrastructure uses **version 4.0 or higher** of the **AI Mentor Studio probes**.

## Configure the forward proxy

To configure the proxy, follow these steps:

1. Go to the AI Mentor Studio LifeTime plugin (`https://<lifetime_environment>/ArchitectureDashboardProbe/`) and select **Configuration**.

    ![Go to the plugin configuration](images/proxy-config-ams.png)

1. In the **Configuration** screen, turn on the **Proxy authentication** toggle.

    ![Turn on the Proxy authentication](images/proxy-auth-toggle-ams.png)

1. In the **Proxy configuration** section, enter the proxy URL and the credentials.

1. Select **Save and update**.

    ![Enter proxy information and save changes](images/proxy-info-ams.png)

After these steps the AI Mentor Studio plugin uses the proxy you configured when connecting to the AI Mentor Studio SaaS.
