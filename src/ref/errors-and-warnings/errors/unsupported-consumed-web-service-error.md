---
locale: en-us
guid: 03541b11-4b74-423c-8148-e3efaa1d8efd
---

# Unsupported Consumed Web Service Error

Service Studio provides extensive support for consuming SOAP Web Services. However, due to the OutSystems language expressiveness, there are scenarios that are only supported through the use of extensions. In these scenarios, when trying to consume a SOAP Web Service in Service Studio, an Unsupported Consumed Web Service error is issued.

The `Unsupported Consumed Web Service` error is displayed in the following situations:

* `Two or more structures named <name> found in WSDL`

    The SOAP Web Service you are consuming has two or more XSD sequences with the same name. When integrating this SOAP web service in your module, the XSD sequences are mapped in Structures and Service Studio does not allow you to have two structures with the same name.

* `The web service you are trying to import has the same name as one of its methods`

    The SOAP Web Service your are consuming has the same name as one of its methods. When integrating this SOAP web service in your module, the method is mapped in an Action and the web service client corresponds to the SOAP Web Service. Service Studio does not allow you to have a SOAP Web Service with the same name as one of its methods.

* `Structure '<structure name>' is recursive / Structure '<structure name>' has attributes with unsupported types`

    The SOAP Web Service you are consuming probably has an array of data types whose elements data type is the parent array type itself.  When integrating this SOAP web service in your module, an array data type is mapped into an Record List of Structures and structure attributes cannot be recursive. There are other situations with indirect loops that may cause this error.

* `Unsupported child of <element> in WSDL`

    The SOAP Web Service you are consuming using has a child element that is not supported by Service Studio.

* `Unsupported XSD extension found in WSDL`

    The SOAP Web Service you are consuming has an extension that is not supported by Service Studio.

* `Unsupported <type> data type definition in WSDL`

    The SOAP Web Service you are consuming has data types that are not supported by Service Studio.

* `Method '<method name>' uses unsupported types`

    The SOAP Web Service you are consuming has data types that are not supported by Service Studio.

To consume a SOAP Web Service in the scenarios presented above, use Integration Studio, either to Import Web Services from a .NET Assembly or implement a custom extension that can be then used in Service Studio.
