---
tags: database
summary: 
en_title: Don't abuse expand inline parameters
---


# Don't abuse expand inline parameters

It's possible to insert SQL content inside OutSystems SQL query - through an expand inline parameter. This parameter it's not a SQL parameter, in the sense that it isn't created in the database. It's calculated during runtime and textually expanded inside the SQL call.

Here are some examples of common use for expand inline parameters:

**Example 1**

Dynamic conditions - for example, if the user fills in a search keyword in the UI, then passes  
`“and {User}.[Name] like '%”+SearchKeyword+”%'”` in an expand inline parameter called SearchClause, otherwise simply passes an empty string in that parameter.  
  
Inside the SQL query definition you can use the inline parameter to textually expand that content:  
  
    SELECT {User}.[Name], {User}.[Phone]  
    FROM {User}  
    WHERE {User}.[IsActive]  
    @SearchClause  
    ORDER BY {User}.[Name]

**Example 2**

Dynamic set of values - for example, a record list resulting from a previous query or action is transformed into a comma separated string of values, and then passed into the query in a expanded inline parameter called UserIds:  
  
    SELECT {User}.[Name], {User}.[Phone]  
    FROM {User}  
    WHERE {User}.[IsActive]  
    AND {User}.[Id] in { @UserIds }  
    ORDER BY {User}.[Name]

## Impact

There is a good chance that every time the query is called in these two examples, a completely different text is passed to the Inline parameter, generating a completely different query for the DB Engine.

Inline parameters that change too often don't allow the database to optimize execution plans, since the engine keeps generating different queries. This is a huge impact on performance. A complex query with volumes of data that takes a couple of seconds at the first execution, executes in milliseconds for each next call after statistical optimization.

## Best practices

Here are some recommendations to avoid expand inline parameters:

* Avoid dynamic SQL to cope with optional filters - use fixed conditions covering the optionality instead.

    To fix the example 1, instead of the inline parameter SearchClause, send the SearchKeyword as a normal parameter and transform the query as follows:  
  
        SELECT {User}.[Name], {User}.[Phone]  
        FROM {User}  
        WHERE {User}.[IsActive]  
        AND @SearchKeyword = '' OR {User}.[Name] like '%'+@SearchKeyword+'%'  
        ORDER BY {User}.[Name]  
  
    With this fix the query is always the same for the DB engine. It's important to place the optionality condition first (`@SearchKeyword = ''`) to make sure that the real condition is never executed when there is no Search keyword. DB engines do a very good job optimizing this type of “dummy” conditions, so preparing the query for this optional filters is practically neglectable.

* Use subqueries instead of injecting the result of a query as comma separated values to the next query.

    If UserIds in the example 2 come from a complex query to select users with a certain logic, that query can be included in the same SQL query. It can even be used to avoid the IN condition that could degrade the performance. For example:  
  
        WITH UserIdTable (Id) as (SELECT ...)  
        SELECT {User}.[Name], {User}.[Phone]  
        FROM {User}  
        INNER JOIN UserIdTable on UserIdTable.ID = {User}.[ID]  
        WHERE {User}.[IsActive]  
        ORDER BY {User}.[Name]  
  
Again, we achieved a fixed query that will be optimized by the DB Engine.

* Use temporary tables when the comma separated list of values don’t come from a single query. Sometimes the list of values is the result of some complex logic (non-SQL processing) that keeps adding elements to the list. Instead of adding the elements to a comma separated list of values, add the values into a temporary table (you can google “Oracle temporary tables” or “SQL temporary tables” to find out how you can create a temporary table in a SQL query). Once you populate the temporary table, the example 2 can be changed into:

        SELECT {User}.[Name], {User}.[Phone]  
        FROM {User}  
        INNER JOIN TemporaryTable on TemporaryTable.ID = {User}.[ID]  
        WHERE {User}.[IsActive]  
        ORDER BY {User}.[Name]
