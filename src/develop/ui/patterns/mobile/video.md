---
tags: runtime-mobileandreactiveweb;   
summary: Learn how to embed a native video player in your app.
---

# Video

You can use the Video UI pattern to embed a native video player into your application.

![](<images/video-image-2.png>)

<div class="info" markdown="1">
 
Note: If you want to stream videos from YouTube, Vimeo, or others, see the [How to Add Video to Your Applications](https://success.outsystems.com/Documentation/Development_FAQs/How_to_Add_Video_to_Your_Applications) article. 
 
</div>

**How to use the Video UI Pattern**

<p><li>If using an external source file, insert the file URL.</li>
<li>If using a local file, include the video in a module as a resource and use the runtime path:</li>
<li>[new] If using binary data:</li></p>

1. Add a OnInitialize screen event
1. Add a JS Node to the client action 
1. Add an input parameter to the JS Node that will receive the binary data
1. Add an output parameter that will have the DataObjectURL
1. In the JS Node content you should add:

    ``$parameters.DataObjectURL = "data:video/mp4;base64," + $parameters.BinaryData;``

<!--1. In Service Studio, in the Toolbox, search for `Video`.

    The Video widget is displayed.

    ![](<images/video-image-10.png>)

1. From the Toolbox, drag the Video widget into the Main Content area of your application's screen.

    ![](<images/video-image-11.png>)
 
1. on the **Properties** tab, set the **SourceFile** property to the source video file you want to embed in your app. 

    * If using an external source file, insert the file URL.

        ![](<images/video-image-3.png>)

    * If using a local file, include the video in a module as a resource and use the runtime path as follows:

        1. On the **Data** tab, right-click the **Resources** folder and select **Import Resource**.

            ![](images/video-image-add-resource.png)
        
        1. Browse and select the video file you want to add and click **Open**.
        1. On the **Interface** tab, from the **Widget Tree**, select the Video pattern.
        1. On the **Properties** tab, select the **SourceFile** dropdown and select **Expression Editor**.
        1. In the Expression Editor, navigate to and select the file you added to the **Resources** folder, and click **Done**.

            ![](<images/video-image-12.png>)
    
            The file is added to the SourceFile property.
              ![](<images/video-image-13.png>)

1. On the **Properties** tab, you can also define (optional) properties, such as the height and width of the video and the audio settings.

      ![](<images/video-image-14.png>)

1. After following these steps and publishing the module, you can test the pattern in your app. 
       
## Properties

| **Property** |  **Description** | 
|---|---|
| SourceFile (Text): Mandatory  |  The video file URL or the runtime path of the resource video file. |
| Width (Text): Optional |  Width (in pixel or percentage) of the video. <p>Examples<ul><li>_Blank_ - The video is 100% wide. This is the default value. </li><li>_150_ - The video is 150px wide.</li></ul></p> | 
| Height (Text): Optional  | Height (in pixel or percentage) of the video. <p>Examples<ul><li>_Blank_ - The video is 100% high. This is the default value. </li><li>_150_ - The video is 150px high.</li></ul></p> |  
| Autoplay (Boolean): Optional | If True, the video starts playing as soon as the page is rendered. If False, the video doesn't play until the Play video control is clicked. This is the default.  | 
| Loop (Boolean): Optional  | If True, the video restarts playing as soon as it ends. If False, it does not reply. This is the default.   | 
| Muted (Boolean): Optional | If True, the audio of the video is disabled. If False, the audio is enabled. This is the default. | 
| Controls (Boolean): Optional  | If False, the video controls are disabled. If True, the video controls are enabled. This is the default. **Note** In the case of mobile apps, the controls are always enabled. |  
| ExtendedClass  | Add custom style classes to the Video UI Pattern. You define your [custom style classes](../../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ No custom styles are added (default value).</li><li>_"myclass"_ Adds the _myclass_ style to the Video UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Video UI styles being applied.</li></ul></p> |
  
## Notes

Autoplay parameter only works if Muted is set to True.

## Device Compatibility

In case of mobile, the controls will always be enabled. -->


