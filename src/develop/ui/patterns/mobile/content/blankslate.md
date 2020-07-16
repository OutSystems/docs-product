---
tags: runtime-mobileandreactiveweb;  
summary: Blank Slate informs end users when they start using the application, complete a task or when there is no data available for display.
---

# Blank Slate

You can use the Blank State UI Pattern to inform end users, for example, to complete a task or when there is no data available for display etc.

![](<images/blankslate-5-ss.png?width=800>)

**How to use the Blank Slate UI Pattern**

1. In Service Studio, in the Toolbox, search for `Blank Slate`.

    The Blank Slate widget is displayed.

    ![](<images/blankslate-2-ss.png>)

1. From the Toolbox, drag the Blank Slate widget into the Main Content area of your application's screen.

    ![](<images/blankslate-3-ss.png?width=800>)

    By default, the Blank Slate widget contains icon, content, and action placeholders. 

1. Add your content to the placeholders. 

    In this example, we change the icon to a calendar icon, enter some text in the Text placeholder, and add a button to the Actions placeholder. This button, when clicked, redirects the user to another page

    ![](<images/blankslate-4-ss.png?width=800>)

After following these steps and publishing the module, you can test the pattern in your app. 

## Properties

| **Property** |  **Description** |
|---|---|
| FullHeight (Boolean): Optional| Displays a larger Blank Slate, taking over full page height. If True, the Blank Slate takes over the full page height. This is the default value. If False, the Blank Slate doesn't take over the full height of the page.|  
| ExtendedClass (Text): Optional  |  Add custom style classes to the Blank Slate UI Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<p>Examples</p><ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the Blank Slate UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Blank Slate UI styles being applied. </li></ul> |
