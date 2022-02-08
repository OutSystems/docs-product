---
tags: runtime-mobileandreactiveweb; 
summary: Advanced use cases for the Progress Bar
---

# Progress Bar Reference

## Structure

OutSystems UI Patterns follow the [BEM convention](http://getbem.com/introduction/) for naming CSS classes and structures.
* osui-§{pattern-name}__§{pattern-element}
* osui-§{pattern-name}__§{pattern-element}-is/has§{pattern-modifier}

**Base Progress Bar block structure**

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
|SetProgressBarValue|Use this action to set a value on the progress bar whenever you feel like it. <br/> By using this action, you can set the progress bar’s value without changing the original value of the progress bar.|<li>WidgetId: string </li><li>Progress: integer</li>|

## API

For advanced users, you can use the  Progress Bar API (OutSystems.OSUI.Patterns.ProgressBarAPI) for more advanced use-cases.


### Methods

|**Function**|**Description**|**Parameters**|
|---|---|---|
|ChangeProperty|Function that will change the property of a given ProgressBar.|<ul><li>progressId: string</li><li> propertyName: string</li><li>propertyValue: any</li></ul>|
|Create|Create the new Progress instance and add it to the progressMap.| <li>progressId: string</li>
configs: string|
|Destroy|Function that will destroy the instance of the given Progress|<li>progressId: string</li>|
|GetAllProgressItemsMap|Function that will return the Map with all the Progress instances at the page|<li>Returns array of Ids</li>|
|GetProgressById|Function that gets the instance of Progress, by a given ID.|<li>progressId: string</li>|
|Initialize|Function that will initialize the pattern instance.|<li>progressId: string</li>|
|SetProgressBarValue|Set a value on the progress bar.|<li>progressId: string</li><li>progress: number</li>|

