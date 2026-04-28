---
guid: e2a036eb-866c-4e34-aff6-d8980255a2af
locale: en-us
summary: Understand the database operations required for data interoperability with a O11 self-managed infrastructure.
figma:
coverage-type:
  - understand
  - apply
topic:
app_type: mobile apps,reactive web apps
platform-version: o11
audience:
  - Tech lead
  - Platform administrator
tags: entities,data interoperability
outsystems-tools:
  - none
helpids:
isautopublish: true
---

# Data interoperability for O11 self-managed infrastructures

Data interoperability from ODC to an O11 self-managed infrastructure requires the manual execution of some database operations at specific moments:

* [Initial setup](#setup)
* [When entities are exposed or promoted](#on-expose)

These operations must be performed by a database administrator (DBA).

## Initial setup {#setup}

When setting up data interoperability for the first time, the following operations must be performed by a DBA **for each** [O11 environment mapped to an ODC stage](intro.md#mapping):

1. Create a dedicated database user for interoperability.

1. Grant the new database user **read access** to the following OutSystems 11 systems tables:

    * `ossys_application`
    * `ossys_app_definition_module`
    * `ossys_entity`
    * `ossys_entity_attr`
    * `ossys_entity_extra_metadata`
    * `ossys_entity_view`
    * `ossys_espace`
    * `ossys_module`

1. Grant the new database user **read access** to the following systems tables specific for your database type:

    * For SQL Server:

        * `sys.columns`
        * `sys.foreign_keys`
        * `sys.foreign_key_columns`
        * `sys.index_columns`
        * `sys.key_constraints`
        * `sys.objects`
        * `sys.schemas`
        * `sys.tables`
        * `sys.types`

    * For Oracle:

        * `all_cons_columns`
        * `all_constraints`
        * `all_tab_cols`
        * `all_tab_columns`
        * `all_types`

## On exposing or promoting O11 entities {#on-expose}

Every time developers [expose an entity in the baseline environment](expose-entities.md#expose) using the O11 LifeTime console, OutSystems creates a new **database view** on the O11 baseline environment. The same way, every time developers [promote an exposed O11 entity to other O11 environment](expose-entities.md#promote), OutSystems creates a new database view on that O11 environment.

When this happens, a DBA must grant the dedicated database user access to these views, as described in the sections below.

### Granting access for exposed application entities {#app-entities}

When O11 application entities are exposed or promoted, the following operations must be performed by a DBA in that O11 environment:

1. Grant the dedicated interoperability database user **read and write** access to the new **database views**, one for each exposed or promoted entity:

    * `OSUSR_VIEW_<entity_name>`, or `OSUSR_VIEW_<custom_view_name>` if the view name was renamed [when the entity was exposed](expose-entities.md#expose).

1. Grant the dedicated interoperability database user **read and write** access to the corresponding **tables**, one for each exposed or promoted entity:

    * `osusr_<entity_name>`

<div class="info" markdown="1">

No manual actions are required when:

* Attributes are added, removed, or renamed in an exposed O11 entity.
* An O11 entity stops being exposed. The corresponding database view is removed automatically.

</div>

### Granting access for exposed system entities {#sys-entities}

The O11 system entities **User** and **Tenant** are [exposed to ODC by default](expose-entities.md#user-tenant) as **read-only**.

If developers want to use these entities in ODC apps, the following operations must be performed by a DBA in the O11 environments mapped by the [ODC data connection](configure-connection.md#create-connection):

1. Grant the dedicated interoperability database user **read** access to the **database view** created for the O11 system entity:

    * User: `OSSYS_VIEW_USER`
    * Tenant: `OSSYS_VIEW_TENANT`

1. Grant the dedicated interoperability database user **read** access to the corresponding O11 system entity **table**:

    * User: `OSSYS_USER`
    * Tenant: `OSSYS_TENANT`
