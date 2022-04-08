---
tags: runtime-mobileandreactiveweb
summary: Provides methods to deal with active view components and their state.
locale: en-us
guid: 5d68d556-eca2-4dad-a0e5-ba6decc5f22b
---

# View

Provides methods to deal with active view components and their state.

## Hierarchy

**View**

## Summary

|Methods|Description|
|---|---|
|[getCurrentScreenRootElement](view.md#getcurrentscreenrootelement)|Returns the current screen DOM element. Used for class tweaks through DOM manipulation for animations.|
|[registerDeviceClassGetter](view.md#registerdeviceclassgetter)|Register a function that provides a list of classes to apply to the document `body`. Expected classes to be returned are `portrait` or `landscape` — for orientation — and `phone` or `tablet` for device type. The method provided may emit other classes.|
|[render](view.md#render)|Returns a `Promise` that will be resolved when the screen/block has been rendered with current model changes. Used to execute logic after the browser has rendered the current changes.|
|[wasCurrentViewRestoredFromCache](view.md#wascurrentviewrestoredfromcache)|Checks if the current view state was restored from cache.|

## Methods

### getCurrentScreenRootElement

**getCurrentScreenRootElement(): Element**

Returns the current screen DOM element. Used for class tweaks through DOM manipulation for animations.

Between transitions there are two screens (the one leaving and the one entering), and this function will return the entering screen.

Example:

```javascript
// add custom class 'slide' to screen DOM element
$public.View.getCurrentScreenRootElement().classList.add("slide");
```

Returns: Element

### registerDeviceClassGetter

**registerDeviceClassGetter(getter: function): void**

Register a function that provides a list of classes to apply to the document `body`. Expected classes to be returned are `portrait` or `landscape` — for orientation — and `phone` or `tablet` for device type. The method provided may emit other classes.

This method will be called upon whenever certain events, such as device orientation changes. All classes returned in previous calls will be removed before applying results of new calls.

Parameters:

* **getter**: function<br/> Method that returns current orientation and device classes to apply.

Returns: void

### render

**render(): Promise&lt;void&gt;**

Returns a `Promise` that will be resolved when the screen/block has been rendered with current model changes. Used to execute logic after the browser has rendered the current changes.

Returns: Promise&lt;void&gt;

`Promise` resolved when the screen/block has been rendered with current model changes.

### wasCurrentViewRestoredFromCache

**wasCurrentViewRestoredFromCache(): boolean**

Checks if the current view state was restored from cache.

Returns: boolean

Returns `true` when the current view state was restored from cache, or `false` otherwise.

