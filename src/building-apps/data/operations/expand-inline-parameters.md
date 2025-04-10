---
tags: sql optimization, performance best practices, database queries, sql queries, security
summary: Explore best practices for avoiding expand inline parameters in OutSystems 11 (O11) to optimize SQL query performance.
guid: 83c88799-85d5-4ac8-a882-f72bb417bb5c
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - backend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - evaluate
---

# Avoid expand inline parameters for dynamic values

By using expand inline parameter, you can insert SQL content inside OutSystems SQL query. This parameter isn't a SQL parameter, in the sense that it isn't created in the database. It's calculated during runtime and textually expanded inside the SQL call. You should be mindful of the performance impact inline parameters can have when used with dynamic values.

<div class="warning" markdown="1">

OutSystems provides ways of implementing common use cases without enabling this property. Refer to the following for more information:

* [Best practices for building dynamic SQL statements](build-dynamic-sql-statements.md) to understand if you can change your implementation to avoid having the Expand Inline property enabled.
* [SQL Injection Warning](https://success.outsystems.com/Documentation/11/Reference/Errors_and_Warnings/Warnings/SQL_Injection_Warning) for guidance on how to resolve this warning the IDE shows when you set Expand Inline property as enabled.

</div>

Here are some examples of common use for expand inline parameters:

**Example 1**

Dynamic conditions. For example, if the user fills in a search keyword in the UI, then passes `“and {User}.[Name] like '%”+SearchKeyword+”%'”` in an expand inline parameter called SearchClause, otherwise simply passes an empty string in that parameter.  
  
Inside the SQL query definition you can use the inline parameter to textually expand that content:  
  
    SELECT {User}.[Name], {User}.[Phone]  
    FROM {User}  
    WHERE {User}.[IsActive]  
    @SearchClause  
    ORDER BY {User}.[Name]

**Example 2**

Dynamic set of values. For example, a record list transforms into a comma separated string of values, and then gets passed into the query, in a UserIds expanded inline parameter:  
  
    SELECT {User}.[Name], {User}.[Phone]  
    FROM {User}  
    WHERE {User}.[IsActive]  
    AND {User}.[Id] in { @UserIds }  
    ORDER BY {User}.[Name]

## Impact

Every time the platform runs the query in these two examples, it can pass a different text to the inline parameter. This generates a different query for the DB Engine. Inline parameters that change too often don't allow the database to optimize execution plans, since the engine keeps generating different queries. This has a significant impact on performance. A complex query with volumes of data that takes a couple of seconds at the first execution, executes in milliseconds for each next call after statistical optimization.

## Best practices

Here are some recommendations to avoid expand inline parameters:

* Avoid dynamic SQL to cope with optional filters - use fixed conditions covering the optionality instead.

    To fix the Example 1, instead of the inline parameter SearchClause, send the SearchKeyword as a normal parameter and transform the query as follows:  
  
        SELECT {User}.[Name], {User}.[Phone]  
        FROM {User}  
        WHERE {User}.[IsActive]  
        AND (@SearchKeyword = '' OR {User}.[Name] like '%'+@SearchKeyword+'%')  
        ORDER BY {User}.[Name]  
  
    With this fix the query is always the same for the DB engine. It's important to place the optionality condition first (`@SearchKeyword = ''`) to make sure that the real condition is never executed when there is no Search keyword. DB engines do a very good job optimizing this type of “dummy” conditions, so preparing the query for this optional filters is efficient.

* Use subqueries instead of injecting the result of a query as comma separated values to the next query.

    If UserIds in the Example 2 come from a complex query to select users with a certain logic, that query can be included in the same SQL query. It can even be used to avoid the IN condition that could degrade the performance. For example:  
  
        WITH UserIdTable (Id) as (SELECT ...)  
        SELECT {User}.[Name], {User}.[Phone]  
        FROM {User}  
        INNER JOIN UserIdTable on UserIdTable.ID = {User}.[ID]  
        WHERE {User}.[IsActive]  
        ORDER BY {User}.[Name]  
  
The DB Engine can now optimize this improved query.

* Use temporary tables when the comma separated list of values don’t come from a single query. Sometimes the list of values is the result of some complex logic (non-SQL processing) that keeps adding elements to the list. Instead of adding the elements to a comma separated list of values, add the values into a temporary table (you can google “Oracle temporary tables” or “SQL temporary tables” to find out how you can create a temporary table in a SQL query). Once you populate the temporary table, the Example 2 can be changed into:

        SELECT {User}.[Name], {User}.[Phone]  
        FROM {User}  
        INNER JOIN TemporaryTable on TemporaryTable.ID = {User}.[ID]  
        WHERE {User}.[IsActive]  
        ORDER BY {User}.[Name]
