---
tags: support-Integrations_Extensions
---

# Execute SAP Stateless Calls

Some SAP BAPI remote functions do not need to commit database changes. However, since there is no way for the OutSystems platform to detect if a given SAP remote function requires a commit or not, by default it creates a new transaction for each SAP remote function call and commits changes before closing it.

This transaction created by the platform can degrade performance when invoking old BAPIs that already do an implicit commit or that do not need any commit.

To overcome this performance issue, create an extension module to manage stateless regions in SAP by following these steps:

1. Create an extension module using SAP Extensibility API to handle stateless connections in SAP.
1. In your application module in Service Studio, add dependencies to the extension actions.
1. Implement logic to execute SAP stateless calls in your application.

## Create the extension module for SAP

1. Get the [SAP Utilities component](<http://www.outsystems.com/forge/component/1012/sap-utilities/>) available in OutSystems Forge. This is a sample component with an extension module for SAP that contains actions for handling both stateful and stateless calls.  

    _Note:_ Since this extension makes use of the SAP Extensibility API, make sure you fulfill its [requirements](../../ref/apis/sap-extensibility-api.md).

1. Publish the extension.

## Add dependencies to extension actions in your module

To implement stateless calls in your application, add references to the following actions in the extension:

* **BeginStatelessRegion**: Starts a stateless connections region in SAP
* **EndStatelessRegion**: Ends the stateless connections region in SAP

Learn [how to consume exposed elements in a module](<../../develop/reuse-and-refactor/expose-and-reuse.md#reuse-functionality-from-other-modules>).

## Implement logic to execute stateless calls

Use SAP remote functions together with actions from the extension mentioned above to implement stateless calls. 

Every call inside a stateless region is made in a stateless connection unless a manual context is created through the **CreateContext** action.

In the following example, we consume a remote function from SAP that does not need a commit:

1. Implement stateless calls in an action by using the following elements in the main flow:

    BeginStatelessRegion
    :   Starts a stateless connections region in SAP.

    BAPI_SelectedMethod
    :   Example SAP remote function that performs some operation. It does not need a database commit.

    EndStatelessRegion
    :   Ends the stateless connections region in SAP.

1. In the exception handling flow add the following element:

    EndStatelessRegion
    :   Ends the stateless connections region in SAP.

![SAP stateless call example](images/sap-stateless-01.png?width=300)
