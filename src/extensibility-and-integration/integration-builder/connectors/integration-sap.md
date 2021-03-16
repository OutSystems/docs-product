# SAP OData integration

The SAP OData integration allows you to perform operations on SAP entities and call SAP actions from your OutSystems applications.

## Prerequisites

* Make sure you meet the general [Integration Builder prerequisites](../set-up.md#prerequisites).
* You have access to a SAP service specification in JSON or EDMX (XML) format. Check [Obtaining the SAP service specification](integration-sap-get-spec.md) for more information.
* Your OutSystems development environment can make HTTPS outbound requests (port 443) to your SAP instance.

## Service specification

Integration Builder accepts SAP service specifications in EDMX format (an XML-based format) or in JSON format.

You can upload the specification file (including dragging-and-dropping the file), or copy and paste the text for the whole specification into the appropriate text box when creating an SAP OData integration.

For more information, check [Obtaining the SAP service specification](integration-sap-get-spec.md).

<div class="info" markdown="1">

The information present in the EDMX and JSON file formats is not exactly the same. If you face any issues while importing a specific specification using one of the supported formats, try importing the service again using a different format.

</div>

## Selecting SAP objects

In the integration creation wizard you must choose what SAP entities and actions to consider in the new integration:

Entities
:   Select the SAP entities you want to interact with in OutSystems, selecting also the attributes of these entities. Integration Builder creates Server Actions to perform CRUD (create, read, update, delete) operations.  
    Note: Integration Builder creates actions for all the entity operations available on the service specification. However, depending on the exact service, some of the CRUD operations may not be available because they're not present in the service specification.

Actions
:   Actions available in the SAP service you want to invoke from OutSystems applications.

## Authentication methods

SAP connections support the following authentication methods through Integration Manager:

* **Basic authentication** — This is the type of authentication normally used with service accounts. You must provide a SAP username, the corresponding password and your SAP server domain.

* **Sandbox API authentication** — The sandbox API uses a key to authenticate requests. If you're using an SAP sandbox with Integration Builder, enter the authentication key provided by SAP.

When using one of these authentication methods, you must associate a connection with the integration after deploying it to a different environment. Use the Integration Manager application that was also deployed in the target environment for this purpose. See [Create a connection for the integration](../use.md#create-connection) for more information.

<div class="info" markdown="1">

You can also implement other authentication methods. Use the AdditionalHeaders input parameter of the Server Actions exposed by the integration.

</div>

## Supported OData versions

Integration Builder supports both OData 2.0 and OData 4.0 specifications. It must know the correct version of the specification because search queries have a different format depending on the OData version. Additionally, DateTime attributes also have a different format in different OData versions.

When Integration Builder can't determine the OData version from the service specification, it will ask you to select the correct version.

<div class="warning" markdown="1">

It's very important that you select the correct OData version when importing the service specification. **Selecting the incorrect OData version causes runtime issues.**

</div>
