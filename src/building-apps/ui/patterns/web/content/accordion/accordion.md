---
tags: runtime-traditionalweb; 
summary: Accordion expands vertically-stacked content by clicking on the header.
locale: en-us
guid: 6f52287b-c093-4b03-84f9-ac1e7ea57152
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing-an-Application?type=design&node-id=222%3A24&mode=design&t=ANpsYvOCthr9AWot-1
---

# Accordion

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

You can use the Accordion UI Pattern to allow users expand and hide content when clicked.

 ![Example of an Accordion UI Pattern in a Traditional Web Application](images/accordion-image-2.png "Accordion UI Pattern in Traditional Web App")

**How to use the Accordion UI Pattern**

1. In Service Studio, in the Toolbox, search for `Accordion`.

    The Accordion widget is displayed.

    ![Accordion widget displayed in the Service Studio toolbox](images/accordion-image-4.png "Accordion Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**.
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Accordion widget into the Main Content area of your application's screen.

    ![Dragging the Accordion widget into the main content area of an application screen](images/accordion-image-5.png "Dragging Accordion Widget into Main Content Area")

    Note: By default, the Accordion widget contains 3 Accordion Item widgets. You can add or delete Accordion Items as required.

    ![Default Accordion widget containing three Accordion Item widgets](images/accordion-image-1.png "Default Accordion Widget with 3 Items")

1. Add the relevant content to the Accordion Item placeholders, for example, FAQs.
  
    ![Adding content to the Accordion Item placeholders, such as FAQs](images/accordion-image-3.png "Adding Content to Accordion Item")

1. After following these steps and publishing the module, you can test the pattern in your app.

## Demo

<iframe width="750" height="500" src="https://www.youtube.com/embed/FWTZ2tLVlfE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen"></iframe>

## Properties

### Accordion

| **Property** | **Description** |
|---|---|
| MultipleItems (Boolean): Optional | If set to True, multiple Accordion Items can be open at the same time. If set to False, only one Accordion Item can be open at any time. This is the default value. |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |

### Accordion Item

| **Property** | **Description** |
|---|---|
| IsOpen (Boolean): Optional | If set to True, when rendering, the Accordion Item is open. If set to False, the Accordion Item is closed. This is the default value. |
| IsDisable (Boolean): Optional | If set to True, the Accordion Item cannot be clicked. If set to False, the Accordion Item is clickable. This is the default value. |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied. </li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
