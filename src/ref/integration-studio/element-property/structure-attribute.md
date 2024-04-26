---
locale: en-us
guid: 227269b0-1de7-4179-8b42-40fe86ac8129
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
summary: The article details the properties of structure attributes in Integration Studio, including their optionality, defaults, and special considerations
---
# Structure Attribute Properties

The next table presents the properties of the [structure attribute](<../../../integration-with-systems/integration-studio/managing-extensions/structure-define.md>) element.  

|Property|Description|Optionality|Default value|Obs.|
|--- |--- |--- |--- |--- |
|Name|Name of the attribute.|Mandatory|`Attribute `|You should change the name of the attribute to a suitable value. See [rules for naming elements](<../element-naming.md>).|
|Mandatory|Indicates whether the attribute is mandatory or optional.|Mandatory|`Mandatory`|To define an attribute as optional, simply un-check this property.|
|Data Type|Indicates the type of the attribute. You can use basic data types such as `Text` or `Integer`; or you might need more complex data types to handle this attribute. Integration Studio provides the `Record` and `Record List` data types. The definition of these two data types are based on the [structures](<../../../integration-with-systems/integration-studio/managing-extensions/structure-define.md>) and [entities](<../../../integration-with-systems/integration-studio/managing-extensions/entity-define.md>) you have available in your extension. <br/>![Warning icon indicating a note about OutSystems not allowing recursive structures](images/warning.gif "Warning Icon") OutSystems does not allow recursive structures.|Mandatory||The possible values are presented in a drop-down list. For more information, see available data types. Since OutSystems has its own data types, you should check how these data types are translated into Microsoft .NET data types.|
|Default value|Default value that is used if no value for this attribute is provided in the module that is using this action.|Optional|||
|Length|Size of the attribute.|Optional||This property is only available for `Text` and `Decimal` types. In the `Decimal` type, this property corresponds to the number of digits, including the decimal part. If the values for these data types are not specified, default values are used. The rest of the data types have a fixed length.|
|Decimals|Number of decimal places.|Optional||This property is only available when the data type is `Decimal` and corresponds to the number of digits of the decimal part.|
|Record Type|If your attribute data type is `Record` or a `Record List`, you have to select the [entities](<../../../integration-with-systems/integration-studio/managing-extensions/entity-add.md>) and/or [structures](<../../../integration-with-systems/integration-studio/managing-extensions/structure-define.md>) that define the Record or Record List. Learn more about these data types. The value of this property is the name of the structure. In case you have a combination of structures, the value is `(Join)`.|Optional||Mandatory only if the Data Type is `Record` or `Record List`.|
|Description|Description of the parameter.|Optional||By default the description is empty, but you should provide a small description of the semantic of this parameter. The maximum allowed size for descriptions is 255 characters.|
