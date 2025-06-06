---
summary: Explore common data type errors and solutions in OutSystems 11 (O11) for expressions, REST API methods, and widgets.
tags: data types, error handling, troubleshooting, service studio, expressions
locale: en-us
guid: cc8e619d-18de-4b4a-a62a-d4058ce5e528
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Invalid Data Type Error

The Invalid Data Type Error is issued, for example, when you use an [Expression](../../../ref/logic/expressions/intro.md) widget or a REST API method.

Double-click on the error line in TrueChange to take you directly to the expression that is issuing the error.

## Incompatible data types in &lt;operator> operator

**Cause**

You are using data types with an operator which are not compatible with it. 

**Recommended action**

Check the data types for the [`<operator>`](../../logic/expressions/operators.md) and ensure you use only allowed [data types](../../../ref/data/data-types/available-data-types.md) in the operation.

## &lt;data-type-needed> data type required instead of &lt;data-type-used>

**Cause**

You are using a property or operator which is set with the incorrect data type, `<data-type-used>`.

**Recommended action**

Set the property or [operator](../../logic/expressions/operators.md) to the correct [`<data-type-needed>`](../../../ref/data/data-types/available-data-types.md).

## Invalid 'Null Value' data type for specified variable

**Cause**

You are using a Null Value property which is incompatible with the Variable assigned to the Input widget.

**Recommended action**

Set the Null Value property to a value of the same [data type](../../../ref/data/data-types/available-data-types.md) as the Variable assigned to the [Input widget](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-input.md). For example, if you assigned a Boolean variable to the Input, set Null Value as `False`.

## Cannot send a 'Binary Data' parameter in the request &lt;send in> of a method with &lt;request format> request format. Change the parameter data type or the method request format.

**Cause**

In a REST API method request, you are defining a parameter and setting it to the Binary Data data type, and the method request format does not correspond with this.

**Recommended action**

Change the [data type](../../../ref/data/data-types/available-data-types.md) of the [parameter](../../../ref/lang/auto/servicestudio-plugin-rest-restactioninput.md) or the request format of the [REST API method](../../../ref/lang/auto/servicestudio-plugin-rest-restaction.md).

## Cannot send a 'List' parameter in the request &lt;send in> of a method with &lt;request format> request format. Change the parameter data type or the method request format.

**Cause**

In a REST API method request, you are defining a parameter and setting it to the List data type, and the method request format does not support this.

**Recommended action**

Change the [data type](../../../ref/data/data-types/available-data-types.md) of the [parameter](../../../ref/lang/auto/servicestudio-plugin-rest-restactioninput.md) or the request format of the [REST API method](../../../ref/lang/auto/servicestudio-plugin-rest-restaction.md).
