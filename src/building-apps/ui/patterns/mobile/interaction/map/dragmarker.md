---
tags: ide usage, reactive web apps, tutorials for beginners, mapping, ui components
summary: Learn how to retrieve draggable marker coordinates in OutSystems 11 (O11) using the OutSystems Map component for Mobile and Reactive Web Apps.
locale: en-us
guid: b7dce067-3d75-4c88-8a92-9de144f97896
app_type: mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
  - forge
coverage-type:
  - apply
---

# How to get draggable marker coordinates  

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

**Prerequisites**

* Download and install the [OutSystems Map component](https://www.outsystems.com/forge/component-overview/9909/outsystems-maps) from Forge.

This example demonstrates how to change the location of a map marker and get the coordinates of the new location.

1. In Service Studio, in the Toolbox, search for `Map`.

    The Map widget is displayed.

    ![Screenshot of the Map widget in the Service Studio toolbar](images/map-widget-ss.png "Map Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Map widget into the Main Content area of your application's screen.

    ![Dragging the Map widget from the toolbox onto the main content area of the application screen](images/map-drag-ss.png "Dragging Map Widget onto the Screen")

1. On the **Properties** tab, enter an API key so that the "For development purposes" watermark is removed. 

    ![Entering an API key in the Properties tab to remove the development watermark from the Map widget](images/map-apikey-ss.png "Entering API Key for Map Widget")

1. From the Toolbox, drag the Marker block onto the **Drag markers here** screen area.

    ![Dragging the Marker block onto the Drag markers here area of the Map widget screen](images/map-marker-ss.png "Placing Marker Block on the Map")

1. On the **Properties** tab, define the Marker's initial coordinates in the **Position** property. 

    ![Defining the initial coordinates of the Marker in the Position property on the Properties tab](images/map-position-ss.png "Defining Marker's Initial Coordinates")

1. To allow users to move a marker, expand the **OptionalConfigs** and set **AllowDrag** to True.

    ![Setting AllowDrag to True in the OptionalConfigs to enable dragging of the map marker](images/map-draggable-ss.png "Enabling Marker Dragging")

1.  To get the new marker coordinates, drag the **Marker Event** block inside the **MarkerEvents** placeholder and on the **Properties** tab, set the **EventName** property as **DragEnd**.

    ![Dragging the Marker Event block inside the MarkerEvents placeholder and setting the EventName property to DragEnd](images/map-markerevent-ss.png "Setting Up Marker DragEnd Event")

1. Create two new local variables (Latitude and Longitude) to store the new coordinate values.

    ![Creating two new local variables for Latitude and Longitude to store new marker coordinates](images/map-variables-ss.png "Creating Latitude and Longitude Variables")

1. Create a handler for the event and assign the new marker coordinates to the variables.

    ![Creating a handler for the DragEnd event to assign new marker coordinates to the Latitude and Longitude variables](images/map-handler-ss.png "Creating Event Handler for New Coordinates")

1. Add two expression widgets to the screen with the **Latitude** and **Longitude** variables to display the marker coordinates in your application. 

    ![Adding expression widgets to the screen to display the new Latitude and Longitude marker coordinates](images/map-expression-ss.png "Displaying New Marker Coordinates")

1. On the **Properties** tab, set the new variables **Default value** to the Boston US office (Latitude: 42.351657835 Longitude: -71.046881100).

    ![Setting the default values of the new variables to the coordinates of the Boston US office on the Properties tab](images/map-draggable-varcoord-ss.png "Setting Default Variable Values")

After following these steps and publishing the module, you can test the component in your app.

**Result**

![Final result showing the draggable marker on the map within the application](images/map-draggable-result-ss.png "Final Result of Draggable Marker")
