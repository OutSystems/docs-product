---
locale: en-us
guid: 0deb5983-3f9e-4a35-bbba-65396634c860
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Define the Extension Elements

Once your extension is [created](<extension-create.md>), you have to create or update the definition of its elements:

Actions
:    Created [manually](<../managing-extensions/action-add.md>) or [imported](<../managing-extensions/net-assembly-import-action.md>) from a .NET assembly.

Structures
:   Created [manually](<../managing-extensions/structure-define.md>).

Entities
:   Created [manually](<../managing-extensions/entity-add.md>) or [imported](<../managing-extensions/entity-import-from-database.md>) from a specific database table.

Resources
:   Most of the required files are automatically included by Integration Studio, during the extension life cycle. When the extension is created, you can check, in the [Resources](<../../../ref/integration-studio/workspace.md>) tree, that all the files needed for the bootstrapping are generated automatically. If necessary, you can [add other types of resources](<../managing-extensions/resource-define.md>), such as Help files and images.
