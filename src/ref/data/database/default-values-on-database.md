---
tags: support-Database
locale: en-us
guid: cbbcab1c-2534-43e7-b734-9fef31683b88
app_type: traditional web apps, mobile apps, reactive web apps
---

# Default Values on Database

The following table represents the default values of the OutSystems data types, and the respective values stored in the database.
If an [Entity Attribute](<../../lang/auto/Class.Entity%20Attribute.final.md>) does not have a default value defined, the following default values will be used:

Data Type  |  OutSystems  |  SQL Server  |  Oracle  |  MySQL  
---|---|---|---|---  
 Text | "" (empty string) | "" (empty string) | " " (single space) | "" (empty string)  
Integer | 0 | 0 | 0 | 0  
Long Integer | 0 | 0 | 0 | 0  
Decimal | 0 | 0 | 0 | 0  
Boolean | False | 0 | 0 | 0  
Date Time | 1900-01-01 00:00:00 | 1900-01-01 00:00:00 | 1900-01-01 00:00:00 | 1900-01-01 00:00:00  
Date | 1900-01-01 | 1900-01-01 00:00:00 | 1900-01-01 00:00:00 | 1900-01-01 00:00:00  
Time | 00:00:00 | 1900-01-01 00:00:00 | 1900-01-01 00:00:00 | 1900-01-01 00:00:00  
Phone Number | "" (empty string) | "" (empty string) | " " (single space) | "" (empty string)  
Email | "" (empty string) | "" (empty string) | " " (single space) | "" (empty string)  
Binary Data | Byte array with no elements | Byte array with no elements | Byte array with no elements | Byte array with no elements  
Currency | 0 | 0 | 0 | 0  
Entity Identifier | "" or 0 | Null | Null | Null  
