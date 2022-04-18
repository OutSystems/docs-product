---
tags: 
locale: en-us
guid: 6b99f36b-866b-47e6-858f-3b360413fcd7
app_type: traditional web apps, mobile apps, reactive web apps
---

# Consumed SOAP Web Services Constraints

Due to the OutSystems language expressiveness, when consuming SOAP Web Services there are scenarios that are only supported through extensions, using Integration Studio.

You need to implement extensions in the following scenarios:

* Web Services with SOAP Arrays (`SOAP-ENC:Array`);
* Web Services with custom simple types;
* Web Services with recursive data types (structures that contain themselves);
* Web Services using mixed content in `complexType` elements;
* Web Services that use `soap:body parts='parameters'` for method input/output definitions;
* Web Services with structured types not created with either "element", "simpleType", "complexType" or "attribute" XSD constructs;
* Web Services that use data types with [mapping limitations](<mapping-xml-to-outsystems.md#mapping-limitations>).

The data types declared in the WSDL which are not used in the web methods will not be imported.

In some cases, Service Studio will mention the exact SOAP feature that is not currently supported while checking the web service to be consumed. In these cases you may be able to manually adjust the WSDL to consume the web service in OutSystems.
