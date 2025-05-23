---
summary: Learn how to resolve the Grid Dimensions Overflow error in OutSystems 11 (O11) by adjusting widget width or grid settings.
locale: en-us
guid: c2b5c213-e7d5-4ddf-b8ef-445dd2612288
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: error handling, ui design, grid layout, outsystems theme customization, widget configuration
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Grid Dimensions Overflow Error

The **Grid Dimensions Overflow** error is issued in the following situation:

* The widget dimensions must be set within the grid boundaries
  
    The widget has the Width property set to 'col' and it is exceeding the number of columns defined in the theme's grid.
    
    Change the Width property so that the value is less than or equal to the grid size. Alternatively, change the Grid property of the theme to increase the number of columns of the grid.
