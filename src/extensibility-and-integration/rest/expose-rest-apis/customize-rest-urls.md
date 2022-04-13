---
summary: Customize the URL of your exposed REST API methods according to your needs.
tags: 
locale: en-us
guid: 3e4b997b-6c2c-4ccb-ae1a-31d4ed3ad0a8
---

# Customize REST URLs


OutSystems allows you to customize the URL of your REST API methods according to your needs.  
For example, you could customize this URL:

`GET https://<server>/PhoneAPI/rest/v1/GetContact?Id={Id}`  

to the following one:

`GET https://<server>/PhoneAPI/rest/v1/contacts/{Id}`

For that, do the following:

1. In the **Logic** tab, open the **Integrations** folder.

1. Expand the REST API and select the method you want to change to display its properties.

1. Set the **URL Path** property of the REST API method to the new custom URL.

    Example: `/contacts/{Id}`

    Note: You must set any input parameters included in the URL as mandatory.

The URL property changes accordingly.

The following sections show some examples of how to customize your endpoints.

## Endpoints for collections example

Use the same name for methods related to a resource. OutSystems knows which method to execute through the HTTP verb (for example, `GET` or `POST`):

Default Endpoint | URL Path | Customized Endpoint
---|---|---
`GET /PhoneAPI/rest/v1/GetContacts` | `/contacts` | `GET /PhoneAPI/rest/v1/contacts`
`POST /PhoneAPI/rest/v1/CreateContact` | `/contacts`  | `POST /PhoneAPI/rest/v1/contacts`
  
_Note:_ Endpoints displayed without protocol and server information for brevity.

## Endpoints for a resource example

When handling a specific resource, start the "URL Path" property value with the collection name and then add one of the following, depending on the HTTP verb:

* For `GET` or `DELETE`: Add the resource identifier (the input parameter of the REST API method) between `{` and `}`.

* For `PUT`: Add nothing, since the resource is already passed in the request Header or Body.

Default Endpoint | URL Path | Customized Endpoint
---|---|---
`GET /PhoneAPI/rest/v1/GetContact` | `/contacts/{Id}`  | `GET /PhoneAPI/rest/v1/contacts/{Id}`
`DELETE /PhoneAPI/rest/v1/DeleteContact` | `/contacts/{Id}` | `DELETE /PhoneAPI/rest/v1/contacts/{Id}`
`PUT /PhoneAPI/rest/v1/UpdateContact` | `/contacts` | `PUT /PhoneAPI/rest/v1/contacts`

## Endpoints for sub-collections example

With master-detail relationships, handle details as a collection under the master resource:

Default Endpoint  |  URL Path  |  Customized Endpoint  
---|---|---  
`GET /PhoneAPI/rest/v1/GetContactAddresses` | `/contacts/{Id}/addresses` | `GET /PhoneAPI/rest/v1/contacts/{Id}/addresses`

## Recommendations for REST API URLs

* You shouldn't end a customized URL with a forward slash ("/") character. It doesn't have an associated meaning and it's a common practice to omit it.

* There are several common naming conventions for REST API resources, such as "camelCase" and "snake_case". You should follow the same naming convention for all the URLs of your REST API.

## Important remarks

* Due to a .NET limitation, the last part of the URL — the part after the last `/` (slash) character — can't contain a `.` (period) character, otherwise method calls won't work.

* You can't use the reserved characters `;` (semicolon), `?` (question mark), and `=` (equal sign) in custom REST URLs of exposed REST API methods.  
    The `?` and `=` characters belong in the query string part of URLs (the part of the URL that starts with a `?` character), and the platform manages the query string part of URLs in exposed REST URL methods.

* When calling an exposed REST API method you must provide any input parameters with the **Receive In** property set to "URL" that aren't included in the custom URL as part of the query string.

    For example, as a follow-up to the examples presented in the previous section, consider an exposed REST API method "GetContactAddress" with two input parameters, "Id" and "AddressId". You could set the **URL Path** property of this method to the following value:

    `/contacts/{Id}/addresses/{AddressId}`

    In this case, all input parameters defined as received in the URL are present in the **URL Path** value. To call this method with `Id=5` (the contact ID) and `AddressId=10` you would use the following URL:

    `GET /PhoneAPI/rest/v1/contacts/5/addresses/10`

    You could also set the **URL Path** property to the following value, without including the "AddressId" input parameter in the custom URL:

    `/contacts/{Id}/addresses`

    In this case, to call the method including a value for the "AddressId" you would include this parameter at the end of the URL as part of the query string:

    `GET /PhoneAPI/rest/v1/contacts/5/addresses?AddressId=10`
