---
summary: Learn how to create an Entity Index to ensure uniqueness and improve findability.
tags: support-application_development; support-Database; support-webapps
locale: en-us
guid: 0611c8e9-7cba-4812-8495-88165c39e20e
app_type: traditional web apps, mobile apps, reactive web apps
---

# Create an Entity Index
  
You can define a database index in your data model to enforce uniqueness of table attributes across multiple rows or to make searches quicker using those attributes as filters. In OutSystems, you can model a database index in the entity element.

To create an index for an entity:

1. Open the entity by double-clicking on it or selecting the Indexes property.
1. Go to the Indexes tab and create a new index.
1. Add the attributes you want to include in the index.
1. If you want to have unique values for the selected attributes, set the  Unique property to `Yes`.
1. To apply the index created in the database, publish the application.


## Example

This example is based on a simple app that manages customers and orders. 

1. Double-click the **OrderProduct** entity.

1. Open the Review entity by right-clicking on the entity and then **Edit Entity**.

1. On the **Indexes** tab, add a new index by clicking **New** and set the **Name** property.

    In this example, the **Name** property is set to `UniqueProductPerOrder`

1. Set the **Unique** property to **Yes**.

    This ensures the index is unique.

1. From the **(AddAttributes)** dropdown, select the attributes you want to add to the index. 

    In this example, the following are added:

    * OrderId
    * ProductId
    
    This ensures that the same value for these attributes cannot be repeated in other records of **OrderProduct** table.

1. Publish the module. While publishing, OutSystems creates the index in the database. 

Now, when a user tries to add the same product to an order more than once, OutSystems raises a database exception.
