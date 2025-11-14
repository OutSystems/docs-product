---
summary: Learn data model performance optimization techniques for OutSystems 11 (O11), including indexing, data isolation, and archiving.
guid: 22ab786d-afc3-4ac2-aa9b-d3ea7df7292b
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: data modeling, performance optimization, database indexing, application design, query optimization
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - backend developers
  - architects
outsystems-tools:
  - service studio
coverage-type:
  - evaluate
---

# Performance best practices for data modeling

The best practices below focus on the data tier of the applications where it is absolutely critical for application performance. Don’t jeopardize performance during the design phase as it may be too costly when best practices are applied late in the development stage.

## Index your Entities

### Description

Create indexes for the most commonly used attributes to improve the overall query speed. However, be aware that indexes cause inserts and updates to take longer.

### Solution

Identify all attributes that are used in query conditions and join expressions in your slower queries. These are the best candidates to be indexed.

The overall performance improvement of the query will differ significantly depending on the attribute data type and if it's indexed or not. Indexing the most sparse attribute values, like dates or small texts, will provide greater performance improvement, then say, a Boolean attribute. This will always depend on the query itself, and how sparse the data is on the entity

### Importance

When queries over large table are taking too long, database indexes will allow a faster access to the data in that table, since the database engine won't need to search the table data pages for the queried values. Instead, it will use a smaller subset of pages, the index pages, which are organized in a specific order, improving the search through sorting algorithms.

You should have an index for every attribute that is commonly queried in a specific entity, and sometimes indexes over a commonly queried groups of attributes in the same table. However, consider that the higher the number of indexes in a table, the longer operations like insert and update will take since these indexes will be automatically updated, thus causing slow performance in these operations. The point is to identify the best compromise between the select and insert/update statements and the number of indexes.

### Remarks

For indexes, column orders are important, so try to always use the same order in queries. For queries that use several columns to be filtered, composite indexes can be created.

## Isolate large text and binary data

### Description

Avoid text attributes with more than 2000 characters. Store binary and large text attributes in their respective separate entities.

### Solution

Reduce Text Attribute length to the minimum possible value. Avoid text attributes with lengths greater than 2000. Service Studio text attributes with length less than or equal to 2000 are created as VarChar columns in SQL Server; otherwise they are created as Text columns.

Isolate Binary Data Attributes in separate Entities.

### Importance

Updating entities that have large texts or binary data attributes is very slow. Having text attributes with more than 2000 characters will be mapped to binary data types in the database and usually binary data types tend to take longer to be changed/updated than simple data types. Additionally, updating a record which has a binary data type will take longer than a record with simple data types because data pages will need to be moved for the binary data type. It is best to avoid having binary data types in entities that change frequently. If this cannot be avoided, isolate them in their own entity.

### Remarks

When designing the data model, grouping and aggregating values will reduce the amount of requests/transactions to obtain the high level searches/reports.

## Beware of Large Excel Files Performance

### Description

When handling large Excel files consider recording the data in an entity and using a timer to process the data in background.

### Solution

If the number of lines to be uploaded is not fixed, then you should ensure that your application is capable of loading 65536 records, the maximum number of records Excel allows (Note: MS Office / Excel 2007 has a limit of 1 Million rows). Additionally, in a worst case scenario, Excel doesn't take more than two minutes to load, keeping in mind that table inserts will be progressively slower with table growth.

The safest way to go is to use a temporary table where you insert the Excel binary info as is and then wake up a timer that will asynchronously process it.

### Importance

By isolating the data processing from the data uploading you avoid the request timeout limit. Also, since the processing will be done in background as a batch processing job, it can comply with other best practices like running on an isolated server, allowing for retries, performing error handling, commits per line, etc.

### Remarks

The process mentioned above is not necessary for excel files used for bootstrapping an application.

## Use of the Delete Rules constraints in Entities

### Description

Whenever possible set Reference Attributes Delete Rule to Ignore instead of Delete.

This is an advanced scenario that must be used with care, since it may cause data inconsistency which can result in serious issues in your application.

### Solution

This best practice applies to applications where the data is effectively deleted from the database and when this happens to entities which other entities depend on. One of three scenarios is possible:

1. Use the Protect rule, which means that your application must be delete all records from child entities first (or the database will return an error) and then when you delete the parent entity record, the database has to check if there are records in the child entities (which is unnecessary or will return an error). This is the worst option in terms of performance.

1. Use the Delete rule, which means that all control is given to the database (which has no business knowledge) and may be trying to delete things that were already deleted.

1. Use the Ignore rule, which may lead to data inconsistency if your application is not working correctly, but is the more performant option by far. If you use this option, it's fundamental that you have a housekeeping strategy on your DB to assure that you get rid of all unindexed data.

### Importance

The Protect and Delete options in the Reference Attributes Delete Rule of entities will trigger multiple actions on its referenced data model. This causes database overhead and takes a lot longer to delete records. This happens because a delete rule of an entity record will cause a select or a delete statement for every record in other tables that link to that record through a foreign key constraint. Using the ignore rule in complex data models is the best choice since these delete statements won't be executed but will require manual identification of the records to be deleted in other referenced entities.

### Remarks

As this may lead to data inconsistency, this best practice regarded as suspicious by many developers who would rather use the protect rule. But in fact while the ignore rule leads to data inconsistency when the application is not deleting all that it should, the protect rule will lead to a database error which while being easier to detect, results in an equally bad end user experience. During the development and testing stages, temporarily setting the constraint to protect could help protect against development errors. Once development and testing are completed, setting the constraint to ignore and adding reminders where the deletes are placed and stating which rules should be revert back to protect during testing are practices that should minimize the risk of data inconsistency.

## Archive old data in separate entities

### Description

You should consider using a separate entity to archive old data when: (a) old data needs to be kept for logging reasons or legal reasons but is not accessible from anywhere in the application; (b) when there is a table with a high growth rate where a small percentage of the data is heavily used and the rest of the data is used just as an archive that is rarely accessed. Consider also developing a separate screen to view the archived data or use a union or a view in a query that is rarely used that allows seeing the data from both tables.

### Solution

Forget about the database script that cleans old records from tables to be executed manually every year because no one will remember. Those activities should be automated and included in the application. If there are tables with historical data like orders or operations, it’s better to have an archive table and have a daily timer to copy the records older than some time from the primary table to the archive table. The same applies to data that are rarely accessed in tables with high growth rate where a small percentage of the data is crucial and the rest is just archive.

### Importance

Old data is dead weight in the tables; it slows down all operations done over the table data; and more often than not, old data is used at the most only 1% of the time.

### Remarks

The timing for when to archive the old data to a separate entity should be well thought out because archiving things too soon can result in having many accesses to the archived data and may result in negative performance gains. [See more details about Data archiving.](../archive.md)
