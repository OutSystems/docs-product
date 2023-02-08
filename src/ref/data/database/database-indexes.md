---
summary: Information for database administrators about database indexes. A preferred way of creating a database index is through Service Studio. You can also create them through SQL, but note that the OSIDX is a reserved prefix for the managed indexes.
tags: support-Database
locale: en-us
guid: d1757e12-d324-45d9-b019-992a4547af24
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Database Indexes

<div class="warning" markdown="1">

We recommend that you don’t add indexes directly to the database. Outsystems only manages its own indexes automatically, and not the ones you create directly in the database. However, if you decide to create an index manually, remember to manually recreate that index when you migrate the application or perform a significant change to its Entity.

</div>

When a developer creates a foreign key in Service Studio, with the delete rule set to **Protect** or **Delete**, the platform automatically creates an index. In the database, this index has the `OSIDX` prefix. The platform deletes the automatically created indexes when you set **Delete Rule** to **Ignore**.

<div class="warning" markdown="1">

The platform manages all indexes starting with `OSIDX_`. You shouldn't create or edit indexes starting with `OSIDX_`, as any custom changes are discarded. Additionally, you may impact the correct functioning of the apps.

</div>

## Create indexes in Service Studio

Developers can define custom indexes in Service Studio to improve the performance of the apps. Creating new indexes in Service Studio is the preferred way of creating database indexes.

<div class="info" markdown="1">

See [Create an Entity Index](<../../../develop/data/modeling/index-create.md>) for instructions about creating indexes in Service Studio.

</div>

## Create indexes through SQL

If you're creating indexes through SQL interface, make sure you **give them a custom prefix**. Here are some examples of queries.

`CREATE UNIQUE INDEX MYINDEX_<internal name> ON <Entity>(<attributes>)`

`CREATE INDEX MYINDEX_<internal name> ON <Entity>(<attributes>)`

Note: If you are using an Oracle database, you can define the Indexes tablespace in the **Configuration Tool**.
