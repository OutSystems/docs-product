---
tags: 
---

# Expose a REST API

If you want to expose methods to allow other systems to retrieve or manipulate information, you can do it using a REST API.

## Create the REST API Service

1. In the **Logic** tab, open the **Integrations** folder. 
2. Right-click REST and select **Expose REST API...** 
3. Set the name of your REST API. Example: `PhoneBook` 

## Create the REST API Method

1. Right-click your REST API and choose **Add REST API Method**. 
1. Set the name of your REST API method. Examples: `GetContacts`, `CreateContact`, `UpdateContact`. 
1. Make sure the HTTP Method property is set to the HTTP verb corresponding to the action your method will perform:  
    * GET – Read 
    * POST – Create 
    * PUT – Update 
    * DELETE – Delete 
1. Design the method as an action that retrieves or manipulates the data you are exposing.  
    Examples: `GetContacts` will return the list of all Contacts, `CreateContact` or `UpdateContact` will receive a "Contact" record and return the "Id" of the created or updated contact. 

After deploying the application, your REST API endpoints will be accessible.

Examples:

Default Endpoint | Description  
---|---  
`GET https://<server>/MyAPI/rest/PhoneBook/GetContacts` | Gets all contacts.
`GET https://<server>/MyAPI/rest/PhoneBook/GetContact` | Gets a contact.
`POST https://<server>/MyAPI/rest/PhoneBook/CreateContact` | Creates a contact.
`PUT https://<server>/MyAPI/rest/PhoneBook/UpdateContact` | Updates a contact.
`DELETE https://<server>/MyAPI/rest/PhoneBook/DeleteContact` | Deletes a contact.
`GET https://<server>/MyAPI/rest/PhoneBook/GetContactAddresses` | Gets all addresses of a contact.
  
The default endpoints are based in the HTTP Method (`GET`, `POST`, `PUT`, `DELETE`) and the name of the REST API Methods, but you can [customize the endpoints](<customize-rest-urls.md>) according to your needs.

You can test your REST API Method using several available tools, such as [curl](https://curl.haxx.se/) or [Postman](https://www.getpostman.com), or building an OutSystems application for that effect.

For manipulation methods where the input parameter is a Record (such as `POST` or `PUT`), you will have to add the "Content-Type" header to the request, with the value `application/json`.
