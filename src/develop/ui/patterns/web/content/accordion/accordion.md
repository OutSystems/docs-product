---
tags: runtime-traditionalweb; 
summary: Accordion expands vertically-stacked content by clicking on the header.
---

# Accordion

You can use the Accordion UI Pattern to allow users expand and hide content when clicked.

 ![](<images/accordion-image-2.png>)

**How to use the Accordion UI Pattern**

1. In Service Studio, in the Toolbox, search for `Accordion`.

    The Accordion widget is displayed.

    ![](<images/accordion-image-4.png>)

    If the UI widget does not display, it may be because you used a ready-made app, which deletes unused widgets from the module. To make additional widgets available in your app:

    a. Go to **Module > Manage dependencies**.

    b. Search for and select the relevant Producer, for example OutSystemsUI. Ensure Show All is selected. 

    c. On the Public elements for the selected Producer displayed on the right, ensure Show All is selected.
    
    d. Search for and select the element you want to add, and click **Apply**. 
    
    e. In Service Studio, in the Toolbox, search for the widget again.

1. From the Toolbox, drag the Accordion widget into the Main Content area of your application's screen.

    ![](<images/accordion-image-5.png>)

    Note: By default, the Accordion widget contains 3 Accordion Item widgets. You can add or delete Accordion Items as required.

    ![](<images/accordion-image-1.png>)

1. Add the relevant content to the Accordion Item placeholders, for example, FAQs. 
  
    ![](<images/accordion-image-3.png>)

1. After following these steps and publishing the module, you can test the pattern in your app. 

## Demo

<iframe width="750" height="500" src="https://www.youtube.com/embed/FWTZ2tLVlfE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen"></iframe>

## Properties

### Accordion

| **Property** |  **Description** |  
|---|---|
| MultipleItems (Boolean): Optional |  If set to True, multiple Accordion Items can be open at the same time. If set to False, only one Accordion Item can be open at any time. This is the default value. | 
| ExtendedClass (Text): Optional  |  Adds custom style classes to the Accordion UI Pattern. You define your [custom style classes](../../../../../../develop/ui/look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the Accordion UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Accordion UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |

### Accordion Item

| **Property** |  **Description** | 
|---|---|
| IsOpen (Boolean): Optional  |  If set to True, when rendering, the Accordion Item is open. If set to False, the Accordion Item is closed. This is the default value.|  
| IsDisable (Boolean): Optional  |  If set to True, the Accordion Item cannot be clicked. If set to False, the Accordion Item is clickable. This is the default value. |
| ExtendedClass (Text): Optional  |  Adds custom style classes to the Pattern. You define your [custom style classes](../../../../../../develop/ui/look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>_Blank_ No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied. </li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |



