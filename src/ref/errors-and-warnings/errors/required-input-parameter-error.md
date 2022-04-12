---
locale: en-us
guid: c0adb2a0-b45d-4ffe-b4c6-28a9f5c7484e
---

# Required Input Parameter Error

The `Required Input Parameter` error is issued in the following situation:

* `'<method name>' method requires an input parameter with '<data type>' data type and the Send In property set to 'Body'. Change or add an input parameter, or change the method's request format.`

    You are trying to change the 'Request Format' property of a REST API method, or 'Data Type', or 'Send In' properties of an input parameter in a REST API method.

    Follow the instructions in the error message to solve it.

* `'<method name>' method requires at least one input parameter with property Send In set to 'Body'. Change or add an input parameter, or change the method request format.`

    The REST API method has a request format that is expecting some information to be sent in the Body of the request and none of the input parameters is set to do so.

    Follow the instructions in the error message to solve it.

Double-click on the error line to take you directly to the REST API method's 'Request Format' property where the problem was detected. 
