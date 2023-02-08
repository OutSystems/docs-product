---
tags: support-application_development; support-Integrations_Extensions
locale: en-us
guid: ac774bf3-82fc-480e-a633-7652e559d52a
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Mapping XML Data Types to OutSystems Data Types

When consuming SOAP Web Services in your module, OutSystems maps the XML Data Types into OutSystems Data Types as follows:

XML Data Types  |  OutSystems Data Types  
---|---  
anySimpleType <br/>anyAtomicType <br/>anyType <br/>anyURI  |  Text <br/>Text <br/>Text <br/>Text  
bool <br/>boolean <br/>base64Binary <br/>byte <br/>bytev  |  Boolean <br/>Boolean <br/>Binary <br/>Integer <br/>Integer 
char  |  Integer  
choice  |  Static Entity + Structure (check Notes)  
date <br/>dateTime <br/>dateTimeStamp <br/>decimal <br/>double <br/>duration <br/>dayTimeDuration <br/>yearMonthDuration  |  Date <br/>Date Time <br/>Date Time <br/>Text <br/>Text <br/>Text <br/>Text <br/>Text
ENTITY <br/>ENTITIES <br/>enum  |  Text <br/>Text <br/>Static Entity (check Notes)
float  |  Text  
gDay <br/>gMonth <br/>gMonthDay <br/>gYearMonth <br/>gYear  |  Text <br/>Text <br/>Text <br/>Text <br/>Text  
hexBinary  |  Binary  
ID <br/>IDREF <br/>IDREFS <br/>int <br/>integer  |  Text <br/>Text <br/>Text <br/>Integer <br/>Text  
language <br/>long  |  Text <br/>Long Integer  
Microsoft Datasets  |  Text  
Name <br/>NCName <br/>negativeInteger <br/>NMTOKEN <br/>NMTOKENS <br/>nonNegativeInteger <br/>nonPositiveInteger <br/>normalizedString <br/>NOTATION  |  Text <br/>Text <br/>Text <br/>Text <br/>Text <br/>Text <br/>Text <br/>Text <br/>Text  
Object  |  Text  
positiveInteger  |  Text  
QName  |  Text  
short <br/>signed byte <br/>string  |  Integer <br/>Integer <br/>Text  
time <br/>token  |  Time <br/>Text  
unsignedByte <br/>unsignedInt <br/>unsignedLong <br/>unsignedShort  |  Integer <br/>Long Integer <br/>Decimal <br/>Integer  
XML Element  |  Text  
XSD Arrays  |  List <br/>In OutSystems, a List is a sequence of elements of any data type. Therefore, an XSD array is mapped into a list of records which elements are a structure that represents those elements in the XSD array. If you have an XSD array of integers, the mapping in Service Studio is a List of structures with one attribute of type Integer.  
XSD Complex data types  |  Record  
(Other types)  |  Text  

## Notes

Enumerations
:   Enumerations will be created as OutSystems read-only static entities with a name like  `Enum_<TypeName>`.  Attributes of elements that are `enum`'s will have its data type set to Enum Static Entity Identifier.

Choices
:   Choices will also be created as read-only static entities but with a name like `Choice_<ElementName>`. 
Along with this static entity, OutSystems will also create a structure to represent the `choice` element itself. This structure will have the following attributes:

* Choice, the Id of the static entity `Choice_<ElementName>`;

* An attribute for each choice option of the respective type.

![SOAP choice structure](<images/soap-choice-structure-ss.png>)

To set the value of a WSDL element of type choice, set the Choice attribute to the Id of the desired choice, and fill in the corresponding structure attribute according to the "Choice" value.


## Mapping Limitations

* Types created via "restriction" over another type are usually the same as the original type. Only the `maxLength` and `fractionDigits` restrictions are considered when creating the appropriate data types, but these restrictions are not enforced at runtime.
* Type `element` having subtype `schema` (i.e. dynamic schemas) is interpreted as a simple Text item.
* Type `simpleType` having subtype that is not "restriction" (such as `list`, a space-separated sequence of text atoms) is interpreted as a simple Text item.
* Type `complexType` having subtype that is not `sequence`, `all` or `complexContent` is interpreted as a simple Text item.
* Subtype `complexContent` that is not "restriction" or "extension" is interpreted as a simple Text item.
* SOAP Web Service annotations are ignored. 

Also check the list of consumed [SOAP Web Services Constraints](<consumed-soap-constraints.md>).
