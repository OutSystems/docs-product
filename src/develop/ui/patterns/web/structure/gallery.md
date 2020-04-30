---
tags: runtime-traditionalweb; 
summary: Gallery enables the users to sequentially browse the content when there are many cards grouped into one or more collections.
---

# Gallery

You can use the Gallery UI Pattern to display groups of content. This UI pattern allows users to sequentially browse images, with the notion of a beginning and an end. 

![](<images/gallery-image-7.png>)

**How to use the Gallery UI Pattern**

The Gallery UI Pattern usually displays dynamic information. In most cases, prior to using this pattern, you will need [to retrieve or update the Data](../../../../../develop/data/intro.md) that contains the information you want to display onscreen. You do this by using an [Action](../../../../../develop/logic/action-web.md). 

1. In Service Studio, in the Toolbox, search for `Gallery`. 

    The Gallery widget is displayed.

    ![](<images/gallery-image-8.png>)

1. From the Toolbox, drag the Gallery widget into the Main Content area of your application's screen.

    ![](<images/gallery-image-9.png>)

1. Drag a [List Record](<../../../../../ref/lang/auto/Class.List Records Widget.md>) or static content into the Gallery widget.
    
    ![](<images/gallery-image-1.png>)

1. On the **Properties** tab, you can set the number of items to display on each row for different device types.
    
    ![](<images/gallery-image-6.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| **Property** |  **Description** |
|---|---|
| ItemsDesktop (Integer): Optional |  Number of Items per line on a desktop. | 
| ItemsTablet (Integer): Optional |  Number of Items per line on a tablet. | 
| ItemsPhone (Integer): Optional|  Number of Items per line on a phone. |
| ExtendedClass (Text): Optional | Add custom style classes to the Badge UI Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_''myclass''_ - Adds the myclass style to the Gallery UI styles being applied.</ui><li>_''myclass1'' ''myclass2''_ - Adds the _myclass1_ and _myclass2_ styles to the Gallery UI styles being applied.</li></ul></p> |  


## Additional notes

Line Separator for ListRecords should be **None**.

![](<images/gallery-image-4.png>)

