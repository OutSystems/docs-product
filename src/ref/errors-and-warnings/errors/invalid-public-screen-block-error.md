---
locale: en-us
guid: aae1e0e4-4838-4c23-9387-a7dda68cbb4f
---

# Invalid Public Screen Block Error

The `Invalid Public Screen Block` error is issued in the following situations:

* `Public Screen Block <screen block> contains a parameter of record type <type> that is not declared as public`
  
    You have a Record parameter in the public screen block and its definition contains Entities/Structures that are not public.

    You must set as public the Entity/Structure that define the Record parameter.

* `Public Screen Block <screen block> contains a parameter of record type <type> that is a reference`
  
    You have a Record parameter in the public screen block and its definition contains Entities/Structures that are module references. You can only expose elements that have elements defined in the current module.

    You must edit the public screen block, select the input parameter, and use Entities/Structures defined in the module.

* `Arguments of '<type>' data type are not allowed in links from Public Screen Blocks`
  
    You have a public screen block containing a link (screen reference, Link, or Button widget) with a Destination property using input parameters of either the Binary Data, Record, or List data type.

    Depending on your requirements, do one of the following: 
    
    * Edit the link and, if the input parameter is optional, do not map the respective Destination argument.
    * Do not expose the screen block.
    * Change the Destination input parameter data type.

Double-click on the error line to take you directly to the screen block reference offending property.
