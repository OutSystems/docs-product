---
locale: en-us
guid: cd6419c6-8176-4cba-8788-49eee2196c4a
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Invalid Request Format Error

The `Invalid Request Format` error is issued in the following situations:

* `(<method name>) method has an invalid Request Format property. Either change it, or remove the input parameters from the method`
  
    You have an invalid value set in the 'Request Format' property of a REST API method, or you don't have any value set at all.

Double-click on the error line to take you directly to the REST API method's 'Request Format' property where the problem was detected.

* `(<method name>) method has an invalid Request Format property. Either change this property, modify the body input Data Type, or add a new body input.`

    The 'Request Format' property of a REST API method is set to multipart/form-data, but you are sending a single basic type. Follow the instructions in the error message to solve the error.
