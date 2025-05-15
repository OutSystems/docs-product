---
summary: Learn about adapting SQL queries after migrating from O11 to ODC.
locale: en-us
guid: 42375e2b-c9a9-4a53-a7a6-910481be7547
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
helpids: 30554
tags: sql query migration, database compatibility, postgresql, aurora postgresql, cloud migration
audience:
  - backend developers
  - full stack developers
outsystems-tools:
  - none
---
# Application with SQL Node

ODC supports two SQL syntaxes within SQL nodes, which are different from the SQL syntax used in OutSystems 11:

* In ODC, PostgreSQL syntax is used when the query includes only internal entities (created in ODC Studio) since apps use Aurora PostgreSQL as the platform database. In contrast, O11 supports SQL Server, Azure SQL Database, DB2, and Oracle as the platform database.

* In ODC, ANSI-92 syntax is used when the query includes external entities, or a mix of internal and external entities. 

These differences mean that after migrating your assets from O11 to ODC, you must review and potentially adapt all SQL queries to ensure compatibility with the ODC syntax.

## How to solve

You must solve this pattern in ODC, after proceeding with the code migration to ODC.

### Solve in ODC

In ODC, you must ensure that all SQL queries used in the migrated apps are compatible with Aurora PostgreSQL. Check each SQL node, and adapt each one depending on the data sources:

* If the SQL query includes only internal entities, check [SQL queries compared to OutSystems 11](https://success.outsystems.com/documentation/outsystems_developer_cloud/onboarding_developers/sql_queries_compared_to_outsystems_11/) to see the main differences in the SQL syntax.
* If the SQL query includes external entities, or a mix of internal and external entities, check [Understand ANSI-92 syntax in SQL nodes](https://www.outsystems.com/tk/redirect?g=4d569b71-1430-4801-96da-cce2e9984174) to see the main differences in the SQL syntax.
