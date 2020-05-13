---
tags: runtime-mobileandreactiveweb;  
summary: Displays an image thumbnail  that can be clicked to open a fullscreen image.
---

# Lightbox Image UI Pattern

You can use the Lightbox Image UI Pattern to open smaller thumbnail images in full screen mode. This UI pattern is often used when creating an image gallery, allowing you to navigate through each of the images and view them in more detail.

## How to Use the Lightbox Image UI Pattern

1. In Service Studio, in the Toolbox, search for `Lightbox Image`.

    The Lightbox Image widget is displayed.

    ![](images/lightboxmob-image-1.png)

1. From the Toolbox, drag the Lightbox Image widget into the Main Content area of your application's screen.

      ![](images/lightboxmob-image-2.png)

      By default, the Lightbox Image widget contains an Image placeholder. You can add as many images as required by dragging the Image widget from the Toolbox into the Lightbox Image widget.

1. Select the **Image** placeholder and on the **Properties** tab, from the **Image** drop-down, select or import the thumbnail image you want to display. In this example, we use the sample OutSystems UI Images.
    
     ![](images/lightboxmob-image-3.png)

     Note: In this example, the image property is set to **Local Image**. You can also choose [External URL or Binary Data](../../../../develop/ui/image/display-image.md).

1.  From the Widget Tree, select the Lightbox Image widget, and on the **Properties** tab, set the relevant properties.



## Properties

**Property** |  **Description** |  
---|---| 
 Title  |  Title of the image that will be displayed.  | 
 Group  |  Images in the same group will be displayed in a gallery.  |  
 ImageURL  |  URL for an image that can be a replacement for the "Image Placeholder" image.  |  
 ImageZoom  |  The zoom value is used to define the size of the image that will open in full screen based on the thumbnail size. %%Note: try to use images with the same ratio to avoid rendering problems:  %%- thumbnail with 100x100 and zoom 2 will open with 200x200  %%- thumbnail with 500x500 and zoom 0.5 will open with 250x250  |  
  

## Compatibility with other patterns

The Lightbox Image UI pattern can be used only with images.

## Samples

Watch how the [Product Overview sample](https://silkui.outsystems.com/Samples_Mobile.aspx#Mobile_Details-Samples_ProductOverview "https://silkui.outsystems.com/Samples_Mobile.aspx#Mobile_Details-Samples_ProductOverview") uses the Lightbox Image UI Pattern:

![](images/Sample_LightBoxImage.gif)
