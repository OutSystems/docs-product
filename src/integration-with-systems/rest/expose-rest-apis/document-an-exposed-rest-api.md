---
summary: Learn how OutSystems 11 (O11) simplifies REST API documentation by automatically generating it upon module publication.
tags: 
locale: en-us
guid: b125017d-f037-4a5f-bba4-cdc563e0a4bf
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/jSgZ0l0unYdVymLxKZasno/Extensibility%20and%20Integration?node-id=418:0
---

# Document an exposed REST API

Adding documentation to your REST API is essential as it helps developers to integrate their applications with your system.

OutSystems facilitates documenting your REST API by automatically generating the documentation when you publish the module. The platform generates the documentation from the properties of the REST API, the REST API methods, and their parameters. Subsequent changes to the exposed REST API (for example, when endpoints or parameters and added or changed) are automatically updated in the generated documentation.

Do the following:

1. In Service Studio, make sure that your REST API methods and their parameters have their "Description" property filled in. You can use [Markdown](http://daringfireball.net/projects/markdown/syntax) in the description to format the text.

1. Publish the module.

OutSystems publishes the documentation under the base URL of the REST API. To open it do the following:

1. In Service Studio, right-click the tree element of your REST API.

1. Choose **Open Documentation**.

    ![Context menu in Service Studio showing the 'Open Documentation' option for a REST API.](images/rest-open-documentation-ss.png "Open REST API Documentation in Service Studio")

The resulting documentation is a standard swagger. You can see a [live example of a Contacts REST API here](https://expertsmobile.outsystems.com/ContactsAPI/rest/v1/).

![Screenshot of OutSystems REST API documentation interface with various HTTP method types for the Contacts API.](images/contacts-rest-swagger.png "Overview of REST API Documentation")

By expanding each of the endpoints, you'll be able to see details, like the request URL, parameters, examples, and responses:

![Detailed view of a PUT method in OutSystems REST API documentation showing request URL, parameters, and response structure.](images/contacts-rest-swagger-detail.png "Detailed REST API Documentation View")
