---
summary: Learn how to create and use a popup in your application.
tags: support-application_development; support-Front_end_Development; support-Mobile_Apps; support-webapps
---

# Create and Use a Popup

Use a popup to show information to users or ask them to enter information. Correctly used popups help you create good user experience, because the users remain on the same page.

## In Reactive Web and Mobile

To create and use a popup in Reactive Web and Mobile Apps:

1. Drag the **Popup** widget to the screen. 

1. Add a variable of boolean type to the screen. 

1. Set the **Show Popup** property with the variable. This toggles the popup according to the variable value. 

1. Add a Client Action to the screen to display the popup by assigning `True` to the variable. 

1. Add your content to the popup.

![Popup preview in a mobile app](images/popup-mobile.png?width=600)


<div class="info" markdown="1">

Here is a [video tutorial about using Popup in Reactive Web and Mobile App](https://www.youtube.com/watch?v=RrMARHvJBXU).

</div>

## In Traditional Web

To create and use a popup in Traditional Web Apps:

1. Name the link that opens the popup.

1. Verify the **OnClick Method** of the link is **Navigate**. 

1. Create a new screen for the popup. In the widget tree, set the **Source Web Block** of the layout of the screen to `Layouts\LayoutPopup`. 

    ![Web Block source properties](images/popup-web-2.png?width=300)

1. In the previous screen, set the link’s Destination to the popup screen.

1. Use the search bar (**Ctrl + F**) to look for the Popup_Editor and drag it to the screen with the link. 

1. Set the **LinkOrButtonWidget** property of the **Popup_Editor** to the Id runtime property of the link. 

    ![Popup preview in a Traditional app](images/popup-web-1.png?width=600)

1. Choose **(New Screen Action)** in the **OnNotify Destination** property of the **Popup_Editor** and leave the flow of the action empty.

1. Add your content to the popup.


<div class="info" markdown="1">

Here is a [video tutorial about using Popup in Traditional Web App](https://www.youtube.com/watch?v=ShOCxc3g91M).

</div>