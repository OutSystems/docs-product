---
summary: How to add an HTTP header using the SOAP Extensibility API.
---

# Example: Add an HTTP header

In this example scenario we will add a new HTTP header to all the requests of a given consumed SOAP web service.

_Tip:_ You can adjust the provided example to remove or modify HTTP headers from your request instead of adding a new header by making the necessary adjustments to the `BeforeSendRequest` function.

## Code overview 

To achieve this, we will need to create C# code to perform the following:

1. In the function placeholder created by Integration Studio corresponding to the action you defined, register a custom endpoint behavior that we will need to implement.

1. Next, create the endpoint behavior class implementing the `IEndpointBehavior` interface from Windows Communication Foundation (WCF).  
This class will add a message inspector (based on another custom class that we will implement next) to the client runtime; it will be responsible for adding the new HTTP header to the request.  

1. Create the message inspector class that will add the HTTP header, adding code to the `BeforeSendRequest` function.

## Example 

Let's follow a concrete example on how to perform these steps:

1\. In Integration Studio, create an extension and define an action that will register a custom message inspector responsible for adding the SOAP request element before sending a request.  
In this example we defined an action in Integration Studio called "RegisterHttpHeaderCallback" with no input parameters.

![](<images/is-action-register-httpheader-callback.png>)

2\. Click 'Edit Source Code .NET'. Set the project target framework and add a reference to the `System.ServiceModel` assembly.  
Enter the code below, replacing the `MssRegisterHttpHeaderCallback` function placeholder that Integration Studio created for you:  

```csharp
// required 'using' statements at the beginning of the file
using System.ServiceModel;
using System.ServiceModel.Channels;
using System.ServiceModel.Description;
using System.ServiceModel.Dispatcher;
using OutSystems.SOAP.API;

/* ... */

// replace the 'MssRegisterHttpHeaderCallback' function placeholder with the following code
public void MssRegisterHttpHeaderCallback() {
    SoapRequest.RegisterEndpointBehavior(new AddHttpRequestHeaderBehavior());
}
```        

3\. Create the custom class `AddSoapHeaderBehavior` implementing WCF's interface `IEndpointBehavior`, containing the following code:

```csharp
class AddHttpRequestHeaderBehavior : IEndpointBehavior {

    void IEndpointBehavior.ApplyClientBehavior(ServiceEndpoint endpoint, ClientRuntime clientRuntime) {
        clientRuntime.ClientMessageInspectors.Add(new AddHttpRequestHeaderMessageInspector());
        // you can add more message inspectors here:
        // clientRuntime.ClientMessageInspectors.Add(new [...]);
    }

    void IEndpointBehavior.AddBindingParameters(ServiceEndpoint endpoint, BindingParameterCollection bindingParameters) {
        // do nothing
    }

    void IEndpointBehavior.ApplyDispatchBehavior(ServiceEndpoint endpoint, EndpointDispatcher endpointDispatcher) {
        // do nothing
    }

    void IEndpointBehavior.Validate(ServiceEndpoint endpoint) {
        // do nothing
    }
}
```

_Note:_ For this use case, you only need to add code to the `ApplyClientBehavior` function.

4\. Create the custom class `AddHttpRequestHeaderMessageInspector` implementing WCF's interface `IClientMessageInspector`, containing the following code:

```csharp
class AddHttpRequestHeaderMessageInspector : IClientMessageInspector {

    object IClientMessageInspector.BeforeSendRequest(ref Message request, IClientChannel channel) {
        string headerName = "MyCustomHeader1";
        string headerValue = "400";

        // before sending a request, add a new HTTP header, specifying its name and value
        if (request.Properties.TryGetValue(HttpRequestMessageProperty.Name, out object httpRequestMessageObject)) {
            HttpRequestMessageProperty httpRequestMessage = httpRequestMessageObject as HttpRequestMessageProperty;
            httpRequestMessage.Headers.Add(headerName, headerValue);
        } else {
            HttpRequestMessageProperty httpRequestMessage = new HttpRequestMessageProperty();
            httpRequestMessage.Headers.Add(headerName, headerValue);
            request.Properties.Add(HttpRequestMessageProperty.Name, httpRequestMessage);
        }
        return null;
    }

    void IClientMessageInspector.AfterReceiveReply(ref Message reply, object correlationState) {
        // here you would handle the web service response
    }
}
```
In this class we can add code to the function that handles the request (`BeforeSendRequest`), to the one handling the reply (`AfterReceiveReply`) or even to both functions, according to our use case.  
Since we want to add an element to the SOAP request header, we add code to the `BeforeSendRequest` function.

5\. Quit Visual Studio .NET and, back in Integration Studio, publish the extension by clicking the "1-Click Publish" toolbar icon or by pressing `F5`.

6\. In Service Studio, add a reference to the "RegisterHttpHeaderCallback" action of your extension in your application module.  

7\. In the flow of the SOAP callback of your SOAP Web Service, i.e. the flow of "OnBeforeRequestAdvanced", drag the "RegisterHttpHeaderCallback" action to the flow. 

8\. Publish the application module and test the application, checking that the HTTP header was added to the web service requests.
