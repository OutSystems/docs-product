---
tags: runtime-traditionalweb; 
summary: Breadcrumbs present the location of the user within the hierarchy of applications.
---

# Breadcrumbs

You can use the Breadcrumbs UI Pattern as a navigational aid that helps users keep track of their location within the app.

  ![](<images/breadcrumbs-2-ss.png>)

**How to use the Breadcrumbs UI Pattern**

The following use case adds the Breadcrumbs UI Pattern to one screen. If you want Breadcrumbs to appear on multiple screens in your app, we recommend adding the pattern to a **web block**. For more information, see [Create and Reuse Screen Blocks](../../../reuse/block-create-reuse.md). 

1. In Service Studio, in the Toolbox, search for `Breadcrumbs`.
  
     The Breadcrumbs widget is displayed.

    ![](<images/breadcrumbs-8-ss.png>)

1. From the Toolbox, drag the Breadcrumbs widget into the Main Content area of your application's screen.

    ![](<images/breadcrumbs-9-ss.png>)

    By default, the Breadcrumbs widget contains three Breadcrumb Item widgets. Each Breadcrumb Item represents a location in the breadcrumb trail. You can add or delete Breadcrumb Items as required. In this example, we add another Breadcrumb Item.

      ![](<images/breadcrumbs-1-ss.png>)

1. From the Toolbox, drag another Breadcrumbs Item into your Breadcrumbs Pattern. 

    ![](<images/breadcrumbs-10-ss.png>)
        
1. In the Title placeholder, enter the breadcrumb title (in this example, **More Details**) and drag an Icon widget into the Icon placeholder.    
    
    ![](<images/breadcrumbs-11-ss.png>)

1. So that each of the Breadcrumb Items are navigational, we add links. To do this, select the text inside the Breadcrumb Item placeholder, right-click, select **Link to** and select the link destination. In this example, we want the **More Details** Breadcrumb Item to link to an existing page called **More Details**. Repeat this process for each of the Breadcrumb Items. 

    ![](<images/breadcrumbs-3-ss.png>)
    
1. So that the new **More Details** Breadcrumb Item icon matches the others, select the Icon widget, and on the **Properties** tab, set the **Name** property to ``Entities.IconName.angle_right``.

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

### Breadcrumbs

| **Property** |  **Description** |
|---|---|
| ExtendedClass (Text): Optional  | Add custom style classes to the Breadcrumbs UI Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_''myclass''_ - Adds the _myclass_ style to the Breadcrumbs UI styles being applied.</li><li>_''myclass1'' ''myclass2''_ - Adds the _myclass1_ and _myclass2_ styles to the Breadcrumbs UI styles being applied.</li></ul></p> | 

### Breadcrumb Item

| **Property** |  **Description** |
|---|---|
| ExtendedClass (Text): Optional  |  Add custom style classes to the Breadcrumb Item UI Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_''myclass''_ - Adds the _myclass_ style to the Breadcrumb Item UI styles being applied.</li><li>_''myclass1'' ''myclass2''_ - Adds the _myclass1_ and _myclass2_ styles to the Breadcrumb Item UI styles being applied.</li></ul></p> |
