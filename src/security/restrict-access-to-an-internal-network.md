---
summary: OutSystems 11 (O11) enables enhanced application security by allowing internal network access restrictions for UI flows, SOAP web services, and REST APIs.
tags: application security, access control, network configuration, service center, environment configuration
locale: en-us
guid: 110c2416-65b4-404d-8adc-e02219af4207
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=280:126
audience:
  - platform administrators
  - full stack developers
  - backend developers
outsystems-tools:
  - service studio
  - service center
coverage-type:
  - apply
---

# Restrict access to an internal network

<div class="info" markdown="1">

To effectively use this feature, you need to [configure your environment Internal Network](https://success.outsystems.com/Documentation/11/Managing_the_Applications_Lifecycle/Secure_the_Applications/Configure_an_Internal_Network) in Service Center.
</div>

You can tighten the security of your applications by restricting access to authenticated users on an internal network IP address.

<div class="info" markdown="1">

Before using this feature, define the IP range of your internal network. See [Configure an internal network](configure-internal-network.md).

</div>

You can restrict internal network access to the following elements:

* UI Flows of a Web application (restricts the access of the Web Screens within the Flow). This is only available for Traditional Web apps.
* Exposed SOAP Web Services
* Exposed REST APIs

To restrict these elements to internal network access, set its **Internal Access Only** property to `Yes`.

![Screenshot showing how to set the Internal Access Only property to Yes for restricting access to internal networks](images/internal-network-set-ss.png "Setting Internal Access Only Property")
