---
tags: runtime-mobileandreactiveweb
summary: Provides methods to show validation messages on widgets and set their validation values. Used when validating widgets inside iterators, since it's not possible to do it in the usual way.
---

# Validation

Provides methods to show validation messages on widgets and set their validation values. Used when validating widgets inside iterators, since it's not possible to do it in the usual way.

## Hierarchy

**Validation**

## Summary

<table markdown="1">
<thead>
<tr>
<th colspan="2">Methods</th>
</tr>
</thead>
<tbody>
<tr>
<td>[isWidgetValid](validation.md#iswidgetvalid)</td>
<td>
Checks if a given widget is currently valid.
</td>
</tr>
<tr>
<td>[setWidgetAsInvalid](validation.md#setwidgetasinvalid)</td>
<td>
Sets a widget as invalid, with a given validation message.
</td>
</tr>
<tr>
<td>[setWidgetAsValid](validation.md#setwidgetasvalid)</td>
<td>
Sets a widget as valid.
</td>
</tr>
</tbody>
</table>

## Methods

### isWidgetValid

**isWidgetValid(widgetId: string): boolean**

Checks if a given widget is currently valid.

Parameters:

* **widgetId**: string<br/> The id of the widget to check for validity.

Returns: boolean

Returns `true` if the widget identified by `widgetId` is valid.

### setWidgetAsInvalid

**setWidgetAsInvalid(widgetId: string, validationMessage: string): void**

Sets a widget as invalid, with a given validation message.

Parameters:

* **widgetId**: string<br/> The id of the widget to mark as invalid.
* **validationMessage**: string<br/> The validation message.

Returns: void

### setWidgetAsValid

**setWidgetAsValid(widgetId: string): void**

Sets a widget as valid.

Parameters:

* **widgetId**: string<br/> The id of the widget to set as valid.

Returns: void

