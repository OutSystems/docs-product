---
locale: en-us
guid: c1e911aa-f9af-45e6-b0b9-495695392881
app_type: traditional web apps, mobile apps, reactive web apps
---

# Action Parameter Properties

The next table presents the properties of the [action parameter](<../../../extensibility-and-integration/integration-studio/managing-extensions/action-parameter.md>) element.  
  
|Property|Description|Optionality|Default value|Obs.|
|--- |--- |--- |--- |--- |
|Name|Name of the parameter.|Mandatory|`Parameter `|You should change the name of the parameter to a suitable value.<br/>See [rules for naming elements](<../element-naming.md>).|
|Input|Indicates whether the parameter is an input or output parameter.|Mandatory|`Input`|See how to [change the type of the parameter](<../editor/action-parameters.md>).|
|Mandatory|Indicates whether the input parameter is mandatory or optional.|Mandatory|`Mandatory`|To define an input parameter as optional simply un-check this property.|
|Data Type|Indicates the type of the parameter. You can use basic data types such as Text or Integer; or you might need more complex data types to handle this parameter. Integration Studio provides the **Record** and **Record List** data types. The definitions of the **Record** and **Record List** data types are based on the [structures](<../../../extensibility-and-integration/integration-studio/managing-extensions/structure-define.md>) and [entities](<../../../extensibility-and-integration/integration-studio/managing-extensions/entity-define.md>) available in your extension.|Mandatory||The possible values are presented in a drop-down list. For more information, see available data types.<br/>Since OutSystems has its own data types, you should check how these data types are translated into Microsoft .NET data types.|
|Default value|Default value that is used if no value for this parameter is provided in the module that is using this action.|Optional|||
|Record Type|If your parameter data type is a Record or a Record List, you have to select the [entities](<../../../extensibility-and-integration/integration-studio/managing-extensions/entity-add.md>) and/or [structures](<../../../extensibility-and-integration/integration-studio/managing-extensions/structure-define.md>) that define the Record or Record List. Learn more about these data types.<br/>The value of this property is the name of the entity or structure. In case you have a combination of both entities and/or structures, the value is (Join).|Optional||Mandatory only if the **Data Type** is `Record` or `Record List`.|
|Description|Description of the parameter.|Optional||By default the description is empty, but you should provide a small description of the semantic of this parameter. The maximum allowed size for descriptions is 255 characters.|
