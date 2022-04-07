---
summary: Use the RuntimePublic.Db API to insert data in the application database.
tags: 
locale: en-us
guid: 58b8df19-233a-40bb-ac4a-e5936cdcbd81
---

# Insert data in the application database

Use the [RuntimePublic.Db API](<intro.md>) to insert data in the application database following this pattern:

1. Retrieve a `DatabaseProvider` from the `DatabaseAccess` instance.
1. Use the provider to create a transaction.
1. Use the transaction to create a `Command`.
1. Use the `Command` to create command parameters.
1. Execute the `Command`.
1. Retrieve the `Command` results.

## Example

The following example shows how you can add a record to the `USEDITEM` table that's in the application database.

### C# code sample

```csharp
using OutSystems.RuntimePublic.Db;

// [...]

// Retrieve the DatabaseProvider for the current application
DatabaseProvider dbaProvider = DatabaseAccess.ForRunningApplication();

// We will use this later to handle query parameters and escape identifiers
SqlHelper sqlHelper = dbaProvider.SqlHelper;

// Here we use the database transaction that is used to handle the current HTTP request
// You can also use a separate transaction
using (RequestTransaction requestTransaction = dbaProvider.GetRequestTransaction()) {
    using (Command cmd = requestTransaction.CreateCommand(
        string.Format("INSERT INTO USEDITEM ({0}, age) VALUES ({1}, {2})",
            // DESC is a keyword in SQL Server you need to escape it before using it as an
            // identifier
            sqlHelper.EscapeIdentifier("DESC"),
            // Parameter names need to be prefixed so they can be properly replaced by
            // their respective values. Each engine has its own parameter prefix so you can
            // use this function to make your SQL database agnostic
            sqlHelper.PrefixParam("desc"), sqlHelper.PrefixParam("age")))) {

        cmd.CreateParameter(sqlHelper.PrefixParam("desc"), DbType.String, "Car");
        cmd.CreateParameter(sqlHelper.PrefixParam("age"), DbType.Int32, 3);
        cmd.ExecuteNonQuery();
    }
}
```
