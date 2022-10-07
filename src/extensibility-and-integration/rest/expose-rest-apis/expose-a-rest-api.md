---
summary: Expose a REST API to allow other systems to retrieve or manipulate information.
tags: 
locale: en-us
guid: 28d56896-53c1-40c0-ac3d-84c757ac71d0
app_type: traditional web apps, mobile apps, reactive web apps
---

# Expose a REST API

If you want to expose methods to allow other systems to retrieve or manipulate information, you can do it using a REST API.

## Create the REST API Service

1. In the **Logic** tab, open the **Integrations** folder.
1. Right-click REST and select **Expose REST API...**
1. Set the name of your REST API.  
    A common recommendation is to name the exposed REST API according to its version. You could name the API `v1` for the first version of a REST API. You can also use a different name, like `PhoneBook`.  

## Create the REST API Method

1. Right-click your REST API and choose **Add REST API Method**.
1. Set the name of your REST API method. Examples: `GetContacts`, `CreateContact`, `UpdateContact`.
1. Set the HTTP Method property to the HTTP verb corresponding to the action your method performs:  
    * `GET` – Read
    * `POST` – Create
    * `PUT` – Update
    * `DELETE` – Delete
1. Design the method as an action that retrieves or manipulates the data you are exposing.  
    Examples: `GetContacts` returns the list of all Contacts, `CreateContact` or `UpdateContact` receive a "Contact" record and return the "Id" of the created or updated contact.

Your REST API endpoints are accessible after deploying the application.

Examples:

Default Endpoint | Description  
---|---  
`GET https://<server>/PhoneAPI/rest/v1/GetContacts` | Gets all contacts.
`GET https://<server>/PhoneAPI/rest/v1/GetContact` | Gets a contact.
`POST https://<server>/PhoneAPI/rest/v1/CreateContact` | Creates a contact.
`PUT https://<server>/PhoneAPI/rest/v1/UpdateContact` | Updates a contact.
`DELETE https://<server>/PhoneAPI/rest/v1/DeleteContact` | Deletes a contact.
`GET https://<server>/PhoneAPI/rest/v1/GetContactAddresses` | Gets all addresses of a contact.
  
OutSystems defines the default endpoints based on the HTTP Method (`GET`, `POST`, `PUT`, `DELETE`) and on the name of the REST API Methods, but you can [customize the endpoints](<customize-rest-urls.md>) according to your needs.

You can test your REST API Method using several available tools, such as [curl](https://curl.haxx.se/) or [Postman](https://www.postman.com), or building an OutSystems application for that effect.

For manipulation methods where the input parameter is a Record (such as `POST` or `PUT`), you must add the "Content-Type" header to the request with the value `application/json`.
