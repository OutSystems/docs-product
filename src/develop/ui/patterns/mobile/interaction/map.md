---
tags: runtime-mobileandreactiveweb;  
summary: Use the Map pattern to ad Google Map to your app.
---

# Map

You can use the Map UI Pattern to provide an interactive satellite map to you users. 

<div class="info" markdown="1>

Google Maps isn’t free. You must always buy an API key. For more info on getting an API Key, see https://developers.google.com/maps/documentation/javascript/get-api-key.

</div>

**How to use the Map UI Pattern**

1. In Service Studio, in the Toolbox, search for `Map`.

    The Map widget is displayed.

    ![Map in the Service Studio toolbar](<images/map-1-ss.png>)

1. From the Toolbox, drag the Map widget into the Main Content area of your application's screen.

    ![Map pattern in the preview screen](<images/map-2-ss.png>)

1. You can you can change the Map's look and feel by setting the (optional) properties.

    In this example, we enter an API key so that the "For development purposes" watermark is removed. We also enter the latitude and longitude coordinates for Lisbon (38.71667, -9.13333) in the **Location** and the **Marker Location** properties. Finally, we set the **Zoom** property to zoom on a city level when the page is loaded.

    ![Map preview with properties](<images/map-3-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
| APIKey (Text): Optional  | Add a Google Maps API key to display the map correctly and remove the development purpose watermark. You can get an API key for Google Maps here: <https://developers.google.com/maps/documentation/javascript/get-api-key> |
| Location (Text): Optional  | Defines where the map is centered. You can input addresses or coordinates (latitude and longitude). By default, the map automatically adjusts to show all markers. You can override this by **Location** and **Zoom** properties. To add markers, drag the MapMarker block into the Content placeholder. | 
| Markers (Marker List): Optional | Sets a location on the map. By default, the marker uses the Google Maps default marker. For more information, see https://developers.google.com/maps/documentation/javascript/markers  |
| Zoom (Zoom Identifier): No | Sets the zoom level to apply to the map, with the levels ranging from 1 (world) to 20 (building). <p>Examples <ul><li>Auto: Fit to all markers present on the map. This is the default.</li><li>Zoom1: World</li><li>Zoom5: Continent</li><li>Zoom10: City</li><li>Zoom15: Streets</li><li>Zoom20: Buildings</li></ul></p><p>For more information, see https://developers.google.com/maps/documentation/javascript/overview#zoom-levels </p> |
| Height (Text): Optional | Sets the height of the map in pixels ("300px"), percentage ("100%"), or viewport height ("100vh"). If this property is left empty, the map fits to the parent height Of using percentages, ensure that the map has a parent with a fixed height value, otherwise, its height is 0. The height property value is applied to a CSS variable ued on the OutSystems UI Theme. This variable can be overridden to manipulate the maps height on your CSS theme.  |
| Style (Style Identifier): Optional | Sets the theme type based on themes provided by Google Maps. To create your own style or to change the theme options, see https://mapstyle.withgoogle.com/. When your custom theme is ready, use the **AdvancedFormat** property to apply it. Note that any style applied won't be visible if the **Satellite** type is selected. For more information, see https://developers.google.com/maps/documentation/javascript/styling. The available styles are as follows: <p><li>Standard (default)</li><li>Silver</li><li>Retro</li><li>Dark</li><li>Night</li><li>Aubergine</li></p>|
| Type (Type Identifier): Optional | Sets the map type to either roadmap (default), satellite, hybrid, or terrain, provided by Google Maps. For more information, see https://developers.google.com/maps/documentation/javascript/maptypes. |
| Offset (Offset): Optional  | Expand the options to set the Offset(X) vertical and the Offset(Y) horizontal in pixels to apply to a map. This is applied based on the defined **Location**.   |
| StaticMap (Boolean): Optional | If True, the map is not interactive. If False, the map is interactive. This is the default. The static map API has limitations. For more information, see  https://developers.google.com/maps/documentation/maps-static/start.  |
| ShowTraffic (Boolean): Optional | If True, traffic mode is enabled on the map. If False, traffic mode is not enabled. This is the default. |
| AdvancedFormat (Text): Optional  | Allows for more options beyond what's provided through the input parameters. For more information, see https://developers.google.com/maps/documentation/javascript/controls. |
| ExtendedClass (Text): Optional| Adds custom style classes to the block. |
