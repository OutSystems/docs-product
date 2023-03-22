---
tags: support-Database
locale: en-us
guid: cb6c0a9e-1714-484f-90ed-74f2afa98f67
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Handling Transactions

While processing a web request, OutSystems begins a database transaction on its first access to the database. The transaction is committed before OutSystems sends the response to the user.

If an exception occurs and it's left uncaught, the transaction is rolled back. This means that changes made to the database within the transaction are all reverted, this way ensuring that your data remains consistent.

If an exception occurs and there's an Exception Handler that handles that exception, you can configure what happens to the currently open transaction in the Exception Handler's **Abort Transaction** property. Check [Aborting database transactions](<../../lang/auto/class.exception.handler.md#aborting>) for more information.

## Ending Transactions Explicitly

You can manage transactions explicitly through the CommitTransaction and AbortTransaction actions:

* **CommitTransaction**: Issues a database COMMIT statement that makes effective all changes done on the database since the beginning of the current transaction. It also ends the current transaction and starts a new one. After a CommitTransaction, the action flow continues.

* **AbortTransaction**: Issues a ROLLBACK statement that undoes all changes performed on the database since the beginning of the current transaction. It also ends the current transaction and starts a new one. After an AbortTransaction, the action flow continues. 

## Isolation Levels

The following table shows the isolation level OutSystems uses in the different databases:

DB2  |  MySQL  |  Oracle  |  SQL Server  | PostgreSQL
---|---|---|---|---  
Read Committed  |  Read Uncommitted  |  Read Committed  | Read Uncommitted  |  Read Commited
  
When using a MySQL or SQL Server database, you are working at **Read Uncommitted** isolation level. You have multiple transactions per web request: one for writes, one for each read.

When using a DB2, PostgreSQL or Oracle database, you are working at **Read Committed** isolation level. All queries, inserts, updates, etc. happen in the same database transaction. The data is stored to the database only when the transaction is committed.  
This means that you are not able to read data that was not yet committed in a transaction. Because of this, before you call a Process instance or a method of a consumed Web Service, you need to commit the database transaction, to see up-to-date data in the process or method.

## Important Remarks

There are some aspects concerning transactions that you should pay attention
to, namely:

* The transactions are always sequential, they cannot be nested.
* After committing or rolling back a transaction, all database locks eventually being held are released.
* When using Multiple Database Catalogs, or when integrating with external systems, OutSystems opens separate connections and transactions for each system, which are committed separately; there is no distributed transaction mechanism. In these cases, transaction handling might need some extra care.
