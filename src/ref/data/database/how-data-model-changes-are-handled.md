---
tags: support-Database
---

# How Data Model Changes are Handled

When changing the data model of your applications, the changes are not immediately reflected in the database. This only happens when you deploy the application, and is done in a way that ensures no data is lost.

<div class="info" markdown="1">

If you cut and paste an Entity in Service Studio, it will generate new keys which in turn creates a new table in the database. This means that if the Entity has data in the database, that data will be lost in the pasted Entity.

</div>

This topic explains how OutSystems handles the following:

* Deleting an Entity or Attribute
* Adding an Entity or Attribute
* Renaming an Entity or Attribute
* Changing the data type of an Attribute
* Changing the Length property of a Text Attribute

## Deleting an Entity or Attribute

When deleting an Entity or Attribute, OutSystems removes it from your application model, but not from the database. The consequence is that you’ll no longer be able to use that Entity or Attribute in the development environment.

Nonetheless, the data is still safely stored on the database. You can access it directly in the database or by rolling back your application.

After deleting an Attribute, OutSystems warns you that the database has more columns than your Entity. Learn more about the [Database Integrity Suggestion](<../../errors-and-warnings/warnings/database-integrity-suggestion-warning.md>).

The association of entities and attributes can be found in the System reference. The Entity reference provides a map between the OutSystems entity name and the database's physical table name. The `Entity` and `Entity_Attr` entities contain a reference to both the active and deleted entities and attributes.

## Adding an Entity or Attribute

When you add an Entity, OutSystems creates a new table in the database.

When you add an Attribute to an Entity, OutSystems checks the database to see if a column with the same name already exists in the associated table. If there is no such column, OutSystems will create it.

If the Entity previously had an Attribute with the same name but you deleted it at some point in time, OutSystems kept the associated database column and data. In this case, OutSystems tries to reuse the existing database column. If the data type of the new attribute is different than the one that exists on the database, OutSystems converts it when deploying the application:

* If it’s possible to convert the data type without losing data, the deployment is successful.
* If it’s not possible to convert the data type, OutSystems displays an error and does not publish the application. This ensures that your data is always safe. 

Check the [Changing the Data Type of an Attribute](<#changing-the-data-type-of-an-attribute>) section to learn more.

## Renaming an Entity or Attribute

If you rename an Entity, OutSystems renames the association in the database but the phyiscal name stays the same. The table with all its data remains in the database untouched.

If you rename an Attribute, OutSystems creates a new column with the new name in the database. The old column with all its data remains in the database untouched, but it won’t be available in the development environment.

If there’s already a column with the same name in the database, OutSystems will try to map the attribute to the existing database column. OutSystems tries to convert the column data type if necessary.

## Changing the Data Type of an Attribute

If there is data stored in the database table, OutSystems tries to convert the values into the new data type. If the conversion is not possible or would cause data loss, no change is made and OutSystems displays the Database Upgrade Error.

Since the conversion is done by the database management system you are using, you need to check its documentation to see the supported type conversions.

## Changing the Length Property of a Text Attribute

OutSystems uses two different data types to store strings in the database. The data type used depends on the string size. Learn more about the [Database Data Types](<database-data-types.md>).

When changing the length of a Text attribute from less than 2000 characters to more than 2000 characters, the data type of the column in the database is changed.

You cannot change the length from more than 2000 to less than 2000 characters. OutSystems gives you an error when you try to deploy this modification, and doesn’t change your application, since it would cause data loss.
