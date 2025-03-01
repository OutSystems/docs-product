---
summary: OutSystems 11 (O11) addresses Invalid Variable Errors by requiring valid values for the Variable property in various widgets and tools.
tags: error handling, debugging, widgets, variables, truechange
locale: en-us
guid: 0eb3292f-592a-4301-a9ee-7ac3c598e70a
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=737:321
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
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

For example, for an [Input](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-input.md), set a valid value for the Variable property.

![Screenshot showing an Invalid Variable Error in the OutSystems development environment](images/invalid-variable-error.png "Invalid Variable Error in OutSystems")

For a [Radio Group](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-radiogroup.md), [Text Area](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-textarea.md), [Switch](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-switch.md), [Checkbox](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-checkbox.md), [Dropdown](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-dropdown.md), or [Button Group](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-buttongroup.md), set a valid value for the Variable property.

##  Unknown variable in Assign

**Cause**

You added a Server Action and added logic to the flow by selecting Set variable. Then, in the Assign, you set the Value but did not set the Variable property. 

**Recommended action**

You need to set a valid value for the [Variable](../../../ref/data/handling-data/variables/intro.md) property of the [Assign](../../../ref/lang/auto/class-assign.md) in the [Server Action](../../../ref/lang/auto/class-server-action.md). 

##  Unknown variable in  &lt;Input_widget_name> Input

**Cause**

You added an Input widget and set the Variable property to a [local variable](../../../ref/lang/auto/class-local-variable.md). The local variable was subsequently deleted.

**Recommended action**

You need to set a valid value for the [Variable](../../../ref/data/handling-data/variables/intro.md) property of the [Input](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-input.md).

##  Unknown object &lt;Variable_name> in variable

**Cause**

You added a Client Action and added logic to the flow by selecting Set variable. Then, in the Assign, you set the Variable property to an [input parameter](../../../ref/lang/auto/class-input-parameter.md), [output parameter](../../../ref/lang/auto/class-output-parameter.md), [local variable](../../../ref/lang/auto/class-local-variable.md), or [client variable](../../../ref/lang/auto/class-client-variable.md). The parameter or variable was subsequently deleted. 

The error is also issued if you set the Variable property of the Assign to a [Site Property](../../../ref/lang/auto/class-site-property.md).

**Recommended action**

You need to set a valid value for the [Variable](../../../ref/data/handling-data/variables/intro.md) property of the [Assign](../../../ref/lang/auto/class-assign.md) in the [Client Action](../../../ref/lang/auto/class-client-action.md).

