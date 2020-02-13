---
tags: 
---

# Database Compatibility Issues

Whenever the DBMS type is set to `(all)` in the [properties of the Module](<../../lang/auto/Class.Module.final.md>), it means that queries are expected to be compatible with all database servers supported by OutSystems.

If you are not concerned with compatibility issues, you can use SQL statements specific to your database server.

## Using the Dual Table

In Oracle databases the `FROM` clause must exist in any SELECT statement even if you're only calculating a scalar value.

In this situations developers use the `Dual` table in the `From` clause of the query. The `Dual` table is created automatically by the Oracle database with a single column named `Dummy`, with type Varchar2, and contains a single row with value "X".

To ensure the compatibility of your queries that use the `Dual` table, OutSystems creates a `Dual` table in all supported databases, with the same definition as Oracle databases.

For All DBMS  |  SQL Server  |  Oracle
---|---|---
SELECT 2 + 2 FROM Dual  |  SELECT 2 + 2  |  SELECT 2 + 2 FROM Dual
  
## Using the getdate() Function

SQL Server and MySQL make a function available for you that returns the current date and time based on the clock of the database server. To ensure compatibility with Oracle, OutSystems provides its own `getdate()`. Therefore, you can use this function in your queries, independently of the database type you are using.

The following table contains of how to use this function.

For All DBMS  |  SQL Server  |  Oracle
---|---|---
SELECT getdate() FROM Dual  |  SELECT getdate()  |  SELECT sysdate FROM Dual
  
The result of this query can be handled as a Date Time, so you can use [Format built-in functions](<../../lang/auto/builtinfunction.Format.final.md#FormatDateTime>) to format the result.

## Using Empty Strings in Query Conditions

When performing text comparisons in the database, you should be aware that due to the way Oracle DBMS represents empty strings, if you want to fetch records that have an empty text row, you should use a single space between the quotes.

The following table contains an example in how to design the query with an empty string for the supported databases.

For All DBMS  |  SQL Server  |  Oracle  |  MySQL  
---|---|---|---  
SELECT {User}.* %%FROM {User} %%WHERE {User}.Username = '&lt;single space&gt;'  |  SELECT {User}.* %%FROM {User} %%WHERE {User}.Username = ''  |  SELECT {User}.* %%FROM {User} %%WHERE {User}.Username = '&lt;single space&gt;'  |  SELECT {User}.* %%FROM {User} %%WHERE {User}.Username = ''  
  
Note that foreign keys for text attributes are stored with a text value if a reference exists, or NULL if there is no reference to a row in another entity.

## Handling Processes and Web Services

When using an Oracle or DB2 database, you are working at Read Committed isolation level, meaning that you are not able to read data that was not committed yet in a transaction. Because of this, if you call a Process instance or a method of a consumed Web Service, the changes made to entity records will only be available in the Process or Method if you commit the database transaction before the call. Learn more about [Handling Transactions](<handling-transactions.md>).

## Case and Accent Insensitive Searches in Large Text Objects

Oracle's native case and accent insensitive queries feature does not work with large text objects (LOB). For further information read the section 'Restrictions for LOB Operations' in Oracle's web page [Working with LOBs](<http://download.oracle.com/docs/cd/B28359_01/appdev.111/b28393/adlob_working.htm#i1006278>).

## Equality Operator with Text Length Above 2000 Characters

A Text type variable that has more than 2000 characters is implemented as a CLOB in Oracle. This database system doesn't allow you to use the '=' operator to compare CLOB values. Replace it with the 'like' operator in your Aggregates and Advanced queries.

To prevent having to replace all your queries when this situation occurs, you can use the 'like' operator whenever you're working with text.
