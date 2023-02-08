---
summary: Learn how to create an Entity Index to ensure uniqueness and improve findability.
tags: support-application_development; support-Database; support-webapps
locale: en-us
guid: 0611c8e9-7cba-4812-8495-88165c39e20e
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Create an Entity Index
  
You can define a database index in your data model to enforce uniqueness of table attributes across multiple rows or to make searches quicker using those attributes as filters. In OutSystems, you can model a database index in the entity element.

<div class="info" markdown="1">

See [Database Indexes](<../../../ref/data/database/database-indexes.md>) for more information about creating database indexes.

</div>

To create an index for an entity:

1. Right-click the Entity and select **Edit Entity**, or click the **Indexes and more** button in the Entity properties.

    ![Edit Entity](images/create-database-index-edit-entity-ss.png)

1. Click the **New index** button to create an index.

1. Enter a name for the index.
    In this example, **OrderProductUnique** is added.

1. If you want this index to be restricted to restrict records only, change the **Unique** property to **Yes**.

    ![Unique property](images/change-unique-property-ss.png)

1. Add the attributes you want to include in the index.

    ![Add Index Attribute](images/add-index-attributes-ss.png)

1. Click **Close**.

1. To apply the index created in the database, publish the module.

    During the publishing process, OutSystems creates the corresponding database index as defined in the Entity properties.
