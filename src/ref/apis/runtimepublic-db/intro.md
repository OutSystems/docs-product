---
summary: Provides functionality to allow you to integrate with your external databases.
tags: article-page; support-application_development; support-Database; support-Integrations_Extensions
---

# RuntimePublic.Db API

The RuntimePublic.Db API provides functionality to allow you to integrate with your external databases.

With this API you enable your extension modules to call the databases configured in the environment management console. It's, by default, imported to your extension project when you create it in Integration Studio. To use this API you only need to reference its classes in your extension's project.

Any table names referenced in SQL statements must be **physical** table names, since this API works at the database level.

This API is available under the `OutSystems.RuntimePublic.Db` .NET namespace.

## Classes

Name | Description
---|---
[Command](#command) | Represents a command to execute queries.
[CommittableTransaction](#committabletransaction) | Represents a transaction that needs to be explicitly managed using commit and roll back operations. Use it for selecting, inserting, updating, and deleting data.
[Connection](#connection) | Represents a connection to a database.
[DatabaseAccess](#databaseaccess) | Creates DatabaseProvider instances to access a database.
[DatabaseProvider](#databaseprovider) | Provides access to a specific database.
[DataParameter](#dataparameter) | Represents the query parameters associated with a command.
[RequestTransaction](#requesttransaction) | Represents the transaction that's automatically managed by the platform. The transaction starts at the beginning of the web request, and the platform commits this transaction when it sends the response to the client. Use it for selecting, inserting, updating, and deleting data.
[SqlHelper](#sqlhelper) | Functions to assist on the manipulation of SQL statements members.
  
## Using the API

* [Call a stored procedure](<call-a-stored-procedure.md>)
* [Insert data in the application database](<insert-data-in-the-application-database.md>)
* [Query data from an external database](<query-data-from-an-external-database.md>)

## API reference

### Command

Represents a command to execute queries.

#### Methods

Name | Description
---|---
[DataParameter](#dataparameter) CreateParameter(string name, DbType type, object value)  | Adds a parameter to the command with a given type and value. The parameter value is modified to a compatible database value.
[DataParameter](#dataparameter) CreateParameter(string name) | Adds a parameter to the command. The parameter value is modified to a compatible database value.
void Dispose() | Frees the resources used by this object.
int ExecuteNonQuery() | Executes the command and returns the number of rows affected.
IDataReader ExecuteReader() | Executes the command text returning the resulting System.Data.IDataReader.
object ExecuteScalar() | Executes the query, and returns the first column of the first row in the resultset returned by the query. Extra columns or rows are ignored.
[Connection](#connection) GetConnection() | Returns the database connection associated to this command.
IDbCommand GetDriverCommand() | Returns the native command object used by the stack in which the application is running.
[DataParameter](#dataparameter) GetParameter(string columnName) | Gets the parameter with the specified name.
  
#### Members

Name | Description  
---|---  
string CommandText | Gets or sets the SQL statements to execute.  
int CommandTimeout | Gets or sets the command execution timeout (in seconds).  
  
### CommittableTransaction

Represents a transaction that needs to be explicitly managed using commit and roll back operations. Use it for selecting, inserting, updating, and deleting data.

#### Methods

Name | Description
---|---
void Close() | Rolls back a transaction from a pending state and closes the transaction.
void Commit() | Commits the transaction.
[Command](#command) CreateCommand(string sql) | Creates a command that you can execute in this transaction.
[Command](#command) CreateCommand() | Creates an empty command that you can execute in this transaction.
void Dispose() | Releases the transaction and frees the resources used by this object.
[Connection](#connection) GetConnection() | Gets the database connection associated with this transaction.
IDbTransaction GetDriverTransaction() | Returns the native transaction object used by the stack in which the application is running. It allows to reuse existing code that receives a native transaction object as parameter.
void Rollback() | Rolls back a transaction from a pending state.
  
### Connection

Represents a connection to a database.

#### Methods

Name | Description
---|---
[CommittableTransaction](#committabletransaction) BeginReadUncommittedTransaction() | Creates an [OutSystems.RuntimePublic.Db.CommittableTransaction](#committabletransaction) with the transaction isolation level set to read uncommitted.<br/>**Warning: This method has been deprecated.**
[CommittableTransaction](#committabletransaction) BeginTransaction() | Creates an [OutSystems.RuntimePublic.Db.CommittableTransaction](#committabletransaction) with the transaction isolation level set to read committed.<br/>**Warning: This method has been deprecated.**
void Close() | Closes the connection to the database.
[Command](#command) CreateCommand(string sql) | Creates a command that doesn't have an associated transaction.
[Command](#command) CreateCommand() | Creates an empty command that doesn't have an associated transaction.
void Dispose() | Closes the connection and frees the resources used by this object.
IDbConnection GetDriverConnection() | Returns the native connection object used by the stack in which the application is running. It allows to reuse existing code that receives a native connection object as parameter.
bool IsClosed() | Checks if the connection is closed.

### DatabaseAccess

Creates DatabaseProvider instances to access a database.

#### Methods

Name | Description
---|---
[DatabaseProvider](#databaseprovider) ForDatabase(string databaseName) | Returns a database provider for a given database catalog or schema. Use it to access data managed by applications that are configured to use this database.
[DatabaseProvider](#databaseprovider) ForExternalDatabase(string connectionName) | Returns a database provider for a specific external database connection. Use it to access data managed by external systems.
[DatabaseProvider](#databaseprovider) ForRunningApplication() | Returns a database provider to access the database of the currently running application. Use it to access data managed by the currently running application, or other applications sharing the same database.
[DatabaseProvider](#databaseprovider) ForSystemDatabase() | Returns a database provider to access the system database. Use it to query the platform metamodel.

### DatabaseProvider

Provides access to a specific database.

#### Methods

Name | Description
---|---
[CommittableTransaction](#committabletransaction) GetCommitableTransaction() | Returns a new transaction that needs to be managed explicitly using a commit or roll back.
[RequestTransaction](#requesttransaction) GetRequestTransaction() | Returns the transaction that starts at the beginning of the web request and is committed when the response is sent to the client. This transaction can't be committed or rolled back inside extensions.

#### Members

Name | Description
---|---
[SqlHelper](#sqlhelper) SqlHelper | Returns a [SqlHelper](#sqlhelper) instance targeted at the manipulation of SQL statements members.
int CommandTimeout | Gets or sets the command execution timeout.

### DataParameter

Represents the query parameters associated with a command.

#### Methods

Name | Description
---|---
IDbDataParameter <br/>GetDriverParameter() | Returns the native parameter object used by the stack in which the application is running.

#### Members

Name | Description
---|---
DbType DbType | Gets or sets the database type.
int Size | Sets the size of the parameter.
object Value | Gets or sets the parameter value.
  
### RequestTransaction

Represents the transaction that's automatically managed by the platform. The transaction starts at the beginning of the web request, and the platform commits this transaction when it sends the response to the client. Use it for selecting, inserting, updating, and deleting data.

#### Methods

Name | Description
---|---
[Command](#command) CreateCommand(string sql) | Creates a command that you can execute in this transaction.
[Command](#command) CreateCommand() | Creates an empty command that you can execute in this transaction.
void Dispose() | Releases the transaction and frees the resources used by this object.
[Connection](#connection) GetConnection() | Gets the database connection associated with this transaction.
IDbTransaction GetDriverTransaction() | Returns the native transaction object used by the stack in which the application is running. It allows to reuse existing code that receives a native data object as parameter.
void Release() | Checks if the transaction exists, and frees the resources associated with it. Since this transaction is automatically managed by the platform, when releasing the transaction the plaform performs no commit or rollback operations.
  
### SqlHelper

Functions to assist in the manipulation of SQL statements members.

#### Methods

Name | Description  
---|---  
string EscapeIdentifier(string identifier) | Escapes an identifier so you can use it in a query.  
string PrefixParam(string paramName) | Prefixes a parameter name used as a placeholder in a query or as the "de facto" parameter name when creating command parameters.  
