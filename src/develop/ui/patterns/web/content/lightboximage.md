---
tags: runtime-traditionalweb; 
summary: Light Box Image displays an image thumbnail that is clicked to open a fullscreen image.
---

# Light Box Image

<div class="info" markdown="1">

We’ve been working on this article. Please let us know how useful this new version is by voting.

</div>

You can use the Lightbox Image UI Pattern to open smaller thumbnail images in full screen mode. This UI pattern is often used when creating an image gallery, allowing you to navigate through each of the images and view them in more detail.  

![](<images/lightboximage-15-ss.png>)

**How to use the Light Box Image UI Pattern**

1. In Service Studio, in the Toolbox, search for `Light Box Image`.

    The Light Box Image widget is displayed.

    ![](<images/lightboximage-12-ss.png>)

    If the UI widget does not display, it may be because you used a ready-made app, which deletes unused widgets from the module. To make additional widgets available in your app:

    a. Go to **Module > Manage dependencies**.

    b. Search for and select the relevant Producer, for example OutSystemsUI. Ensure Show All is selected. 

    c. On the Public elements for the selected Producer displayed on the right, ensure Show All is selected.
    
    d. Search for and select the element you want to add, and click **Apply**. 
    
    e. In Service Studio, in the Toolbox, search for the widget again.

1. From the Toolbox, drag the Light Box Image widget into the Main Content area of your application's screen.

    ![](<images/lightboximage-13-ss.png>)

1. From the Toolbox, drag the [Image widget](<../../../../../ref/lang/auto/Class.Image Widget.final.md>) into the Light Box Image widget. This is a thumbnail image.

    The **Select Image** pop-up is displayed.

1. Select or import the image you want to display. In this example, we use the sample OutSystems UI images.

    ![](<images/lightboximage-9-ss.png>)

    Note: In this example, the image property Type is set to **Static**. You can also choose [External URL or Database](../../../../../develop/ui/image/display-image.md).

1. From the Widget tree, select the Light Box Image widget.

    ![](<images/lightboximage-14-ss.png>)

1. On the **Properties** tab, set the relevant Light Box Image properties, for example, the title of the image that is displayed, the group the image belongs to, and the size that the image will display in full screen mode.

     ![](<images/lightboximage-10-ss.png>)

1. Repeat steps 2-6 for each of the images you want in your Light Box Pattern.

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
| Title (Text): Optional  |Image title that is displayed when previewing the image in ful screen mode. <p>Examples<ul><li>_"Image 1"_ - Displays *Image 1* as the image title. </li></ul></p>|
| Group (Text): Optional | Name of the group of images. Similar to the concept of a picture album. You can navigate through pictures with the same group name when viewing them in full screen mode.<p>Examples<ul><li>_Gallery 1_ - Adds this image to the _Gallery 1_ group</li></ul></p> |
| ImageURL (Text): Optional | URL for the image you want to show in full screen mode. If empty, a zoomed version of the thumbnail is displayed. Use this if you want to load a lower quality image as a thumbnail and display a higher quality version in full screen mode.   |
| ImageZoom (Decimal): Optional  |  Defines the size of the image that opens in full screen mode (based on the thumbnail size).<p>To avoid rendering problems, try to use images with the same ratio.<p>Examples</p><ul><li>_2_ - A thumbnail with 100x100, and zoom 2 opens with 200x200.</li><li> _0.5_ - A thumbnail with 500x500, and zoom 0.5 opens with 250x250.</li></ul></p> |
| ExtendedClass (Text): Optional |  Adds custom style classes to the Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |
