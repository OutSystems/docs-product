---
summary: OutSystems 11 (O11) simplifies SOAP Web Service documentation by auto-generating it upon module publication based on the "Description" properties.
tags: soap web services, api documentation, module publishing, service studio features, web service integration
locale: en-us
guid: 07a471e4-c784-44ba-b868-8c90605481c0
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/jSgZ0l0unYdVymLxKZasno/Extensibility%20and%20Integration?node-id=418:36
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# Document an Exposed SOAP Web Service

Adding documentation to your SOAP Web Service is essential as it helps developers to integrate their applications with your system.

OutSystems facilitates documenting your SOAP Web Service by automatically generating the documentation when you publish the module. The documentation text is based on the "Description" property of the SOAP Web Service and its methods.

Do the following:

1. Fill in the "Description" property of the SOAP Web Service and the SOAP Web Service Methods.
2. Publish the module. 

After publishing, the documentation is available under the module URL at `<ModuleName>/<WebServiceName>.asmx`.

To open the SOAP Web Service documentation, right-click the tree element of your SOAP Web Service in Service Studio and select **Open Documentation**.

![Right-clicking the SOAP Web Service in Service Studio to select 'Open Documentation'](images/soap-open-documentation-ss.png "Open SOAP Web Service Documentation")

Note: The description of the Input and Output Parameters of the Web Service Methods is not used for documentation purposes.

