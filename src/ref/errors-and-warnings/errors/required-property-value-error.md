---
summary: Check the causes and recomendations on how to solve the different Required Property Value TrueChange errors
tags:
en_title:
---

# Required Property Value Error

## Value must be set

**Cause**

You added an Expression, Button Group, or Radio Group widget, and did not set a value for the Value property. 

**Recommended action**

You need to set a valid value in the Value property.

For an [Expression](../../../ref/lang/auto/ServiceStudio.Plugin.NRWidgets.Expression.final.md), you need to define a [valid expression](../../../ref/logic/expressions/intro.md).


![Location of Expression value](images/required-property-value-error.png?width=400)


For a [Button Group](../../../ref/lang/auto/ServiceStudio.Plugin.NRWidgets.ButtonGroup.final.md), set a valid value for the Value property of each of the options. 


![Location of Button Group value](images/required-property-value-error-03.png?width=300)


For a [Radio Group](../../../ref/lang/auto/ServiceStudio.Plugin.NRWidgets.RadioGroup.final.md), set a valid value for the Value property of each of the options, and also ensure a value is set for the [Variable property](#variable-must-be-set). 



## Source must be set

**Cause**

You added a Table or a List widget to your application, and did not set a value for the Source property.  

**Recommended action**

You need to set a valid value for the Source property. 

For a Table or a [List](../../../ref/lang/auto/ServiceStudio.Plugin.NRWidgets.List.final.md), set a valid value for the Source property to determine the source of the data you want to display on the screen. 


For example, for a table, set the Source property by selecting the value for the list result of an Aggregate that is already created for fetching data from the database.

## On Click must be set

**Cause**

You added a List Item, Button, or Link widget, and did not set a value for the On Click property of the Event.

**Recommended action**

You need to set a valid value for the On Click property for the Event. 

For a [List Item](../../../ref/lang/auto/ServiceStudio.Plugin.NRWidgets.ListItem.final.md), [Button](../../../ref/lang/auto/ServiceStudio.Plugin.NRWidgets.Button.final.md), or [Link](../../../ref/lang/auto/ServiceStudio.Plugin.NRWidgets.Link.final.md), set a valid value for the On Click property of the Event.



## Variable must be set

**Cause**

You added an Input, Text Area, Switch, Checkbox, Radio Group, Dropdown, or Button Group widget, and did not set a value for the Variable property.

**Recommended action**

You need to set a valid value for the Variable property.

For a [Radio Group](../../../ref/lang/auto/ServiceStudio.Plugin.NRWidgets.RadioGroup.final.md), set a valid value for the Variable property, and also ensure a value is set for the [Value property](#value-must-be-set) of each of the options.


![Location of Radio Group variable](images/required-property-value-error-02.png?width=300)



For an [Input](../../../ref/lang/auto/ServiceStudio.Plugin.NRWidgets.Input.final.md), [Text Area](../../../ref/lang/auto/ServiceStudio.Plugin.NRWidgets.TextArea.final.md), [Switch](../../../ref/lang/auto/ServiceStudio.Plugin.NRWidgets.Switch.final.md), [Checkbox](../../../ref/lang/auto/ServiceStudio.Plugin.NRWidgets.Checkbox.final.md), [Dropdown](../../lang/auto/ServiceStudio.Plugin.NRWidgets.Dropdown.final.md), or [Button Group](../../lang/auto/ServiceStudio.Plugin.NRWidgets.ButtonGroup.final.md), set a valid value for the Variable property.



## List must be set

**Cause**

You added a Dropdown widget and did not set a value for the List property.

**Recommended action**

You need to set a valid value for the List property of the [Dropdown](../../lang/auto/ServiceStudio.Plugin.NRWidgets.Dropdown.final.md).



## Options Value must be set

**Cause**

You added a Dropdown widget and did not set a value for the Options Value property.

**Recommended action**

You need to set a valid value for the Options Value property of the [Dropdown](../../lang/auto/ServiceStudio.Plugin.NRWidgets.Dropdown.final.md).



## File Content must be set

**Cause**

You added an [Upload](../../../ref/lang/auto/ServiceStudio.Plugin.NRWidgets.Upload.final.md) widget and did not set a value for the File Content property.



**Recommended action**

You need to set a valid value for the File Content property of the [Upload](../../../ref/lang/auto/ServiceStudio.Plugin.NRWidgets.Upload.final.md).


## File Name must be set

**Cause**

You added an [Upload](../../../ref/lang/auto/ServiceStudio.Plugin.NRWidgets.Upload.final.md) widget and did not set a value for the File Name property.


**Recommended action**

You need to set a valid value for the File Name property of the [Upload](../../../ref/lang/auto/ServiceStudio.Plugin.NRWidgets.Upload.final.md).



## Show Popup must be set

**Cause**

You added a Popup widget and did not set a value for the Show Popup property.

**Recommended action**

You need to set a valid value for the Show Popup property of the [Popup](../../../ref/lang/auto/ServiceStudio.Plugin.NRWidgets.Popup.final.md).



## Source Block must be set in Block

**Cause**

You added a Block widget and did not set a value for the Source Block property.

**Recommended action**

You need to set a valid value for the Source Block property of the [Block](../../../ref/lang/auto/Class.Block%20Widget.final.md).



## Condition must be set in If

**Cause**

You added an If widget and did not set a value for the Condition.

**Recommended action**

You need to set a valid value for the Condition property of the [If](../../../ref/lang/auto/Class.If%20Widget.final.md).


## Unknown &lt;entity_name> &lt;property> in &lt;element> &lt;element_type>

**Cause**

You deleted an entity, but an existing element in your application (such as a widget or a variable) still uses it. 

For example, an existing entity was added to a list or a table, and you subsequently deleted the entity, such as an obsolete database table. Because this was feeding data to the list or table, the error was issued.

**Recommended action**

Double-click on the error line to take you directly to the missing property and update it. 

For example, for a [List](../../../ref/lang/auto/ServiceStudio.Plugin.NRWidgets.List.final.md) or a Table, select a valid entity for the Source value, such as another database table, to replace the deleted one as the data source.


## URL Path must be set

**Cause**

The URL Path property in a REST API method doesn't have any value.

**Recommended action**

Set the URL Path property of the REST API method to a valid URL. 

**More info**

Check [Customize REST URLs](../../../extensibility-and-integration/rest/expose-rest-apis/customize-rest-urls.md) for more information.


## Set a valid expression for the attribute &lt;attribute>.

**Cause**

You added an inline record, but you did not specify the mandatory attribute. Or you added an inline record, but the value you entered for the attribute is invalid.

**Recommended action**

You need to define a [valid expression](../../../ref/logic/expressions/intro.md) for the attribute.

Double-click on the error line to take you directly to the missing property and update it.
