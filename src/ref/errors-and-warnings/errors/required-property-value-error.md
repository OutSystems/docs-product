---
summary: Check the causes and recomendations on how to solve the different Required Property Value TrueChange errors
tags:
locale: en-us
guid: 104aade7-8bf2-4e15-9871-f05e91e008f6
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=857:1425
---

# Required Property Value Error

The Required Property Value Error is issued when you use an Expression widget or, for example, a Button Group widget. It can also occur if you add a chart, such as a Donut Chart.

Double-click on the error line in TrueChange to take you directly to the property that is issuing the error.

## Value must be set

**Cause**

You added an Expression, Button Group, or Radio Group widget, and did not set a value for the Value property. 

**Recommended action**

You need to set a valid value in the Value property.

For an [Expression](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-expression.md), you need to define a [valid expression](../../../ref/logic/expressions/intro.md).

![Screenshot showing an example of a Required Property Value Error in the development environment](images/required-property-value-error.png "Required Property Value Error Example")

For a [Button Group](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-buttongroup.md), set a valid value for the Value property of each of the options. 

![Illustration of a Button Group widget with a missing Value property causing an error](images/required-property-value-error-03.png "Button Group Value Property Error")

For a [Radio Group](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-radiogroup.md), set a valid value for the Value property of each of the options, and also ensure a value is set for the [Variable property](#variable-must-be-set). 

## Source must be set

**Cause**

You added a Table or a List widget to your application, and did not set a value for the Source property.  

**Recommended action**

You need to set a valid value for the Source property. 

For a [Table](../../../ref/lang/auto/class-table-widget.md) or a [List](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-list.md), set a valid value for the Source property to determine the source of the data you want to display on the screen. 

For example, for a table, set the Source property by selecting the value for the list result of an Aggregate that is already created for fetching data from the database.

## On Click must be set

**Cause**

You added a List Item, Button, or Link widget, and did not set a value for the On Click property of the Event.

**Recommended action**

You need to set a valid value for the On Click property for the Event.
This value sets the behavior after a click on the element, and you must set it to one of the following:

* An Action that is triggered on click.
* A Screen to which the user is redirect on click.
* A RedirectToURL, with an URL to which the user is redirect on click.

For a [List Item](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-listitem.md), [Button](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-button.md), or [Link](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-link.md), set a valid value for the On Click property of the Event.

## Variable must be set

**Cause**

You added an Input, Text Area, Switch, Checkbox, Radio Group, Dropdown, or Button Group widget, and did not set a value for the Variable property.

**Recommended action**

You need to set a valid value for the Variable property.

For a [Radio Group](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-radiogroup.md), set a valid value for the Variable property, and also ensure a value is set for the [Value property](#value-must-be-set) of each of the options.

![Example of a Radio Group widget with an unset Variable property resulting in an error](images/required-property-value-error-02.png "Variable Property Error in Radio Group")

For an [Input](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-input.md), [Text Area](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-textarea.md), [Switch](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-switch.md), [Checkbox](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-checkbox.md), [Dropdown](../../lang/auto/servicestudio-plugin-nrwidgets-dropdown.md), or [Button Group](../../lang/auto/servicestudio-plugin-nrwidgets-buttongroup.md), set a valid value for the Variable property.

## List must be set

**Cause**

You added a Dropdown widget and did not set a value for the List property.

**Recommended action**

You need to set a valid value for the List property of the [Dropdown](../../lang/auto/servicestudio-plugin-nrwidgets-dropdown.md).

## Options Value must be set

**Cause**

You added a Dropdown widget and did not set a value for the Options Value property.

**Recommended action**

You need to set a valid value for the Options Value property of the [Dropdown](../../lang/auto/servicestudio-plugin-nrwidgets-dropdown.md).

## File Content must be set

**Cause**

You added an [Upload](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-upload.md) widget and did not set a value for the File Content property.

**Recommended action**

You need to set a valid value for the File Content property of the [Upload](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-upload.md).

## File Name must be set

**Cause**

You added an [Upload](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-upload.md) widget and did not set a value for the File Name property.

**Recommended action**

You need to set a valid value for the File Name property of the [Upload](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-upload.md).

## Show Popup must be set

**Cause**

You added a Popup widget and did not set a value for the Show Popup property.

**Recommended action**

You need to set a valid value for the Show Popup property of the [Popup](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-popup.md).

## Source Block must be set in Block

**Cause**

You added a Block widget and did not set a value for the Source Block property.

**Recommended action**

You need to set a valid value for the Source Block property of the [Block](../../../ref/lang/auto/class-block-widget.md).

## Condition must be set in If

**Cause**

You added an If widget and did not set a value for the Condition.

**Recommended action**

You need to set a valid value for the Condition property of the [If](<../../../ref/lang/auto/class-if-widget.md>).

## Unknown &lt;entity_name> &lt;property> in &lt;element> &lt;element_type>

**Cause**

You deleted an entity, but an existing element in your application (such as a widget or a variable) still uses it. 

For example, an existing entity was added to a list or a table, and you subsequently deleted the entity, such as an obsolete database table. Because this was feeding data to the list or table, the error was issued.

**Recommended action**

Double-click on the error line to take you directly to the missing property and update it. 

For example, for a [List](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-list.md) or a [Table](../../../ref/lang/auto/class-table-widget.md), select a valid entity for the Source value, such as another database table, to replace the deleted one as the data source.

## URL Path must be set

**Cause**

The URL Path property in a REST API method doesn't have any value.

**Recommended action**

Set the URL Path property of the REST API method to a valid URL. 

**More info**

Check [Customize REST URLs](../../../integration-with-systems/rest/expose-rest-apis/customize-rest-urls.md) for more information.

## Set a valid expression for the attribute &lt;attribute>.

**Cause**

You added an inline record, but you did not specify the mandatory attribute. Or you added an inline record, but the value you entered for the attribute is invalid.

**Recommended action**

You need to define a [valid expression](../../../ref/logic/expressions/intro.md) for the attribute.

Double-click on the error line to take you directly to the missing property and update it.

## Required Property Value: A valid expression must be set for parameter 'SourceDataPointList'
 
**Cause**

You added an Area Chart, Bar Chart, Column Chart, Donut Chart, Line Chart, or Pie Chart widget and did not set a value for the 'SourceDataPointList' property. 

**Recommended action**

For the Chart, you need to set a value for the 'SourceDataPointList' property to determine the source list for the data points that are to be plotted on the chart. 

For example, to create a Pie or Donut Chart and add the data points, see [Create Pie and Donut Charts](../../../ref/apis/charts/chart-task-piedonut.md). 

**More info**

Also, check out [Create Column or Bar Charts](../../../ref/apis/charts/chart-task-columnbar.md) and [Create Line and Area Charts](../../../ref/apis/charts/chart-task-linearea.md).

## Required Property Value: A valid expression must be set for parameter &lt;Parameter_name>
 
**Cause**

The issue can occur, for example, if you added a Client Action, added it to the logic in a flow, and subsequently added an input parameter for it.

It can also occur, for example, if you add a Client Action, add an input parameter for it, and then drag the Client Action to the logic in a flow. 

**Recommended action**

You need to set a [valid expression](../../../ref/logic/expressions/intro.md) for the [input parameter](../../../ref/lang/auto/class-input-parameter.md) of the [Client Action](../../../ref/lang/auto/class-client-action.md) in the logic. 

Alternatively, to add a Client Action to the logic and have the parameter automatically set to itself, select AI-Assisted Development in the logic and choose the Client Action.    
