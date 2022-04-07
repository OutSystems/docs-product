---
locale: en-us
guid: ecc60a02-004d-4d98-997d-4b5c5fff124b
---

# Extension Properties

To access the properties of an [extension](<../../../extensibility-and-integration/integration-studio/extension-life-cycle/extension-create.md>), simply double-click on the extension in the Extension tab, in the [Multi-tree Navigator](<../multi-tree-navigator.md>).

The extension properties are explained below.

Name
:   Name of the extension. See [rules for naming elements](<../element-naming.md>).


DBMS
:   Indicates the Database Management System (DBMS) type that the extension is prepared to work with. This property is used during the validation of the extension to, for example, check whether the physical table name associated with an entity is valid or not.

    The possible values are: `Oracle`, `SqlServer`, and `(All)`.

    Default value: `(All)`.

Description
:   Free text that describes the extension. Useful for documentation and knowledge transfer purposes. The maximum size of this property is 255 characters.
