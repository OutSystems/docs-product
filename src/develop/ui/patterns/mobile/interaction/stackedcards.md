---
tags: runtime-mobileandreactiveweb;  
summary: Adds swipeable cards that can be dragged in multiple directions triggering events, such as deny, approve, and archive.
locale: en-us
guid: c4e2edb1-3142-4f82-b34d-dab8d2356155
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=213:82
---

# Stacked Cards

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

You can use Stacked Cards UI Pattern to add swipeable cards that can be dragged in multiple directions triggering events, such as deny, approve, and archive. This pattern is ideal when you want to individually scan multiple cards.

   ![](images/stackedcards-1.png)

## How to use the Stacked Cards Pattern

1. In Service Studio, in the Toolbox, search for  `Stacked Cards`.

    The Stacked Cards widget is displayed.

    ![](images/stackedcards-2-ss.png)

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Swipe Events widget into the Main Content area of your application's screen.

    ![](images/stackedcards-3-ss.png)

    By default, the Stacked Cards widget contains a List, Overlay Top, Overlay Right, and Overlay Left placeholders.

1. Add content to the List placeholder. In this example, from the **Data** tab, we drag a list of Employees into the List placeholder.

    ![](images/stackedcards-4-ss.png)

    The **GetEmployees** aggregate is automatically created.

    ![](images/stackedcards-5-ss.png)

1. From the Toolbox, drag the Icon widget into the OverlayTop placeholder, and from the Pick an Icon editor, choose an icon. Click **Select**.

    ![](images/stackedcards-6-ss.png)

1. Repeat step 4 for the OverlayRight and OverlayLeft placeholders.

    ![](images/stackedcards-7-ss.png)

1. To create a swipe action for the OverlayLeft placeholder, select the pattern, and from the OnLeftSwipe **Handler** drop-down, select **New Client Action**.

    ![](images/stackedcards-8-ss.png)

1. From the Toolbox, drag a **Run Server Action** onto the client action, and from the **Select Action** editor, navigate to the action you want the swipe left action to perform. In this example, we use the **DeleteEmployee** action.

    ![](images/stackedcards-9-ss.png)

1. From the **Id** drop-down, select the action Id. In this example, the Id is the currently selected employee. This means, that when the user swipes left, the currently selected user is deleted form the list of employees.

   ![](images/stackedcards-10-ss.png)

1. Repeat step 7 for the OverlayTop (swipe up) and OverLayRight (swipe right) placeholders.

1. From the **Properties** tab, you can change the Stacked Card's look and feel by setting the (optional) properties.

   ![](images/stackedcards-11-ss.png)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property                                                   | Description                                                                                                                                                                                                                                                                                |
|------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| StackedOptions (StackedCardsPosition Identifier): Optional | Change stacked cards view from bottom, top, or none.  <p>Examples <ul><li>Entities.StackedCardsPosition.Bottom - The stacked cards are positioned on the bottom. This is the default. </li><li>Entities.StackedCardsPosition.Top - The stacked cards are positioned on top. </li></ul></p> |
| Rotate (Boolean): Optional                                 | If True, the rotation for each move on the stacked cards is activated. This is the default. If False, each move is not activated.                                                                                                                                                          |
| Items (Integer): Optional                                  | Number of visible elements when the StackedOptions property is set to bottom or top. <p>Examples <ul><li>Blank - 5 elements are visible. This is the default. </li><li>3 - 3 elements are visible. </li></ul></p>                                                                          |
| ElementsMargin                                             | Define the distance between each element when the StackedOptions property is set to bottom or top. <p>Examples <ul><li>Blank - 5 elements are visible. This is the default. </li><li>3 - 3 elements are visible. </li></ul></p>                                                            |
| UseOverlays (Boolean): Optional                            | If True, overlays for swipe elements are enabled. This is the default. If False, the overlays are disabled.                                                                                                                                                                                |
  
## Compatibility with other patterns

Avoid using the Stacked Cards Pattern inside patterns with swipe events / touch events, like [Tabs](<../navigation/tabs.md>) or [Carousel](<carousel.md>).
