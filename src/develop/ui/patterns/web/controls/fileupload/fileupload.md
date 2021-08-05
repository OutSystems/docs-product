---
tags: runtime-traditionalweb; 
summary: FileUpload allows the end user to transfer a file or add content to the application.
---

# File Upload

You can use the File Upload UI Pattern to allow users upload files to the app.

The File Upload pattern is commonly used in a form, but it can also be used as a stand-alone element.

![](<images/fileupload-image-1.png>)

**How to use the File Upload Pattern**


1. In Service Studio, in the Toolbox, search for `File Upload`.

    The File Upload widget is displayed.

    ![](<images/fileupload-image-3.png>)

    If the UI widget does not display, it may be because you used a ready-made app, which deletes unused widgets from the module. To make additional widgets available in your app:

    a. Go to **Module > Manage dependencies**.

    b. Search for and select the relevant Producer, for example OutSystemsUI. Ensure Show All is selected. 

    c. On the Public elements for the selected Producer displayed on the right, ensure Show All is selected.
    
    d. Search for and select the element you want to add, and click **Apply**. 
    
    e. In Service Studio, in the Toolbox, search for the widget again.

1. From the Toolbox, drag the File Upload widget into the Main Content area of your application's screen.

    ![](<images/fileupload-image-4.png>)

1. After following these steps and publishing the module, you can test the pattern in your app. 



## Demo

<iframe width="750" height="500" src="https://www.youtube.com/embed/l0YPl_3ya9s" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen"></iframe>

## Properties

| **Property** | **Description** |  
|---|---|
| ExtendedClass (Text): Optional  |  Adds custom style classes to the Pattern. You define your [custom style classes](../../../../../../develop/ui/look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/><ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied. </li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |




