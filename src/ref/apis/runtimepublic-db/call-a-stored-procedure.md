---
summary: Use the RuntimePublic.Db API to call a stored procedure.
tags: 
---

# Call a stored procedure

To call a stored procedure you have to use some .NET native objects that you can obtain by calling the [RuntimePublic.Db API](<intro.md>) methods. To obtain them, all query objects have a `GetDriver<ClassName>` method that returns the language native object.

When using .NET native objects, make sure that you comply with:

* The database engine's specific syntax
* The specific behaviors of the driver

## Example

In this example, there's an external database accessed through a connection called 'Data Warehouse' defined in the environment management console.

The code below invokes a store procedure called `COMPUTE_SCORE`, which calculates the performance score for an employee. The input parameter is the employee's name and the `score` output parameter, an integer number, corresponds to the calculated employee performance score. The stored procedure calculates the score and returns it in the output parameter.

### C# code sample

```csharp
using OutSystems.RuntimePublic.Db;

// [...]

// Get a reference (dbaProvider) to the external database "Data Warehouse"
DatabaseProvider dbaProvider = DatabaseAccess.ForExternalDatabase("Data Warehouse");

SqlHelper sqlHelper = dbaProvider.SqlHelper;

using (RequestTransaction trans = dbaProvider.GetRequestTransaction()) {
    using (Command cmd = trans.CreateCommand("COMPUTE_SCORE")) {
        // There is no API to set the command type so you need to access the
        // underlining ADO.NET objects
        cmd.GetDriverCommand().CommandType = CommandType.StoredProcedure;

        // Set the employee (input) and performanceScore (output) parameters
        cmd.CreateParameter("employee", DbType.String, "John Baker");
        var performanceScore = cmd.CreateParameter("score", DbType.Int32, DBNull.Value);

        // Set parameter direction on ADO.NET Data Parameter
        // The driver will fill the output parameter with a value after the query executes
        performanceScore.GetDriverParameter().Direction = ParameterDirection.Output;

        // Call the store procedure
        cmd.ExecuteNonQuery();

        // Print the store procedure's output
        Console.WriteLine(performanceScore.Value);
    }
}
```
