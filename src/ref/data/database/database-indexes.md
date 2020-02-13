---
tags: support-Database
---

# Database Indexes

When defining your entities, you can specify indexes, in addition to the ones automatically created by OutSystems.

## Automatic indexes

For each foreign key you create with its delete rule set to Protect or Delete, OutSystems automatically creates an index. On the database, this index is prefixed with `OSIDX`.

`CREATE INDEX OSIDX_<internal name> ON <Entity>(<reference attribute>)`

Automatic indexes are deleted if the attribute Delete Rule is changed to Ignore.

## Custom Indexes

You can define your own [indexes](<../../../develop/data/modeling/index-create.md>), improve the performance of your applications. When you create an index, OutSystems creates it on the database with the `OSIDX` prefix.

### Unique index

`CREATE UNIQUE INDEX OSIDX_<internal name> ON <Entity>(<attributes>)`

### Not Unique index

`CREATE INDEX OSIDX_<internal name> ON <Entity>(<attributes>)`

If you are using an Oracle database, you can define the Indexes tablespace in the Configuration Tool.
