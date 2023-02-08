---
tags: support-Database
locale: en-us
guid: ee918919-4249-4a56-9ac3-a2ccedd30e54
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Database Data Types

The following table represents how OutSystems data types are mapped to the data types of the database being used.

OutSystems | SQL Server / SQL Azure | Oracle | Obs.  
---|---|---|---
Text | nvarchar(&lt;length&gt;) if the length is less than or equal to 2000, NVarchar(max) otherwise. | VARCHAR2(&lt;length&gt;), if the length is less than or equal to 2000, CLOB otherwise. |
Integer | int If an attribute with this type is set to auto number, the IDENTITY attribute is added. | NUMBER(10) If an attribute with this type is set to auto number, a sequence is added. |
Long Integer | bigint If an attribute with this type is set to auto number, the IDENTITY attribute is added. | NUMBER(20) If an attribute with this type is set to auto number, a sequence is added. |
Decimal | decimal() The precision and scale values, are the ones defined by the Length and Decimals properties of the attribute. | NUMBER() The precision and scale values, are the ones defined by the Length and Decimals properties of the attribute. | At runtime, when values are read from (or saved to) the database, the number of decimal digits depends on the stack of the application server. Consider the restrictions of System.Decimal.  
Boolean | bit | NUMBER(1) |
Date Time | datetime | TIMESTAMP |
Date | datetime | TIMESTAMP |
Time | datetime | TIMESTAMP |
Phone Number | varchar(20) | VARCHAR2(20) |
Email | varchar(250) | VARCHAR2(250) |
Binary Data | image | BLOB |
Currency | decimal(37,8) | NUMBER(37,8) |
Entity Identifier | Depends on the type of the Identifier. 
