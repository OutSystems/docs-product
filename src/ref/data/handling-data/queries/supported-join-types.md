---
tags: ide usage, reactive web apps, tutorials for beginners, data modeling, aggregates, entity relationships, database queries
locale: en-us
guid: d2ac8884-a37b-423d-9655-b235291485cd
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=843:1507
summary: Explore the supported join types in OutSystems 11 (O11) for efficiently querying and combining data from multiple entities.
audience:
  - frontend developers
  - full stack developers
  - backend developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
topic:
  - joins
---

# Supported Join Types

Usually your data is not stored in a single Entity. So, when performing queries on the data, you need to combine the records that is stored in multiple Entities. This is also known as joining records from multiple Entities.

To do this, just drag the entities into your aggregate. They are automatically joined together, but you can always customize how they are combined in the **Sources** tab. There are four ways to join records from two entities:

* Only fetch records that have a match in both entities.
* Fetch all rows from the first entity, even if there are no matches on the second entity.
* Fetch rows from both entities.
* For each record in the first entity, match it with a record from the second entity.

In the examples below we will combine the following two entities:

![Screenshot of the original tables before joining in a database query](images/original-tables-ss.png "Original Tables")

## Only fetch records with a match

To only retrieve Issues that have an Engineer assigned, use **Only With**.

![Example screenshot showing the result of an 'Only With' join between two database tables](images/onlywith-example-ss.png "Only With Join Example")

Notice how Issues that have no Engineer assigned yet are not returned.

## Fetch all records from an entity, even if they don’t have a match

To retrieve all Issues regardless of whether they have an Engineer assigned to them, use **With or Without**.

In this join type the order of the Entities in the join condition makes a difference in the returned rows. The idea is to retrieve all records from the first entity, and combine the rows of the second entity to them. So if you swap the order of the Entities, you will get a different result.

![Screenshot illustrating the difference in results when using 'With or Without' join in different entity order](images/withorwithout-difference-ss.png "With or Without Join Difference")

Notice that for the Issues that have no Engineer assigned, the columns with the Engineer information contain the default values.

## Fetch rows from both entities

To fetch all Issues and all Engineers, even if there is no match between them, use **With**.

![Screenshot demonstrating the 'With' join type fetching rows from both entities regardless of matching](images/with-example-ss.png "With Join Example")

Notice that for Issues without an engineer assigned, the columns with the engineer information contain the default values.

For engineers that don’t have an issue assigned to them, the issue information contains the default values.

This option is specially useful for exporting data into third-party systems.

## Combine all records, ignore relationship

To combine each record from an entity with all records of a second entity (for example: to create a list that pairs each team with every adversary team), just make sure that there is no Join defined in the Sources tab.

To pair each team with their adversaries, add the Team entity twice to your aggregate.

![Screenshot showing the result of a cross join, combining each record from one entity with all records from another](images/crossjoin-example-ss.png "Cross Join Example")

Then filter the aggregate to ensure that a team is not paired up with itself.
