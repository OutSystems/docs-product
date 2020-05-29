---
tags: runtime-traditionalweb; 
summary: Organizes content and enables the user to navigate their way around your app using hyperlinks.
---

# Navigation Bar

You can use the Navigation Bar UI Pattern to organize content and enable the user to navigate their way around your app using hyperlinks. You use this pattern when the user needs to navigate through an application's main sections while maintaining the ability to browse to another subsection. 

![](images/navigationbar-7-ss.png)

**How to use the Navigation Bar UI Pattern**

The following use case adds the Navigation Bar UI Pattern to **one** screen. If you want the Navigation Bar to appear on multiple screens in your app, we recommend adding the pattern to a web block. For more information, see [Create and Reuse Screen Blocks](../../../../../develop/ui/reuse/block-create-reuse.md). 

1. In Service Studio, in the Toolbox, search for `Navigation Bar`. 

    The Navigation Bar widget is displayed.

    ![](images/navigationbar-6-ss.png)

1. From the Toolbox, drag the Navigation Bar widget into the Main Content area of your application's screen.

    ![](images/navigationbar-1-ss.png)

    By default, the Navigation Bar widget contains a Navigation Bar Item widget and a Navigation Bar SubItem widget. You can add or delete as many of these widgets as required.

1. Add the required content to the Navigation Bar Item and Navigation Bar SubItem placeholders. 

    In this example we add `Phones`, `Audio`, and `Accessories` to the Navigation Bar Item **Title** placeholders.

    ![](images/navigationbar-12-ss.png)   

    We also add links to the Navigation Bar SubItem **Content** placeholders. For each of the links, on the **Properties** tab, we add a link name and title, as well as the link destination.
    
    ![](images/navigationbar-9-ss.png)   

1. On the **Properties** tab, you can alsocustomize the Navigation Bar's look and feel by setting any of the optional properties.

    ![](images/navigationbar-3-ss.png)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

### Navigation Bar

| **Property** |  **Description** |  
|---|---|
| IsFixed (Boolean): Optional |  If True, the navigation bar is always in the same position on the screen. This is the defult value. If False, the navigation bar scrolls with the page content. |  
| TopPosition (Integer): Optional  |  Set the top position when the navigation bar is fixed. |  
| MultipleItems (Boolean): Optional | If True, multiple Navigation Bar Items can be opened at the same time. This is the default value. If False, only one Navigation Bar Item can be opened at a time. | 
| ExtendedClass (Text): Optional | Add custom style classes to the Navigation Bar UI Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_''myclass''_ - Adds the _myclass_ style to the Navigation Bar UI styles being applied.</li><li>_''myclass1'' ''myclass2''_ - Adds the _myclass1_ and _myclass2_ styles to the Navigation Bar UI styles being applied.</li></ul></p> | 

### Navigation Bar Item

| **Property** |  **Description** | 
|---|---|
| IsActive (Boolean): Optional | If True, when the page is rendered, the Item is selected. If False, the Item is not selected. This is the default value. | 
| IsOpen (Boolean): Optional  |  If True, when the page is rendered, the Navigation Bar Item is open. If False, the Navigation Bar Item is not open. This is the default.| 
| ExtendedClass (Text): Optional | Add custom style classes to the Navigation Bar Item UI Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value)</li><li>_''myclass''_ - adds the _myclass_ style to the Navigation Bar Item UI styles being applied.</li><li>_''myclass1'' ''myclass2''_ - adds the _myclass1_ and _myclass2_ styles to the Navigation Bar Item UI styles being applied.</li></ul></p> | 

### Navigation Bar Sub Item

| **Property** |  **Description** |  
|---|---|
| IsActive (Boolean): Optional  |  If True, when the page is rendered, the Sub Item is selected. If False, the Sub Item is not selected. | 

## Device compatibility

In Internet Explorer, `position: fixed` is used instead of `position: sticky` as the latter is not supported.

