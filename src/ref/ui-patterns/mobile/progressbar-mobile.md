---
tags: ui patterns, css naming conventions, outsystems ui, progress bars, api
summary: Explore the structured use and customization of the Progress Bar in OutSystems 11 (O11) for Mobile and Reactive Web Apps.
locale: en-us
guid: fdef91ac-b3e1-4e49-a652-7921c46c9b35
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?type=design&node-id=1317%3A1554&mode=design&t=xOFe93sVU3cU3chE-1
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Progress Bar Reference

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

## Structure

OutSystems UI Patterns follow the [BEM convention](http://getbem.com/introduction/) for naming CSS classes and structures:

* ``osui-§{pattern-name}__§{pattern-element}``

* ``osui-§{pattern-name}__§{pattern-element}-is/has§{pattern-modifier}``

**Progress Bar block structure**

![Diagram illustrating the structure of the Progress Bar block in OutSystems UI Patterns](images/progressbar-diag.png "Progress Bar Block Structure Diagram")

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
|SetProgressBarValue|Sets a value on the Progress Bar. By using this action, you can set the Progress Bar’s value without changing the original value of the Progress Bar.|<ul><li>WidgetId: string </li><li>Progress: integer</li></ul>|

## API

For advanced users, you can use the Progress Bar API (OutSystems.OSUI.Patterns.ProgressBarAPI) for more advanced use cases.

### Methods

|**Function**|**Description**|**Parameters**|
|---|---|---|
|ChangeProperty|Changes the property of a given progress bar.|<ul><li>progressId: string</li><li> propertyName: string</li><li>propertyValue: any</li></ul>|
|Create|Creates the new progress instance and adds it to the ProgressMap.|<ul> <li>progressId: string</li><li>configs: string</li></ul>|
|Destroy|Destroys the instance of the given Progress.|<ul><li>progressId: string</li></ul>|
|GetAllProgressItemsMap|Returns the Map with all the Progress instances on the page.|<ul><li>Returns array of Ids</li></ul>|
|GetProgressById|Gets the instance of Progress, by a given ID.|<ul><li>progressId: string</li></ul>|
|Initialize|Initializes the pattern instance.|<ul><li>progressId: string</li></ul>|
|SetProgressBarValue|Sets a value on the progress bar.|<ul><li>progressId: string</li><li>progress: number</li></ul>|

