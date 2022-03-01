---
tags: runtime-mobileandreactiveweb;  
summary: Advanced use cases for the Progress Circle UI Pattern.
---

# Progress Circle Reference
 
## Structure

![Structure diagram](images/progresscircle-diag.png)

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
|ChangeProperty|Changes the property of a given Progress Circle.|<li>progressId: string</li><li>propertyName: string</li><li>propertyValue: any</li>|  
|Create|Create the new Progress Circle instance and add it to the progressMap.|<li>progressId: string</li>configs: string<li></li>|  
|Destroy|Destroys the instance of the given Progress Circle.|<li>progressId: string</li>|  
|GetAllProgressItemsMap|Return the Map with all the Progress Circle instances on the page.|<li>Returns array of Ids</li>|  
|GetProgressById|Gets the instance of the Progress Circle by a given Id.|<li>progressId: string</li>|  
|Initialize|Initializes the pattern instance.|<li>progressId: string</li>|  
 

