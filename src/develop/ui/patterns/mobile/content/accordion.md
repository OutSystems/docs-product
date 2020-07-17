---
tags: runtime-mobileandreactiveweb;  
summary: Accordion expands vertically-stacked content by clicking on the header.
---

# Accordion

You can use the Accordion UI Pattern to allow users expand and hide content when clicked.

![](<images/accordion-2.png>)

**How to use the Accordion UI Pattern**

1. In Service Studio, in the Toolbox, search for `Accordion`.

    The Accordion widget is displayed.
    
    ![](<images/accordion-4-ss.png>)

1. From the Toolbox, drag the Accordion widget into the Main Content area of your application's screen.

    ![](<images/accordion-5-ss.png?width=800>)

    Note: By default, the Accordion widget contains 3 Accordion Item widgets. You can add or delete Accordion Items as required.

1. Add the relevant content to the Accordion Item placeholders. In this example, we add some FAQs. 
  
    ![](<images/accordion-3-ss.png>)

1. On the **Properties** tab, you can customize the Accordion's look and feel by setting any of the (optional) properties. 

After following these steps and publishing the module, you can test the pattern in your app. 

## Properties

### Accordion

| **Property** |  **Description** |  
|---|---|
| MultipleItems (Boolean): Optional |  If set to True, multiple Accordion Items can be open at the same time. If set to False, only one Accordion Item can be open at any time. This is the default value. |
| ExtendedClass (Text): Optional  |  Add custom style classes to the Accordion UI Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the Accordion UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Accordion UI styles being applied.</li></ul> |

### Accordion Item

| **Property** |  **Description** | 
|---|---|
| IsExpanded (Boolean): Optional  |  If set to True, when rendering, the Accordion Item is open. If set to False, the Accordion Item is closed. This is the default value.|  
| UsePadding (Boolean): Optional  |  If set to True, padding is applied to the content area. This is the default value. If set to False, the content area has no padding.|  
| IsDisabled (Boolean): Optional  |  If set to True, the Accordion Item cannot be clicked. If set to False, the Accordion Item is clickable. This is the default value. |
| ExtendedClass (Text): Optional  |  Add custom style classes to the Accordion Item UI Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>_Blank_ No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the Accordion Item UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Accordion Item UI styles being applied. </li></ul> |
