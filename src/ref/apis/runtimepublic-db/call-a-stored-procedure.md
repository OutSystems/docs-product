---
tags: 
---

# Call a Stored Procedure

To call a stored procedure you have to use some .NET native objects that you can obtain by calling the [RuntimePublic.Db API](<intro.md>) methods. To obtain them, all query objects have a `GetDriver<ClassName>` method that returns the language native object.

When using .NET native objects, make sure that you comply with:

* The database engine's specific syntax
* The specific behaviors of the driver 

## Example

In this example, we have an external database accessed through a connection called 'Data Warehouse' that is defined in the environment management console.

We will call a store procedure called COMPUTE_SCORE, which calculates the score performance for an employee. To do it, it receives the employee's name and the output parameter, an integer number, and returns that parameter with the value correspondent to the performance for the employee.

### C# Code Sample
    
    
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
