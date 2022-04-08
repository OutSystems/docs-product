---
tags: support-Integrations_Extensions
locale: en-us
guid: e45e96ca-8a1e-4bb1-b23f-e2306f0157be
---

# Execute SAP Stateful Calls

Some BAPI remote functions commit database changes, but some don’t have a commit implemented in their code. By default, OutSystems creates a new transaction for each SAP remote function call, and commits changes before closing it.

However, there are situations where you need to make several calls to SAP remote functions in the same transaction.

To achieve this, you need an extension module to manage stateful calls in SAP.

## Create an Extension Module Using SAP Extensibility API

1. Go to Forge and get the component [SAP Utilities](<http://www.outsystems.com/forge/component/1012/sap-utilities/>). It's a sample with an extension module for SAP, with actions for handling stateful calls.
1. Because SAPUtilities extension makes use of the SAP Extensibility API, setup your extension following the requirements described in [here](<../../ref/apis/sap-extensibility-api.md>).
1. Publish the extension.

## Use the Extension in your Application

To implement stateful calls in your application do the following:

1. Add dependencies to the following actions of the SAPUtilities extension:
    * **BeginContext**: starts a stateful connection in SAP
    * **EndContext**: ends the stateful connection in SAP
    * **Commit**: commits changes inside a stateful connection in SAP
    * **Rollback**: rolls back changes inside a stateful connection in SAP
2. Use SAP remote functions together with the actions from the extension to implement a stateful call. 
