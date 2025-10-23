---
summary: OutSystems 11 (O11) utilizes an internal IP address range in the `a.b.c.0/24` format, derived from the front-end server's IP in the cloud environment.
tags: outsystems cloud, ip address range, ipv4, network configuration, environment health
locale: en-us
guid: 4b1ae768-0a96-45b1-8eb5-b5590ac28274
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
coverage-type:
  - apply
audience:
  - platform administrators
outsystems-tools:
  - service center
---
# Find out internal IP address range of your OutSystems Cloud

The internal IP address range of your OutSystems Cloud is an IPv4 address range with `a.b.c.0/24` format.  
The network part of the internal IP address range, `a.b.c`, can be obtained from the IP address of a front end Server in one of your environments.
Follow these steps:

1. Open Service Center for one of the environments in your OutSystems Cloud.

1. In the **Monitoring** tab, select **Environment Health** and check the **IP Address** of one of your **Front-end Servers**.

    The internal IP address range of your OutSystems Cloud is `a.b.c.0/24`, where `a.b.c` are the first three parts of the IP address of the front end server.

Example
:   If the IP address of your front end server is `10.8.2.111`, your OutSystems Cloud internal IP range is `10.8.2.0/24`.
