---
tags: support-application_development; support-Integrations_Extensions
---

# Mapping XML Data Types to OutSystems Data Types

When consuming SOAP Web Services in your module, OutSystems maps the XML Data Types into OutSystems Data Types as follows:

XML Data Types  |  OutSystems Data Types  
---|---  
anySimpleType %%anyAtomicType %%anyType %%anyURI  |  Text %%Text %%Text %%Text  
bool %%boolean %%base64Binary %%byte %%bytev  |  Boolean %%Boolean %%Binary %%Integer %%Integer 
char  |  Integer  
choice  |  Static Entity + Structure (check Notes)  
date %%dateTime %%dateTimeStamp %%decimal %%double %%duration %%dayTimeDuration %%yearMonthDuration  |  Date %%Date Time %%Date Time %%Text %%Text %%Text %%Text %%Text
ENTITY %%ENTITIES %%enum  |  Text %%Text %%Static Entity (check Notes)
float  |  Text  
gDay %%gMonth %%gMonthDay %%gYearMonth %%gYear  |  Text %%Text %%Text %%Text %%Text  
hexBinary  |  Binary  
ID %%IDREF %%IDREFS %%int %%integer  |  Text %%Text %%Text %%Integer %%Text  
language %%long  |  Text %%Long Integer  
Microsoft Datasets  |  Text  
Name %%NCName %%negativeInteger %%NMTOKEN %%NMTOKENS %%nonNegativeInteger %%nonPositiveInteger %%normalizedString %%NOTATION  |  Text %%Text %%Text %%Text %%Text %%Text %%Text %%Text %%Text  
Object  |  Text  
positiveInteger  |  Text  
QName  |  Text  
short %%signed byte %%string  |  Integer %%Integer %%Text  
time %%token  |  Time %%Text  
unsignedByte %%unsignedInt %%unsignedLong %%unsignedShort  |  Integer %%Long Integer %%Decimal %%Integer  
XML Element  |  Text  
XSD Arrays  |  List %%In OutSystems, a List is a sequence of elements of any data type. Therefore, an XSD array is mapped into a list of records which elements are a structure that represents those elements in the XSD array. If you have an XSD array of integers, the mapping in Service Studio is a List of structures with one attribute of type Integer.  
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
