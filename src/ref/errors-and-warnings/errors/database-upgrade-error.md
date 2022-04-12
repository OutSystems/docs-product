---
locale: en-us
guid: 3bb08332-800d-426b-bdf2-2de08f859c9b
---

# Database Upgrade Error

The `Database Upgrade` error is issued in the following situations:

* `Failed to convert site property <site property> from data type <type> to data type <type>` in Platform Server 11.11.0 and earlier, or:

* `The database upgrade has failed because site property <site property> type was changed from data type <type> to data type <type> after publishing. If you want to change it, please delete the site property <site property> first and then create a new site property with a different type.` in Platform Server 11.12.0 and later

    You are trying to change the data type of a Site Property and this conversion is not supported by the database. This situation only occurs if the module has been published with this Site Property and if the data types are not compatible.

* `Could not find database column for <attribute> attribute`
  
    Attribute `<attribute>` was deleted or changed directly in the database and the entity definition does not match the table as defined in the database.
  
    Do one of the following:
    
    * Delete the attribute from your entity definition.
    * Add the column to the database table as specified in your module.

* `Could not create/change primary key in <table> table. Inconsistent database table and entity primary key definitions`
  
     You are trying to change the primary key of the entity that corresponds to `<table>` table but it is not possible due to database constraints. Suppose, for example, that the attribute you are trying to set as the primary key has duplicate values. Edit the entity and change the primary key to a suitable attribute.

    Do one of the following:

    * Delete the attribute from your entity definition.
    * Add the column to the database table as specified in your module.

* `A single tenant entity cannot be upgraded to a multi-tenant entity after it has been created in the database (Entity <entity>, database table <table>)`
  
    You are trying to upgrade a single-tenant entity to a multi-tenant entity, after creating the corresponding table in the database.

* `Could not change the <attribute_name> attribute from <old_type> to <new_type>, since existing records could not be converted to <new_type>. Either rename <attribute_name> (data will remain in the database, but not accessible from your application) or create a procedure that handles the records with values that cannot be converted. Press F1 for more information`
  
    You are trying to change the type of an attribute, but it already contains data that cannot be automatically converted to the new data type.

    Do one of the following:

    a) Rename the attribute. If you rename the attribute after this error,  OutSystems creates a new empty column for you in the database table, and starts using this new column instead of the old one. It still keeps the old column and its data in the table, but it won't be visible in the development environment. You can retrieve the old data using direct access to the database using a script, for example.

    b) Alternatively, you can create a timer that is executed one time, when publishing the application, to move or delete the records that are not allowing the conversion.

    Don't forget to apply the same solution after deploying your application to another environment.

If the error you have got does not match any of these situations, please check with your Database Administrator for what might be the cause.
