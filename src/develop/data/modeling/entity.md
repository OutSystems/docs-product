---
summary: Learn about Entities in OutSystems.
locale: en-us
guid: 5a13a09e-6e8f-40b2-8ca3-eb7af13e3b40
app_type: traditional web apps, mobile apps, reactive web apps
---

# Entities

Entities are elements that allow you to persist information in the database and to implement your database model. You can think of them as database tables or views. 

An Entity is defined through Entity Attributes that store the information related to it. Examples of entity attributes are: Name, Address, Zip Code, City and so on.

## Primary Key

In OutSystems, a primary key is called Entity Identifier.

When an Entity is created, an attribute called Id is automatically added as Entity Identifier. By default, it is of data type Long Integer and its value is automatically calculated in sequence (an AutoNumber in OutSystems). This way, you don't have to implement any specific logic to uniquely identify each entity record. 

You can use other data types as Entity Identifiers or switch off the AutoNumber in an attribute. In these cases, you have to implement the logic to uniquely identify each entity record.

To set another attribute as Entity Identifier simply go to that attribute, right-click and set it as identifier.

In OutSystems, it is not possible to have composite keys because only one attribute can be the Entity Identifier. But you can use indexes to create alternate keys (see more below about indexes).

## Sequential Attributes

Sequential attributes are useful for Entity Identifier attributes. It is an easy way to ensure that each record has a unique primary key. 

When creating new records in the database with Entity Actions, the platform automatically calculates a new sequential and unique value. 

There can be only one sequential attribute per Entity.

## Indexes

Like in relational databases, OutSystems provides indexes for faster access to data in the entity. If you usually search or sort by one or more attributes of the entity, you can create an index based on those attributes to make it faster.

Indexes can also be used to create alternate and composite keys. 

When creating an index there is always a relevant trade-off between fetching and inserting data as it may bring some overhead to the latter.

## Impacts when Changing Entities

When you create a new entity attribute, the platform automatically manages the update of all records stored in the database for you. The new attribute is added to the records and set with the default value for its data type.

When you set an entity attribute as mandatory it is automatically validated on the user interface by the platform. However, in the database, mandatory attributes are created allowing null values thus, at the database level there's no validation for mandatory attributes.

When you delete an entity or an entity attribute, the platform is permissive and lets you do it whether it is being used or not, but you must fix the elements where it is being used. In the database, the entity or entity attribute is not deleted by the platform.

## Convert an entity to a static entity

To convert an existing entity to a static entity right-click the entity and select **Convert to Static Entity** from the **Advanced** menu.

After converting an entity to a static entity the records from the database can be imported as static records. To import the database records, right-click the static entity, select **Edit Entity**, and then click the **Import from Database** button.

<div class="info" markdown="1">
To convert an existing static entity to an entity right-click the static entity and select **Convert to Entity** from the **Advanced** menu.
</div>

