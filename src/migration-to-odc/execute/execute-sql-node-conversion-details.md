---
guid: 39294c65-0ea8-4928-bd92-08d0755df07c
locale: en-us
summary: O11 to ODC SQL node conversion details explain clause, function, and type mappings for PostgreSQL-ready queries in OutSystems Developer Cloud (ODC).
figma:
coverage-type:
  - remember
  - understand
topic:
  - adapt-converted-sql
  - sql-conversion-mapping
app_type: mobile apps,reactive web apps
platform-version: o11
audience:
  - Developer
tags:
  - Data
  - SQL
outsystems-tools:
  - odc studio
helpids:
isautopublish: true
---

# O11 to ODC SQL node conversion details

Currently, the conversion tool automatically converts most of the standard O11 queries that involve only [internal entities](https://www.outsystems.com/tk/redirect?g=5a13a09e-6e8f-40b2-8ca3-eb7af13e3b40) into their ODC PostgreSQL-compatible syntax described in [SQL queries compared to OutSystems 11](https://www.outsystems.com/tk/redirect?g=db4685f5-477f-436a-b4cc-92af8e347c02).

This page provides the technical details on the mapping used for SQL node conversion and highlights some scenarios that require attention.

<div class="info" markdown="1">

See [SQL nodes conversion limitations](execute-adjust-converted-code.md#sql-limitations) for the scenarios that require manual conversion.

</div>

## System Entities

The set of system entities available in ODC is different from O11. The conversion tool keeps the original system entity name and attributes in the converted SQL nodes. Thus, queries containing **system entities** that don't match between O11 and ODC will fail.

For O11 system entities that are no longer available in ODC, you might need to refactor your code to use ODC capabilities instead. See [System entities not available in ODC](https://success.outsystems.com/documentation/11/outsystems_11_to_odc_conversion/o11_to_odc_conversion_patterns/asset_consuming_o11_platform_system_elements/#system-entities) for further details.

## General SQL clauses and functions

The table below shows the O11 to ODC mapping used during the automatic conversion for the listed SQL clauses and functions:

| O11 syntax | ODC syntax |
| --- | --- |
| `SELECT TOP 10 * FROM {Organization}` | `SELECT {Organization}.* FROM {Organization} LIMIT 10` |
| `LEN()` | `LENGTH()` |
| `SUBSTRING(str, start, len)` | `SUBSTRING(str FROM start FOR len)` |
| `NEWID()` | `gen_random_uuid()` |
| `RAND()` | `random()` |
| `ISNULL(a, b)` | `COALESCE(a, b)` |
| `IIF(condition, true, false)` | `CASE WHEN…` |
| `WAITFOR DELAY 'HH:MM:SS'` | `SELECT pg_sleep(seconds)` |
| `FORMAT()` | `TO_CHAR()` |
| `CONVERT(data_type(length), expression, style)` | `CAST ( expression AS target_type )` |
| `CHARINDEX(substring, string)` | `STRPOS(string, substring)` |
| `GETDATE()` | `CURRENT_TIMESTAMP` |
| `GETUTCDATE()` | `CURRENT_TIMESTAMP AT TIME ZONE 'UTC'` |
| `SYSDATETIME()` | `CURRENT_TIMESTAMP` |
| `DATEADD(day, 7, date)` | `date + INTERVAL '7 day'` |
| `DATEADD(month, -3, date)` | `date - INTERVAL '3 month'` |
| `DATEADD(year, 1, date)` | `date + INTERVAL '1 year'` |
| `DATEDIFF(day, start, end)` | `EXTRACT EPOCH / 86400` |
| `DATEDIFF(hour, start, end)` | `EXTRACT EPOCH / 3600` |
| `DATEDIFF(minute, start, end)` | `EXTRACT EPOCH / 60` |
| `DATEPART(year, date)` | `EXTRACT(YEAR FROM date)` |
| `DATEPART(month, date)` | `EXTRACT(MONTH FROM date)` |
| `DATEPART(day, date)` | `EXTRACT(DAY FROM date)` |
| `YEAR(date)` | `EXTRACT(YEAR FROM date)` |
| `MONTH(date)` | `EXTRACT(MONTH FROM date)` |
| `DAY(date)` | `EXTRACT(DAY FROM date)` |
| `EOMONTH(date)` | `DATE_TRUNC('month', date) + INTERVAL '1 month' - INTERVAL '1 day'` |
| `DATETRUNC(month, date)` | `DATE_TRUNC('month', date)` |
| `DATENAME(month, date)` | `TO_CHAR(date, 'month')` |

## Oracle-specific clauses and functions

The table below shows the O11 to ODC mapping used during the automatic conversion for the listed Oracle-specific clauses and functions:

| O11 syntax | ODC syntax |
| --- | --- |
| `SELECT * FROM {Organization} WHERE ROWNUM <= 10` | `SELECT * FROM {Organization} LIMIT 10` |
| `SELECT Id FROM Users MINUS SELECT UserId FROM Orders` | `SELECT Id FROM Users EXCEPT SELECT UserId FROM Orders` |
| `SELECT * FROM DUAL` | `SELECT *` <br/><br/>(`FROM DUAL` is removed from the converted query) |
| `NVL()` | `COALESCE()` |
| `NVL2(x, y, z)` | `CASE WHEN x IS NOT NULL THEN y ELSE z END` |
| `SUBSTR(str, start, len)` | `SUBSTRING(str FROM start FOR len)` |
| `INSTR(string, substring)` | `STRPOS(string, substring)` |
| `SYS_GUID()` | `gen_random_uuid()` |
| `DBMS_RANDOM.VALUE` | `random()` |
| `SYSDATE` | `CURRENT_TIMESTAMP` |
| `SYSTIMESTAMP` | `CURRENT_TIMESTAMP` |
| `TRUNC(number)` | `TRUNC(number)` |
| `TRUNC(date, 'month')` | `DATE_TRUNC('month', date)` |
| `ADD_MONTHS(date, months)` | `date + INTERVAL 'months month'` |
| `TO_DATE(date, format)` | `TO_TIMESTAMP(date, format)` |

## Data type conversion

O11 SQL queries containing data types are converted into ODC SQL queries by translating the types following the patterns shown below.

### SQL Server/Azure SQL

| O11 data type | ODC data type |
| --- | --- |
| NVARCHAR(MAX), VARCHAR(MAX) | TEXT |
| NVARCHAR2(n), NVARCHAR(n) | VARCHAR(n) |
| NCHAR(n) | CHAR(n) |
| SMALLDATETIME, DATETIME, DATETIME2 | TIMESTAMP |
| DATETIMEOFFSET | TIMESTAMPTZ |
| SMALLMONEY, MONEY | NUMERIC |
| TINYINT | SMALLINT |
| FLOAT | DOUBLE PRECISION |
| INT | INTEGER |
| UNIQUEIDENTIFIER | UUID |
| BIT | BOOLEAN |
| VARBINARY(MAX), VARBINARY(n), IMAGE | BYTEA |

### Oracle

| O11 data type | ODC data type |
| --- | --- |
| CLOB, NCLOB, LONG | TEXT |
| VARCHAR2(n), NVARCHAR2(n) | VARCHAR(n) |
| NUMBER, NUMBER(p) (if p <= 10), BINARY_INTEGER, PLS_INTEGER, SIMPLE_INTEGER | INTEGER |
| NUMBER(p) (if p > 10) | BIGINT |
| NUMBER(p, s) (if scale > 0) | NUMERIC(p, s) |
| FLOAT, BINARY_FLOAT, BINARY_DOUBLE | DOUBLE PRECISION |
| BLOB, LONG RAW, RAW(n) | BYTEA |
| DATE | TIMESTAMP |

## String concatenation

The following rules apply for SQL queries having concatenated text strings:

| Rule | O11 syntax | ODC syntax |
| --- | --- | --- |
| String literals should use `'`\|\|`'` | `'First' + 'Last'` | `'First'` \|\| `'Last'` |
| Column + string should use `'`\|\|`'` | `{Entity1}.[TextAttr] + 'suffix'` | `[TextAttr]` \|\| `'suffix'` |
| Multiple strings should use `'`\|\|`'` | `'A' + 'B' + 'C'` | `'A'` \|\| `'B'` \|\| `'C'` |
| Numeric addition should stay as `'+'` | `{Entity1}.[NumericAttr] + 10` | `[NumericAttr] + 10` |
| String concatenation with COALESCE/ISNULL | `ISNULL({Entity1}.[TextAttr], '') + ' - ' + ISNULL({Entity1}.[TextAttr2], '')` | `COALESCE({Entity1}.[TextAttr], '')` \|\| `' - '` \|\| `COALESCE({Entity1}.[TextAttr2], '')` |

## Cast time type column

For O11 SQL queries containing time data type comparison, the conversion tool adds the key `::time` to the **Time** type column:

`{UseCase_Time}.[Time]::time > '11:01:41'`

## Temporary tables

Temporary tables created in SQL queries have different approaches in O11 and ODC. The table below shows the scenarios that are automatically converted:

| O11 syntax | ODC syntax |
| ---------- | ---------- |
| `SELECT INTO #temp` | `CREATE TEMP TABLE temp AS SELECT` |
| `CREATE TABLE #temp (...)` | `CREATE TEMP TABLE temp (...)` |

## Pattern matching operators

O11 SQL queries containing `LIKE` clauses are wrapped with the `caseaccent_normalize` function in ODC queries:

`SELECT * from table WHERE caseaccent_normalize(col1 collate "default") LIKE caseaccent_normalize(col2 collate "default");`

## Result schema expansion scenario

When you use `SELECT *` in PostgreSQL, the database returns every single column generated by the query's projection. This includes any computed, derived, or expanded attributes you created, such as row numbers, or calculated values.

Compared to O11 SQL syntax, PostgreSQL is much stricter about its output structure. If your application expects a specific number of columns and the query returns an extra "hidden" column, your application will likely throw a runtime error, such as **Column count doesn't match output structure attribute count.**

In PostgreSQL, the schema of a result set is defined by the `SELECT` list of the innermost query, or subquery. If an expression is in that list, it is visible to SELECT *. Consider the following example:

```
WITH RankedSalary AS (
    SELECT [Name], [Salary], 
      ROW_NUMBER() OVER (PARTITION BY [DepartmentId] ORDER BY [Salary] DESC) as SalaryRank
    FROM {Employee}
)
SELECT * FROM RankedSalary WHERE SalaryRank = 1;
```

For this example, the PostgreSQL result schema is the following:

`RankedSalary.*, SalaryRank`

Common patterns that increase the number of returned attributes:

* Window functions, such as `ROW_NUMBER`, `RANK`, or `DENSE_RANK`

* Subqueries that include computed expressions, such as a total, or price

* Table-returning functions or JSON expansion functions

* LATERAL joins that project additional columns

* Views defined using `SELECT *` together with derived expressions

To avoid column count mismatch errors, explicitly list your attributes in the final `SELECT` statement rather than using `*`. This ensures your application receives exactly what it expects, regardless of how many temporary columns were used in the subqueries.
