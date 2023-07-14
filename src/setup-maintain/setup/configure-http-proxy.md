---
summary: OutSystems on-premises.
tags: 
locale: en-us
guid: b367660c-65e1-45d5-a6c2-c4ea29a9c8ab
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/ZDYZVg9kmMXl758XX7ytXc/Setup-and-maintain-your-OutSystems-Infrastructure?type=design&node-id=2252%3A3570&mode=design&t=iLJvc2VqD06T9g7F-1
---

# How to configure a HTTP proxy server in Service Studio

This article explains how to configure a HTTP proxy server on your local computer so you can deploy your Service Studio apps in an OutSystems environment.

To configure a HTTP proxy server:
1. [Configure the proxy server in the operating system](#configure-the-proxy-server-in-the-operating-system)
1. [Configure the proxy authentication in Service Studio](#configure-the-proxy-authentication-in-service-studio)

## Configure the proxy server in the operating system 

Service Studio relies on the proxy servers (HTTP and HTTPS) that are defined in the operating system (Windows or MacOS) when connecting to an OutSystems environment. This means the configuration steps depend on the operating system.

### Windows setup

1. Click the **Start** icon and select **Settings**. 

    ![Go to settings](images/windows-http-proxy-settings.png)

1. Select **Network & Internet**.

    ![Select network and internet](images/windows-http-proxy-network-internet.png)

1. Select **Proxy**.

1. On the proxy configurations screen:

    1. Enable the **Use a proxy server** toggle.

    1. In the **Address** field, enter ``http=example.net:9090;https=example.net:9090``replacing ``example.net`` with your proxy server name or IP address and ``9090`` with your proxy server port. 

    1. Leave the **Port** field empty.

        ![Enter proxy configurations](images/windows-http-proxy-setup.png)

    1. Click **Save**.

### MacOS setup

1. Open **System Preferences**.

1. Search for **Proxies**.

    ![Enter proxy configurations](images/mac-http-proxy-search.png)

1. Click **Advanced**.

    ![Enter proxy configurations](images/mac-http-proxy-advanced.png)

1. Select **Proxies**.

    ![Enter proxy configurations](images/mac-http-proxy-proxies.png)

1. In the **Select a protocol to configure** section, choose **Web Proxy (HTTP)**.

    1. In the **Web proxy server** field, enter the proxy server name or IP address and port. In the example below, the proxy server is ``example.net`` and the proxy port is ``9090``.

        ![Enter proxy configurations](images/mac-http-proxy-web-settings.png)

1. In the **Select a protocol to configure** section, select **Secure Web Proxy (HTTPS)** and enter the proxy server name or IP address and port.

    ![Enter proxy configurations](images/mac-http-proxy-secure-settings.png)

1. Click **Ok**.

## Configure the proxy authentication in Service Studio 

Some proxy servers require user authentication. In this case, you must provide the proxy credentials in the Service Studio Preferences dialog.

1. Open Service Studio.

1. Open the **Preferences** dialog.

1. Enable the **Use proxy authentication** option.

1. Enter the **Proxy username** and **Proxy password**.

    ![Enter proxy configurations](images/mac-http-proxy-authen.png)

1. Click **Apply**.
