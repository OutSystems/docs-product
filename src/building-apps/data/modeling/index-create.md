---
summary: Learn how to create and manage database indexes in OutSystems 11 (O11) to enhance search performance and enforce attribute uniqueness.
tags: database management, entity modeling, performance optimization, application development, data uniqueness
locale: en-us
guid: 0611c8e9-7cba-4812-8495-88165c39e20e
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=159:21
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
topic:
  - indexes
---

# Create an Entity Index
  
You can define a database index in your data model to enforce uniqueness of table attributes across multiple rows or to make searches quicker using those attributes as filters. In OutSystems, you can model a database index in the entity element.
Note that adding several indexes to Entities can impact negatively the performance of the database operations, namely write operations.

<div class="info" markdown="1">

See [Database Indexes](<../../../ref/data/database/database-indexes.md>) for more information about creating database indexes.

</div>

To create an index for an entity:

1. Right-click the Entity and select **Edit Entity**, or click the **Indexes and more** button in the Entity properties.

    ![Screenshot of the Edit Entity dialog in OutSystems with the Indexes and more button highlighted](images/create-database-index-edit-entity-ss.png "Edit Entity Dialog")

1. Click the **New index** button to create an index.

1. Enter a name for the index.
    In this example, **OrderProductUnique** is added.

1. If you want this index to be restricted to restrict records only, change the **Unique** property to **Yes**.

    ![Screenshot showing the Unique property toggle set to Yes for a new index in OutSystems](images/change-unique-property-ss.png "Unique Property Toggle")

1. Add the attributes you want to include in the index.

    ![Screenshot of adding attributes to a new index in the OutSystems platform](images/add-index-attributes-ss.png "Adding Index Attributes")

1. Click **Close**.

1. To apply the index created in the database, publish the module.

    During the publishing process, OutSystems creates the corresponding database index as defined in the Entity properties.
