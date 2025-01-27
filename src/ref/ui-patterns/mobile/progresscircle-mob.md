---
tags: css customization, ui patterns, api usage, progress circle, outsystems ui framework
summary: Explore the CSS class structure and API methods of the Progress Circle UI Pattern in OutSystems 11 (O11) for advanced customization and control.
locale: en-us
guid: 7541fb66-768c-42c8-9d92-636b17d9f2f1
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?type=design&node-id=2863%3A282&mode=design&t=Cx8ecjAITJrQMvRn-1
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

# Progress Circle Reference
 
<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

## Structure

![Diagram illustrating the CSS class structure for the Progress Circle UI Pattern](images/progress-classes-diag.png "Progress Circle CSS Classes Diagram")

### Modifiers

|Event Name|Description|Mandatory| 
|---|---|---|  
|ProgressColor|--progress-color|.osui-progress-circle|  
|TrailColor|--trail-color|.osui-progress-circle|  
|Thickness|--thickness|.osui-progress-circle|  
|Size|--circle-size (width and height)|.osui-progress-circle|  

## API

If you are an advanced user, you might want to use our Progress Circle API (OutSystems.OSUI.Patterns.ProgressCircleAPI) for more advanced use cases. 

### Methods

|Function|Description|Parameters| 
|---|---|---|  
|ChangeProperty|Changes the property of a given Progress Circle.|<ul><li>progressId: string</li><li>propertyName: string</li><li>propertyValue: any</li></ul>|  
|Create|Create the new Progress Circle instance and add it to the progressMap.|<ul><li>progressId: string</li>configs: string<li></li></ul>|  
|Destroy|Destroys the instance of the given Progress Circle.|<ul><li>progressId: string</li></ul>|  
|GetAllProgressItemsMap|Return the Map with all the Progress Circle instances on the page.|<ul><li>Returns array of Ids</li></ul>|  
|GetProgressById|Gets the instance of the Progress Circle by a given Id.|<ul><li>progressId: string</li></ul>|  
|Initialize|Initializes the pattern instance.|<ul><li>progressId: string</li></ul>|  
 

