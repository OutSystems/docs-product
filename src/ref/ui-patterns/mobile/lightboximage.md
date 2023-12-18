---
tags: runtime-mobileandreactiveweb;  
summary: Advanced use cases for the Lightbox Image UI Pattern.
locale: en-us
guid: b0e2b293-97b8-47b4-abfe-d5b99df4bc3c
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=612:359
---

# Lightbox Image Reference

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

## Adding a Filter to an Open Image

![Screenshot showing the addition of a filter to an image in Lightbox](images/light_box_add_filter.png "Adding a Filter to Lightbox Image")

**Result**:

![Animated GIF demonstrating the result of adding a filter to an image in Lightbox](images/Lightbox_filter.gif "Result of Adding Filter to Lightbox Image")

## Loading Binary Images After Click on Lightbox Image (images from database)

To expose the image, you need to create a REST service first and then consume that REST service to obtain the URL. Go to the **Logic** tab ( **Integrations** folder) to create the REST services.

Follow the steps below to **expose the REST API**:

1. Right-click the REST service and select **Expose REST API** (call **GetImages** for example).

1. Right-click the **Expose REST API** and **add REST API method** (call **GetFullImage** for example).

1. Add an input parameter to expose the URL. Call **PictureID** and set the Data Type as Pictures Identifier. In the **Advanced** section, select the **URL** option on the **Receive IN** drop-down.

1. Add an output parameter (call **Image** for example) and set the Data type to Binary Data. In the **Advanced** section, select the **Body** option on the **Send IN** drop-down.

1. On the **GetFullSizeImage** REST API method, drag your Pictures database and filter by **Pictures.Id=PictureId**.

1. Drag the assign widget and set Image (output parameter) with **GetPictureById.List.Current.Pictures.Image**.

    ![Screenshot of the process to set the image output parameter in Lightbox by dragging a widget](images/lightbox-drag-widget-set-image-ss.png "Setting Image Output Parameter in Lightbox")

Follow the steps below to **consume the REST API**:

1. Right-click the REST service and select **CONSUME REST API** (call **GetImages** for example).

1. Add Single Method.

1. On the method URL, paste your domain URL + URL Path (get this on Expose REST API) + ?PictureId={PictureId}

    ![Screenshot showing where to paste the domain URL for the REST API in Lightbox](images/lightbox-paste-your-domain-ss.png "Pasting Domain URL for REST API in Lightbox")

Now we are able to create our screen with all pictures from the database using the LightBoxImage pattern to display them.

1. Add a new screen.

1. Right-click on the screen and select **Fetch data from other resources** (call **GetImagesIds** for example).

1. Rename the **Output parameter** to **List** and define **Pictures Identifier List** as the Data type.

1. Drag your Pictures database to the **GetImagesIds** action and the **ListAppendAll** action.

    ![Screenshot illustrating the action of dragging the pictures database to the GetImagesIds action in Lightbox](images/lightbox-drag-pictures-database-ss.png "Dragging Pictures Database to GetImagesIds Action")

1. In the **ListAppendAll** set the aggregate as source list (GetPictures.List) and map from pictures to Pictures Identifier. To do that, set **Pictures.Id** in the **Value** option.

    ![Screenshot showing the ListAppendAll action in Lightbox to append pictures to a list](images/lightbox-list-append-all-ss.png "Appending to List in Lightbox")

1. Drag the List widget to the screen.

1. Drag the LightboxImage pattern to the List widget.

    ![Screenshot demonstrating how to drag the Lightbox Image pattern to a List widget](images/lightbox-image-pattern-drag-ss.png "Dragging Lightbox Image Pattern to List Widget")

1. Set the ImageURL parameter on the **Lightbox Image** with your URL REST API + your fetched data.  
a. "/your-module/rest/GetImages/GetFullSizeImage?PictureId=" + GetImagesIds.List.Current

    ![Screenshot of setting the ImageURL parameter on the Lightbox Image pattern](images/lightbox-set-url-parameter-ss.png "Setting ImageURL Parameter in Lightbox")

1. In the Lightbox Thumbnail Image set External URL on type and the URL REST API + your fetched data.  
a. "/your-module/rest/GetImages/GetFullSizeImage?PictureId=" + GetImagesIds.List.Current

    ![Screenshot showing the setting of an external URL in the Lightbox Thumbnail Image](images/lightbox-set-external-url-ss.png "Setting External URL in Lightbox Thumbnail Image")

1. Publish your app.

## Lightbox Image with External URL Images

1. Drag your database to the screen.

1. Drag the **LightBoxImage** pattern to the List widget.

1. Set the **ImageURL** parameter on the LightBoxImage and **Thumbnail** image with your external URL.  
For example: GetPictures.List.Current.Pictures.ExternalURL.

    ![Screenshot of setting the ImageURL parameter in Lightbox with an external URL](images/lightbox-set-image-url-ss.png "Setting Image URL in Lightbox with External URL")

1. Publish your app.  

## Layout and Classes

![Screenshot displaying the layout and classes used in Lightbox](images/lightbox-layout-classes.png "Lightbox Layout and Classes")
