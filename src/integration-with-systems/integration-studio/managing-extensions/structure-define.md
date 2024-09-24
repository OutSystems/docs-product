---
locale: en-us
guid: 64abe2b1-809c-4f5c-8dcd-b24547c83ee8
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
summary: Integration Studio allows the definition of complex data types using Structures, which can be used in parameters and attributes as Record or Record List data types
---
# Define Extension Structures

Integration Studio provides some base data types, such as Integer or Text, but you can define more complex data types using Structures. Once structures are defined, they can be used in the data type definition of parameters and attributes. In such cases, you should use the Record data type or the Record List data type.

A structure is necessary when you are integrating with a component that handles complex data in a .NET class. For example, suppose that, in this component, you have a File class with two attributes: File Name and File Size. In Integration Studio, you may create a Structure with this definition and, afterward, use it in the definition of your records or record lists.  

To create a structure do the following:

1. Right-click on the Structures folder in the Multi-tree Navigator and select the ![Context menu with 'Add Structure' option in Integration Studio](images/structure.gif "Add Structure Option") Add Structure option.

1. Specify the following properties:

    * **Name**: name of the structure
    * **Description**: description of the structure

    For more details about these properties, see [Structure Properties](<../../../ref/integration-studio/element-property/structure.md>).

1. Specify the attributes of the structure by simply editing the [Attributes Editor](<../../../ref/integration-studio/editor/attributes.md>).


![Lightbulb icon indicating a tip about using the Structure editor in Integration Studio](images/tip.gif "Structure Editor Tip") The [Structure editor](<../../../ref/integration-studio/editor/structure.md>) allows you to change the structure properties.

Once the structures are defined and the extension is published on the Platform Server, the Service Studio developer simply needs to add a reference to these structures in order to [use them](<../extension-life-cycle/extension-use.md>) in the module. 
