---
summary: Learn how to create and use a popup in your application.
tags: support-application_development; support-Front_end_Development; support-Mobile_Apps; support-webapps
---

# Create and Use a Popup

You can use a popup to provide information to the end users or ask for their input. This results in a better experience for end users because they are kept in context while entering the input.

## In Reactive Web and Mobile

To create and use a popup in Reactive Web and Mobile apps:

1. Drag the Popup widget to the screen. 

1. Add a variable of Boolean type to the screen to control the popup visibility (you can use it to show or hide the popup). 

1. Set the Show Popup property with the variable. This will effectively toggle the popup according to the variable value. 

1. Implement a Client Action in the screen to display the popup by assigning `True` to the variable. 

1. Implement the popup content. 

![](images/popup-mobile.png?width=750)

For a video tutorial, view the following link:

[Create and Use a Popup in a Reactive Web App](https://www.youtube.com/watch?v=RrMARHvJBXU)

## In Traditional Web

To create and use a popup in Traditional Web apps:

1. Name the link that will open the popup and check that its OnClick Method property is set to Navigate. 

1. Create a new screen for the popup. In the widget tree, set the **Source Web Block** of the layout of the screen to `Layouts\LayoutPopup`. 

    ![](images/popup-web-2.png?width=500)

1. In the previous screen, set the link’s Destination to the popup screen.

1. Use the search bar (Ctrl + F) to look for the Popup_Editor and drag it to the screen with the link. 

1. Set the LinkOrButtonWidget property of the Popup_Editor to the Id runtime property of the link. 

    ![](images/popup-web-1.png?width=750)

1. Choose **(New Screen Action)** in the OnNotify Destination property of the Popup_Editor and leave the flow of the action empty.

1. Implement the popup content. 

For a video tutorial, view the following link:

[Create and Use a Popup in a Traditional Web App](https://www.youtube.com/watch?v=ShOCxc3g91M)
