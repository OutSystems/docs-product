---
tags: runtime-traditionalweb; 
summary: Breadcrumbs present the location of the user within the hierarchy of applications.
---

# Breadcrumbs

You can use the Breadcrumbs UI Pattern as a navigational aid that helps users keep track of their location within the app.

  ![](<images/breadcrumbs-image-2.png>)

**How to use the Breadcrumbs UI Pattern**

The following example demonstrates how you can create a breadcrumb trail with four breadcrumb items. 

1. In Service Studio, in the Toolbox, search for `Breadcrumbs`.
  
     The Breadcrumbs widget is displayed.

    ![](<images/breadcrumbs-image-8.png>)

1. From the Toolbox, drag the Breadcrumbs widget into the Main Content area of your application's screen.

      ![](<images/breadcrumbs-image-9.png>)

     By default, the Breadcrumbs widget contains three Breadcrumb Item widgets. Each Breadcrumb Item represents a location in the breadcrumb trail. You can add or delete Breadcrumb Items as required.

1. From the Toolbox, drag another Breadcrumbs Item into your Breadcrumbs Pattern. 
        ![](<images/breadcrumbs-image-10.png>)
        
1. In the Title placeholder, enter the breadcrumb title (in this example, More Details) and drag an Icon widget into the Icon placeholder.    
    
    ![](<images/breadcrumbs-image-11.png>)
    
1. So that the new Breadcrumb Item widget icon matches the others, select the Icon widget, and on the **Properties** tab, set the **Name** property to ``Entities.IconName.angle_right``.

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

### Breadcrumbs

| **Property** |  **Description** |
|---|---|
| ExtendedClass (Text): Optional  | Add custom style classes to the Breadcrumbs UI Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value)</li><li>_''myclass''_ - adds the myclass style to the Breadcrumbs UI styles being applied.<li>_''myclass1'' ''myclass2''_ - adds the _myclass1_ and _myclass2_ styles to the Breadcrumbs UI styles being applied.</li></ul></p> | 

### Breadcrumb Item

| **Property** |  **Description** |
|---|---|
| ExtendedClass (Text): Optional  |  Add custom style classes to the Breadcrumb Item UI Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value)</li><li>_''myclass''_ - adds the myclass style to the Breadcrumb Item UI styles being applied.<li>_''myclass1'' ''myclass2''_ - adds the _myclass1_ and _myclass2_ styles to the Breadcrumb Item UI styles being applied.</li></ul></p> |

<!---  Added to yml file
## See also

* OutSystems UI Live Style Guide: [Breadcrumbs](https://outsystemsui.outsystems.com/WebStyleGuidePreview/Breadcrumbs.aspx)
* OutSystems UI Pattern Page: [Breadcrumbs](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/PatternDetail?PatternId=10)
