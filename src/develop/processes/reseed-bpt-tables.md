---
summary: Reseeding identity values in BPT tables 
tags: 
locale: en-us
guid: b12b531a-097a-41c5-965b-7354fcdc2cef
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
---

# Reseeding identity values in BPT tables - SQL Server

<div class="info" markdown="1">

Applies to self-managed infrastructures only 

</div>

In scenarios where you're using a lot of business process technology (BPTs) (even in situations where BPT maintenance is carried out), it's possible that the identity values of the core BPT tables can reach the maximum limit supported by the SQL Server INT type of 2,147,483,647. If you reach the identity value limit, you can no longer insert new rows into a table, as it is not possible to add rows with an identity value greater than the maximum allowed INT size. 

To avoid reaching the identity value limit, you can reseed the BPT identity values in your tables. Reseeding the identity values to use negative values doubles the number of entries that you can insert into the affected tables.

Depending on the needs of the business, you can immediately purge tables of old processes. The OutSystems [BPT API](../../ref/apis/auto/bpt-api.final.md) offers methods to help in the maintenance of BPT processes. Examples of this API being used are available in the Forge with tools such as [DBCleaner](https://www.outsystems.com/forge/component-overview/423/dbcleaner-o11), [DBCleaner on Steroids](https://www.outsystems.com/forge/component-overview/5018/db-cleaner-on-steroids-o11), [OneClickCLeanup](https://www.outsystems.com/forge/component-overview/2176/oneclickcleanup-o11), and [BPT Utils](https://www.outsystems.com/forge/component-overview/1313/bpt-utils-o11).

If old BPT data is still required, [you can archive that data](https://success.outsystems.com/documentation/how_to_guides/processes/how_to_archive_old_processes_bpt/) before purging old BPT processes.

If you use BPTs a lot, it may be worth considering alternative design patterns, such as [Light BPT processes](light-process.md). Light BPT processes are used for simple automation tasks that leave no footprint behind and are a big benefit if you use data-driven event handling.

To check the current identity values in your BPT tables, you can run the following SQL statement:

```sql
Unset
DBCC CHECKIDENT(<table_name>, NORESEED);
```
The expected output will look like something like this:

```sql
Unset
Checking identity information: current identity value '<current identity value>', current column value '<current column value>'. DBCC execution completed. If DBCC printed error messages, contact your system administrator.
```

<div class="info" markdown="1">

To run this SQL statement, you must own the schema that contains the table or be a member of the ``sysadmin fixed server`` role, the ``db_owner fixed database`` role, or the ``db_ddladmin fixed database`` role.

</div>

To avoid reaching the identity value limit, you can reseed the BPT identity values in your tables. 

## Reseed the BPT identity values

The following steps demonstrates how you can reseed the identity value for the ``ossys_BPM_Activity`` table to a negative value:

1. Run the following SQL statement in the OutSystems Platform Database.

    ```sql
    Unset
    DBCC CHECKIDENT (ossys_BPM_Activity, RESEED, -2147483648);
    GO
    ```

1. Run the following SQL statement to verify the identity value has been reseeded.

    ```sql
    Unset
    DBCC CHECKIDENT (ossys_BPM_Activity, NORESEED);
    GO
    ```

1. Repeat steps 1 and 2 for the ``ossys_BPM_Process`` table if required.

<div class="warning" markdown="1">

If you don't clean up your BPT data after performing a reseed operation, eventually, the number of new rows inserted can result in the identity value reaching the value of an existing entry. Later, when you insert new rows into the tables, an error is thrown because the generated identity value will conflict with an existing value.

</div>
