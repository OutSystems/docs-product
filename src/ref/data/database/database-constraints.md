---
tags: support-Database
locale: en-us
guid: dcf4b1f6-3561-4cf7-b2ee-4b0caca4130b
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Database Constraints

When defining your entities, you can specify their Identifiers and the relationships they have with other entities of your eSpace, through Reference Attributes.

In database terminology, the Identifier of an entity corresponds to its Primary Key and the Reference Attributes correspond to Foreign keys. OutSystems automatically creates the necessary database constraints as explained below.

## Primary Key

When you define an attribute as an Identifier, the database creates a Primary Key constraint, prefixed as `OSPRK`, as presented below.

### SQL Server

`CONSTRAINT OSPRK_<internal name> PRIMARY KEY CLUSTERED (<attribute>)`

### Oracle

`CONSTRAINT OSPRK_<internal name> PRIMARY KEY (<attribute>)`

## Foreign Keys

Only attributes where the Delete Rule property is set to Protected or Delete create a Foreign key database constraint. These constraints, prefixed as `OSFRK`, depend on this Delete Rule property, as explained below.

### Protected

`CONSTRAINT OSFRK_<internal name> FOREIGN KEY (<reference attribute>) REFERENCES <Entity>(<attribute>)`

### Delete

`CONSTRAINT OSFRK_<internal name> FOREIGN KEY (<reference attribute>) REFERENCES <Entity>(<attribute>) ON DELETE CASCADE`
