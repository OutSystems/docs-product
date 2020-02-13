# Database Integrity Suggestion Warning

Message
:   `Inconsistent database table and entity definitions: Column <table>.<column> exists in database, but there is no corresponding attribute in entity '<entity>'`

Cause
:   The entity definition, in your module, does not include the attribute associated with `<column>`. You deleted this attribute from entity, but OutSystems kept the corresponding column in the table. This inconsistency only occurs if the module has been published with the previous entity definition.

Recommendation
:   Do one of the following:

    * Drop column from the table, in the database, and publish the module again;
    * Add a new attribute to entity with the same name as column;
    * Ignore the warning.

---

Message
:   `Inconsistent database table and entity definitions: 'Binary Data' column <table>.<column> exists in database, but there is no corresponding attribute in entity '<entity>'`

Cause
:   The entity definition, in your module, does not include the attribute associated with column. You deleted this attribute from entity, but OutSystems kept the corresponding column in the table. This inconsistency only occurs if the module has been published with the previous entity definition.

Recommendation
:   Do one of the following:

    * Drop column from the table, in the database, and publish the module again;
    * Add a new attribute to entity with the same name as column. In this situation, it is advisable that you don't ignore the warning to prevent runtime errors.

---

Message
:   `Inconsistent database table and entity definitions: 'Auto Number' column <table>.<column> exists in database, but there is no corresponding attribute in entity '<entity>'`

Cause
:   The entity definition, in your module, does not include the attribute associated with column. You deleted this attribute from entity, but OutSystems kept the corresponding column in the table. This inconsistency only occurs if the module has been published with the previous entity definition.

Recommendation
:   Do one of the following:

    * Drop column from the table, in the database, and publish the module again;
    * Add a new attribute to entity with the same name as column. In this situation, it is advisable that you don't ignore the warning otherwise you won't be able to create another auto number attribute, since only one is allowed by the database.

---

Message
:   `Column <entity>.<column> exist in the database with unknown / unsupported data type: <type>`

Cause
:   You have an attribute with an unknown or unsupported data type.
   
---

Message
:   `The table name of <entity> entity is not supported. You should change it, in the database, in order to prevent runtime errors`

Cause
:   The physical table name of `<entity>` is not supported. This situation occurs if, for example, changes are made directly in the database and therefore the table name does not have the `OS*_` prefix.
