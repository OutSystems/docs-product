---
summary: Learn how OutSystems 11 (O11) handles auto number attributes in databases, ensuring unique values with SQL Server and Oracle configurations.
tags: database configuration, entity modeling, auto number, sql server, oracle
locale: en-us
guid: 3a57d1cf-1b4f-4a9b-b1c3-29214eb15c14
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - backend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Auto Numbers on Database

<div class="warning" markdown="1">

OutSystems advises against using the AutoNumber property for Static Entity identifiers. Database-generated numbers aren't guaranteed to be the same across different environments (Development, QA, Production), which can lead to data inconsistency, broken foreign key relationships, and deployment failures.

</div>

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
