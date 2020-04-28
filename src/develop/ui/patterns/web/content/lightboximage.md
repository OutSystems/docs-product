---
tags: runtime-traditionalweb; 
summary: LightBoxImage displays an image thumbnail that is clicked to open a fullscreen image.
---

# Light Box Image

You can use the Lightbox Image UI Pattern to open smaller thumbnail images in full screen mode. This UI pattern is often used when creating an image gallery, allowing you to navigate through each of the images and view them in more detail.  

![](<images/lightboxweb-image-11.png>)

**How to use the Light Box Image UI Pattern**

1. In Service Studio, in the Toolbox, search for `Light Box Image`. 

    The Light Box Image widget is displayed.

    ![](<images/lightboximage-image-12.png>)    

1. From the Toolbox, drag the Light Box Image widget into the Main Content area of your application's screen.
   
    ![](<images/lightboximage-image-13.png>)

1. From the Toolbox, drag the [Image widget](<../../../../../ref/lang/auto/Class.Image Widget.final.md>) into the Light Box Image widget. This is a thumbnail image. 

    The **Select Image** pop-up is displayed.

1. Select or import the image you want to display. In this example, we use the sample OutSystems UI images.

    ![](<images/lightboximage-image-9.png>)

    Note: In this example, the image property Type is set to **Static**. You can also choose [External URL or Database](../../../../../develop/ui/image/display-image.md).

1. From the Widget tree, select the Light Box Image widget.
    
    ![](<images/lightboximage-image-14.png>)

1. On the **Properties** tab, set the relevant Light Box Image properties, for example, the title of the image that is displayed,the group the image belongs to, and the size that the image will display in full screen mode.

     ![](<images/lightboximage-image-10.png>)

1. Repeat steps 2-6 for each of the images you want in your Light Box Pattern. 

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| **Property** |  **Description** |
|---|---|
| Title (Text): Optional  |Image title that is displayed when previewing the image in ful screen mode. <p>Examples<ul><li>_"Image 1"_ - Displays *Image 1* as the image title. </li></ul></p>|
| Group (Text): Optional | Name of the group of images. Similar to the concept of a picture album. You can navigate through pictures with the same group name when viewing them in full screen mode.<p>Examples<ul><li>_Gallery 1_ - Adds this image to the _Gallery 1_ group</li></ul></p> |
| ImageURL (Text): Optional | URL for the image you want to show in full screen mode. If empty, a zoomed version of the thumbnail is displayed. Use this if you want to load a lower quality image as a thumbnail and display a higher quality version in full screen mode.   |
| ImageZoom (Decimal): Optional  |  Defines the size of the image that opens in full screen mode (based on the thumbnail size).<p>To avoid rendering problems, try to use images with the same ratio.<p>Examples</p><ul><li>_2_ - A thumbnail with 100x100, and zoom 2 opens with 200x200.</li><li> _0.5_ - A thumbnail with 500x500, and zoom 0.5 opens with 250x250.</li></ul></p> |
| ExtendedClass (Text): Optional |  Add custom style classes to the Lightbox Image UI Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the Lightbox Image UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Lightbox Image UI styles being applied.</li></ul></p> |


<!--- ## See also
* OutSystems UI Live Style Guide: [Lightbox Image](https://outsystemsui.outsystems.com/WebStyleGuidePreview/LightboxImage.aspx)
* OutSystems UI Pattern Page: [Lightbox Image](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/PatternDetail?PatternId=46)
-->
