---
summary: OutSystems 11 (O11) enables end users to upload files using the Upload widget in both Reactive Web and Mobile, as well as Traditional Web applications.
tags: ide usage, reactive web apps, tutorials for beginners, file upload, user interface components
locale: en-us
guid: cf21f903-1b6f-4fe9-b0a0-622c45bac166
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=199:66
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# Enable End Users to Upload Files


Use the Upload widget to allow users to upload files, such as photos to your application.

## Reactive Web and Mobile

To upload a file in Reactive Web and Mobile apps:

1. In Service Studio, in the Toolbox, search for `Upload`.

    The Upload widget is displayed.

    ![Screenshot showing the Upload widget in the Service Studio toolbox](images/upload-1-ss.png "Upload Widget in Service Studio")

1. Drag the Upload widget into the Main Content area of your screen.

    ![Screenshot of dragging the Upload widget into the Main Content area of the screen](images/upload-2-ss.png "Drag Upload Widget to Main Content")

    By default, the Upload widget contains an icon and text placeholder.

1. To hold the file content, create a local variable by right-clicking on your screen name and selecting **Add Local Variable**. Enter a name for the variable and set the data type to Binary Data.

    ![Screenshot of creating a local variable for file content in Service Studio](images/upload-3-ss.png "Create Local Variable for File Content")

1. Repeat step 3 to create a local variable to hold the file name, but in this case, select Text as the data type.

    ![Screenshot of creating a local variable for file name with Text data type in Service Studio](images/upload-5-ss.png "Create Local Variable for File Name")

1. Select the Upload widget, and on the **Properties** tab, set the **File Content** property to the local variable you created (BinaryDataVar) to hold the file content and set the **File Name** property to the local variable you created (TextVar) to hold the file name.

    ![Screenshot showing the properties tab for the Upload widget with File Content and File Name set to local variables](images/upload-4-ss.png "Set Properties for Upload Widget")

### Save the uploaded file

There are several ways to save the uploaded file. For example,  you can use a Client Action to call a Server Action to send the file to the server. To do this:

1. Create a Button or Link, and inside the associated Client Action, call the Server Action.

1. Ensure the Server Action has an input parameter to accept the contents of the BinaryDataVar variable.

1. Inside the Server Action, create the logic to process or store the uploaded file.

After following these steps and publishing the module, you can test the pattern in your app.

## Traditional Web

To upload a file in a Traditional Web app:

1. In Service Studio, in the Toolbox, search for `Upload`.

    The Upload widget is displayed.

    ![Screenshot displaying the Upload widget in the toolbox for a Traditional Web app in Service Studio](images/uploadweb-1-ss.png "Upload Widget in Traditional Web App")

1. Drag the Upload widget into the Main Content area of your screen.

    ![Screenshot of the Upload widget placed in the Main Content area of a Traditional Web app screen](images/uploadweb-2-ss.png "Upload Widget on Traditional Web Screen")

### Save the uploaded file

There are several ways to save the uploaded file. For example, you can add a Button to the screen that executes a screen action and the logic defined in the screen action saves the file. To save the uploaded file, inside the Screen Action flow, use the following Runtime Properties of the Upload widget:

* `Upload.Content`: The file content
* `Upload.Filename`: The file name
* `Upload.Type`: The file type

After following these steps and publishing the module, you can test the pattern in your app.
