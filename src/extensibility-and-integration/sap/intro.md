---
summary: Learn how you can integrate with SAP in OutSystems.
tags: 
locale: en-us
guid: 3c630499-23ad-4947-9600-ad9392538dd6
app_type: traditional web apps, mobile apps, reactive web apps
---

# SAP

The connection between OutSystems and SAP relies on sapnco **SAP Connector for Microsoft.NET 3.0.x for Windows 64bit (Compiled with .NET Framework 4.0)** which is fully documented **[here](http://logosworld.com/docs/SAP/Connector/SAP%20Connector%20for%20Microsoft%20.NET%20%20NCo_30_ProgrammingGuide.pdf)**. Therefore, it uses the regular username and password in the connection string. 

<div class="info" markdown="1">

The Exact version of SAP connector can be find in the [Platform Server installation checklist](https://www.outsystems.com/Downloads/search/Platform-Server/11/).
</div>

If you need an alternative authentication mechanism you can find more information **[here](https://success.outsystems.com/Documentation/11/Reference/OutSystems_Language/Extensibility_and_Integration/SAP/SAP_Connection)**.

Furthermore, this connection assumes that you are using a secure network is, which means it doesn’t use a secure protocol (communication is performed through HTTP).

Adding a secure layer, requires a custom configuration, including on the server side (SAP system). This is present in the documentation in SNC_MODE parameter (**[SAP .NET Connector, pp 40](http://logosworld.com/docs/SAP/Connector/SAP%20Connector%20for%20Microsoft%20.NET%20%20NCo_30_ProgrammingGuide.pdf)**).

In addition, by default the data transmitted is not encrypted. However, you can configure it on the OnBeforeConnection() callback that you can find more information in **[this article](https://success.outsystems.com/Documentation/11/Extensibility_and_Integration/SAP/Integrate_with_a_SAP_System)**. 

Combining this information with the **[SAP Extensibility API](https://success.outsystems.com/Documentation/10/Reference/OutSystems_APIs/SAP_Extensibility_API#SAPConnection_Class_Net)** it is possible to implement an alternative authentication mechanism.

This section provides all the information you need to integrate SAP and OutSystems.
