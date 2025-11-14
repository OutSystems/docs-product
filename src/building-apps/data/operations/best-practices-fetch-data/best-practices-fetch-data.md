---
summary: OutSystems 11 (O11) performance best practices focus on optimizing database queries to enhance application efficiency and reduce bottlenecks.
guid: 53c2c027-cc58-4e6e-8b6d-95e9e0a9c278
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: database optimization, performance tuning, best practices, application efficiency, sql queries
audience:
  - backend developers
  - full stack developers
  - architects
outsystems-tools:
  - service studio
coverage-type:
  - evaluate
---

# Best practices for fetching data

In multi-tier applications, the bottleneck is often situated at the database level, namely in the queries. The importance of these practices is more notable when dealing with external/linked servers. Specific knowledge about the database engine will help in optimizing your queries. However, if you follow the next set of practices, you’ll considerably diminish your application’s performance drawbacks.

## Don’t do joins over linked servers

### Description

Cross server joins are very inefficient. Avoid them at all costs.

### Solution

When using linked servers, avoid the cross server joins.

### Importance

The table in the linked server is completely loaded to the DB server and then the join is performed.

### Remarks

Inner joins with foreign entities tend to result in slow queries. However, if you must make a join over a linked server, make sure to use additional logic so that only a data subset is pulled from the linked server and only what was pulled is joined (temporary tables, OPENQUERY, ...). Whatever the case, joins over linked servers need to be addressed very carefully.

## Minimize the number of fields fetched from the database

### Description

Avoid passing large Records/RecordLists as parameters of actions because this results in the platform fetching all the queried fields.

### Solution

When dealing with actions that receive or output Record/RecordLists with a large number of attributes consider using Structures instead of Entities for those records. Structures narrow down the amount of data that flows through the entire system producing significant net benefits.

### Importance

To minimize the size of data fetched from database and to prevent slow queries and excessive memory usage, the compiler optimizer automatically detects which fields from query result records are used. The unused fields are unnecessary and as such are not fetched from the database. However when the records of a query result are used as argument of an action the optimizer doesn't have enough information to determine which fields are used and which fields aren't. In this situation all the fields will be fetched from the database, which in some cases might be a prohibitive amount of data.

### Remarks

There is a balance that needs to be taken into account between maintainability and performance. Using entity records as query results and input/output parameters usually results in highly reusable easy to change components. This best practice should only be used when dealing with entities/query results with a large number of fields.

## Keep Max Records consistent with your needs

### Description

Keep the Max Records property of Aggregates consistent with the amount of data that you're displaying.

### Solution

When there are limitations to the amount of records that are fetched from a query, you should fill in the Max Records property of an Aggregate accordingly to optimize the query execution time. This is especially useful in table records or when an Aggregate is used to get a single record.

### Importance

Usually, there's no need to display thousands of records in a single screen, so there's no need to get them all from the database. Only get the amount of rows that will be displayed. This improves screen loading.

### Remarks

Setting the Max Records property in SQL elements **doesn't** change its SQL statement. This limit is only applied at the application level to the results returned by the database. Unlike Aggregates, you need to add a SQL clause to the statement of the SQL element (for example, TOP) to filter the results at the database level.

## Use SQL queries for bulk operations

### Description

When performing massive operations, use SQL queries instead of using a For Each loop with Aggregates (keep in mind that Aggregates are always more built to change, though). Also, updates and massive deletes are faster in SQL queries than using entity actions. Write queries that update as many rows as possible in a single statement rather than using multiple queries to update the same rows.

### Solution

1. If you don't need to retrieve all entity attributes, consider replacing the Get entity action with an Aggregate using an Identifier parameter. OutSystems optimizes the query to retrieve the required attributes.

1. If you need to delete multiple records, use an SQL Query with a single Delete instead of a For Each followed with a Delete operation for each record.

1. Use Update instead of a Delete followed by a Create.

1. Use a CreateOrUpdate instead of a Select followed by a Delete and a Create.

1. Use an SQL query with a sub query instead of an Aggregate, followed by a For Each loop over the query result with another simple query for each record.

### Importance

Every operation done against the database pays a round trip cost of communicating with the server. When doing a large number of operations, the sum of all the round trip cost is quite significant, so there is a real benefit in reducing the number of operations.

Also the databases are significantly more efficient at performing batch operation than many small ones. There is also a significant benefit in not retrieving information that isn't necessary.

### Remarks

SQL queries should never be the first option, as Aggregates provide you with more straightforward and optimized data manipulation. However, the huge performance gains when using SQL queries to perform bulk operations justifies its usage for this specific scenario.

## Avoid using isolated Aggregates

### Description

Never create an action to execute an Aggregate. When the query is isolated in an action by itself, the Platform can't optimize the number of fields to be retrieved.

### Solution

The compiler optimizer automatically detects the used fields. However, when calling an action whose output is an entity or record list, the entity (or entities in the case of a record list) are fetched entirely from the DB.

### Importance

This is true even if the action doesn’t read all the fields of the entity/record list. This causes unnecessary database overload and unnecessary memory usage.

### Remarks

Please note that this invalidates code reusability - so, in some cases, (especially when the output isn't large) it's better to have isolated queries instead of a lot of similar ones.

## Iterate only once and avoid using indexers ([ ]) over a query

### Description

Iterating more than once over a query result isn't a good practice. By doing so, the query results are copied into the memory. The same applies when using direct indexers (like query[2].value expressions).

### Solution

If conserving server memory is necessary, try to avoid doing multiple iterations (for each, table/list records) over the same query. It's better to do another query to execute the second iteration (Note: if DB is the bottleneck, this doesn’t apply).

### Importance

When doing multiple iterations on the same query, the query results are automatically loaded into memory. If the query returns a lot of results this may increase memory consumption substantially, especially if the page is loaded very often. Using indexers on your expression also loads the results in memory independently of the number of iterations.

### Remarks

This also applies to lists displayed on a screen. For example if you iterate a query once and then display it in a table records, your query is copied into memory. This happens because the rendering of the table records iterates through the query results again.

## Minimize the number of executed queries

### Description

Minimize the number of executed queries. Often, it's possible to fetch all necessary data in a single query execution instead of multiple ones.

### Solution

Whenever possible, group several Aggregates or SQL queries into a single one to avoid unnecessary trips to the database:

* Merge sequences of Aggregates that reference one another into a single Aggregate, [using a join](https://success.outsystems.com/Documentation/11/Reference/OutSystems_Language/Data/Handling_Data/Queries/Supported_Join_Types) to retrieve all the needed data.

* Avoid executing Aggregates or SQL queries inside a For Each cycle. Instead, replace that Aggregate or SQL query with a more complex one that gets all the related information, and execute it before the cycle. In most of the cases that you have an Aggregate to fetch the master entity before the cycle followed by another Aggregate inside the cycle to fetch the details, you can eliminate the inner Aggregate by [adding a Join](https://success.outsystems.com/Documentation/11/Reference/OutSystems_Language/Data/Handling_Data/Queries/Supported_Join_Types) to the outer Aggregate.

* If it’s not possible to refactor the query, consider [enabling the cache](https://success.outsystems.com/Documentation/11/Developing_an_Application/Use_Data/Caching#Activating_the_caching_feature) for the Aggregate or SQL query. In this case, do proper business rules validation regarding cache configuration and impact.

### Importance

Even the simplest Aggregate has to pay the round trip cost for contacting the database. The higher the number of Aggregates and SQL queries, the higher is the communication overhead.

For reasons of code readability, is frequent to use a simple query to retrieve data from a master entity and then fetch the details inside a cycle using another query. However, Aggregates and SQL queries executed inside a cycle can have severe performance impact due to database communication overhead repeated at each iteration. The impact can be greatly worsened when iterating through a list with a high number of elements or when having nested cycles.

The net cost of querying and loading data is lower when executing a single query instead of multiple queries.

### Remarks

While minimizing the number of executed queries can result in large performance gains, it's usually done at the expense of code readability. Thus, the key here is to optimize only when required. Use the Service Center Analytics reports to pinpoint the bottlenecks. Remember that a single fast query won't show up on the queries performance report, but if it’s executed often in a cycle, the accumulated time can influence other reports or logs, such as the screens performance report, or the screen requests logs.
