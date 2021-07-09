---
tags: runtime-mobileandreactiveweb;  
summary: Displays content (such as cards) in a specific set of columns, configurable per device type and orientation. 
---

# Gallery

You can use the Gallery UI Pattern to display groups of content. This UI pattern allows users to sequentially browse images, with the notion of a beginning and an end.

## How to use the Gallery UI Pattern

1. In Service Studio, in the Toolbox, search for `Gallery`.

    The Gallery widget is displayed.

    ![](<images/gallerymob-8-ss.png>)

1. From the Toolbox, drag the Gallery widget into the Main Content area of your application's screen.

    ![](<images/gallerymob-9-ss.png>)

1. Add the required content to the Gallery widget.

    By default, the Gallery widget expects a list.

    ![](<images/gallerymob-13-ss.png>)

    To use the Gallery UI Pattern with items from a database, drag a [List](<../../../../../ref/lang/auto/ServiceStudio.Plugin.NRWidgets.List.final.md>) into the Gallery widget and create your custom content.

    In this example, we delete the list and add local images to the Gallery widget.

    ![](<images/gallerymob-10-ss.png>)

1. On the Element tree, select the Image widget, and on the **Properties** tab, from the **Image** drop-down, select or import the image you want in the Gallery.

    Note: In this example, the image property Type is set to **Local** image. You can also add External and Binary Data images.

    ![](<images/gallerymob-11-ss.png>)
  
1. On the **Properties** tab, set the relevant (optional) properties, for example, the number of items you want to display on each device (see below for examples) and the space between each item (GutterSize).

    ![](<images/gallerymob-12-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

**4 items per row**

![](<images/gallerymob-14-ss.png>)

**3 items per row**
    
![](<images/gallerymob-15-ss.png>)

**2 items per row**

![](<images/gallerymob-16-ss.png>)

**1 item per row**

![](<images/gallerymob-17-ss.png>)

## Properties

| Property | Description |
|---|---|
| ItemInPhone (Integer): Optional |  Number of items displayed on a phone. <p>Examples<ul><li>_Blank_ - 1 item is displayed. This is the default value.</li><li>_2_ - 2 items are displayed.</li></ul></p> |
| ItemsInTablet (Integer):  |  Number of items displayed on a tablet. <p>Examples<ul><li>_Blank_ - 3 items are displayed. This is the default value.</li><li>_2_ - 1 item is displayed.</li></ul></p> |
| ItemsInDesktop (Integer):  |  Number of items displayed on a desktop. <p>Examples<ul><li>_Blank_ - 4 items are displayed. This is the default value.</li><li>_3_ - 3 items are displayed.</li></ul></p> |
| GutterSize (Space Identifier): Optional  | Defines the space between the items. The predefined sizes are:<p><ul><li>None</li><li>Extra Small</li><li>Small</li><li>Base</li><li>Medium</li><li>Large</li><li>Extra Large</li><li>Extra Extra Large</li></ul></p><p>Examples<ul><li>_Blank_ - A space of 16px between each item. This is the default value (_Entities.Space.Base_). </li><li>_Entities.Space.Large_ - A space of 32px between each item.</li></ul></p> |
