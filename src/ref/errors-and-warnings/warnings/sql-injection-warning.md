---
summary: Check the causes and recomendations on how to solve the different SQL Injection TrueChange warnings
tags:
---

# SQL Injection Warning

OutSystems uses [prepared statements](<https://en.wikipedia.org/wiki/Prepared_statement>) by default to execute the SQL queries that you define in [SQL elements](<../../../develop/data/query/sql.md>). These prepared statements contain SQL parameters or placeholders, for which you define values before executing the SQL statement. These parameters can only store a value of a given type and not arbitrary SQL fragments. Learn more on how the use of prepared statements can prevent SQL injection attacks in OWASP's [SQL Injection Prevention Cheat Sheet](<https://www.owasp.org/index.php/SQL_Injection_Prevention_Cheat_Sheet>).

Also, OutSystems uses a SQL parameter for every Query Parameter that has the **Expand Inline** property **disabled**. This property is disabled by default, providing you **default protection against SQL injection attacks**.

If you enable the Expand Inline property for a Query Parameter, its value will no longer be handled as a SQL parameter value. Instead, the Query Parameter value will be included in the SQL statement without first being evaluated and turned into a literal by the SQL engine. This means that you are able to use the Query Parameter to dynamically insert SQL fragments in the full SQL statement, but it also means that your end users may be able exploit this fact if you do not take the necessary precautions.

The SQL Injection warning is issued when you enable the Expand Inline property of a SQL Query Parameter. You must carefully analyze each of these warnings to ensure you take the necessary precautions to protect your application against SQL injection attacks.

Double-click on the error line in TrueChange to take you directly to the parameter that is issuing the warning.

## Avoid enabling the Expand Inline property of a SQL Query Parameter since it could make your application vulnerable to SQL injection.

**Cause**

You enabled the Expand Inline property for a SQL Query Parameter, meaning that your application can be vulnerable to SQL injection if you don't take the necessary precautions.

**Recommended action**

Avoid using Expand Inline.

OutSystems provides ways of implementing common use cases without enabling this property. See [Building dynamic SQL statements the right way](<https://success.outsystems.com/Documentation/Best_Practices/Building_dynamic_SQL_statements_the_right_way>) to understand if you can change your implementation to avoid having the Expand Inline property enabled.

If you **must** use Expand Inline to implement your use case, follow the [recommendations below](#recommendations).

**When is it safe to hide the warning?**

You should **only** hide this warning when you have ensured that your SQL statement doesn't contain values provided by end users.

## When adding an expand inline parameter after a Group By or Order By, make sure to sanitize the parameter value. Otherwise, the action may be vulnerable to SQL injection.

**Cause**

You enabled the Expand Inline property for a SQL Query Parameter used after an "ORDER BY" or "GROUP BY" snippet in your SQL statement. Your application can be vulnerable to SQL injection if you don't take the necessary precautions.

**Recommended action**

Make sure the expand inline Query Parameter used after the "ORDER BY" or "GROUP BY" snippet in your SQL statement doesn't contain values provided by end users.

See [How to use dynamic sorting in a table fed by a SQL query](https://success.outsystems.com/Documentation/How-to_Guides/Development/How_to_use_the_List_Sort_Column_Widget_with_a_SQL_query) for further details. See also the [recommendations below](#recommendations) when using Expand Inline.

**When is it safe to hide the warning?**

You should **only** hide this warning when you have ensured that the expand inline Query Parameter used after the "ORDER BY" or "GROUP BY" snippet doesn't contain values provided by end users.

## Recommendations when using Expand Inline { #recommendations }

**Proper use of parameters being expanded inline is hard**, since you need to make sure that any user input has been properly escaped in the right way before using it in a SQL statement. If possible, avoid enabling this property altogether.

If you **must** use Expand Inline, take the following recommendations into account:

Use EncodeSql to encode string literals
:   The EncodeSql function encodes string literals to be used in SQL statements when the Expand Inline property is enabled.

    Make sure you avoid the following bad practices of using EncodeSql:

    — **Do not** use EncodeSql to encode the full contents of a SQL parameter. For example:  
    `myparameter = EncodeSql("WHERE surname = " + @myVariable1 + " OR name = " + @myVariable2)`  
    This pattern is wrong in most occasions, and thus you will get a warning if you do it.  
    Use EncodeSql only to encode **string literals**, not complete fragments of a SQL statement. 

    — **Do not** build "WHERE column IN (@values)" clauses by wrapping all the values in a EncodeSql call:  
    `values = EncodeSql(name1 + "," + name2 + "," + name)`  
    This approach will **not** protect you from SQL injection.  
    Instead, use the [BuildSafe_InClauseIntegerList](../../apis/auto/sanitization-api.final.md#BuildSafe_InClauseIntegerList) and [BuildSafe_InClauseTextList](../../apis/auto/sanitization-api.final.md#BuildSafe_InClauseTextList) functions to build "WHERE column IN (@values)" clauses.
    

Do not perform manual string encoding using the Replace
:   String literals should **only** be encoded using the EncodeSql function. Doing it manually through the Replace function is prone to errors and can introduce bugs in your application that can later be exploited by end users of your application.

<div class="info" markdown="1">

To learn more about SQL in OutSystems, check out the following free courses:

* [SQL Queries](https://www.outsystems.com/training/courses/146/sql-queries/). Write your SQL queries to interact with data in OutSystems.
* [Getting Started with OutSystems for SQL Developers](https://www.outsystems.com/training/courses/169/getting-started-with-outsystems-for-sql-developers/). Learn how to create a data model, fetch data, and how to use an existing external database in an OutSystems app.

</div>
