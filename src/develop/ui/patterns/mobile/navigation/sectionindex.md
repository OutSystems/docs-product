---
tags: runtime-mobileandreactiveweb;
summary: Section Index organizes the content of a screen, enabling quick navigation within the page.
---

# Section Index

You can use the Section Index UI Pattern to organize the content of a screen, enabling quick navigation within the page.

![](<images/sectionindex-7-ss.png>)

**How to use the Section Index UI Pattern**

1. In Service Studio, in the Toolbox, search for `Section Index`.

    The Section Index widget is displayed.

    ![](<images/sectionindex-8-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Section Index widget into the Main Content area of your application's screen.

    In this example, we drag the Section Index widget into a column. 

    ![](<images/sectionindex-1-ss.png?width=800>)

1. In the Toolbox, search for and drag the Section widget into the Main Content area of your application's screen. Add as many sections as you require for your app.

    In this example, we drag 4 Section widgets into a column. Each section widget contains Title and Content placeholders. 

    ![](<images/sectionindex-2-ss.png?width=800>)

1. Add the relevant content to Section widget's **Title** and **Content** placeholders.

    In this example, we add employee names to the **Title** placeholders, and Card Sectioned widgets with some text and images to the **Content** placeholder.

    ![](<images/sectionindex-3-ss.png?width=800>)

    A link is automatically created to every section you have on the screen. The name of the link is based on the text you entered in the **Title** placeholder of each section. In the following example, the links are set to the employee names we entered in step 2.

    ![](<images/sectionindex-4-ss.png>)

1. On the **Properties** tab, you can customize the Section Index's look and feel by setting any of the optional properties.

    ![](<images/sectionindex-5-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| **Property** |  **Description** |
|---|---|
| IsSmooth (Boolean): Optional  |  If True, the navigation to the destination is animated. This is the default. If False, the navigation is instant. |
| IsFixed (Text): Optional  | If True, the Section Index Pattern is always in the same position on the screen. This is the default. If False, the Section Index Pattern scrolls with the page content. |
| TopPosition (Integer): Optional  |  Distance in pixels from the top of the page to the first item in the section index. The default value is 0. |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_''myclass''_ - Adds the _myclass_ style to the UI styles being applied.</li><li>_''myclass1'' ''myclass2''_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |
  
## Additional notes

Remember to use the **Title** placeholder in the Section Index pattern as this defines the text for each Section Index link.
