---
summary: OutSystems 11 (O11) supports creating one-to-many relationships between entities using foreign keys.
tags: entity relationships, data modeling, foreign keys, entity diagrams, deletion rules
locale: en-us
guid: b6ccd0f3-6d0c-4628-bb6a-b9c9e40bc3a0
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=159:9
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - understand
  - apply
---

# Create a One-to-Many Relationship

When modeling data, it is sometimes necessary to create one-to-many relationships between entities. For instance, a `Place` (parent entity) can have many `Reviews` (child entity). This is typically implemented with a foreign key - the identifier of the parent record - in the child records.

To create a one-to-many relationship between two entities:

1. Select the entity with the child records (e.g. `Review`).
1. Add a new attribute that holds the identifier of the parent entity (e.g. identifier of the `Place` entity). This attribute will be the foreign key.

Having an identifier attribute pointing to another entity automatically creates a relationship. You can see the relationships between entities if you have them in the same Entity Diagram.

![Diagram illustrating a one-to-many relationship between Place and Review entities with a foreign key](images/one-to-many-relationship-1.png "Entity Diagram Showing One-to-Many Relationship")

When you create relationships between entities in your module, you must define the referential integrity you want to use when deleting records. For more information on deletion rules, see [Delete Rules](delete-rules.md)