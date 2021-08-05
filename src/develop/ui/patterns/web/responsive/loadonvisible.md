---
tags: runtime-traditionalweb; 
summary: LoadOnVisible improves both the actual and perceived speed of your application.
---

# Load on Visible 

You can use the Load on Visible UI Pattern to enhance the speed of your application as well as improve user experience. Using this UI pattern, information is loaded onto the page only when it is visible to the user. For example, instead of loading all text and images onto a page at once, they only appear when the user scrolls down the page and the information/image becomes visible.

**How to use the Load on Visible UI Pattern**

1. In Service Studio, in the Toolbox, search for `Load on Visible`. 

    The Load on Visible widget is displayed.

     ![](<images/loadonvisible-3-ss.png>)

    If the UI widget does not display, it may be because you used a ready-made app, which deletes unused widgets from the module. To make additional widgets available in your app:

    a. Go to **Module > Manage dependencies**.

    b. Search for and select the relevant Producer, for example OutSystemsUI. Ensure Show All is selected. 

    c. On the Public elements for the selected Producer displayed on the right, ensure Show All is selected.
    
    d. Search for and select the element you want to add, and click **Apply**. 
    
    e. In Service Studio, in the Toolbox, search for the widget again.

1. From the Toolbox, drag the Load on Visible widget into the Main Content area of your application's screen.

    ![](<images/loadonvisible-4-ss.png>)

1. Add the required content to the placeholder inside the Load on Visible widget. 

    In this example, we add images by dragging the Image widget into the Load on Visible widget and selecting an image from the sample OutSystems UI images.

    ![](<images/loadonvisible-5-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

