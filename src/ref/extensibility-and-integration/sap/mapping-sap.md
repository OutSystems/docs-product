---
tags: 
locale: en-us
guid: b494a3d0-48d5-4988-ac70-8e7df29cc0ce
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Mapping SAP Data Types to OutSystems Data Types

When integrating with a SAP System in your module, OutSystems maps the SAP Data Types into OutSystems Data Types as follows:

SAP Data Type | OutSystems Data Type | Comments  
---|---|---  
BCD | Decimal <br/>Text | Decimal, if the length of the field is less than 28 characters. <br/>Text otherwise.  
BYTE | Binary Data | 
CHAR | Text | 
CLASS | Structure | 
DATE | Date | 
DECF16 <br/>DECF34 <br/>FLOAT | Decimal | Values of these SAP data types can be outside of the boundaries of the Decimal data type. If the integer part is higher than the biggest Decimal value of OutSystems, you get a runtime error. <br/>If the fractional part is outside of OutSystems' Decimal boundaries, it will be rounded. <br/>If you need to work with values out the Decimal range of OutSystems, use Text data type.  
INT1 <br/>INT2 <br/>INT | Integer | 
NUM | Text | 
STRING | Text | 
STRUCTURE | Structure | 
TABLE | List | If a table is input and output parameter at the same time, OutSystems generates two separate parameters.  
TIME | Time | 
XSTRING | BinaryData | 
