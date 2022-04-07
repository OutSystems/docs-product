---
locale: en-us
guid: cf34b4c6-2dc9-4ea3-82d0-f77dcc9f68ca
---

# Entity Editor

The Entity Editor allows you to edit the [properties](<../element-property/entity.md>) of an entity that belongs to your extension.

This editor is displayed when an entity is selected in the [Multi-tree Navigator](<../multi-tree-navigator.md>) or in the [Multi-tab Editor](<../multi-tab-editors.md>).

## Set the Entity Identifier

The identifier is the attribute that uniquely identifies the rows of your entity.

To set the entity identifier, do one of the following:

* In the **Entity editor**, edit the Identifier property and select the attribute you want from the drop-down list;

* In the **Attributes table**, right-click on the attribute you want and select the Set as Identifier ![](images/identifier.gif) option.

## Entity Attributes

To manage entity attributes, see [Attributes Editor](<attributes.md>).

## Change the Entity Properties

You can change the properties of the entity at any time. Simply double-click in the entity in the [Multi-tree navigator](<../multi-tree-navigator.md>) or select the action in the [Multi-tab editor](<../workspace.md>).

## Import Details

This button is enabled when this entity is [imported from a database](<../../../extensibility-and-integration/integration-studio/managing-extensions/entity-import-from-database.md>), and displays a report where you can check the original table definition and the corresponding entity definition. The following information is displayed:

* **Entity**: Name of the entity and its status with the following syntax:

    `Entity <entity_name>: <entity_status>`

* **Database Connection**: Name of the database connection and its Database Management System (DBMS). If the entity is imported without using a Database Connection this line is omitted. The syntax is as follows: 

    `Database Connection <Database_Connection_Name> ( <DBMS> )`

* **Physical Table Name**: Indicates the full name of the physical table associated with this entity.

* **Identifier**: Name of the attribute that corresponds to the Primary Key, if any.

* **Attributes**: Attributes of the entity created by the wizard. The Attribute syntax is as follows:

    `<attribute_name> ( <OutSystems_data_type> <- <database_data_type> ): <attribute_status>`
