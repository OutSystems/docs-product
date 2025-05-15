---
locale: en-us
guid: 6d427a2f-1395-4386-abde-fe9f074f7e38
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/design/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=3067-146&t=0cuQUgeosMV2m0Kw-1
summary: OutSystems 11 (O11) facilitates importing .NET assembly items as actions with specific properties and parameters.
tags: ide usage, reactive web apps, .net integration, outsystems development, import actions
audience:
  - full stack developers
  - backend developers
  - frontend developers
outsystems-tools:
  - service studio
  - integration studio
coverage-type:
  - remember
---

# Imported Actions Properties

The Import Actions from .NET Assembly wizard allows you to import action definitions from a .NET assembly. Using introspection of a .NET assembly, this wizard will create an action for each method, property and public field you checked in step 3 of the [Import Actions from .NET Assembly](<../../../integration-with-systems/integration-studio/managing-extensions/net-assembly-import-action.md>) wizard. The properties of the imported actions depend on the type of the assembly item you select, as explained below.

![Icon indicating a note or important information in the documentation](images/note-icon.png "Note Icon") All actions created with this mechanism are created with the Function property set to its default, that is, `No`.

## Constructors as Actions

For each .NET constructor selected in the wizard, a new action is created with the following properties:

Name
:   `<.NET_class_name>Create`

Parameters
:   One output parameter is added, besides the ones natively declared in the Constructor. This new parameter represents the created object and has the following properties:

    * Name: `New_<.NET_class_name_of_the_Object_created>`

    * Type: Object. For more information about this data type, see [Data Types](<../../data/data-types/available-data-types.md>).

## Methods as Actions

For each .NET method selected in the wizard, a new action is created with the following properties:

Name
:   `<.NET_class_name><.NET_method_name>`

Parameters
:   For each input or output parameter declared in this method, an input or output parameter is created as follows:

    * Name: Name of the .NET parameter.

    * Data type: OutSystems' data type that corresponds to the .NET data type. For more information, see [Data Types at Runtime](<../../data/data-types/data-types-at-runtime.md>).

    In the following situations, Integration Studio creates more parameters than the method defines, in order to correctly map the method signature into the action definition.

    * If the method is **non-static**, then an extra input parameter is created as follows:<br/>
    Name: `This_<.NET_class_name>`<br/>
    Data type: Object. For more information about this data type, see [Data Types](<../../data/data-types/available-data-types.md>).<br/>
    ![Icon indicating a note or important information in the documentation](images/note-icon.png "Note Icon") This parameter holds the object where this non-static method will be invoked.

    * If the method has a **return value**, then an extra output parameter is created as follows:<br/>
    Name: `Return_<.NET_class_name_of_the_method_return>`<br/>
    Data type: OutSystems' data type that corresponds to the .NET data type. For more information, see [Data Types at Runtime](<../../data/data-types/data-types-at-runtime.md>).<br/>
    ![Icon indicating a note or important information in the documentation](images/note-icon.png "Note Icon") This parameter holds the result of this method.

    * If the method has a **reference parameter**, then two input and output parameters are created as follows:<br/>
    Name: `In_<.NET_parameter_name>`<br/>
    Type: Input parameter<br/>
    Data type: OutSystems' data type that corresponds to the .NET data type. For more information, see [Data Types at Runtime](<../../data/data-types/data-types-at-runtime.md>).

    * Name: `Out_<.NET_parameter_name>`<br/>
    Type: Output parameter<br/>
    Data type: OutSystems' data type that corresponds to the .NET data type. For more information, see [Data Types at Runtime](<../../data/data-types/data-types-at-runtime.md>).

## Properties as Actions

For each .NET property selected in the wizard, two new actions might be created with the following properties:

Name
:   `<.NET_class_name><.NET_property_name>Get`

    ![Icon indicating a note or important information in the documentation](images/note-icon.png "Note Icon") This action is created only if the property is readable.

Parameters
:   The following parameters are created:

    * Name: `This_<.NET_class_name>`<br/>+
    Type: Input parameter<br/>
    Data type: Object. For more information about this data type, see [Data Types](<../../data/data-types/available-data-types.md>).<br/>
    ![Icon suggesting a tip or helpful hint in the documentation](images/tip-icon.png "Tip Icon") This parameter should hold the object where the property will be invoked.

    * Name: `<property_name>`<br/>
    Type: Output parameter<br/>
    Data type: OutSystems' data type that corresponds to the .NET data type. For more information, see [Data Types at Runtime](<../../data/data-types/data-types-at-runtime.md>).

Name
:   `<.NET_class_name><.NET_property_name>Set`

    ![Icon indicating a note or important information in the documentation](images/note-icon.png "Note Icon") This action is created only if the property is writable.

Parameters
:   The following parameters are created:

    * Name: `This_<.NET_class_name>`<br/>
    Type: Input parameter<br/>
    Data type: Object. For more information about this data type, see [Data Types](<../../data/data-types/available-data-types.md>).<br/>
    ![Icon suggesting a tip or helpful hint in the documentation](images/tip-icon.png "Tip Icon") This parameter should hold the object where the property will be invoked.

    * Name: `<property_name>`<br/>
    Type: Output parameter<br/>
    Data type: OutSystems' data type that corresponds to the .NET data type. For more information, see [Data Types at Runtime](<../../data/data-types/data-types-at-runtime.md>).

## Public Fields as Actions

For each .NET public field selected in the wizard, two new actions are created with the following properties:

Name
:   `<.NET_class_name><.NET_field_name>Get`

Parameters
:   The following parameters are created:

    * Name: `This_<.NET_class_name>`<br/>
    Type: Input Parameter<br/>
    Data type: Object. For more information about this data type, see [Data Types](<../../data/data-types/available-data-types.md>).<br/>
    ![Icon suggesting a tip or helpful hint in the documentation](images/tip-icon.png "Tip Icon") This parameter should hold the object from which the field will be obtained.

    * Name: `<property_name>`<br/>
    Type: Output Parameter<br/>
    Data type: OutSystems' data type that corresponds to the .NET data type. For more information, see [Data Types at Runtime](<../../data/data-types/data-types-at-runtime.md>).

Name
:   `<.NET_class_name><.NET_field_name>Set`

Parameters
:   The following parameters are created:

    * Name: `This_<.NET_class_name>`<br/>
    Type: Input Parameter<br/>
    Data type: Object. For more information about this data type, see [Data Types](<../../data/data-types/available-data-types.md>).<br/>
    ![Icon suggesting a tip or helpful hint in the documentation](images/tip-icon.png "Tip Icon") This parameter should hold the object from which the field will be obtained.

    * Name: `<property_name>`<br/>
    Type: Output Parameter<br/>
    Data type: OutSystems' data type that corresponds to the .NET data type. For more information, see [Data Types at Runtime](<../../data/data-types/data-types-at-runtime.md>).

![Icon indicating a note or important information in the documentation](images/note-icon.png "Note Icon") The "Import Actions from .NET Assembly" wizard has the necessary mechanisms to avoid name clashing. Also, by default, the icon associated with actions imported from a .NET assembly is ![Icon representing an action imported from a .NET assembly in the documentation](images/imported-action-icon.png "Imported Action Icon").

![Icon suggesting a tip or helpful hint in the documentation](images/tip-icon.png "Tip Icon") In the [Action editor](<../editor/action.md#import-details>) you can see the details about the Import Operation.
