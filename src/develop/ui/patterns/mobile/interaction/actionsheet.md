---
tags: runtime-mobileandreactiveweb;  
summary: Option menu, which slides from the bottom of the screen, triggered by a user action.
---

# Action Sheet

You can use the Action Sheet UI Patterns to add a menu that slides from the bottom of the screen when triggered by a user action.

![](<images/actionsheet-1-ss.png>)

**How to use the Action Sheet UI Pattern**

1. In Service Studio, in the Toolbox, search for `Action Sheet`.

    The Action Sheet widget is displayed.

    ![](<images/actionsheet-2-ss.png>)

1. From the Toolbox, drag the Action Sheet widget into the Main Content area of your application's screen.

    ![](<images/actionsheet-3-ss.png>)

    By default, the Action Sheet widget contains 5 button placeholders. 

1. Add the relevant content to the Button placeholders. In this example, we add 
 
1. On the **Properties** tab, you can also define (optional) properties, such as the height and width of the video and the audio settings.

After following these steps and publishing the module, you can test the pattern in your app. 
       
## Properties

| **Property** | **Description** | 
|---|---|
| SourceFile (Text): Mandatory | The video file URL or the runtime path of the resource video file. |
| Width (Text): Optional | Width (in pixel or percentage) of the video.<br/><br/>Examples<br/><br/><ul><li>_Blank_ - The video is 100% wide. This is the default value.</li><li>_150_ - The video is 150px wide.</li></ul> | 
| Height (Text): Optional | Height (in pixel or percentage) of the video.<br/><br/>Examples<br/><br/><ul><li>_Blank_ - The video is 100% high. This is the default value.</li><li>_150_ - The video is 150px high.</li></ul> |  
| Autoplay (Boolean): Optional | If True, the video starts playing as soon as the page is rendered. If False, the video doesn't play until the Play video control is clicked. This is the default.  | 
| Loop (Boolean): Optional | If True, the video restarts playing as soon as it ends. If False, it does not replay. This is the default. | 
| Muted (Boolean): Optional | If True, the audio of the video is disabled. If False, the audio is enabled. This is the default. | 
| Controls (Boolean): Optional | If False, the video controls are disabled. If True, the video controls are enabled. This is the default.<br/>**Note** In the case of mobile apps, the controls are always enabled. |  
| ExtendedClass | Add custom style classes to the Video UI Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/><ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the Video UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Video UI styles being applied.</li></ul> |