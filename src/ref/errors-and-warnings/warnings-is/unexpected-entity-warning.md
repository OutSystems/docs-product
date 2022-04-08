---
locale: en-us
guid: 8af78fca-1b14-4d21-a4c6-560929c22322
---

# Unexpected Entity Warning

Message
:   `<entity> should not be exclusively composed of an 'Auto Number' attribute.`

Cause
:   You have an entity with just one sequential attribute and this situation is not allowed by some of databases supported by OutSystems.

Recommendation
:   Depending on your requirements, either add a new attribute to your entity; or un-check the Auto Number property. Learn more about [entity attributes](<../../../extensibility-and-integration/integration-studio/managing-extensions/entity-attribute.md>).

---

Message
:   `<entity> should only have one attribute of 'Binary Data' data type.`

Cause
:   Your entity has more than one Binary data attributes and this situation is not supported by the database.

Recommendation
:   Depending on your requirements, either change the data type of one of these attributes or [create](<../../../extensibility-and-integration/integration-studio/managing-extensions/entity-add.md>) a new entity and move one of these attributes to this new entity.

---

Message
:   `<table> is an invalid table name in <database>.`
  
Cause
:   The physical table name you specified has an invalid table for SQL Server and/or Oracle databases.

Recommendation
:   [Edit this entity](<../../../extensibility-and-integration/integration-studio/managing-extensions/entity-add.md>) and specify the Table Name property. 
