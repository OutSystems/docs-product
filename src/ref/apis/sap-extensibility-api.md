---
summary: The OutSystems SAP Extensibility API enables you to customize your connection and calls to SAP remote functions through an extension.
tags: support-application_development; support-Integrations_Extensions
---

# SAP Extensibility API

The OutSystems SAP Extensibility API is a .NET API that enables you to customize your connection and calls to SAP remote functions through an extension. See more about [how to develop an OutSystems extension](<../../extensibility-and-integration/integration-studio/getting-started/intro.md>).

## Required Files

To be able to use this API, you need to have these files in your extension:

* `OutSystems.SAP.API.dll`: File with the OutSystems SAP Extensibility API methods. You can find it in your Platform installation folder under '\Integration Studio\Extensibility\SAP\NET'. 

* `sapnco.dll` and `sapnco_utils.dll`: Drivers to communicate with SAP. You can find them in the [SAP Connector for Microsoft .NET](<https://support.sap.com/en/product/connectors/msnet.html>). Download and install the driver. When asked to install assemblies to GAC, choose 'None'. Remember the installation path, it will be needed. 

Optional: to access elements defined in namespaces, without having to write the whole namespace, you can include the following namespaces into your extension classes: `OutSystems.RuntimePublic.SAP` and `SAP.Middleware.Connector`.

## The Extension

Setup the extension:

1. Create the extension in Integration Studio. 
2. Create the actions your need. 
3. Open Visual Studio in button 'Edit Source Code .NET'. 
4. Edit project properties and set the project target framework to '.NET Framework 4.5.1'. 
5. Copy files `sapnco.dll` and `sapnco_utils.dll` to directory `\Source\NET\Bin\` of the extension. 
6. In Visual Studio, add `\Source\NET\Bin\sapnco.dll`, `\Source\NET\Bin\sapnco_utils.dll`, and `\Source\NET\Bin\OutSystems.SAP.API.dll` references to the project. 

Implement the .NET code:

1. In Visual Studio, implement the logic of the actions and use functionality you need from the SAP Extensibility API. 
2. Close Visual Studio. 
3. In Integration Studio, go to Resources tab. If `sapnco.dll` and `sapnco_utils.dll` are not grayed out, double-click on them and set their Deploy Action to 'Ignore'. 
4. Publish the extension. 

Use the extension:

1. In Service Studio, add a dependency to the actions you need from the extension.
2. Use SAP callback actions to call the actions implemented in the extension. 

## API Class Reference

The available classes in the SAP Extensibility API are:

* [SAPConnection](#sapconnection-class): Provides access and control over the connection parameters of the SAP connection. 
* [SAPContext](#sapcontext-class): Enables you to take control over the flow when calling an SAP remote function. 
* [SAPRequest](#saprequest-class): Allows to access parameter values sent and received when calling an SAP remote function. 

### SAPConnection Class

The object with information about the connection established when calling an SAP Remote Function Call. With the methods available in this class you can check and modify the connection parameters of the SAP connection being used to call a remote function call, e.g. you can change the authentication method to use SAP Logon Ticket instead of the method chosen in the development environment.

To handle the connection configurations, create an extension module, and use its methods in the 'OnBeforeConnection' callback action of the SAP connection.

#### Methods

Method  |  Description  
---|---  
static %%SAPConnection GetCurrent()  |  Returns the object with the configurations used to establish the connection to call an SAP remote function, when invoked inside the 'OnBeforeConnection' callback action of the SAP connection. Otherwise, returns null.  
SAP.Middleware.Connector.RfcConfigParameters GetRfcConfigParameters()  | Returns the SAP connector SAP.Middleware.Connector.RfcConfigParameters object, with the configurations used in the connection established to call an SAP remote function.  
void %%SetRfcConfigParameters(SAP.Middleware.Connector.RfcConfigParameters rfcConfigParameters)  |  Sets the SAP connector object SAP.Middleware.Connector.RfcConfigParameters object, with configurations used in the connection established to call an SAP remote function.  
  
#### Example

The following example shows how you can use the SAPConnection class to change the configuration of your connection to the SAP in order to call the remote functions, with the logon ticket instead of a username and password.
    
    
```csharp
using OutSystems.RuntimePublic.SAP;
using SAP.Middleware.Connector;
  
namespace OutSystems.SAPLogonTicketExtension {
  
    public class SAPLogonTicketExtension {
    
        public void SetTicketForAuthentication(string Ticket) {
            SAPConnection connection = SAPConnection.GetCurrent();
            RfcConfigParameters configParameters = connection.GetRfcConfigParameters();
        
            // Remove the user and password from the connection parameters.
            configParameters.Remove(RfcConfigParameters.User);
            configParameters.Remove(RfcConfigParameters.Password);
        
            // Set the ticket to use in the connection.
            configParameters[RfcConfigParameters.SAPSSO2Ticket] = Ticket;
            connection.SetRfcConfigParameters(configParameters);
        }
    }
}

```    

### SAPContext Class

The object with information about the connection's context when calling an SAP Remote Function Call. With the methods available in this class you can adjust and control the flow of an SAP Remote Function Call, e.g. you can adjust a connection to call multiple sap remote functions in the same context instead of only one.

To handle the connection's context, create an extension module, and use its methods in the 'OnBeforeCall' and 'OnAfterCall' callback actions of the SAP connection.

#### Methods

Method  |  Description  
---|---  
static void BeginContext()  |  Begins a stateful call sequence allowing the user to orchestrate two or more remote function calls in the same context.  
static void Commit()  |  Commits the changes made so far in the stateful call sequence by calling the remote function 'BAPI_TRANSACTION_COMMIT'.  
static void EndContext()  |  Ends a stateful call sequence. Must be placed after a beginContext() method.  
static void Rollback()  |  Rolls back any changes made so far in the stateful call sequence by calling the remote function 'BAPI_TRANSACTION_ROLLBACK'.  
  
#### Example

This example shows how you can have a stateful connection with SAP using the SAPContext class. It defines the begin and end of the context, as the commit and rollback of the changes made so far.
    
    
```csharp
using OutSystems.RuntimePublic.SAP;

namespace OutSystems.SAPStatefulConnectionExtension {

    public class SAPStatefulConnectionExtension {

        // We'll call this extension method to start the stateful call 
        //and before making any SAP RFC invocation.
        public void BeginContext() {
            SAPContext.BeginContext();
        }

        // We can now make several calls to SAP RFCs
        //inside the started stateful call

        // After invoking all SAP RFCs we want, we'll invoke
        //this method, that commits the transaction.
        //Then, we also end the SAP stateful call context to free
        //resources.
        public void Commit() {
            SAPContext.Commit();
            SAPContext.EndContext();
        }

        // If any problem happens we want to rollback all
        //the changes made so far, and close the stateful call
        //context.
        public void Rollback() {
            SAPContext.Rollback();
            SAPContext.EndContext();
        }
    }
}
```    

### SAPRequest Class

The object with information about the request of an SAP remote function call. With the methods available in this class you can adjust the parameters sent and received from the SAP Remote Function Calls, e.g. customize the received parameters values returned by SAP to show them differently to the end user.

To handle the remote function parameters, create an extension module, and use its methods in the 'OnBeforeCall' and 'OnAfterCall' callback actions of the SAP connection.

#### Methods

Method  |  Description  
---|---  
static %%SAPRequest GetCurrent()  |  Returns the object with information about the current SAP remote function call, when invoked inside the 'OnBeforeCall', or 'OnAfterCall' callback actions of the SAP connection. Otherwise, returns null.  
SAP.Middleware.Connector.IRfcFunction GetIRfcFunction()  |  Returns the SAP connector SAP.Middleware.Connector.IRfcFunction object, with the metadata and the parameters value for the current SAPRequest.  
  
#### Example

This example shows how you can adjust the input parameters values when calling an SAP remote function. For that we will get the remote function metadata of the 'Bapi\_Customer\_Getlist', and ensure that the customer id we are sending to SAP has 9 digits as the SAP internal value for this parameter. If not, we will add trailing zeros to the parameter value till it has the 9 digits.
    
    
```csharp
using System;
using OutSystems.RuntimePublic.SAP;
using SAP.Middleware.Connector;

namespace OutSystems.SAPChangeParamsExtension {

    public class SAPChangeParamsExtension {

        public void ChangeInputParams() {
            SAPRequest request = SAPRequest.GetCurrent();
            IRfcFunction func = request.GetIRfcFunction();
            IRfcTable table = func.GetTable("IDRANGE");

            foreach (IRfcStructure idRange_struct in table) {
                // Get the customer id parameter.
                String clientId_str = (string)idRange_struct.GetValue("LOW");

                // Set the parameter with a 9-digit value.
                int clientId_number = Convert.ToInt32(clientId_str);
                clientId_str = clientId_number.ToString("D9");
                idRange_struct.SetValue("LOW", clientId_str);
            }
    
            // Result for the following CUSTOMER values: 
            //    original: "1234"          new value: "000001234"
            //    original: "20548"         new value: "000020548"
            //    original: "521489653"     new value: "521489653"
        }
    }
}
```
