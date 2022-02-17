---
tags: runtime-mobileandreactiveweb; 
summary: Advanced use cases for the Progress Bar
---

# Progress Bar Reference

## Structure

OutSystems UI Patterns follow the [BEM convention](http://getbem.com/introduction/) for naming CSS classes and structures:

* ``osui-§{pattern-name}__§{pattern-element}``

* ``osui-§{pattern-name}__§{pattern-element}-is/has§{pattern-modifier}``

**Progress Bar block structure**

![Progress Bar Structure](images/progressbar-diag.png)

### Modifiers

|**Modifier**|**Attribute**|**Element**|
|---|---|---|
|ProgressColor|--progress-color|.osui-progress-bar|
|TrailColor|--trail-color|.osui-progress-bar|
|Thickness|--thickness|.osui-progress-bar|
|Shape|–shape|.osui-progress-bar|


## Client actions

|**Client action**|**Description**|**Parameters**|
|---|---|---|
|SetProgressBarValue|Sets a value on the Progress Bar. By using this action, you can set the Progress Bar’s value without changing the original value of the Progress Bar.|<li>WidgetId: string </li><li>Progress: integer</li>|

## API

For advanced users, you can use the Progress Bar API (OutSystems.OSUI.Patterns.ProgressBarAPI) for more advanced use cases.

### Methods

|**Function**|**Description**|**Parameters**|
|---|---|---|
|ChangeProperty|Changes the property of a given progress bar.|<ul><li>progressId: string</li><li> propertyName: string</li><li>propertyValue: any</li></ul>|
|Create|Creates the new progress instance and adds it to the ProgressMap.| <li>progressId: string</li>
configs: string|
|Destroy|Destroys the instance of the given Progress.|<li>progressId: string</li>|
|GetAllProgressItemsMap|FuReturns the Map with all the Progress instances on the page.|<li>Returns array of Ids</li>|
|GetProgressById|Gets the instance of Progress, by a given ID.|<li>progressId: string</li>|
|Initialize|Initializes the pattern instance.|<li>progressId: string</li>|
|SetProgressBarValue|Sets a value on the progress bar.|<li>progressId: string</li><li>progress: number</li>|

