---
summary: OutSystems 11 (O11) handles database transactions with automatic and explicit controls, supporting various isolation levels.
locale: en-us
guid: cb6c0a9e-1714-484f-90ed-74f2afa98f67
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: database transactions, error handling, data consistency, transaction management, isolation levels
audience:
  - full stack developers
  - backend developers
  - platform administrators
outsystems-tools:
  - service studio
coverage-type:
  - remember
topic:
  - data-isolation
---

# Handling transactions

While processing a web request, OutSystems begins a database transaction on its first access to the database. The transaction is committed before OutSystems sends the response to the user.

If an exception occurs and it's left uncaught, the transaction is rolled back. This means that changes made to the database within the transaction are all reverted, this way ensuring that your data remains consistent.

If an exception occurs and there's an Exception Handler that handles that exception, you can configure what happens to the currently open transaction in the Exception Handler's **Abort Transaction** property. Check [Aborting database transactions](../../lang/auto/class-exception-handler.md#aborting) for more information.

## Ending transactions explicitly

You can manage transactions explicitly through the CommitTransaction and AbortTransaction actions:

* **CommitTransaction**: Issues a database COMMIT statement that makes effective all changes done on the database since the beginning of the current transaction. It also ends the current transaction and starts a new one. After a CommitTransaction, the action flow continues.

* **AbortTransaction**: Issues a ROLLBACK statement that undoes all changes performed on the database since the beginning of the current transaction. It also ends the current transaction and starts a new one. After an AbortTransaction, the action flow continues. 

## Isolation levels

<div class="info" markdown="1">

The same isolation levels apply for transactions done in the Platform database and external databases. Check the [system requirements](../../../setup-infra-platform/setup/system-requirements.md) for the supported databases.

</div>

The following table shows the isolation level OutSystems uses in the different databases:

| | Read Uncommitted | Read Committed |
|---|:---:|:---:|
| SQL Server | X | |
| Azure SQL | X | |
| MySQL | X | |
| DB2 | | X |
| Oracle | | X |
| PostgreSQL | | X |
| Aurora PostgreSQL | | X |

  
When using SQL Server, Azure SQL, and MySQL databases you're working at **Read Uncommitted** isolation level. You have multiple transactions per web request: one for writes, one for each read.

When using a DB2, Oracle, PostgreSQL, and Aurora PostgreSQL database, you're working at **Read Committed** isolation level. All queries, inserts, updates, etc. happen in the same database transaction. The data is stored to the database only when the transaction is committed.  
This means that you're not able to read data that wasn't yet committed in a transaction. Because of this, before calling a Process instance or a method of a consumed Web Service, you need to commit the database transaction, to see up-to-date data in the process or method.

## Important remarks

There are some aspects concerning transactions that you should pay attention
to, namely:

* The transactions are always sequential, they cannot be nested.
* After committing or rolling back a transaction, all database locks eventually being held are released.
* When using Multiple Database Catalogs, or when integrating with external systems, OutSystems opens separate connections and transactions for each system, which are committed separately; there is no distributed transaction mechanism. In these cases, transaction handling might need some extra care.
