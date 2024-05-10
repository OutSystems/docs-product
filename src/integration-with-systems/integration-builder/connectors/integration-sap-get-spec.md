---
locale: en-us
guid: dc751f41-faba-4421-be15-a595e5bd4a55
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/jSgZ0l0unYdVymLxKZasno/Extensibility%20and%20Integration?node-id=1019:6342
summary: Explore how to obtain SAP service specifications for integration with OutSystems 11 (O11) using the SAP API Business Hub and custom service endpoints.
---
# Obtaining the SAP service specification

The process of obtaining the SAP service specification that you must provide in Integration Builder depends on the type of service:

* **Default SAP Service**: Download the specification from the SAP API Business Hub
* **Custom SAP Service**: Download the specification from a specific service endpoint

## Service specification for a default SAP Service

Do the following:

1. Open the [SAP API Business Hub](https://api.sap.com/) in your browser.

    ![Homepage of the SAP API Business Hub showing the main interface](images/sap-hub-1.png "SAP API Business Hub Homepage")

1. In the main services list, search for the SAP service you want to integrate with and click the card for that service.

    For example, consider that you wanted to integrate with the "Business Partner (A2X)" OData API, available in SAP S/4HANA Cloud.

    ![Service selection in SAP API Business Hub, highlighting the Business Partner (A2X) OData API card](images/sap-get-spec-1.png "Selecting a Service in SAP API Business Hub")

    **Note:** The Business Hub includes REST, SOAP, and OData APIs. **Make sure the API you select is an OData API.**

1. Open the **Details** tab (1).

    ![Details tab in SAP API Business Hub with the Download API Specification option](images/sap-get-spec-2.png "Downloading API Specification from SAP API Business Hub")

1. Click **Download API Specification** (2) and select either **JSON** or **EDMX** from the available formats (3).

## Service specification for a custom SAP Service

To get the specification for a custom SAP Service, you must make a request to its `/$metadata` endpoint. For this purpose, you can use an API client like Postman or SAP Gateway Client.

Do the following:

1. Using an API client, make a `GET` request to the `/$metadata` endpoint of the SAP service you want to integrate with.

    Example endpoint:  
    `https://<your_sap_hostname>/sap/opu/odata/sap/API_CUSTOMER_MATERIAL_SRV/$metadata`

1. Copy the service specification code returned as a response.

1. In Integration Builder, click the link in the sentence "You can also **paste the specification** code.", available in the **Upload specification** step.

    ![Integration Builder interface with an option to paste the SAP service specification code](images/sap-custom-spec-1.png "Paste Specification Code in Integration Builder")

1. Paste the service specification in the pop-up window and press **Upload**.

    ![Pop-up window in Integration Builder for uploading the SAP service specification](images/sap-custom-spec-2.png "Uploading Service Specification")
