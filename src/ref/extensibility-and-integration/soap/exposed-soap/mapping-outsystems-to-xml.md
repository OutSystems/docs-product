---
tags: support-application_development; support-Integrations_Extensions
---

# Mapping OutSystems Data Types to XML Data Types

When exposing SOAP Web Services in your module, OutSystems Data Types are mapped into the following XML Schema Data Types:

OutSystems Data Type | XML Data Type | Is an Input Parameter of this Type Mandatory?  
---|---|---  
Binary | base64Binary | No  
Boolean | boolean | Yes  
Currency | decimal | Yes  
Date | date | Yes  
Date Time | dateTime | Yes  
Decimal | decimal | Yes  
Entity Identifier | long | Yes  
Integer | long | Yes  
Long Integer | long | Yes  
Record of Entities/Structures | XSD complex data type which is a sequence of elements that represent the attributes of the Entity or Structure. | No  
Record List | XSD arrays | No  
Phone Number | string | No  
Text | string | No  
Time | time | Yes  
