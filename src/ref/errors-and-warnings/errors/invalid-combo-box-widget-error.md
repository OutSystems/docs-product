---
locale: en-us
guid: c8ac04ea-7e81-44be-b645-bf003af44f25
---

# Invalid Combo Box Widget Error

The `Invalid Combo Box Widget` error is issued in the following situations:

* `Source Entity/Struct, 'Source Record List' or 'Special List' must be defined`
  
    You have a Combo Box widget with no values to populate.

    Edit the Combo Box widget and, depending on your requirements, define one of the following properties:
    
    * Source Entity/Struct, if you want to display all the rows of an entity or structure

    * Source Record List, if you want to filter some of the entity rows to display
    
    * Special List, if you want to display generic values

* `'Variable' cannot be set if 'Source Entity/Struct' is not set`
  
    Either you have a Combo Box widget to display generic values (i.e.: not using a Source Entity or Source Structure) with the Variable property is set. Or you have set the variable that gathers the end user input but no Source Entity or Source Structure is defined.

    Edit this Combo Box widget and do one of the following operations: 
    
    * If you are using a special list for generic values, you have to use the Special Variable property to gather end user input and, therefore, unset the Variable property. 

    * If you want to use Entities or Structures, set the Variable property accordingly with, the Identifier of the Entity or the Source Identifier Attribute property.

* `'Variable' must be set with a variable of <Entity> Identifier data type in <Combo Box> widget`
  
    The list of records used to populate a Combo Box widget is composed of Entities and, in this situation, the variable that gathers end user input must be in accordance with the Identifier of the Entity.

    Edit this Combo Box widget and set the Variable property to a variable whose data type is compatible with the data type of the Identifier of the Entity.

* `'Variable' must be set with a variable of <type> compatible data type in <Combo Box> widget`
  
    The list of records used to populate a Combo Box widget is composed of Structures and, in this situation, the variable that gathers end user input must be in accordance with the Identifier attribute of the Structure.

    Edit this Combo Box widget and set the Variable property with a variable whose data type is compatible with the data type of the Source Identifier Attribute property.

* `'Source Attribute' must be a <entity | structure> attribute in <Combo Box> widget`
  
    You haven't defined the attribute to display in a Combo Box widget. This attribute must be compliant with the definition of the records presented in this widget.

    Edit the Combo Box widget and specify the Source Attribute property:
    
    * If you are displaying the content of an Entity, you have to select an Entity Attribute
    
    * If you are displaying the content of a Structure, you have to select a Structure Attribute. 
    
    This property is not mandatory if you are displaying generic values, through the Special List property.

* `Use of 'Source Record List' requires 'Source Entity/Struct' and 'Attribute' to be set`
  
    The list of records used to populate a Combo Box widget is composed of Entities, but neither the Entity nor the Attribute to display are specified.

    Edit the Combo Box widget and specify the Source Entity/Structure and Source Attribute properties to indicate the Attribute Name displayed for each row of the Entity.

* `'Source Record List' must be defined when 'Source Entity/Struct' is defined by a Structure`
  
    You have a Combo Box widget that displays the content of a Structure but you haven't defined the list of records.

    Edit the Combo Box widget and specify in the Source Record List property the Structure with the records to be displayed in the widget.

* `'Source Identifier Attribute' must be set with a <structure> attribute in <Combo Box> widget`
  
    The list of records used to populate a Combo Box widget is composed of Structures but the Attribute to display was not specified.

    Edit the Combo Box widget and specify the Source Identifier Attribute property as the Structure Attribute to be displayed.

* `'Source Identifier Attribute' must not be of 'Binary Data', 'Record', or 'List' data types in <Combo Box> widget`
  
    The structure attribute displayed in a Combo Box widget is a Binary Data, Record, or List data type and cannot be.

    Edit the Combo Box widget and change the Source Identifier Attribute property to a valid data type.

* `'Source Entity' must have an Identifier in <Combo Box> widget`
  
    The entity used to populate the Combo Box widget must have an Identifier.

    Edit the Entity and define one of its attributes or a new attribute as Identifier.

Double-click on the error line to take you directly to the property of the Combo Box widget.
