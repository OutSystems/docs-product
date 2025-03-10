---
summary: Explore how to query data from an external database using the RuntimePublic.Db API in OutSystems 11 (O11).
tags: database integration, api usage, c# development, external databases, data retrieval
locale: en-us
guid: 21dbc0f4-e74a-47aa-91fb-c2acc5252916
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - backend developers
  - full stack developers
  - architects
outsystems-tools:
  - service center
coverage-type:
  - remember
---

# Query data from an external database

Use the RuntimePublic.Db API to query data from an external database following this pattern:

1. Retrieve a `DatabaseProvider` from the `DatabaseAccess` instance.
1. Use the provider to create a transaction.
1. Use the transaction to create a `Command`.
1. Use the `Command` to create command parameters.
1. Execute the `Command`.
1. Retrieve the `Command` results.

## Example

In the following example there's a connection called `Oracle DB Connection` accessing an external database. You define the connection in the environment management console (Service Center).

The code below gets the records of people with less than 20 years old from the `PERSON` table in an external Oracle database using the previously obtained connection.

### C# code sample

```csharp
using OutSystems.RuntimePublic.Db;

// [...]

// Retrieve the DatabaseProvider for the external database.
// You need to have a Database Connection called "Oracle DB Connection" configured
// in Service Center.
DatabaseProvider dbaProvider = DatabaseAccess.ForExternalDatabase("Oracle DB Connection");

// We will use a separate transaction to execute the query
// A committable transaction can be committed and rolled back explicitly 
using (CommittableTransaction commitableTransaction = dbaProvider.GetCommittableTransaction()) {
    using (Command cmd = commitableTransaction.CreateCommand("SELECT AGE FROM PERSON WHERE AGE < 20")) {
        // Results are read using a standard IDataReader object
        using (IDataReader reader = cmd.ExecuteReader()) {
            while (reader.Read()) {
                Console.WriteLine(reader.GetInt32(0));
            }
        }
    }
}
```
