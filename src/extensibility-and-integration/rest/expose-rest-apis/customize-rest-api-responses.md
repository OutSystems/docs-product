---
summary: Customize the information sent in responses when exposing a REST API.
tags: 
---

# Customize REST API Responses

<div class="info" markdown="1">

We’ve been working on this article. Please let us know how useful this new version is by voting.

</div>

OutSystems allows you to customize the information sent in responses when exposing a REST API.

For that, do the following:

1. In the **Logic** tab, open the **Integrations** folder. 

1. In the exposed REST API, set the property On Response to `New OnResponse`. 

    ![REST API in Service Studio](images/ss-rest-expose-onresponse.png)

1. Open the "OnResponse" callback action that is now available under the REST API.

1. Design the logic to customize the information of the response. 

    ![Input and output parameters of OnResponse callback](images/ss-rest-expose-onresponse-tree.png)

    You can get the text of the response by accessing the "ResponseText" attribute of the "Response" input parameter or its binary contents by accessing the "ResponseBinary" attribute.

    Make sure to set the "CustomizedResponse" output to the request after your preprocessing.

Once defined and configured in the REST API, the "OnResponse" callback will be executed for **all methods** exposed by the REST API.
