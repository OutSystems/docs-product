---
tags: runtime-mobileandreactiveweb;  
summary: Advanced use cases for the Date Picker UI Pattern.
locale: en-us
guid: 0134e6e2-5319-4f34-9f72-5a137e9971a4
app_type: mobile apps, reactive web apps
---

# Date Picker Reference

<div class="info" markdown="1">

Applies only to Mobile Apps and Reactive Web Apps

</div>

## Events

| **Event Name** |  **Description** |  **Mandatory**  |
| ---|---|--- |  
| OnSelect | Action to execute after selecting a DatePicker day. If SelectInterval is enabled, both parameters return values. If not, only the StartDate has a value.  |  True  |
  
## Layout and Classes

![](images/datepicker-layout-classes-diag.png)

## CSS Selectors

| **Element** |  **CSS Class** |  **Description**  |
|---|---|---  
| td | .is-selected  | Clicked day. | 
| td | .is-startrange  | If SelectInterval is True , this class will be the start range value.  |

