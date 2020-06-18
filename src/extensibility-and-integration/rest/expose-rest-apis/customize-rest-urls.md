---
summary: Customize the URL of your exposed REST API methods according to your needs.
tags: 
---

# Customize REST URLs

<div class="info" markdown="1">

We've been working on this article. Please let us know how useful this new version is by voting.

</div>

OutSystems allows you to customize the URL of your REST API methods according to your needs.  
For example, you could customize this URL:

`GET https://<server>/PhoneAPI/rest/v1/GetContact?Id={Id}`  

to the following one:

`GET https://<server>/PhoneAPI/rest/v1/Contacts/{Id}`

For that, do the following:

1. In the **Logic** tab, open the **Integrations** folder.
1. Expand the REST API and select the method you want to change to display its properties.
1. Set the "URL Path" property of the REST API method to the new custom URL.

    Example: `/Contacts/{Id}`

    Note: You must set any input parameters included in the URL as mandatory.

The URL property changes accordingly.

The following sections show some examples of how to customize your endpoints.

## Endpoints for collections example

Use the same name for methods related to a resource. OutSystems knows which method to execute through the HTTP verb (for example, `GET` or `POST`):

Default Endpoint | URL Path | Customized Endpoint
---|---|---
`GET /PhoneAPI/rest/v1/GetContacts` | `/Contacts` | `GET /PhoneAPI/rest/v1/Contacts`
`POST /PhoneAPI/rest/v1/CreateContact` | `/Contacts`  | `POST /PhoneAPI/rest/v1/Contacts`
  
_Note:_ Endpoints displayed without protocol and server information for brevity.

## Endpoints for a resource example

When handling a specific resource, start the "URL Path" property value with the collection name and then add one of the following, depending on the HTTP verb:

* For `GET` or `DELETE`: Add the resource identifier (the input parameter of the REST API method) between `{` and `}`.
* For `PUT`: Add nothing, since the resource is already passed in the request Header or Body.

Default Endpoint | URL Path | Customized Endpoint
---|---|---
`GET /PhoneAPI/rest/v1/GetContact` | `/Contacts/{Id}`  | `GET /PhoneAPI/rest/v1/Contacts/{Id}`
`DELETE /PhoneAPI/rest/v1/DeleteContact` | `/Contacts/{Id}` | `DELETE /PhoneAPI/restv1/Contacts/{Id}`
`PUT /PhoneAPI/rest/v1/UpdateContact` | `/Contacts` | `PUT /PhoneAPI/rest/v1/Contacts`

## Endpoints for sub-collections example

With master-detail relationships, handle details as a collection under the master resource:

Default Endpoint  |  URL Path  |  Customized Endpoint  
---|---|---  
`GET /PhoneAPI/rest/v1/GetContactAddresses` | `/Contacts/{Id}/Addresses` | `GET /PhoneAPI/rest/v1/Contacts/{Id}/Addresses`
