---
summary: This guide details configuring a HTTP proxy server in OutSystems 11 (O11) Service Studio for developers on restricted networks.
tags: ide usage, reactive web apps, tutorials for beginners, network configuration, proxy setup
locale: en-us
guid: b367660c-65e1-45d5-a6c2-c4ea29a9c8ab
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/ZDYZVg9kmMXl758XX7ytXc/Setup-and-maintain-your-OutSystems-Infrastructure?type=design&node-id=2252%3A3570&mode=design&t=iLJvc2VqD06T9g7F-1
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - understand
  - apply
---

# How to configure a HTTP proxy server in Service Studio

This article explains how to configure a HTTP proxy server on your local computer to be used by Service Studio. This applies when developers are working on a network where communications to the Internet need to go through an HTTP proxy.

To configure a HTTP proxy server:
1. [Configure the proxy server in the operating system](#configure-proxy-OS)
1. [Configure the proxy authentication in Service Studio](#configure-proxy-ss)

## Configure the proxy server in the operating system { #configure-proxy-OS }

Service Studio relies on the proxy servers (HTTP and HTTPS) that are defined in the operating system (Windows or MacOS) when connecting to an OutSystems environment. This means the configuration steps depend on the operating system.

### Windows setup

1. Click the **Start** icon and select **Settings**. 

    ![Start menu with Settings option highlighted for configuring HTTP proxy in Windows](images/windows-http-proxy-settings.png "Windows HTTP Proxy Settings")

1. Select **Network & Internet**.

    ![Network & Internet settings option highlighted in Windows settings](images/windows-http-proxy-network-internet.png "Windows Network & Internet Settings")

1. Select **Proxy**.

1. On the proxy configurations screen:

    1. Enable the **Use a proxy server** toggle.

    1. In the **Address** field, enter ``http=example.net:9090;https=example.net:9090``replacing ``example.net`` with your proxy server name or IP address and ``9090`` with your proxy server port. 

    1. Leave the **Port** field empty.

        ![Proxy configuration screen in Windows with 'Use a proxy server' toggle enabled and address field filled out](images/windows-http-proxy-setup.png "Windows Proxy Configuration")

    1. Click **Save**.

### MacOS setup

1. Open **System Preferences**.

1. Search for **Proxies**.

    ![System Preferences search field with 'Proxies' entered in MacOS](images/mac-http-proxy-search.png "MacOS Proxy Search")

1. In the **Select a protocol to configure** section, choose **Web Proxy (HTTP)**.

    1. In the **Web proxy server** field, enter the proxy server name or IP address and port. In the example below, the proxy server is ``example.net`` and the proxy port is ``9090``.

        ![Web Proxy (HTTP) settings with server name and port entered in MacOS](images/mac-http-proxy-web-settings.png "MacOS Web Proxy Settings")

1. In the **Select a protocol to configure** section, select **Secure Web Proxy (HTTPS)** and enter the proxy server name or IP address and port.

    ![Secure Web Proxy (HTTPS) settings with server name and port entered in MacOS](images/mac-http-proxy-secure-settings.png "MacOS Secure Web Proxy Settings")

1. Click **Ok**.

## Configure the proxy authentication in Service Studio { #configure-proxy-ss }

Some proxy servers require user authentication. In this case, you must provide the proxy credentials in the Service Studio Preferences dialog.

1. Open Service Studio.

1. Open the **Edit** > **Preferences...** dialog.

1. Enable the **Use proxy authentication** option.

1. Enter the **Proxy username** and **Proxy password**.

    ![Service Studio Preferences dialog with 'Use proxy authentication' option enabled and credentials entered](images/mac-http-proxy-authen.png "Service Studio Proxy Authentication")

1. Click **Apply**.
