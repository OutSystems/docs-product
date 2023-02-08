---
locale: en-us
guid: 0d31202a-6526-4903-a88d-4ed9b8e73ab2
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Entity Properties

The next table presents the properties of the [entity](<../../../extensibility-and-integration/integration-studio/managing-extensions/entity-define.md>) element.  

|Property|Description|Optionality|Default value|Obs.|
|--- |--- |--- |--- |--- |
|Name|Name of the entity.|Mandatory||See [rules for naming elements](<../element-naming.md>).|
|Physical Table Name|Physical table name. The name you specify for this field depends on the database you are connecting to.|Mandatory||In a SQL Server, the full physical table name is:<br/>`[].[].[].`<br/>In Oracle, the full physical name is:<br/>`[].@[]`|
|Logical Database|The logical name that represents the external database. In Service Center of each environment map the Database Connection to this Logical Database name. This is especially useful when staging between environments, allowing to dynamically change the entity's external database.|Optional||This field is used only for entities imported using Database Connections.|
|Identifier|Attribute that uniquely identifies the entity rows.|Optional||In database terminology, the Identifier is called the Primary Key.|
|Description|Free text that describes the action.|Optional||Useful for documentation and knowledge transfer purposes.<br/>The maximum size of this property is 255 characters.|
|Default Value behavior|Indicates how the default values of the entity's attributes are stored in the database and retrieved from the database:<br/>`No conversion to/from Database`: all the entity's attributes that have the default value set are stored in and retrieved from the database without any conversion, i.e., it is the default value that is stored in and retrieved from the database.<br/> `Convert to/from Null value in Database`: all the entity's attributes that have the default value set are stored in the database with the `null` value. When retrieving data from the database, the null value is converted to the attribute's default value. If no default value is defined for the attribute,  the null value is then converted to the Platform default value for the data type.|Mandatory|`No conversion to/from Database`|Only optional attributes are converted. The mandatory attributes cannot be empty so no conversion occurs.<br/>Check also the list of [default values at runtime](<../../data/data-types/available-data-types.md>) and [in the database](<../../data/database/default-values-on-database.md>) for further information.|
