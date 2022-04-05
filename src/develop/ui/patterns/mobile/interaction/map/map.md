---
tags: runtime-mobileandreactiveweb;  
summary: Use the Map pattern to add Google Maps to your app.
---

# How to use the Map component

**Prerequisites**

* Download and install the [OutSystems Map component](https://www.outsystems.com/forge/component-overview/9909/outsystems-maps) from Forge.

You can use the Map component to provide an interactive satellite map to your users. 

<div class="info" markdown="1" >

Currently, only Google Maps is supported. Google Maps isn’t free. You must always buy an API key. For more info on getting an API Key, see [Using API Keys](https://developers.google.com/maps/documentation/javascript/get-api-key).

</div>

This example demonstrates how to highlight OutSystems office locations around the world on the OutSystems Map component using Markers. 

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

1. Create an aggregate (GetOffices) that fetches the office location data.

    ![Create an aggregate](<images/map-aggregate-ss.png>)

1. Drag the **List** widget onto the **Drag markers here** screen area and on the **Properties** tab, enter the List widget source (the list of offices). 

    ![Drag List widget onto the screen](<images/map-list-ss.png>)

1. Drag the **Marker** block into the **List** widget. On the **Properties** tab, from the **Position** dropdown, select the office address property.

    **Note:** Marker blocks can only be added to the Map block. To add markers to a Static Map, you can use the Markers input parameter.

    ![Drag Marker block onto the screen](<images/map-marker-ss.png>)

1. You can change the Map's look and feel by setting the (Optional) properties on the **Properties** tab.

After following these steps and publishing the module, you can test the component in your app.

**Result**

![Result](<images/map-result.png>)

## Properties

| Property | Description |
|---|---|
| APIKey (Text): Optional  | Add a Google Maps API key to display the map correctly and remove the development purpose watermark. You can get an API key for Google Maps [here](https://developers.google.com/maps/documentation/javascript/get-api-key). |
| Center (Text): Optional  | Defines where the map is centered. Works with addresses and coordinates (latitude and longitude).<br/><br/>If left empty, the default location is the OutSystems Boston office. Note that the map automatically adjusts to show all markers by default. You can override this by setting the **Location** and **Zoom** properties.<br/><br/>On maps with markers, the default location is the location of the first marker on the list. | 
| Markers (Marker List): Optional | Sets a location on the map. By default, the marker uses the Google Maps default marker. For more information, see [Google Markers](https://developers.google.com/maps/documentation/javascript/markers). |
| Zoom (Zoom Identifier): Optional | Sets the zoom level to apply to the map, with the levels ranging from 1 (world) to 20 (building). <br/><br/>Examples <ul><li>Auto: Fit to all markers present on the map. This is the default.</li><li>Zoom1: World</li><li>Zoom5: Continent</li><li>Zoom10: City</li><li>Zoom15: Streets</li><li>Zoom20: Buildings</li></ul><br/>For more information, see [Google Zoom Levels](https://developers.google.com/maps/documentation/javascript/overview#zoom-levels). |
| Height (Text): Optional |Sets the height of the map in pixels ("300px"), percentage ("100%"), or viewport height ("100vh"). If this property is left empty, the map fits to the parent height.<br/><br/>If using percentages, ensure that the map has a parent with a fixed height value, otherwise, its height is 0 (zero). <br/><br/>The height property value is applied to a CSS variable used on the OutSystems UI Theme. This variable can be overridden to manipulate the maps height on your CSS theme. |
| Style (Style Identifier): Optional | Sets the theme type based on themes provided by Google Maps. To create your own style, or to change the theme options, see [Map Style with Google](https://mapstyle.withgoogle.com/). When your custom theme is ready, use the **AdvancedFormat** property to apply it.<br/> **Note:** Any style applied is not visible if the **Satellite** type is selected.<br/><br/>The available styles are as follows: <ul><li>Standard (default)</li><li>Silver</li><li>Retro</li><li>Dark</li><li>Night</li><li>Aubergine</li></ul><br/> For more information, see [Styling your maps](https://developers.google.com/maps/documentation/javascript/styling). |
| Type (Type Identifier): Optional | Sets the map type to either roadmap (default), satellite, hybrid, or terrain, provided by Google Maps. For more information, see [Google Map Types](https://developers.google.com/maps/documentation/javascript/maptypes). |
| Offset (Offset): Optional  | Expand the options to set the Offset(X) vertical and the Offset(Y) horizontal in pixels to apply to a map. This is applied based on the defined **Location**.   |
| StaticMap (Boolean): Optional | If True, the map is not interactive. If False, the map is interactive. (False is the default.) The static map API has the following limitations:<br/><ul><li>The **AdvancedFormat** property only works when applying a custom style to the map</li><li>The **Offset** property doesn't work when the **StaticMap** property is set to True</li><li>The static map doesn't react in runtime, switching the value on **StaticMap** property</li><li>Google Maps API has a URL Size Restriction (8192 characters)</li></ul><br/>For more information, see [Maps Static API](https://developers.google.com/maps/documentation/maps-static/start).  |
| ShowTraffic (Boolean): Optional | If True, traffic mode is enabled on the map. If False, traffic mode is not enabled. (False is the default.) |
| AdvancedFormat (Text): Optional  | Allows for more options beyond what's provided through the input parameters. For more information, see [Google Controls](https://developers.google.com/maps/documentation/javascript/controls). |
| ExtendedClass | Adds custom style classes to the component. You define your [custom style classes](../../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/><ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |


