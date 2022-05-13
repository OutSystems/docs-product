---
tags: runtime-mobileandreactiveweb;  
summary: A marker is added to the Map component when the user clicks the map. 
locale: en-us
guid: 64103ccc-9190-4483-8145-3f063dd1b823
app_type: mobile apps, reactive web apps
---

# How to add a marker on map click 

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

**Prerequisites**

* Download and install the [OutSystems Map component](https://www.outsystems.com/forge/component-overview/9909/outsystems-maps) from Forge.

This example demonstrates how to get the coordinates of a location when the user clicks the map.

1. In Service Studio, in the Toolbox, search for `Map`.

    The Map widget is displayed.

    ![Map in the Service Studio toolbar](<images/map-widget-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

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

1. Create a handler for the event and assign the new marker coordinates to the variables. 

    ![Add an Assign to the event handler](<images/map-handler-ss.png>)

After following these steps and publishing the module, you can test the component in your app.
   
**Result**

![Result](<images/map-draggable-result-ss.png>)
