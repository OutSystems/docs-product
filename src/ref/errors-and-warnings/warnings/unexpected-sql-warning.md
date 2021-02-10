# Unexpected SQL Warning

Message:
:   `There is a mismatch between the number of select columns SELECT and the output structure in <query>`

Cause
:   You have an SQL query where the specified Output Structure does not match the attributes being selected. This can happen because the number of attributes is different or because there is a data type mismatch.

Recommendation
:   Edit your query and do one of the following:

    * Change the specified Output Structure of the query.
    * Change the attributes being selected.

<div class="info" markdown="1">

To learn more about SQL in OutSystems, check out the following free courses:

* [SQL Queries](https://www.outsystems.com/training/courses/146/sql-queries/). Write your SQL queries to interact with data in OutSystems.
* [Getting Started with OutSystems for SQL Developers](https://www.outsystems.com/training/courses/169/getting-started-with-outsystems-for-sql-developers/). Learn how to create a data model, fetch data, and how to use an existing external database in an OutSystems app.


</div>

---

Message
:   `SELECT statements with 'Expand Inline' parameters cannot be validated against the output structure in <query>`

Cause
:   Since you have a query with expand in line parameters, it is not possible to check whether the Output Structure matches the selected attributes.

Recommendation
:   You should open your SQL query and check whether the specified Output Structure contains the necessary attributes to fetch the selected attributes, specified in the Inline parameters.

---

Message
:   `SELECT statements with '*' cannot be validated against the output structure in <query>`

Cause
:   Since you are selecting all attributes (*) of the entities in the query, OutSystems is not able to confirm that the Output Structure matches these attributes.

Recommendation
:   You should open your SQL query and check whether the Output Structure contains the necessary attributes to hold the selected attributes. To avoid this warning it is advisable that you use `SELECT {Entity}.*` instead of just `SELECT *`.

---

Message
:   `There is a mismatch between the SELECT'ed entities and the output structure in <query>`

Cause
:   You are selecting the entities, in your query, with `SELECT {Entity}.*` and the output structure includes these entities or entities with the same definition. In this situation, Service Studio is not able to confirm that the Output Structure matches the selected attributes. This warning is launched when, for example, you are selecting `SELECT {EntityA}.*` , `{EntityB}.*` and the order in the output structure is `EntityB` and `EntityA`.

Recommendation
:   You should change the order by which entities are selected to make it the same as the Output Structure.

---

Message
:   `Unexpected <text> in SQL statement of <query>. Recheck the SQL to make sure it is valid`

Cause
:   The SQL statement is not recognized by OutSystems, but might be valid. This validation is made based on the Database module property, which indicates the database type where the module is published.

Recommendation
:   Re-check the SQL of the query to be sure it is valid.
