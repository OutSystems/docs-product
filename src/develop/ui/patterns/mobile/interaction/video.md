---
tags: runtime-mobileandreactiveweb;  
summary: Video allows you to embed a native video player.
---

# Video

You can use the Video UI pattern to embed a native video player into your application.

<div class="info" markdown="1">
 
Note: If you want to stream videos from YouTube, Vimeo, or others, see the [How to Add Video to Your Applications](https://success.outsystems.com/Documentation/Development_FAQs/How_to_Add_Video_to_Your_Applications) article. 
 
</div>

**How to use the Video UI Pattern**

1. In Service Studio, in the Toolbox, search for `Video`.

    The Video widget is displayed.

    ![](<images/video-2-ss.png>)

1. From the Toolbox, drag the Video widget into the Main Content area of your application's screen.

    ![](<images/video-3-ss.png>)
 
1. On the **Properties** tab, set the **VideoURL** property to the source video file you want to embed in your app. 

    * If using an external source file, insert the file URL.

        ![](<images/video-4-ss.png>)

    * If using a local file, include the video in a module as a resource and use the runtime path as follows:

        1. On the **Data** tab, right-click the **Resources** folder and select **Import Resource**.

            ![](<images/video-5-ss.png>)
        
        1. Browse and select the video file you want to add and click **Open**.

        1. On the **Resource** properties tab, from the **Deploy Action** drop-down, select **Deploy to Target Directory**.

            ![](<images/video-6-ss.png>)

        1. On the **Interface** tab, from the **Widget Tree**, select the Video pattern.
       
        1. In the **VideoURL** property, enter the runtime path of the video file.

            ![](<images/video-7-ss.png>)
    
            **Tip**: You can copy the runtime path from the Resource Runtime Path property tab.

            ![](<images/video-8-ss.png>)

1. On the Video **Properties** tab, you can also define (optional) properties, such as the height and width of the video and the audio settings.

    ![](<images/video-9-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app. 
       
## Properties

| Property | Description | 
|---|---|
| VideoURL (Text): Mandatory | The video file URL or the runtime path of the resource video file. |
| PosterURL (Text): Optional | The URL to the poster image that displays before the video starts. |
| Width (Text): Optional | Width (in pixel or percentage) of the video.<br/><br/>Examples<br/><br/><ul><li>_Blank_ - The video is 100% wide. This is the default value.</li><li>_150_ - The video is 150px wide.</li></ul> | 
| Height (Text): Optional | Height (in pixel or percentage) of the video.<br/><br/>Examples<br/><br/><ul><li>_Blank_ - The video is 100% high. This is the default value.</li><li>_150_ - The video is 150px high.</li></ul> |  
| Muted (Boolean): Optional | If True, the video audio is muted. If False, the video audio is not muted. This is the default.  | 
| Loop (Boolean): Optional | If True, the video replays as soon as it ends. If False, the video does not replay. This is the default.  | 
| Controls (Boolean): Optional | If True, the video controls are enabled. If False, the video controls are disabled. This is the default.<br/>**Note** In the case of mobile apps, the controls are always enabled. |  
| Autoplay (Boolean): Optional | If True, the video starts once the page is loaded. If False, the video doesn't start immediately. This is the default.|  
| ExtendedClass | Add custom style classes to the Video UI Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/><ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the Video UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Video UI styles being applied.</li></ul> |
