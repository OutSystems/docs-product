---
summary: How to add support for Message Transmission Optimization Mechanism (MTOM) using the SOAP Extensibility API.
locale: en-us
guid: 37ee4b4e-0cfb-471e-aa97-6fb0bb427ff4
---

# Use MTOM

The Message Transmission Optimization Mechanism (MTOM) allows you to optimize the transmission and/or wire format of SOAP messages by selectively encoding portions of the message as binary data.

In this example scenario we will add support for encoding SOAP messages using MTOM.

Do the following:

1\. In Integration Studio create an extension and define an action that will enable MTOM.  
For example, define an action in Integration Studio called "EnableSoapMTOM" without any parameters.

2\. Click 'Edit Source Code .NET'. Set the project target framework and add a reference to the `System.ServiceModel` assembly.  
Enter the code below, replacing the `MssEnableSoapMTOM` function placeholder that Integration Studio created for you:  

```csharp
// required 'using' statements at the beginning of the file
using System.Linq;
using System.ServiceModel.Channels;
using OutSystems.SOAP.API;

/* ... */

// replace the 'MssEnableSoapMTOM' function placeholder with the following code
public void MssEnableSoapMTOM() {
    // Get current request
    var client = SoapRequest.GetCurrentClient();

    // Create a binding based on the one already set up
    var customBinding = new CustomBinding(client.Endpoint.Binding);

    // Get the TextMessageEncodingBindingElement;
    // it will be replaced with the MTOM encoding element
    var textEncodingElement = customBinding.Elements.OfType<TextMessageEncodingBindingElement>().Single();
    var mtomEncodingElement = new MtomMessageEncodingBindingElement(client.Endpoint.Binding.MessageVersion, textEncodingElement.WriteEncoding);

    // Insert MTOM encoding element where TextMessageEncodingBindingElement was
    // This is necessary to respect the mandatory order of elements in a custom binding: 
    // https://docs.microsoft.com/en-us/dotnet/framework/wcf/extending/custom-bindings
    customBinding.Elements.Remove(textEncodingElement);
    customBinding.Elements.Insert(customBinding.Elements.Count - 1, mtomEncodingElement);

    //Replace previous binding
    client.Endpoint.Binding = customBinding;
}
```        

3\. Quit Visual Studio .NET and, back in Integration Studio, publish the extension by clicking the "1-Click Publish" toolbar icon or by pressing `F5`.

4\. In Service Studio, add a reference to the "EnableSoapMTOM" action of your extension in your application module.  

5\. In the flow of the SOAP callback of your SOAP Web Service, i.e. the flow of "OnBeforeRequestAdvanced", drag the "EnableSoapMTOM" action to the flow. 

6\. Publish the application module and test the application.
