---
summary: Explore how to manage and extend the capacity of BPT tables in SQL Server by reseeding identity values using OutSystems 11 (O11) tools and APIs.
tags: sql server, database management, identity reseeding, bpt (business process technology), data archiving
locale: en-us
guid: b12b531a-097a-41c5-965b-7354fcdc2cef
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - platform administrators
  - backend developers
  - full stack developers
  - infrastructure managers
outsystems-tools:
  - service studio
coverage-type:
  - evaluate
  - apply
---

# Avoid maximum ID limits in BPT tables

<div class="info" markdown="1">

Applies to self-managed infrastructures only.

</div>

In scenarios when you use business process technology (BPT), even in situations where BPT maintenance is carried out, it's possible that the values used for the ID columns of the core BPT tables can reach the maximum limit supported by the standard integer data type of 2,147,483,647. If you reach this value, you encounter undefined behavior, as the Platform doesn't handle values greater than 2,147,483,647 when processing BPT processes and activities.

To avoid BPT ID values reaching this limit, you can either reseed the identity values or restart the sequence values used in your tables. This depends on the use of SQL Server or Oracle Platform Database. Performing the relevant action to use negative values doubles the number of entries that you can insert into the affected tables.

Depending on the business's needs, you can immediately purge tables of old processes. The OutSystems [BPT API](../../ref/apis/auto/bpt-api.final.md) offers methods to help in the maintenance of BPT processes. Examples of this API being used are available in the Forge with tools such as [DBCleaner](https://www.outsystems.com/forge/component-overview/423/dbcleaner-o11), [DBCleaner on Steroids](https://www.outsystems.com/forge/component-overview/5018/db-cleaner-on-steroids-o11), [OneClickCLeanup](https://www.outsystems.com/forge/component-overview/2176/oneclickcleanup-o11), and [BPT Governor](https://www.outsystems.com/forge/component-overview/17901/bpt-governor-o11).

If old BPT data is still required, [you can archive that data](https://success.outsystems.com/documentation/how_to_guides/processes/how_to_archive_old_processes_bpt/) before purging old BPT processes.

If you use frequently work with BPTs, consider alternative design patterns, such as [Light BPT processes](light-process.md). Light BPT processes are used for simple automation tasks that leave no footprint behind and are a big benefit if you use data-driven event handling.

<div class="warning" markdown="1">

If you don't clean up your BPT data after performing the specified operation, eventually, the number of new rows inserted can result in the sequence value reaching the value of an existing entry. Later, when you insert new rows into the tables, an error is thrown because the ID column value will conflict with an existing value in the associated table.

</div>

## SQL Server - Reseed identity values in BPT tables

To check the current identity values in your BPT tables, you can run the following SQL statement:

```
DBCC CHECKIDENT(<!--table_name>, NORESEED);
```

The expected output will look similar to this:

```
Checking identity information: current identity value '<current identity value>', current column value '<current column value>'. DBCC execution completed. If DBCC printed error messages, contact your system administrator.
```

<div class="info" markdown="1">

To run this SQL statement, you must own the schema that contains the table or be a member of the `sysadmin fixed server` role, the `db_owner fixed database` role, or the `db_ddladmin fixed database` role.

</div>

To avoid reaching the identity value limit, you can reseed the BPT identity values in your tables.

### Reseed the BPT identity values

The following steps demonstrate how you can reseed the identity value for the `ossys_BPM_Activity` table to a negative value:

1. Run the following SQL statement in the OutSystems Platform Database.

    ```
    DBCC CHECKIDENT (ossys_BPM_Activity, RESEED, -2147483648);
    GO
    ```

1. Run the following SQL statement to verify the identity value has been reseeded.

    ```
    DBCC CHECKIDENT (ossys_BPM_Activity, NORESEED);
    GO
    ```

1. Repeat steps 1 and 2 for the `ossys_BPM_Process` table if required.

## Oracle - Restart sequence values for BPT tables

To check the current sequence values for your BPT tables, you can run the following SQL statement:

```
SELECT OSADMIN.<!--sequence_name>.nextval FROM dual;
```

<div class="info" markdown="1">

This command will consume a value in the sequence used.

To run this SQL statement, you must have the `SELECT` privilege on the sequence or have the DBA privilege on the database

</div>

To avoid reaching the identity value limit, you can restart the BPT identity values in your tables.

### Restart the BPT sequence values

The following steps demonstrate how you can restart the sequence value for the sequence used by the `ossys_BPM_Activity` table to a negative value:

1. Run the following SQL statement in the OutSystems Platform Database.

    <div class="info" markdown="1">

    To run this SQL statement, you must have the `ALTER` object privilege on the sequence or the `ALTER ANY SEQUENCE` system privilege

    </div>

    ```
    --Specify RESTART to reset NEXTVAL to MINVALUE
    ALTER SEQUENCE OSADMIN.OSSEQ_BPM_ACTIVITY MINVALUE -2147483648 RESTART;
    ```

1. Run the following SQL statement to verify the identity value has been reseeded.

    ```
    SELECT OSADMIN.OSSEQ_BPM_ACTIVITY.nextval FROM dual;
    ```

1. Repeat steps 1 and 2 for the `OSSEC_BPM_PROCESS` sequence used by the `ossys_BPM_Process` table if required.
