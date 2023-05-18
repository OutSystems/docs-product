---
tags:
summary: 
locale: en-us
guid: 1aecc52f-daef-42a3-ab1b-12e31f086dcb
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---


# Control the number of records fetched from the DB

In an app usually only a fixed set of rows is returned when listing information. Additional records are fetched with the use of pagination or infinite scroll mechanism. Your Aggregates or SQL queries should always take into account the required number of records. 

## Impact

Not limiting the number of rows in a query results in unnecessary CPU use, IO consumptions on the database, and unwanted memory take on the Web Server - just to hold the result of the entire query. Imagine fetching 1K records in every call when all you need is the first 10 records.

## Best practices

With Aggregates:

* Set the **Max. Records** property of the aggregate to the required usage.

* If required, the **&lt;Aggregate&gt;.Count** contains the total count of records, without the **Max. Records** limitation.

With SQL queries:

To limit the number of rows, to the rows required in a SQL query, it isn't enough to set the **Max. Records**. This doesn't change the query itself to limit the number of rows (it limits the number of rows that are copied to the output record list, so there is still an unnecessary load on the database).

The solution is to control the number of rows inside the query:

![](images/limit-rows-sql.png)

The SQL version only works if you set the @maxrows input parameter as **Expand Inline**. Otherwise, the SQL engine would evaluate the parameter and turn it into a literal. As the input parameter needs to be set as **Expand Inline**, its data type has to be text.

<div class="warning" markdown="1">

Whenever possible, avoid using **Expand Inline** parameters on your queries, as they represent a risk of SQL injection and you may have [findings on AI Mentor Studio](ref-code-patterns.md#sql-injection).

</div>

In this particular case, ensure you're passing a valid value to the query input @maxrows, by using the **EncodeSQL** method. See [recommendations when using Expand Inline](../../../ref/errors-and-warnings/warnings/sql-injection-warning.md#recommendations) for more information.

By changing your queries to limit the number of retrieved rows, you no longer rely on the **&lt;Query&gt;.Count** property to get the correct count of rows complying with the original query conditions and joins. If you need the total number of rows, you must make a separate query to do that count.
