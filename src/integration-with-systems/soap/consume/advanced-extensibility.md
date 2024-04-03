---
locale: en-us
guid: 74906504-7e14-40cd-8a55-221155e073a7
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/jSgZ0l0unYdVymLxKZasno/Extensibility%20and%20Integration?node-id=418:17
summary: The article explains how to use .NET code for advanced extensibility in SOAP web services with OutSystems, including a Forge component for common use cases
---
# Use Advanced Extensibility

When consuming a SOAP web service you can use your own .NET code to change the connection or to customize the message in the request and/or response.

To accelerate this, a Forge component called [SOAP Extensibility](<https://www.outsystems.com/forge/component-overview/5322/soap-extensibility-samples>) contains [server actions](https://www.outsystems.com/forge/component-documentation/5322/soap-extensibility/0) implementing many SOAP extensibility use cases using the [SOAP Extensibility API](../../../ref/apis/soap-extensibility-api.md).

You can use the [server actions](https://www.outsystems.com/forge/component-documentation/5322/soap-extensibility/0) provided by this component directly in your applications or use them as a starting point for implementing your own specific extensibility use cases.

If your use case is not covered by the component or you want to create it from scratch, the general workflow for implementing an advanced extensibility scenario is the following:

1\. Set up an OutSystems extension
:   Create a new extension in Integration Studio and define the actions you need.

2\. Implement the .NET code
:   Open Visual Studio .NET for editing the extension source code by clicking 'Edit Source Code .NET'.  
    Edit the project properties and set the project target framework to '.NET Framework 4.7.2' or greater, according to the version you're using.  
    Add any necessary assembly references.  
    Still in Visual Studio, implement the logic of the actions using the functionality you need from the [SOAP Extensibility API](<../../../ref/apis/soap-extensibility-api.md>). When you finish, close Visual Studio.  
    In Integration Studio, publish the extension.

3\. Use the extension
:   In Service Studio, add a dependency to the actions you need from the extension.  
    
   Select your SOAP Web Service element in the element tree and create a new SOAP callback in the OnBeforeRequest property (the callback's name is "OnBeforeRequestAdvanced").  

   ![Screenshot of SOAP Web Service properties with the OnBeforeRequest callback highlighted](images/soap-properties-beforerequest-ss.png "SOAP Web Service Properties")    

   Open the callback flow and drag the desired extension action(s) to the flow according to your use case.  
    
   **Note:** Extension actions using the SOAP Extensibility API can only be used in the context of a SOAP callback flow.

   ![Screenshot showing how to add a callback action to a SOAP callback flow in Service Studio](images/flow-add-callback-ss.png "Adding a Callback to a SOAP Flow")

## SOAP extensibility component use cases { #example-use-cases }

Check this page sub-topics for guidelines on how to implement common use cases of SOAP advanced extensibility.
