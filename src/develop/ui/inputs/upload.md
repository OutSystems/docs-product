---
summary: Learn how to enable end users to upload files using your application.
tags: support-application_development; support-Front_end_Development; support-Mobile_Apps; support-webapps
---

# Enable End Users to Upload Files

Use the Upload widget to add files, such as photos to your application.

## Reactive Web and Mobile

To upload a file in Reactive Web and Mobile apps:

1. In Service Studio, in the Toolbox, search for `Upload`.

    The Upload widget is displayed. 

    ![Upload widget](images/upload-1-ss.png)

1. Drag the Upload widget into the Main Content area of your screen. 
    
    ![Drag widget onto screen](images/upload-2-ss.png)

    By default, the Upload widget contains an icon and text placeholder.

1. To hold the file content, create a local variable by right-clicking on your screen name and selecting **Add Local Variable**. Enter a name for the variable and set the data type to binary data. 

    ![Add local variable](images/upload-3-ss.png)

1. Repeat step 3 to hold the file name, but in this case, select Text as the data type.

    ![Add local variable](images/upload-5-ss.png)

1. Select the Upload widget, and on the **Properties** tab, set the **File Content** property to the local variable you just created to hold the file content and the **File Property** property to the local variable you created to hold the file name.

    ![Set File Content and File Name variables](images/upload-4-ss.png)

<!--1. Use a Client Action to call a Server Action to send the file to the server:

    * Change the Server Action to accept the variable in the File Content property as an input parameter and save it. 
    * In the Client Action, add the variable as an argument to the Server Action. -->
After following these steps and publishing the module, you can test the pattern in your app.

## Traditional Web

To upload a file in a Traditional Web app:

1. In Service Studio, in the Toolbox, search for `Upload`.

    The Upload widget is displayed. 

    ![Upload widget](images/uploadweb-1-ss.png)

1. Drag the Upload widget into the Main Content area of your screen. 
    
    ![Drag widget onto screen](images/uploadweb-2-ss.png)

1. Add a Button to the screen that executes a Screen Action to save the file and make sure its Method property is set to Submit.

1. To save the file in the Screen Action, use the Runtime Properties of the Upload widget:

    * `Upload.Content`: The file content 
    * `Upload.Filename`: The file name 
    * `Upload.Type`: The file type 

1. In the screen you want to upload the file, create a link to navigate to the newly created screen containing the Upload widget. Alternatively, you can put the screen with the Upload widget inside a [popup](popup.md).
