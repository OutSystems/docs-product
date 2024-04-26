---
summary: Learn how you can integrate with SAP in OutSystems.
tags: 
locale: en-us
guid: 3c630499-23ad-4947-9600-ad9392538dd6
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
---

# SAP

The connection between OutSystems and SAP relies on sapnco **SAP Connector for Microsoft.NET 3.0.x for Windows 64bit (Compiled with .NET Framework 4.0)** which is fully documented **[here](https://support.sap.com/content/dam/support/en_us/library/ssp/products/connectors/msnet/dotnet_connector_30_programming_guide.pdf)**. Therefore, it uses the regular username and password in the connection string. 

<div class="info" markdown="1">

The Exact version of SAP connector can be find in the [Platform Server installation checklist](https://www.outsystems.com/Downloads/search/Platform-Server/11/).
</div>

If you need an alternative authentication mechanism you can find more information **[here](../../ref/lang/auto/servicestudio-plugin-sap-sapclient.md)**.

Furthermore, this connection assumes that you are using a secure network is, which means it doesn’t use a secure protocol (communication is performed through HTTP).

Adding a secure layer, requires a custom configuration, including on the server side (SAP system). This is present in the documentation in SNC_MODE parameter (**[SAP .NET Connector, pp 43](https://support.sap.com/content/dam/support/en_us/library/ssp/products/connectors/msnet/dotnet_connector_30_programming_guide.pdf)**).

In addition, by default the data transmitted is not encrypted. However, you can configure it on the OnBeforeConnection() callback that you can find more information in **[this article](integrate-with-a-sap-system.md)**.

Combining this information with the **[SAP Extensibility API](../../ref/apis/sap-extensibility-api.md)** it is possible to implement an alternative authentication mechanism.

This section provides all the information you need to integrate SAP and OutSystems.
