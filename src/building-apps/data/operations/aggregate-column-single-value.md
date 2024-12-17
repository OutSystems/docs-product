---
summary: Discover how to aggregate a column into a single value using OutSystems 11 (O11) with functions like Sum, Average, Max, Min, and Count.
tags: database operations, data manipulation, ui interactions, data aggregation, application development
locale: en-us
guid: 65fc5101-2962-4239-a14a-f1a4f9d19fab
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=173:7
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - understand
---

# Aggregate a Column into a Single Value

Sometimes displaying a single aggregated value can be more meaningful than displaying the full list of records available in the database.

To aggregate a column into a single value, hover on the column, right-click, and select one of the aggregate functions:

* Sum: sums all the values in the column
* Average: calculates the average of the values in the column
* Max: finds the maximum value in the column
* Min: finds the minimum value in the column
* Count: counts how many rows there are in the column

![Context menu showing aggregate functions including Sum, Average, Max, Min, and Count on a database column](images/aggregate-column-single-value.png "Aggregate Functions Menu")

The list of available aggregate functions depends on the data type of the column. Sum and Average are only available for numeric data types whereas textual data types (text, email, and phone number) only have the Count function available.
