---
tags: 
---

# Auto Numbers on Database

When modeling Entities to store data on the database, you can make Integer attributes auto numbers to ensure they have unique values for each record.

This page explains what happens on the database when setting an attribute's IsAutoNumber property to `Yes`.

## SQL Server

When creating a sequential attribute with a SQL Server database, a column with Int  data type, and with Identity (1,1)  is created. This ensures the value starts at 1, and is incremented by 1, each time a new record is inserted.
   
```sql    
CREATE TABLE Product (
    Id INT IDENTITY(1,1),
    Name VARCHAR(50)
);
```  

## Oracle

In Oracle, a sequential attribute is mapped to the following Oracle objects:

1. A sequence, prefixed with `OSSEQ`, is created to guarantee the uniqueness of the corresponding column. This sequence starts at 1 and has an increment of 1.
2. A trigger, prefixed with `OSTRG`, is created in order to calculate the next value of the sequence. This trigger is invoked before inserting new records. 
