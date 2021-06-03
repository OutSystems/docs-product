---
summary: Check the causes and recomendations on how to solve the different Required Property Value TrueChange errors
tags:
en_title:
---

# Required Property Value Error

## Value must be set

**Cause**

You added an Expression, Button Group, or Radio Group widget, and did not set a value for the Value property. 

<!-- Screenshot to be added showing the location of the Value property -->

**Recommended action**

You need to define a valid value in the Value property.

For example, in an Expression you need to define a [valid expression](../../../ref/logic/expressions/intro.md).

For a Button Group, set a [valid value](../../../develop/ui/patterns/web/controls/buttongroup.md) for the Value property. 

<!-- Link to be added to 'valid value' above to go to Developing_an_Application/Design_UI/Patterns/Using_Traditional_Web_Patterns/Controls/Button_Group  -->

For a Radio Group, set a valid value for the Value property of each of the three options, and also ensure a value is set for the [Variable property](#Variable-must-be-set). 

## Source must be set

**Cause**

You added a Table or a List widget to your application, and did not set a value for the Source property.  

**Recommended action**

You need to set a valid value for the Source property. 

For example, for a Table or a List, set a valid value for the Source property to determine the source of the data.

## On Click must be set

**Cause**

You added a List Item, a Button, or a Link widget, and did not set a value for the On Click property of the Event.

**Recommended action**

You need to set a valid value for the On Click property for the Event. 

For a List Item, Button, or Link, set a valid value for the On Click property of the Event.

## Variable must be set

**Cause**

You added an Input, Text Area, Switch, Checkbox, Radio Group, Dropdown, or Button Group widget, and did not set a value for the Variable property.

**Recommended action**

You need to set a valid value for the Variable property.

For an Input, Text Area, Switch, Checkbox, Dropdown, or Button Group, set a valid value for the Variable property.

For a Radio Group, set a valid value for the Variable property, and also ensure a value is set for the [Value property](#Value-must-be-set) of each of the three options.

## List must be set

**Cause**

You added a Dropdown widget and did not set a value for the List property.

**Recommended action**

You need to set a valid value for the List property of the Dropdown.

## Options Value must be set

**Cause**

You added a Dropdown widget and did not set a value for the Options Value property.

**Recommended action**

You need to set a valid value for the Options Value property of the Dropdown.

## File Content must be set

**Cause**

You added an Upload widget and did not set a value for the File Content property.

**Recommended action**

You need to set a valid value for the File Content property of the Upload.

## File Name must be set

**Cause**

You added an Upload widget and did not set a value for the File Name property.

**Recommended action**

You need to set a valid value for the File Name property of the Upload.

## Show Popup must be set

**Cause**

You added a Popup widget and did not set a value for the Show Popup property.

**Recommended action**

You need to set a valid value for the Show Popup property of the Popup.

## Source Block must be set in Block

**Cause**

You added a Block widget and did not set a value for the Source Block property.

**Recommended action**

You need to set a valid value for the Source Block property of the Block.

## Condition must be set in If

**Cause**

You added an If widget and did not set a value for the Condition.

**Recommended action**

You need to set a valid value for the Condition property of the If.

## Unknown &lt;entity_name> &lt;property> in &lt;element> &lt;element_type>

**Cause**

You deleted an entity, but an existing element in your application (such as a widget or a variable) still uses it. 

For example, an existing entity was added to a list or a table, and you subsequently deleted the entity, such as an obsolete database table. Because this was feeding data to the list or table, the error was issued.

**Recommended action**

Double-click on the error line to take you directly to the missing property and update it. 

For example, select a valid entity, such as another database table, to replace the deleted one as the data source value for the Source.

## URL Path must be set

**Cause**

The URL Path property in a REST API method doesn't have any value.

**Recommended action**

Set the URL Path property of the REST API method to a valid URL.

## Set a valid expression for the attribute &lt;attribute>.

**Cause**

You added an inline record, but you did not specify the mandatory attribute. Or you added an inline record, but the value you entered for the attribute is invalid.

**Recommended action**

Double-click on the error line to take you directly to the missing property and update it.
