---
summary: Explore how to display database-stored images in applications using OutSystems 11 (O11).
tags:
locale: en-us
guid: 0e4fc725-6ba9-4e5e-8834-71ca8b4aa180
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=199:102
---

# Display an Image Stored in the Database

You can display different types of images in your applications such as static images, external images fetched from URLs, and images stored in the database.

## In Reactive Web and Mobile

To display a database image in Reactive Web and Mobile:

1. Open the screen where you want to display the image. 

    ![Screenshot of the OutSystems interface highlighting the option to open a screen.](images/open-screen-ss.png "OutSystems Open Screen Interface")


1. Check if there is an aggregate fetching the image from the database. Add the aggregate if needed. 

    ![Screenshot showing how to add an aggregate to fetch data from the database in OutSystems.](images/add-aggregate-ss.png "Adding an Aggregate in OutSystems")


1. Drag the Image widget from the toolbox to the screen. 

    ![Screenshot illustrating the process of dragging an image widget onto the screen in OutSystems.](images/drag-image-widget-ss.png "Dragging an Image Widget in OutSystems")

    

1. Set the property Type to `Binary Data`. 

    ![Screenshot displaying the property settings for an image widget with the type set to Binary Data.](images/set-property-type.png "Setting Property Type to Binary Data")

  

1. Set the property Image Content to the entity attribute that stores the image.

    ![Screenshot showing the Image Content property being set to an entity attribute that stores the image.](images/set-property-image-content.png "Setting Image Content Property")

## In Traditional Web

To display a database image in Traditional Web:

1. Open the screen where you want to display the image.
1. Check if there is an aggregate fetching the image from the database. Add the aggregate to the Preparation if needed.
1. Drag the Image widget from the toolbox to the screen. 
1. Select an existing image resource or import a new image as an image default. This image is used as a placeholder during design time and as default during runtime. 
1. Select the image and change its property Type to `Database`.
1. Set the Attribute property to an entity attribute of type `Binary Data` that stores the image in the database. 
1. Set the Filename property to the name of the file when the end user saves the image.
1. Set the Entity Identifier property to the identifier of the specific entity record that contains the image to display. 
