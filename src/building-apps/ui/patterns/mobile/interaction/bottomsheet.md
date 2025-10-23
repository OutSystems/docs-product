---
tags: ide usage, reactive web apps, tutorials for beginners, ui patterns, mobile app development
summary: Learn how to implement and customize the Bottom Sheet UI pattern in OutSystems 11 (O11) for enhanced mobile app interfaces.
locale: en-us
guid: 4CCAE716-CF2A-4601-9F03-D6ACF603F01A
app_type: mobile apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=2885:24642
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# Bottom Sheet

<div class="info" markdown="1">

Applies to Mobile Apps only

</div>

You can use the Bottom Sheet Pattern to display additional information. This additional information is displayed at the bottom of the screen and supports the user's understanding of the main content.

**How to use the Bottom Sheet UI Pattern**

In this example, we create a button that opens and closes the Bottom Sheet widget.

1. In Service Studio, in the Toolbox, search for `Bottom Sheet`.

    The Bottom Sheet widget is displayed.

    ![Screenshot showing how to search for the Bottom Sheet widget in Service Studio](images/bottomsheet-widget-ss.png "Bottom Sheet Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.

    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**.

    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Bottom Sheet widget into the Main Content area of your application's screen and on the **Properties** tab, in the **Name** field, enter a name for the Bottom Sheet widget.

    ![Image depicting the process of dragging the Bottom Sheet widget into the Main Content area in Service Studio](images/bottomsheet-dragwidget-ss.png "Dragging Bottom Sheet Widget")

    By default, the Bottom Sheet widget contains a **TopBar** and a **Content** placeholder.

    ![Screenshot of the Bottom Sheet widget's default placeholders for TopBar and Content in Service Studio](images/bottomsheet-placeholder-ss.png "Bottom Sheet Widget Placeholder")

1. Add the relevant content to the TopBar and Content placeholders.

    ![Example of adding text, an icon, and a close button to the Bottom Sheet widget placeholders](images/bottomsheet-content-ss.png "Adding Content to Bottom Sheet")

    In this example, we add text, an icon, and a button to close the widget.

1. To close the bottom sheet, select the **Close** button, and on the **Properties** tab, from the **On Click** dropdown, select **New Client Action**.  

    ![Screenshot showing the selection of a new client action for the Close button on the Bottom Sheet widget](images/bottomsheet-onclick-ss.png "Setting On Click Action for Close Button")

1. Drag a **Run Client Action** to the client action, add from the **Select Action** popup, navigate to the **BottomSheetClose** action and click **Select**.

    ![Image illustrating how to add the BottomSheetClose action to a client action in Service Studio](images/bottomsheet-close-ss.png "Adding BottomSheetClose Action")

1. On the **Properties** tab, set the **WidgetId** to **BottomSheet.Id**.

    ![Screenshot demonstrating how to set the WidgetId to BottomSheet.Id in the properties tab](images/bottomsheet-id-ss.png "Setting WidgetId Property")

1. In this example we create a button to open the Bottom sheet by dragging the **Button** widget just below the **Bottom Sheet** widget and on the **Properties** tab, in the **Text** field, enter the text you want to appear on the button.

    ![Image showing the addition of an Open button below the Bottom Sheet widget in Service Studio](images/bottomsheet-openbutton-ss.png "Adding Open Button for Bottom Sheet")

1. Select the button, and on the **Properties** tab, from the **On Click** dropdown, select **New Client Action**.

1. Drag a **Run Client Action** to the client action, add from the **Select Action** popup, navigate to the **BottomSheetOpen** action and click **Select**.

    ![Screenshot depicting the process of adding the BottomSheetOpen action to a new client action](images/bottomsheet-openaction-ss.png "Adding BottomSheetOpen Action")

1. On the **Properties** tab, set the **WidgetId** to **BottomSheet.Id**.

1. You can customize the Bottom Sheet by selecting the pattern, and on the **Properties** tab, set the relevant (optional) properties.

    ![Image displaying the customization options for the Bottom Sheet pattern in the properties tab](images/bottomsheet-properties-ss.png "Customizing Bottom Sheet Properties")

After following these steps and publishing the module, you can test the pattern in your app.

![Screenshot of the Bottom Sheet UI pattern as it appears in a mobile app after implementation](images/bottomsheet-resultapp.png "Bottom Sheet in Mobile App")

## Properties

|Property|Description|
|---|---|
|Shape (Shape Identifier): Optional|Defines the Bottom Sheet shape.<br/>The predefined options are: SoftRounded, Rounded, and Sharp.<br/><br/>For example, Entities.Shape.Rounded inherits the rounded style. This is the default shape.|
|ShowHandler (Boolean): Optional|If set to True, a handler is displayed on top of the Bottom Sheet. The default value is True. If set to False, no handler is displaed.|
| ExtendedClass (Text): Optional|Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS. <br/>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |

## Events

### Bottom Sheet

|Event| Description|
|---|---|
|OnToggle: Optional|Event is triggered when the Bottom Sheet is opened or closed.|
