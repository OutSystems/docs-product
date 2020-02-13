---
summary: Use the RuntimePublic API to query data from an external database.
tags: 
---

# Query Data from an External Database

Use the RuntimePublic API to query data from an external database following this pattern:

1. Retrieve a `DatabaseProvider` from the `DatabaseAccess` instance.
1. Use the provider to create a transaction.
1. Use the transaction to create a `Command`.
1. Use the `Command` to create command parameters.
1. Execute the `Command`.
1. Retrieve the `Command` results. 

## Example

In this example, we have an external database accessed through a connection called 'Oracle DB Connection' that is defined in the environment management console.

We get records of people with less than 20 years old from the PERSON table in an external Oracle database.

### C# Code Sample
       
```csharp
using OutSystems.RuntimePublic.Db;

// [...]

// Retrieve the DatabaseProvider for the external database.
// You need to have a Database Connection called “Oracle DB Connection” configured
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
