---
tags: runtime-mobileandreactiveweb;  
summary: A marker is added to the Map component when the user clicks the map. 
locale: en-us
guid: 64103ccc-9190-4483-8145-3f063dd1b823
app_type: mobile apps, reactive web apps
platform-version: o11
figma:
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

    ![Screenshot of the Map widget in the Service Studio toolbar](images/map-widget-ss.png "Map Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsMaps** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Map widget into the Main Content area of your application's screen.

    ![Dragging the Map widget from the toolbox into the main content area of the application screen](images/map-drag-ss.png "Dragging Map Widget onto the Screen")

1. On the **Properties** tab, enter an API key so that the "For development purposes" watermark is removed. 

    ![Entering an API key in the Properties tab to remove the 'For development purposes' watermark from the Map widget](images/map-apikey-ss.png "Entering API Key for Map Widget")

1. Drag the **Map Event** block inside the **Events_Placeholder**.

    ![Dragging the Map Event block into the Events_Placeholder on the application screen](images/map-addmarker-event-ss.png "Adding Map Event Block")

1. On the **Properties** tab, set the **EventName** property to **Click**. 

    This allows you to handle the event every time the user clicks the map.

    ![Setting the EventName property to 'Click' on the Properties tab for the Map Event block](images/map-addmarker-click-ss.png "Setting EventName to Click")
        
1. Create a handler for the event.

    ![Creating a handler for the map click event in the application](images/map-addmarker-action-ss.png "Creating Event Handler")
    
1. Create two new local variables (Latitude and Longitude) to store the new coordinate values.

    ![Creating two new local variables named Latitude and Longitude to store coordinate values](images/map-variables-ss.png "Creating Latitude and Longitude Variables")

1. From the Toolbox, drag the Marker block onto the Drag markers here screen area.
    
    On the **Properties** tab, set the **Position** property to Latitude + "," + Longitude

1. Create a handler for the event and assign the new marker coordinates to the variables. 

    ![Adding an Assign action to the event handler to set the new marker coordinates to the Latitude and Longitude variables](images/map-handler-ss.png "Assigning Marker Coordinates")

After following these steps and publishing the module, you can test the component in your app.
   
**Result**

![Final result showing a draggable marker added to the map in the application](images/map-draggable-result-ss.png "Map with Draggable Marker Result")
