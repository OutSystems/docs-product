---
summary: Explore how to effectively implement and manage popups in OutSystems 11 (O11) for both Reactive Web and Mobile as well as Traditional Web applications.
tags:
locale: en-us
guid: f43cd1e1-13d3-4960-b025-4f75f9383ee8
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=199:49
---

# Create and use a Popup


You can use a popup to show information to users or ask them to enter information. Correctly used popups help you create a good user experience, because the users remain on the same page.

## Reactive Web and Mobile

To create and use a popup in Reactive Web and Mobile Apps:

1. In Service Studio, in the Toolbox, search for `Popup`.

    The **Popup** widget is displayed.

    ![Screenshot showing the Popup widget in the Service Studio toolbox](images/popup-1-ss.png "Popup Widget in Service Studio Toolbox")

1. Drag the **Popup** widget into the **Main Content** area of your screen. 

    ![Screenshot of dragging the Popup widget into the Main Content area of the screen](images/popup-2-ss.png "Dragging Popup Widget into Main Content")

1. Add a variable of boolean data type to the screen by right-clicking on your screen name (located in the element tree) and selecting **Add Local Variable**. In this example, we call the variable `ShowPopup`.

    ![Screenshot of adding a local variable to the screen in Service Studio](images/popup-3-ss.png "Adding Local Variable to Screen")

    ![Screenshot of naming the local variable as ShowPopup in Service Studio](images/popup-4-ss.png "Naming Local Variable ShowPopup")

1. Select the Popup widget, and on the **Properties** tab, enter the new variable for the **Show Popup** property. This toggles the popup according to the variable value.

    ![Screenshot showing the Show Popup property being set in the Popup widget properties](images/popup-5-ss.png "Setting Show Popup Property")

1. Add your content to the popup.

    In this example, we add some text and a **Close Popup** button. We also add a **Show Popup** button to the **Actions** screen area.

    ![Screenshot of adding text and buttons to the content of the Popup widget](images/popup-6-ss.png "Adding Content to Popup")

1. Select the **Close Popup** button, and from the **On Click** dropdown, select **New Client Action**.

    ![Screenshot of creating a new client action for the Close Popup button in Service Studio](images/popup-8-ss.png "Creating New Client Action for Close Popup Button")

1. Drag an **Assign** onto the client action, and set the **ShowPopup** variable to **False**.

    ![Screenshot of an Assign action setting the ShowPopup variable to False in Service Studio](images/popup-7-ss.png "Assigning ShowPopup Variable to False")

    Clicking the **Close Popup** button sets the **ShowPopup** variable to **False** and closes the popup.

1. Repeat steps 6 and 7 for the Open Popup button, substituting the variable value to True. Clicking the **Open Popup** button sets the ShowPopup variable to **True** and opens the popup.

After following these steps and publishing the module, you can test the pattern in your app.

<div class="info" markdown="1">

Here's a [video tutorial about using Popup in Reactive Web and Mobile App](https://www.youtube.com/watch?v=RrMARHvJBXU).

</div>

## Traditional Web

To create and use a popup in Traditional Web Apps:

1. In Service Studio, in the Toolbox, search for and drag the **Link** widget into the **Actions** placeholder of your screen.

    ![Screenshot showing the Link widget being added to the Actions placeholder in Service Studio](images/popupweb-1-ss.png "Link Widget in Actions Placeholder")

1. Enter a name and some text for the link. In this example we enter `PopupLink` for the link name and ``Show Popup`` as the link text. Ensure the **Method** property is set to **Navigate**.

    ![Screenshot of setting the name and text properties for a Link widget in Service Studio](images/popupweb-2-ss.png "Setting Link Properties for Popup")

1. Create a new screen for the popup. Select the **Widget Tree**, and from the **Source Web Block** dropdown, select **Layouts\LayoutPopup**.

    ![Screenshot of creating a new screen for the popup using the LayoutPopup template in Service Studio](images/popupweb-3-ss.png "Creating New Screen for Popup")

1. Delete the **Center**, **Left**, and **Right** placeholders from the screen until you are left with only the **MainContent** placeholder.

    ![Screenshot of deleting the Center, Left, and Right placeholders from the popup screen in Service Studio](images/popupweb-4-ss.png "Deleting Placeholders from Popup Screen")

1. Add the popup content. In this example, we add some text.

    ![Screenshot of adding text content to the new popup screen in Service Studio](images/popupweb-5-ss.png "Adding Popup Content to New Screen")

1. Select your main screen again, and from the **Properties** tab, set the link's **On Click** destination property to the popup screen you just created.

    ![Screenshot of setting the On Click destination property for a Link widget to the popup screen in Service Studio](images/popupweb-6-ss.png "Setting On Click Destination Property")

1. From the Toolbox, search for and drag the **Popup Editor** widget into the **Main Content** area of your screen.

    ![Screenshot of adding the Popup Editor widget to the Main Content area of the screen in Service Studio](images/popupweb-7-ss.png "Adding Popup Editor Widget to Main Content")

1. On the **Properties** tab, from the  **LinkOnButtonWidgetId** dropdown, select the Link widget Id (in this example, PopupLink.Id).

    ![Screenshot of configuring the Popup Editor widget properties by linking it to a Link widget ID in Service Studio](images/popupweb-8-ss.png "Configuring Popup Editor Properties")

    You can also create a screen action for the Popup Editor widget by selecting **New Screen Action** from the **Destination** dropdown. In this example, we select **New Screen Action**, but leave the flow of the action empty.

After following these steps and publishing the module, you can test the pattern in your app.

<div class="info" markdown="1">

Here is a [video tutorial about using Popup in Traditional Web App](https://www.youtube.com/watch?v=ShOCxc3g91M).

</div>

### Notes

Here are some additional notes about the Popup widget.

#### Showing a Confirmation Message for a Link that navigates to a Popup

When a Link widget has a Confirmation Message with the destination **RichWidgets\Popup_Upload**, the app doesn't show the Confirmation Message. To show the message, first navigate to a hidden Link that can then navigate to a RichWidgets\Popup_Upload:

1. Add a **Link** widget and enter the message in the property **Confirmation Message**.

1. Set the Link **Destination** to **Server Action** that uses **RichWidgets\Widget_Click** and select the **id** of the second Link widget.

1. Set the second Link **Visibility** property as **False** and its **Destination** as **RichWidgets\Popup_Upload**.
