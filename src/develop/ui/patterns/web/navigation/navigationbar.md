---
tags: runtime-traditionalweb; 
summary: 
---

# Navigation Bar

You can use the Navigation Bar UI Pattern to organize the content and enable quick navigation through an application with vertically stacked links. These stacked links can be displayed with different hierarchy levels. 

You user this pattern when the end user needs to navigate through an application's main sections while maintaining the ability to browse to another subsection quickly. 

![](images/navigationbar-image-7.png)

**How to use the Navigation Bar UI Pattern**

1. In Service Studio, in the Toolbox, search for `Navigation Bar`. 

    The Navigation Bar widget is displayed.

      ![](images/navigationbar-image-6.png)

1. From the Toolbox, drag the Navigation Bar widget onto your application's screen. 

    ![](images/navigationbar-image-1.png?width=500)

1. Drag the required number of Navigation Bar Item blocks into the Content placeholder.

1. Drag the required number of Navigation Bar Sub Item blocks into the Navigation Bar Item Content placeholder.

    ![](images/navigationbar-image-2.png)

1. On the **Properties** tab, set the required values.

    ![](images/navigationbar-image-3.png)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

#### Navigation Bar

| **Property** |  **Description** |  **Usage** | 
|---|---|---|
| IsFixed (Boolean): Optional |  If set to True, the navigation bar will allways be in the same position on the screen. If set to False, it scrolls with the page content. |  
| TopPosition (Integer): Optional  |  Set the top position when the navigation bar is fixed. (Insert a number - the pixels unit is automatically added.) |  
| MultipleItems (Boolean): Optional |  Allows multiple Navigation Bar Items to be opened having an accordian effect. | 
| ExtendedClass (Text): Optional |  Add custom style classes to the block. | T|

#### Navigation Bar Item

| **Property** |  **Description** |  **Usage** | 
|---|---|---|
| IsActive  |  Set IsActive to true, to define as the selected element. |  Boolean | False | False |
| IsOpen  |  If true, when rendering the NavigationBarItem is open. |  Boolean | False | False |
| ExtendedClass  |  Add custom style classes to this Block. | Text | False | none |

#### Navigation Bar Sub Item
| **Property** |  **Description** |  **Usage** | 
|---|---|---|
| IsActive  |  Set IsActive to true, to define as the selected element. |  Boolean | False | False |

## Device compatibility

In Internet Explorer, `position: fixed` is used instead of `position: sticky` as the latter is not supported.

## See also

* OutSystems UI Live Style Guide: [Navigation Bar](https://outsystemsui.outsystems.com/WebStyleGuidePreview/NavigationBar.aspx)

