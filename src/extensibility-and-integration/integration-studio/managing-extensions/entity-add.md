# Add an Entity

You can manually [add an entity](<entity-define.md>) to your extension as explained below. Integration Studio also provides you the [Import Entities from Database wizard](<entity-import-from-database.md>), which, through introspection, allows you to add several entities with less effort.  

To create an entity do the following:

1. Right-click on the Entities folder in the Multi-tree Navigator and select the ![](images/entity.gif) Add Entity option.

1. Specify the following properties:

    * **Name**: name of the entity.
    * **Logical Database**: the external database logical name. This name is used in Service Center to map the entity to its physical database.
    * **Physical Table Name**: physical table name.
    * **Identifier**: attribute that uniquely identifies the entity rows.
    * **Description**: description of the entity.
    * **Default Value behavior**: define how the entity's attributes default values are stored in and retrieved from the database regarding being converted to `Null` or not. See [Entity Properties](<../../../ref/integration-studio/element-property/entity.md>) for further information.

1. Specify the **attributes** of the entity by simply editing the [Attributes Editor](<../../../ref/integration-studio/editor/attributes.md>).

![](images/tip.gif) The [Entity editor](<../../../ref/integration-studio/editor/entity.md>) allows you to late change the action properties.

Once the entities are defined and the extension is published on the Platform Server the Service Studio developer simply needs to add a reference to these entities in order to [use them](<../extension-life-cycle/extension-use.md>) in the module. 
