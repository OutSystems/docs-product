---
tags: runtime-traditionalweb; 
summary: Iframe displays information from other apps on the screen in small previews.
locale: en-us
guid: e334605f-9e05-484e-b50e-5450497c2412
---

# Iframe

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

You can use the Iframe UI Pattern to display information from other apps, on your screen, in bite-size previews. For more information about Iframes, see [HTML Iframes](https://www.w3schools.com/html/html_iframe.asp).

![](<images/iframe-8.png>)

**How to use the Iframe UI Pattern**

1. In Service Studio, in the Toolbox, search for `Iframe`.

    The Iframe widget is displayed.

    ![](<images/iframe-6-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Iframe widget into the Main Content area of your application's screen.

    ![](<images/iframe-7-ss.png>)

1. On the **Properties** tab, set the relevant properties, for example, the source URL, its title, as well as its width and height. In this example, we use the Wikipedia Website.

    Note: The target destination must have the necessary security permissions that allow you to embed their website in your app.

    ![](<images/iframe-5-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
| SourceURL (Text): Mandatory | The target URL that loads on the Iframe.<p>Examples<ul><li>"https://www.wikipedia.com" - Displays the Wikipedia website in your app as a bite-size preview</li></ul></p> | 
| Title (Text): Optional | Iframe title.<p>Examples<ul><li>"Wikipedia Website" - Displays **Wikipedia Website** as the Iframe title</li></ul></p>|
| Height (Text): Optional  | Iframe height (default is 100%). <p>Examples<ul><li>"100%" - The iframe height is 100% </li><li>200 - The iframe is 200 pixels high </li></ul></p>|
| Width (Text): Optional | Iframe width (default is 100%). <p>Examples<ul><li> "100%" - The iframe width is 100%</li><li>200 - The iframe is 200 pixels wide </li></ul></p>|
