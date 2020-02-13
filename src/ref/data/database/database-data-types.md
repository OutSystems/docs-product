---
tags: support-Database
---

# Database Data Types

The following table represents how OutSystems data types are mapped to the data types of the database being used.

OutSystems  |  SQL Server / SQL Azure  |  Oracle  |  MySQL  |  Obs.  
---|---|---|---|---  
Text | nvarchar(&lt;length&gt;) if the length is less than or equal to 2000, NVarchar(max) otherwise. | VARCHAR2(&lt;length&gt;), if the length is less than or equal to 2000, CLOB otherwise. | VARCHAR(&lt;length&gt;), if the length is less than or equal to 2000, LONGTEXT otherwise. |  |
Integer | int If an attribute with this type is set to auto number, the IDENTITY attribute is added. | NUMBER(10) If an attribute with this type is set to auto number, a sequence is added. | INT(11) If an attribute with this type is set to auto number, the AUTO_INCREMENT attribute is added. |  |
Long Integer | bigint If an attribute with this type is set to auto number, the IDENTITY attribute is added. | NUMBER(20) If an attribute with this type is set to auto number, a sequence is added. | BIGINT(20) If an attribute with this type is set to auto number, the AUTO_INCREMENT attribute is added. |  |
Decimal | decimal() The precision and scale values, are the ones defined by the Length and Decimals properties of the attribute. | NUMBER() The precision and scale values, are the ones defined by the Length and Decimals properties of the attribute. | DECIMAL() The precision and scale values, are the ones defined by the Length and Decimals properties of the attribute. | At runtime, when values are read from (or saved to) the database, the number of decimal digits depends on the stack of the application server. Consider the restrictions of the System.Decimal in .NET, and those of the java.math.BigDecimal in Java.  
Boolean | bit | NUMBER(1) | TINYINT(1) |  |
Date Time | datetime | TIMESTAMP | DATETIME() |  |
Date | datetime | TIMESTAMP | DATETIME() |  |
Time | datetime | TIMESTAMP | DATETIME() |  |
Phone Number | varchar(20) | VARCHAR2(20) | VARCHAR(20) |  |
Email | varchar(250) | VARCHAR2(250) | VARCHAR(250) |  |
Binary Data | image | BLOB | BLOB |  |
Currency | decimal(37,8) | NUMBER(37,8) | DECIMAL(37,8) | 
Entity Identifier | Depends on the type of the Identifier.  
