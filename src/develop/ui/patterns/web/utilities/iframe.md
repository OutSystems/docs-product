---
tags: runtime-traditionalweb; 
summary: Iframe displays information from other apps on the screen in small previews.
---

# Iframe
 
<div class="info" markdown="1">

We’ve been working on this article. Please let us know how useful this new version is by voting.

</div>

 You can use the Iframe UI Pattern to display information from other apps, on your screen, in bite-size previews. For more information about Iframes, see [HTML Iframes](https://www.w3schools.com/html/html_iframe.asp).

![](<images/iframe-image-8.png>)

**How to use the Iframe UI Pattern**

1. In Service Studio, in the Toolbox, search for `Iframe`. 

    The Iframe widget is displayed.
    
    ![](<images/iframe-image-6.png>)
      
1. From the Toolbox, drag the Iframe widget into the Main Content area of your application's screen.

    ![](<images/iframe-image-7.png>)

1. On the **Properties** tab, set the relevant properties, for example, the source URL, its title, as well as its width and height. In this example, we use the Wikipedia Website.

    Note: The target destination must have the necessary security permissions that allow you to embed their website in your app.

    ![](<images/iframe-image-5.png>)

After following these steps and publishing the module, you can test the pattern in your app.



## Properties

| **Property** |  **Description** |
|---|---|
| SourceURL (Text): Mandatory | The target URL that loads on the Iframe.<p>Examples<ul><li>_"https://www.wikipedia.com"_ - Displays the Wikipedia website in your app as a bite-size preview</li></ul></p> | 
| Title (Text): Optional | Iframe title.<p>Examples<ul><li>_"Wikipedia Website"_ - Displays _Wikipedia Website_ as the Iframe title</li></ul></p>|
| Height (Text): Optional  | Iframe height (default is 100%). <p>Examples<ul><li>_"100%"_ - The iframe height is 100% </li><li>_200_ - The iframe is 200 pixels high </li></ul></p>|
| Width (Text): Optional | Iframe width (default is 100%). <p>Examples<ul><li> _"100%"_ - The iframe width is 100%</li><li>_200_ - The iframe is 200 pixels wide </li></ul></p>|
