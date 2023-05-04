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

The SQL Version only works if you set the @maxrows input parameter to be an **Expand Inline** one. And that oblies you to change the data type of the query input parameter to text.
**Expand Inline** parameters on your queries are not recommended, may be exploited and you may have findings on AI Mentor Studio:

* [Learn more about AI Mentor Studio Findings](https://success.outsystems.com/documentation/11/managing_the_applications_lifecycle/manage_technical_debt/code_analysis_patterns/).

In this particular case make sure to pass what you are passing to the query input @maxrows, if it's a variable or an input, through the **VerifySqlLiteral** function provided by the **Sanitization** extension.
With this change you no longer rely on the **&lt;Query&gt;.Count** property to get the correct count of rows complying with the original query conditions and joins.
You need to make a separated query just to do the count if you need it.
