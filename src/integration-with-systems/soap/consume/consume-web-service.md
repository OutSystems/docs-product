---
summary: Guide on consuming SOAP Web Services in OutSystems 11 (O11), including WSDL configuration and method integration.
tags: soap web services, wsdl configuration, service integration, logic tab, web service definition
locale: en-us
guid: 12679c35-25ab-4d32-a6f2-11a3b94ee3d7
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/jSgZ0l0unYdVymLxKZasno/Extensibility-and-Integration?type=design&node-id=418%3A4&mode=design&t=8a1ub9syb4QKHbuk-1
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# Consume a SOAP Web Service

To consume a SOAP Web Service in your application, do the following:

1. In the **Logic** tab, open the **Integrations** folder.

1. Right-click the SOAP element and select **Consume SOAP Web Service...**.

    ![Screenshot of the 'Consume SOAP Web Service' dialog in OutSystems Service Studio](images/soap-consume-add-consume-ss.png "Consume SOAP Web Service Dialog")

1. In the displayed dialog, specify the location of the Web Service definition (WSDL) and click **Consume**.

    ![Dialog box for specifying the WSDL location of a SOAP Web Service in OutSystems](images/soap-consume-wsdl-ss.png "Specify WSDL Location")

    When providing a remote URL, type it exactly the same way as you would type it into your web browser. To import a WSDL from your local file system, click **Upload file** and select your WSDL.

1. If the service supports more than one binding, choose the desired binding and click **Next**. Otherwise, Service Studio skips this step.

    ![Selection of SOAP service bindings in OutSystems Service Studio](images/soap-consume-bindings-ss.png "Select SOAP Service Binding")

1. If the service supports more than one method, choose the methods you wish to consume and click **Finish**. Otherwise, Service Studio skips this step.

    ![Choosing methods from a SOAP Web Service to consume in OutSystems](images/soap-consume-methods-ss.png "Choose SOAP Service Methods")

Be aware that, for all remote WSDL files, the URL address must be accessible from the machine running **Platform Server** and not directly from Service Studio.

![Illustration showing the requirement for the WSDL file to be accessible from the Platform Server in OutSystems](images/wsdl-files-diag.png "WSDL File Accessibility")

When you consume a SOAP Web Service, OutSystems does the following for you:

* Creates the SOAP Web Service
* Creates the exposed Web Service Methods with the corresponding input and output parameters
* Creates the Structures and Static Entities to hold the complex types defined in the WSDL
* Maps the [XML data types into OutSystems data types](<../../../ref/integration-with-systems/soap/consumed-soap/mapping-xml-to-outsystems.md>)

![Result of consuming a SOAP Web Service in OutSystems, showing created elements](images/soap-consume-result.png "SOAP Web Service Consumption Result")

OutSystems doesn't provide direct support for Web Services Enhancements (WSE). Instead, you can use the [SOAP Extensibility API](<../../../ref/apis/soap-extensibility-api.md>) to implement the functionality provided by Web Services Enhancements in your applications.

## Use a SOAP Web Service Method in an Application

OutSystems translates the methods exposed by a SOAP Web Service into OutSystems actions, with the same semantics as any action created by you in Service Studio.

You can now use the newly created method in your application the same way you use the remaining Server Actions:

1. Go to the action flow where you want to use the Web Service Method.

1. In the **Logic** tab, open the **Integrations** folder and SOAP element.

1. Open the SOAP Web Service and drag the Web Service Method into your action flow.

![Dragging a SOAP Web Service method into an action flow in OutSystems Service Studio](images/soap-consume-invoke.png "Invoke SOAP Web Service Method")
