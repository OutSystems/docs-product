---
tags: runtime-mobileandreactiveweb;  
summary: A marker is added to the Map component when the user clicks the map. 
---

# How to add a marker on map click 

**Prerequisites**

* Download and install the [OutSystems Map component](https://www.outsystems.com/forge/component-overview/9909/outsystems-maps) from Forge.

This example demonstrates how to get the coordinates of a location when the user clicks the map.

1. In Service Studio, in the Toolbox, search for `Map`.

    The Map widget is displayed.

    ![Map in the Service Studio toolbar](<images/map-widget-ss.png>)

    If the UI widget does not display, it may be because you used a ready-made app, which deletes unused widgets from the module. To make additional widgets available in your app:

    a. Go to **Module > Manage dependencies**.

    b. Search for and select the relevant Producer, for example OutSystemsUI. Ensure Show All is selected. 

    c. On the Public elements for the selected Producer displayed on the right, ensure Show All is selected.
    
    d. Search for and select the element you want to add, and click **Apply**. 
    
    e. In Service Studio, in the Toolbox, search for the widget again.

1. From the Toolbox, drag the Map widget into the Main Content area of your application's screen.

    ![Drag Map widget onto the screen](<images/map-drag-ss.png>)

1. On the **Properties** tab, enter an API key so that the "For development purposes" watermark is removed. 

    ![Enter API key](<images/map-apikey-ss.png>)

1. Drag the **Map Event** block inside the **Events_Placeholder**.

    ![Drag Map Event onto the screen](<images/map-addmarker-event-ss.png>)

1. On the **Properties** tab, set the **EventName** property to **Click**. 

    This allows you to handle the event every time the user clicks the map.

    ![Set EventName to Click ](<images/map-addmarker-click-ss.png>)
        
1. Create a handler for the event.

    ![Create a handler for the event ](<images/map-addmarker-action-ss.png>)
    
1. Create two new local variables (Latitude and Longitude) to store the new coordinate values.

    ![Create 2 new variables](<images/map-variables-ss.png>)

1. From the Toolbox, drag the Marker block onto the Drag markers here screen area.
    
    On the **Properties** tab, set the **Position** property to Latitude + "," + Longitude

1. Create a handler for the event and assign the new marker coordinates to the variables. 

    ![Add an Assign to the event handler](<images/map-handler-ss.png>)

After following these steps and publishing the module, you can test the component in your app.
   
**Result**

![Result](<images/map-draggable-result-ss.png>)
