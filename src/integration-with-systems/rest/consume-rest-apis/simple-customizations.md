---
summary: Add logic to customize the information sent in requests or received in responses of consumed REST APIs.
tags: 
locale: en-us
guid: 21574391-c5b3-4831-a7b2-8aaf94df2230
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/jSgZ0l0unYdVymLxKZasno/Extensibility%20and%20Integration?node-id=410:85
---

# Simple Customizations

When consuming a REST API, you can add logic to customize the information that is sent in the requests or received in the responses. Use the following callbacks for this purpose:

OnBeforeRequest
:   Use to modify the information of the original request, such as the URL, the request text or the headers. 

OnAfterResponse
:   Use to modify the information of the original response, such as the status code or the response text. 

In these callbacks you can access the information from the original request or response, manipulate it and assign a modified value to the customized request or response.

If you have an advanced integration scenario requiring .NET code to customize requests or responses, check [Advanced Customizations](advanced-customizations.md).

In the [OutSystems Forge](https://www.outsystems.com/forge/) you can find several components providing an interface to third-party services using REST integration, such as the [Box Connector](https://www.outsystems.com/forge/component/586/box-connector/) or the [JIRA Connector](https://www.outsystems.com/forge/component/936/jira-connector/), where you can see in detail how the REST requests and responses are customized.

<div class="info" markdown="1">

Using this simple customization method you can add HTTP headers and/or change their values, but you cannot remove existing headers. To remove HTTP headers you must use the OutSystems REST Extensibility API. Check [Advanced Customizations](advanced-customizations.md) for more information.

</div>

## Customize the request

To customize the request before it is sent:

1. Set the **On Before Request** property of the REST API to `New OnBeforeRequest`.
  
    ![Screenshot showing how to select 'New OnBeforeRequest' in the REST API properties](images/rest-new-onbeforerequest-ss.png "Select New OnBeforeRequest")

    An "OnBeforeRequest" action is made available under the REST API.

1. Double-click the newly created action to edit it.

1. Add your own logic to customize the request.

### Customize the parts of a multipart/form-data request { #multipart}

To customize specific parts of a [multipart/form-data request](consume-multipart-form-data.md) inside the **OnBeforeRequest** callback, such as adding, removing, or editing parts, you can use the **RequestParts** attribute that represents a **RequestPart** list.

![Screenshot of the RequestParts attribute in the REST API editor](images/requestparts-ss.png "RequestParts Attribute")

The following example shows the logic flow of an **OnBeforeRequest** callback that appends, removes, and edits a part from the request. In this example, the **Request.RequestParts** list is edited. 

![Example logic flow in an OnBeforeRequest callback showing how to append, remove, and edit parts of a request](images/requestparts-action-ss.png "OnBeforeRequest Callback Logic Flow")

### Example use case: Adding a header for token-based authentication

<div class="info" markdown="1">

Consider using [OAuth client credentials flow](rest-oauth2-authorization.md) as a straightforward method to access remote resources in your app.

</div>

Consider a REST API that uses token-based HTTP authentication, requiring consumers to include an authorization token in an HTTP header. After importing this REST API to your OutSystems application, use the "OnBeforeRequest" callback to add a new header with the token.

You can add the following steps to the callback logic flow, as an example:

1. Add a local variable with "HTTPHeader" data type to the OnBeforeRequest callback action.

1. Define a new HTTP header (name and value) using the local variable you created in the previous step.

    Example:  
    Name = `"Authorization"`  
    Value = `"Bearer " + AccessTokenVar`

1. Add this header to the list of request headers using the "ListAppend" action.
   The current request headers are in the "Request.Headers" attribute.

1. Set the "CustomizedRequest" output parameter to our changed "Request" using an Assign element.

![Screenshot illustrating the steps to add an authorization header in the OnBeforeRequest callback](images/rest-example-onbeforerequest-ss.png "Adding a Header for Token-Based Authentication")

## Customize the response

To customize the response after it has arrived:

1. Set the **On After Response** property of the REST API to `New OnAfterResponse` action.

    ![Screenshot showing how to select 'New OnAfterResponse' in the REST API properties](images/rest-new-onafterresponse-ss.png "Select New OnAfterResponse")

    An "OnAfterResponse" action is made available under the REST API.

1. Double-click the newly created action to edit it.

1. Add your own logic to customize the response. 
