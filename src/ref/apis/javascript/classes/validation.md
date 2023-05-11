---
tags: runtime-mobileandreactiveweb
summary: Provides methods to show validation messages on widgets and set their validation values. Used when validating widgets inside iterators, since it's not possible to do it in the usual way.
locale: en-us
guid: 68b5f614-594d-4374-bde6-fc2f815c8b05
app_type: mobile apps, reactive web apps
platform-version: o11
---

# Validation

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

Provides methods to show validation messages on widgets and set their validation values. Used when validating widgets inside iterators, since it's not possible to do it in the usual way.

## Hierarchy

**Validation**

## Summary

|Methods|Description|
|---|---|
|[isWidgetValid](validation.md#iswidgetvalid)|Checks if a given widget is currently valid.|
|[setWidgetAsInvalid](validation.md#setwidgetasinvalid)|Sets a widget as invalid, with a given validation message.|
|[setWidgetAsValid](validation.md#setwidgetasvalid)|Sets a widget as valid.|

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

