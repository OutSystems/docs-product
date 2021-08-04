---
tags: runtime-mobileandreactiveweb;  
summary: Use the Button Loading pattern to call actions that don't run immediately.
---

# Button Loading

You can use the Button Loading UI Pattern to call actions that don't run immediately, provide a visual hint, and disable the button from being clicked until it becomes available again.


**How to use the Button Loading UI Pattern**

1. In Service Studio, in the Toolbox, search for `Button Loading`.

    The Button Loading widget is displayed.

    ![](<images/buttonloading-1-ss.png>)

    If the UI widget does not display, it may be because you used a ready-made app, which deletes unused widgets from the module. To make additional widgets available in your app:

    a. Go to **Module > Manage dependencies**.

    b. Search for and select the relevant Producer, for example OutSystemsUI. Ensure Show All is selected. 

    c. On the Public elements for the selected Producer displayed on the right, ensure Show All is selected.
    
    d. Search for and select the element you want to add, and click **Apply**. 
    
    e. In Service Studio, in the Toolbox, search for the widget again.

1. From the Toolbox, drag the Button Loading widget into the Main Content area of your application's screen.

    In this example, we drag the widget onto a form that is already in the Main Content area.

    By default the **Button Loading** widget contains a **Button** widget. We change the text of the button to **Create New User**.

    ![](<images/buttonloading-2-ss.png>)

3. Create a new local variable (of Boolean type) to control the state of the **Button Loading** widget. In this example, we call it **CreatingNewUser** and set the default value to **False**.

    ![](<images/buttonloading-3-ss.png>)

1. In this example, we also set the **ShowLoadingAndLabel** property to **False** so that the spinner doesn't show while the button logic is being executed.

    ![](<images/buttonloading-4-ss.png>)

5. Double-click the **Button** widget and add the necessary logic. In this example, the **ButtonOnClick** action creates a new user. We also add **Assign** logic for the **Button Loading** widget. The first Assign has the **CreatingNewUser** set to **False**. This is so the spinner doesn't display. The second Assign has the **CreatingNewUser** set to **True**. (The logic is added between the two Assigns.)

    ![](<images/buttonloading-5-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

**Result**

![](<images/buttonloading-6-ss.png>)


## Properties

| Property | Description |
|---|---|
| IsLoading (Boolean): Mandatory | If True, the button shows the loading spinner. If False, the button doesn't show the loading spinner. |
| ShowLoadingAndLabel (Boolean): Optional | If True, the loading spinner displays beside the label. If False, the loading spinner displays underneath the label. This is the default. |
| ExtendedClass (Text): Optional | <p>Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.</p> <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |
