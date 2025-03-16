---
summary: Learn to consume REST API methods in OutSystems 11 (O11) using OpenAPI specifications or individual methods in Service Studio.
tags: rest api, openapi specification, api integration, service studio ide, integrations
locale: en-us
guid: b7ea1336-4e6b-49a8-8a61-fd56c2ae5f57
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
topic:
  - consume-refresh-methods
---

# Consume one or more REST API methods

Make sure you gather all the information you need from the REST API documentation before starting. You can also take a quick video tour about [Consuming a REST API in 10 minutes with OutSystems](https://youtu.be/gNyWIeJYfG0).

In Service Studio you can:

* consume several REST API methods (all methods or just the methods you select) described in a OpenAPI specification file, provided either by entering a URL or by selecting a specification file from the local file system.

* Consume a single REST API method.

## Consume several methods of a REST API { #all-methods }

You can consume several methods of a REST API (all API methods or just the methods you select) if that API is compliant with the [OpenAPI specification](https://swagger.io/resources/open-api/). REST APIs exposed by OutSystems are compliant with this specification.  

You can import OpenAPI specifications either by providing a URL or by selecting a specification file from the local file system.

Do the following:

1. In the **Logic** tab, open the **Integrations** folder.

1. Right-click on the **REST** element and select **Consume REST API...**

    ![Context menu in Service Studio showing the option to consume a REST API](images/ss-rest-consume-menu.png "Service Studio Consume REST API Menu")

1. In the displayed dialog, choose **Add Multiple Methods**.

    ![Dialog window in Service Studio for adding multiple REST API methods](images/ss-rest-consume-dialog-multiple.png "Add Multiple Methods Dialog in Service Studio")

1. If you're importing an OpenAPI 3.0 specification file and the specification includes more than one server endpoint, choose the desired endpoint and click **Next**.

    **Note:** You can't change the server endpoint after importing the REST API.

1. Choose the REST API methods you want to import (by default, all methods) and click **Finish**.

    ![Selection of REST API methods to import in Service Studio](images/ss-rest-consume-choose-methods.png "Select REST API Methods to Import")

When importing the REST API, Service Studio does the following:

* Creates the REST API
* Creates REST API Methods with the corresponding input and output parameters
* Creates the Structures to hold the corresponding input and output parameters under a new tree element with the REST API name
* Maps the [REST Data Types into OutSystems Data Types](../../../ref/integration-with-systems/rest-apis/consumed-rest-api/mapping.md)

![REST API elements created in Service Studio after importing methods](images/ss-rest-consume-created-elements.png "REST API Elements Created in Service Studio")

![Data structures created in Service Studio corresponding to the REST API methods](images/ss-rest-consume-created-structures.png "REST API Structures Created in Service Studio")

## Consume a single method of a REST API { #single-method }

In OutSystems you can consume a **single method** of a REST API, based on example content for the request and/or response. You may need to specify input parameters in the URL and/or a body for manipulation methods like `POST` or `PUT`.

Do the following:

1. In the **Logic** tab, open the **Integrations** folder.

1. Right-click on the **REST** element and select **Consume REST API...**.

    ![Context menu in Service Studio showing the option to consume a REST API](images/ss-rest-consume-menu.png "Service Studio Consume REST API Menu")

1. In the displayed dialog, choose **Add Single Method**.

    ![Dialog window in Service Studio for adding a single REST API method](images/ss-rest-consume-dialog-single.png "Add Single Method Dialog in Service Studio")

1. Fill the information about the **Method URL**. You can include parameters between braces in the URL for the method's input parameters.

    Examples:  
    `GET https://api.example.com/Portal/rest/Contacts/GetAll`  
    `GET https://api.example.com/Portal/rest/Contacts/Get?Id={Id}`  
    `POST https://api.example.com/Portal/rest/Contacts/Create`  

    Each input parameter defined between braces in the URL becomes an input parameter of the method.

    <div class="info" markdown="1">

    **Note:** Input parameters in URL query strings must follow a specific format. See [Using parameters in the URL query string](#using-params-query-string) for details.

    </div>

1. If the REST API you are consuming requires specific headers or uses HTTP Basic Authentication, open the **Headers / Auth** tab and fill the necessary information.

    ![Configuration of headers and authentication for a REST API in Service Studio](images/ss-rest-consume-headers-auth.png "Headers and Authentication Configuration in Service Studio")

1. Fill the information about the Request and the Response. The easiest way to do this is to perform a test to the API and use the test result.

    Alternatively, you can add the JSON structure or text/plain example directly in the **Request** and **Response** fields in the **Body** tab. Open the **Test** tab. If you have parameters in your **Method URL**, you need to insert the parameter values to execute the test:

    ![Testing a REST API method in Service Studio with parameters and response](images/ss-rest-consume-test.png "Test REST API Method in Service Studio")

    For manipulation methods, such as `POST` or `PUT`, fill the **Request** of the Body Content with the corresponding request structure:  

    ![Filling the request body content for testing a REST API method in Service Studio](images/ss-rest-consume-test-request.png "Request Body Content for REST API Method Test")

1. Click **Test**. If the test is successful, you see the method's response in the Response area of **Test** tab.

    Use that information to fill in the Response in the **Body** tab by clicking **Copy to Response body** in the **Response** area. Leave only the needed fields.

    For manipulation methods (such as `POST` or `PUT`), do the same for the Request, by pressing **Copy to Request body** in the Request area:

    ![Copying the test request to the request body field in Service Studio](images/ss-rest-consume-test-request-copy.png "Copy Test Request to Request Body in Service Studio")

    Usually, you obtain the most common fields this way. To know in full detail all the available fields, check the API documentation.

1. Check if the **Request** and **Response** information is correct in the **Body** tab and click **OK**:

    ![Finalizing the REST API method import with request and response details in Service Studio](images/ss-rest-consume-body.png "Finalize REST API Method Import in Service Studio")

When importing the REST API method, Service Studio does the following:

* Creates a REST API element under the **REST** element in the tree
* Creates a REST API Method with the corresponding input and output parameters
* Creates the Structures to hold the corresponding input and output parameters under a new tree element with the REST API name
* Maps the [REST Data Types into OutSystems Data Types](../../../ref/integration-with-systems/rest-apis/consumed-rest-api/mapping.md)

![REST API elements created in Service Studio after importing methods](images/ss-rest-consume-created-elements.png "REST API Elements Created in Service Studio")

![Data structures created in Service Studio corresponding to the REST API methods](images/ss-rest-consume-created-structures.png "REST API Structures Created in Service Studio")

## Use a REST API Method in your Application { #use }

OutSystems translates the methods exposed by a REST API into **OutSystems actions**, with the same semantics as any action created by you in Service Studio.

You can now use the newly created methods in your application the same way you use any Server Action:

1. Go to the action flow where you want to use the REST API Method.
  
    ![Dragging a REST API method into an application flow in Service Studio](images/ss-rest-consume-use-method-3.png "Using REST API Method in Application Flow")

1. In the **Logic** tab, open the **Integrations** folder and the **REST** element.

1. Expand the REST API element and drag the REST API Method into your action flow.
  
    ![Expanding the REST API element to use a method in Service Studio](images/ss-rest-consume-use-method-1.png "Expand REST API Element to Use Method")

1. Use the method's output parameters as you do for any other action.
  
    ![Using output parameters of a REST API method in an application flow in Service Studio](images/ss-rest-consume-use-method-2.png "Output Parameters of REST API Method")

## Using parameters in the URL query string { #using-params-query-string }

OutSystems supports using input parameters in URL query string as name/value pairs, like in `key={value}`, where `value` is an input parameter. The URL query string is the part of the URL after the `?` (question mark) character.

For example, you can use the following URLs:

* `http://apps.example.com/Orders/{id}/?show_details={ShowDetails}`

    Uses `id` outside the query string, as part of the URL.  
    Uses `ShowDetails` as the value of a query string parameter, following the allowed format (`key={value}`).

* `http://apps.example.com/Orders/?key1={value1}&key2={value2}`

    Uses `value1` and `value2` as input parameters, following the allowed format.  
    You can separate parameters in the query string using the `&` (ampersand) character.

Using input parameters in the query string following a different format, or as a way of defining the whole query string, is **not supported** in OutSystems.

For example, you can't use any of the following URLs because they're not currently supported:

* `http://apps.example.com/Orders/?{key}={value}`

    You can't use an input parameter (in this case, `key`) to define a query string parameter name.

* `http://apps.example.com/Orders/?key={value1},{value2}`

    You can't use several input parameters (in this case, `value1` and `value2`) to define a composed value for a query string parameter.

* `http://apps.example.com/Orders/?name={"last":{value1},"first":{value2}}`

    You can't use JSON structures as query string parameter values.

* `http://apps.example.com/Orders/?{QueryString}`

    You can't define a generic query string that's only defined at runtime using an input parameter.
