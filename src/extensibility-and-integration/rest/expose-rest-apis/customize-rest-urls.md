---
summary: Customize the URL of your exposed REST API methods according to your needs.
tags: 
---

# Customize REST URLs

OutSystems allows you to customize the URL of your REST API methods according to your needs.  
For example, you could customize this URL:

`GET https://<server>/MyAPI/rest/PhoneBook/GetContact?Id={Id}`  

to the following one:

`GET https://<server>/MyAPI/rest/PhoneBook/Contacts/{Id}`

For that, do the following:

1. In the **Logic** tab, open the **Integrations** folder; 
1. Expand the REST API and select the method you want to change to display its properties; 
1. Set the "URL Path" property of the REST API method to the new custom URL;
    1. Example: `/Contacts/{Id}` (input parameters must be set as mandatory). 

The URL property will change accordingly.

The following sections show some examples of how to customize your endpoints.

## Endpoints for Collections Example

Use the same name for methods related to a resource. OutSystems knows which method to execute through the HTTP verb (e.g. `GET`, `POST`):

Default Endpoint | URL Path | Customized Endpoint
---|---|---
`GET https://<server>/MyAPI/rest/PhoneBook/GetContacts` | `/Contacts` | `GET https://<server>/MyAPI/rest/PhoneBook/Contacts`
`POST https://<server>/MyAPI/rest/PhoneBook/CreateContact` | `/Contacts`  | `POST https://<server>/MyAPI/rest/PhoneBook/Contacts`
  
## Endpoints for a Resource Example

When handling a specific resource, start the "URL Path" property value with the collection name and then add one of the following, depending on the HTTP verb:

* For `GET` or `DELETE`: Add the resource identifier (the input parameter of the REST API method) between `{` and `}`.
* For `PUT`: Add nothing, since the resource is already passed in the request Header or Body. 

Default Endpoint | URL Path | Customized Endpoint
---|---|---
`GET https://<server>/MyAPI/rest/PhoneBook/GetContact` | `/Contacts/{Id}`  | `GET https://<server>/MyAPI/rest/PhoneBook/Contacts/{Id}`
`DELETE https://<server>/MyAPI/rest/PhoneBook/DeleteContact` | `/Contacts/{Id}` | `DELETE https://<server>/MyAPI/rest/PhoneBook/Contacts/{Id}`
`PUT https://<server>/MyAPI/rest/PhoneBook/UpdateContact` | `/Contacts` | `PUT https://<server>/MyAPI/rest/PhoneBook/Contacts`

## Endpoints for Sub-Collections Example

With master-detail relationships, handle details as a collection under the master resource:

Default Endpoint  |  URL Path  |  Customized Endpoint  
---|---|---  
`GET https://<server>/MyAPI/rest/PhoneBook/GetContactAddresses` | `/Contacts/{Id}/Addresses` | `GET https://<server>/MyAPI/rest/PhoneBook/Contacts/{Id}/Addresses`
