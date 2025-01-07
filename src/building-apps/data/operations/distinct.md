---
summary: OutSystems 11 (O11) enables the extraction of distinct values from database tables by using aggregates with grouped columns.
tags: database operations, data aggregation, entity modeling, data manipulation, aggregate functions
locale: en-us
guid: 4ceecc67-9976-48c7-bcdb-fa895a141d81
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=174:7
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - understand
  - apply
---

# Get Distinct Values from the Database

Database tables may have columns containing repeated values. There are situations when you only want to get the distinct values, instead of all the data including the repetitions. To obtain distinct values of entity attributes, you can use an aggregate with grouped columns.

To get distinct values of an entity attribute:

1. In an aggregate in the action flow, add the entity.

1. Right-click on the attribute for which you want to obtain distinct values, and choose to group by the attribute.

![Screenshot showing how to group by a single attribute in an aggregate to get distinct values](images/distinct.png "Grouping by a Single Attribute")

The aggregate only outputs the attribute values that are grouped.

To get distinct values using multiple entity attributes, select all the required attributes and choose to `Group by selected attributes`.

![Screenshot demonstrating grouping by multiple attributes in an aggregate for distinct values](images/distinct-2.png "Grouping by Multiple Attributes")
