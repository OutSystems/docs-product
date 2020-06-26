# Use Advanced Extensibility

When consuming a SOAP web service you can use your own .NET code to change the connection or to customize the message in the request and/or response.

The general workflow for implementing an advanced extensibility scenario is the following:

1\. Set up an OutSystems extension
:   Create a new extension in Integration Studio and define the actions you need.

2\. Implement the .NET code
:   Open Visual Studio .NET for editing the extension source code by clicking 'Edit Source Code .NET'.  
    Edit the project properties setting the project target framework to '.NET Framework 4.6.1'.  
    Add any necessary assembly references.  
    Still in Visual Studio, implement the logic of the actions using the functionality you need from the [SOAP Extensibility API](<../../../ref/apis/soap-extensibility-api.md>). When you finish, close Visual Studio.  
    In Integration Studio, publish the extension.

3\. Use the extension
:   In Service Studio, add a dependency to the actions you need from the extension.  
    Select your SOAP Web Service element in the element tree and create a new SOAP callback in the OnBeforeRequest property (the callback's name is "OnBeforeRequestAdvanced").  

    ![](<images/ss-soap-properties-beforerequest.png>)    

    Open the callback flow and drag the desired extension action(s) to the flow according to your use case.  
    
    **Note:** Extension actions using the SOAP Extensibility API can only be used in the context of a SOAP callback flow.

    ![](<images/ss-flow-add-callback.png>)

## Example SOAP extensibility use cases { #example-use-cases }

OutSystems provides guidelines on how to implement common use cases of SOAP advanced extensibility. Check the sub-topics of this page for more information.

<div class="info" markdown="1">

OutSystems provides a Forge component called [SOAP Extensibility Samples](<https://www.outsystems.com/forge/component-overview/5322/soap-extensibility-samples>) that contains server actions implementing many SOAP extensibility use cases using the SOAP Extensibility API.

You can use the server actions provided by this component directly in your applications or use them as a starting point for implementing your own specific extensibility use cases.

</div>
