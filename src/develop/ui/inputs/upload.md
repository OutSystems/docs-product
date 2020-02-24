---
summary: Learn how to enable end users to upload files using your application.
tags: support-application_development; support-Front_end_Development; support-Mobile_Apps; support-webapps
---

# Enable End Users to Upload Files

Use the Upload widget to add files — such as photos — to your application.

## In mobile

To upload a file in a mobile app:

1. Drag the Upload widget from the Widgets toolbar to the screen.

1. On the screen, create a local variable of Binary Data type to hold the file content. 

1. Set the File Content property of the Upload widget to the local variable.

    ![](images/upload-mobile.png?width=750)

1. Use a Client Action to call a Server Action to send the file to the server:

    * Change the Server Action to accept the variable in the File Content property as an input parameter and save it. 
    * In the Client Action, add the variable as an argument to the Server Action.

## In web

To upload a file in a web application:

1. Drag the Upload widget from the Widgets toolbar to your screen. 

    ![](images/upload-web.png?width=750)

1. Add a Button to the screen that executes a Screen Action to save the file and make sure its Method property is set to Submit.

1. To save the file in the Screen Action, use the Runtime Properties of the Upload widget:

    * `Upload.Content`: The file content 
    * `Upload.Filename`: The file name 
    * `Upload.Type`: The file type 

1. In the screen you want to upload the file, create a link to navigate to the newly created screen containing the Upload widget. Alternatively, you can put the screen with the Upload widget inside a [popup](popup.md).
