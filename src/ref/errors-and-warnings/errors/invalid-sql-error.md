---
locale: en-us
guid: 87c242a3-2d64-4c38-b1d9-95b761d7290f
app_type: traditional web apps, mobile apps, reactive web apps
---

# Invalid SQL Error

The `Invalid SQL` error is issued in the following situations:

* `<entity> is an unknown entity in <SQL>`

    You have a SQL query that is using an entity that no longer exists.

    Fix the SQL associated with this query to use an existing entity.

* `<attribute> is an unknown attribute of <entity> at <query>`

    You have a SQL query in your application that is using an attribute that no longer exists.

    Fix the SQL associated with this query to use an existing attribute of the entity.

<div class="info" markdown="1">

To learn more about SQL in OutSystems, check out the following free courses:

* [SQL Queries](https://www.outsystems.com/training/courses/146/sql-queries/). Write your SQL queries to interact with data in OutSystems.
* [Getting Started with OutSystems for SQL Developers](https://www.outsystems.com/training/courses/169/getting-started-with-outsystems-for-sql-developers/). Learn how to create a data model, fetch data, and how to use an existing external database in an OutSystems app.


</div>

* `Unknown <parameter> parameter in <query>`

    You have an SQL query in our application that is using a parameter that no longer exists.

    Do one of the following: 
    
    * Fix the SQL associated with this query, in order to use an existing parameter.
    * Change the input parameters of the query.

* `Parameters with no separating spaces found in <query>`

    The SQL query is using parameters not separated by spaces. For example: `SELECT @Parameter1@Parameter2`.

    Fix the SQL associated with this query, in order to have spaces separating your input parameters.

* `<text> is a reserved prefix in <query>`
  
    You are using system tables in your SQL query and this is not allowed for security reasons. System tables are start with the following prefixes: `osusr_`, `ossys_`, and `oslog_`. If your query uses any of these prefixes in a condition, for example, this error is displayed.

    Fix the SQL associated with this query, in order to remove the references to any of the above system tables.

* `Output structure must be set in <SQL>`

    You haven't defined the output structure to store the result of the query.

    Edit the query and set its output structure.

* `Output structure cannot contain structures with nested Records/List`

    The SQL query has a output structure with a definition containing nested records or lists.

    You have to fix the query output structure by doing one of the following: 
    
    * Use a different structure with no nested elements.
    * Redefine this structure in order to avoid nested Records or Lists.

* `Parameters with 'Expand Inline' set to 'Yes' must be of 'Text' data type`

    You have a query that is using inline parameters but their data type is not Text.

    Edit the input parameters of this query and do one of the following: 
    
    * Set the Expand Inline property of the input parameter.
    * Change the data type of this input parameter to Text.

* `In the query '<SQL>' the Foreign Entities are located in different databases: '<Foreign Entity 1>', '<Foreign Entity 2>',… in '<Database Connection A>'; '<Foreign Entity 3>', '<Foreign Entity 4>',…  in '<Database Connection B>'; ...`

    You are using Foreign Entities in the query that are located in different databases. Each SQL query can only use Foreign Entities located in the same database.

    Edit the query and put each group of Foreign Entities in its separate query — the groups are detailed in the error message to help you. If you have joins between Foreign Entities that have to be separated, join manually the result sets.

* `Cannot use the query count output parameter. The SQL query '<SQL query>' must be a SELECT statement`

    You are using the Count output parameter of an SQL query that cannot return a query count result because the query is not a SELECT statement.

    Review the logic of your application so that the query you are using is a SELECT statement and thus, have the query count filled with the number of records.

Double-click on the error line to take you directly to the parent action flow and highlights the SQL query.
