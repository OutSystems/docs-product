---
tags: 
summary: 
locale: en-us
guid: 9508496b-0e5a-4373-a0df-1c3dba6e9f5b
app_type: traditional web apps, mobile apps, reactive web apps
---

# Optimize data preparation

Data preparation for a screen should be very efficient. This ensures a pleasant experience for the user. 

Data preparation is usually inefficient when:

  1. The Data Model doesn't support the use case of the screen - for example, it is necessary to group large volume of data by complex criteria to get averages, counts and alikes, or values must be calculated on the fly for each listed record.

  2. Aggregates and loops used instead of lean SQL queries. For example, instead of a single SQL query to combine all the information, a simple aggregate is used to retrieve the data from the master entity. Then, an aggregate inside a loop collects the details for each row to be appended to a record list.

## Impact

Long preparations to get the required information, many queries and calculations, and overuse of loops, results in considerable Web Server and Database Server load.

## Best practices

* Know your data requirements and design a DB model to contain all required information to support your screens, without having to calculate the information on each screen request.
* This requires all the calculations to be made in advance:

    * When data is generated - for example, every time you add a vacation period, immediately update the remaining available days in the employee detail instead of calculating it when you want to list the available vacation days per employee.

    * In asynchronous jobs (Timers or BPT with automatic activities) to prepare data upfront - for example, prepare agglomeration tables to support dashboards.

* Use proper joins and SQL functions to gather all required data in a single query.

* Make decisions in the preparation to get data with different queries, instead of making decisions on the screen to call different expressions with different queries.

* Create different specialized screens, instead of a power screen with inefficient data preparation that needs to cope with all situations.
