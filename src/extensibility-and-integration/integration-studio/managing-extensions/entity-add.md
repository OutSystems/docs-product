---
locale: en-us
guid: 16186793-9357-420f-a833-2c5e0d3c47b5
---

# Add an Entity

You can manually [add an entity](<entity-define.md>) to your extension as explained below. Integration Studio also provides you the [Import Entities from Database wizard](<entity-import-from-database.md>), which, through introspection, allows you to add several entities with less effort.  

To create an entity do the following:

1. Right-click the **Entities** folder in the Multi-tree Navigator and select ![](images/entity.gif) **Add Entity**.

1. Specify the following properties:

    * **Name**: Name of the entity.
    * **Logical Database**: The external database logical name. This name is used in Service Center to map the entity to its physical database.
    * **Physical Table Name**: Physical table name.
    * **Identifier**: Attribute that uniquely identifies the entity rows.
    * **Description**: Description of the entity.
    * **Default Value behavior**: Define how the entity's attributes default values are stored in and retrieved from the database regarding being converted to `Null` or not. See [Entity Properties](<../../../ref/integration-studio/element-property/entity.md>) for more information.

1. Specify the **attributes** of the entity in the [Attributes Editor](<../../../ref/integration-studio/editor/attributes.md>).

![](images/tip.gif) The [Entity editor](<../../../ref/integration-studio/editor/entity.md>) allows you to later change the action properties.

Once the entities are defined and the extension is published on the Platform Server, the Service Studio developer must add a reference to these entities to [use them](<../extension-life-cycle/extension-use.md>) in the module.
