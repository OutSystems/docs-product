---
summary:  Check the causes and recomendations on how to solve the different Invalid Variable TrueChange errors.
tags:
locale: en-us
guid: 0eb3292f-592a-4301-a9ee-7ac3c598e70a
---

# Invalid Variable Error

The Invalid Variable Error can be issued when you use widgets, such as an Input, Text Area, Switch, Checkbox, Radio Group, Dropdown, or Button Group widget, which require a valid value to be set for the Variable property. It can also be issued when you use the Assign Tool. 

Double-click on the error line in TrueChange to take you directly to the variable that is issuing the error.

## Unknown variable

**Cause**

Your module is using a variable that no longer exists.

**Recommended action**

You need to set a valid value for the [Variable](../../../ref/data/handling-data/variables/intro.md) property.

Use the Find tool to discover where the variable is being used and use an existing variable instead. Or, double-click on the error line in TrueChange to take you directly to the property containing the error.

## Unknown variable in &lt;element>

**Cause**

Your module is using a variable that no longer exists. 

For example, you added an Input, Text Area, Switch, Checkbox, Radio Group, Dropdown, or Button Group widget, and set a value for the Variable property. That value was subsequently deleted.

**Recommended action**

You need to set a valid value for the [Variable](../../../ref/data/handling-data/variables/intro.md) property. 

For example, for an [Input](../../../ref/lang/auto/ServiceStudio.Plugin.NRWidgets.Input.final.md), set a valid value for the Variable property.

![Location of Variable property of Input](images/invalid-variable-error.png?width=300)

For a [Radio Group](../../../ref/lang/auto/ServiceStudio.Plugin.NRWidgets.RadioGroup.final.md), [Text Area](../../../ref/lang/auto/ServiceStudio.Plugin.NRWidgets.TextArea.final.md), [Switch](../../../ref/lang/auto/ServiceStudio.Plugin.NRWidgets.Switch.final.md), [Checkbox](../../../ref/lang/auto/ServiceStudio.Plugin.NRWidgets.Checkbox.final.md), [Dropdown](../../../ref/lang/auto/ServiceStudio.Plugin.NRWidgets.Dropdown.final.md), or [Button Group](../../../ref/lang/auto/ServiceStudio.Plugin.NRWidgets.ButtonGroup.final.md), set a valid value for the Variable property.

##  Unknown variable in Assign

**Cause**

You added a Server Action and added logic to the flow by selecting Set variable. Then, in the Assign, you set the Value but did not set the Variable property. 

**Recommended action**

You need to set a valid value for the [Variable](../../../ref/data/handling-data/variables/intro.md) property of the [Assign](../../../ref/lang/auto/Class.Assign.final.md) in the [Server Action](../../../ref/lang/auto/Class.Server%20Action.final.md). 

##  Unknown variable in  &lt;Input_widget_name> Input

**Cause**

You added an Input widget and set the Variable property to a [local variable](../../../ref/lang/auto/Class.Local%20Variable.final.md). The local variable was subsequently deleted.

**Recommended action**

You need to set a valid value for the [Variable](../../../ref/data/handling-data/variables/intro.md) property of the [Input](../../../ref/lang/auto/ServiceStudio.Plugin.NRWidgets.Input.final.md).

##  Unknown object &lt;Variable_name> in variable

**Cause**

You added a Client Action and added logic to the flow by selecting Set variable. Then, in the Assign, you set the Variable property to an [input parameter](../../../ref/lang/auto/Class.Input%20Parameter.final.md), [output parameter](../../../ref/lang/auto/Class.Output%20Parameter.final.md), [local variable](../../../ref/lang/auto/Class.Local%20Variable.final.md), or [client variable](../../../ref/lang/auto/Class.Client%20Variable.final.md). The parameter or variable was subsequently deleted. 

The error is also issued if you set the Variable property of the Assign to a [Site Property](../../../ref/lang/auto/Class.Site%20Property.final.md).

**Recommended action**

You need to set a valid value for the [Variable](../../../ref/data/handling-data/variables/intro.md) property of the [Assign](../../../ref/lang/auto/Class.Assign.final.md) in the [Client Action](../../../ref/lang/auto/Class.Client%20Action.final.md).

