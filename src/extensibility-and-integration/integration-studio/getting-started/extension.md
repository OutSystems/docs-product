---
summary: Extensions, defined in Integration Studio, allow you to increment OutSystems functionality and integrate with external systems.
locale: en-us
guid: 84e1a2bb-ddb5-40d3-9419-17be22398c15
app_type: traditional web apps, mobile apps, reactive web apps
---

# Extensions

An **extension** is a set of actions, structures, and entities, defined in Integration Studio, that increments OutSystems and allows the integration with external systems.

An extension can be used by any module that has access to it and can be published in multiple installations of the platform.


## Extension Elements

An extension is composed by actions, structures, entities, and resources as presented below.

Actions
:   Correspond to the functionality that you want to expose in the extension. There must be an Action for each C# method with which you want to integrate. To create an Action, in Integration Studio, add it [manually](<../managing-extensions/action-add.md>) or use the [import](<../managing-extensions/net-assembly-import-action.md>) feature.

    These elements are displayed in the **Actions** folder of the [Extension tree](<../../../ref/integration-studio/multi-tree-navigator.md>).

Structures
:   Correspond to more complex data types handled by your actions. You must define the Structures for each data type that you want to expose to your module. To create a Structure, in Integration Studio, add it [manually](<../managing-extensions/structure-define.md>).

    These elements are displayed in the **Structures** folder of the [Extension tree](<../../../ref/integration-studio/multi-tree-navigator.md>).

Entities
:   Correspond to tables that exist outside OutSystems that you want to access in your application. There must be an Entity for each physical table with which you want to integrate. To create an Entity, in Integration Studio, add it [manually](<../managing-extensions/entity-add.md>) or use the [import](<../managing-extensions/entity-import-from-database.md>) feature.

    These elements are displayed in the Entities folder of the [Extension tree](<../../../ref/integration-studio/multi-tree-navigator.md>).

Resources
:   Correspond to the files that implement the defined actions or that support other aspects of the extension. The resources can be added [manually](<../managing-extensions/resource-define.md>) or automatically when [importing actions](<../managing-extensions/net-assembly-import-action.md>).

    These elements are displayed in the **Resources** folder of the [Resources tree](<../../../ref/integration-studio/resources-tree.md>).
