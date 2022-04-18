---
tags:
summary: 
locale: en-us
guid: 6d74e154-6ca6-4b2b-9fb1-178d4dbff78d
app_type: traditional web apps, mobile apps, reactive web apps
---


# Avoid large session variables

Session variables are designed to store information across requests in an application. They typically keep small amounts of information that help customize the application’s behavior, serialized and stored as a binary in the database. The session is loaded each time a request is made, so storing large data structures or large amounts of information in the session can cause performance problems. 

Here is an example:

Imagine that we have a multi-page wizard that's collecting partial information in each page. The information will be stored when the wizard completes. We may think that storing this temporary information in the session is a good idea, but each time any request to a page is made, all partial information stored in the session will be loaded. This also happens if we make an AJAX request to retrieve something like a dynamic drop down list that doesn't use any session information.

## Impact

Having large session variables can increase contention on the database (instances competing for access) and CPU utilization. Each request requires the session retrieval from the database and deserialization. As the number of users gets bigger, the contention increases as well, because the processing required to serialize and deserialize the variables is higher.

## Best practices

Store large session variables in a specific database table. Use the session Id as the primary key for the data. This way the large pieces of data have to be loaded only for the requests which need it.
