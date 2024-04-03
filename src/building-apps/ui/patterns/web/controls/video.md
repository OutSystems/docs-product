---
tags: runtime-traditionalweb; 
summary: Learn how to embed a native video player in your app.
locale: en-us
guid: 23431108-d3aa-4c10-9307-c8ad925dc9f1
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing-an-Application?type=design&node-id=238%3A1&mode=design&t=KpVEJMvnBwiukqql-1
---

# Video

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

You can use the Video UI pattern to embed a native video player into your application.

![Screenshot of an embedded native video player in a Traditional Web App](images/video-image-2.png "Embedded Video Player UI")

<div class="info" markdown="1">

Note: If you want to stream videos from YouTube, Vimeo, or others, see the [How to Add Video to Your Applications](https://success.outsystems.com/documentation/how_to_guides/front_end/how_to_add_video_to_your_applications/) article. 

</div>

**How to use the Video UI Pattern**

1. In Service Studio, in the Toolbox, search for `Video`.

    The Video widget is displayed.

    ![Image showing the Video widget in the Service Studio toolbox](images/video-image-10.png "Video Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Video widget into the Main Content area of your application's screen.

    ![Illustration of dragging the Video widget into the Main Content area of an application screen](images/video-image-11.png "Dragging Video Widget into Main Content")
 
1. On the **Properties** tab, set the **SourceFile** property to the source video file you want to embed in your app. 

    * If using an external source file, insert the file URL.

        ![Example of setting the SourceFile property with an external video file URL](images/video-image-3.png "Setting SourceFile Property to External URL")

    * If using a local file, include the video in a module as a resource and use the runtime path as follows:

        1. On the **Data** tab, right-click the **Resources** folder and select **Import Resource**.

            ![Dialog for importing a video file as a resource into the module](images/video-image-add-resource.png "Importing Video File as Resource")
        
        1. Browse and select the video file you want to add and click **Open**.
        1. On the **Resource** properties tab, from the **Deploy Action** drop-down, select **Deploy to Target Directory**.

             ![Dropdown menu for selecting 'Deploy to Target Directory' as the deploy action for a video resource](images/video-image-12.png "Setting Deploy Action for Video Resource")

        1. On the **Interface** tab, from the **Widget Tree**, select the Video pattern.
       
        1. In the **SourceFile** property, enter the runtime path of the video file.

            ![Input field for entering the runtime path of the video file in the SourceFile property](images/video-image-13.png "Entering Runtime Path in SourceFile Property")
    
            **Tip**: You can copy the runtime path from the Resource Runtime Path property tab.

            ![Resource properties tab showing the runtime path of the video file for copying](images/video-image-14.png "Copying Runtime Path from Resource Properties")

1. On the Video **Properties** tab, you can also define (optional) properties, such as the height and width of the video and the audio settings.

1. After following these steps and publishing the module, you can test the pattern in your app. 

## Properties

| **Property** | **Description** |
|---|---|
| SourceFile (Text): Mandatory | The video file URL or the runtime path of the resource video file. |
| Width (Text): Optional | Width (in pixel or percentage) of the video.<br/><br/>Examples<br/><br/><ul><li>Blank - The video is 100% wide. This is the default value.</li><li>150 - The video is 150px wide.</li></ul> |
| Height (Text): Optional | Height (in pixel or percentage) of the video.<br/><br/>Examples<br/><br/><ul><li>Blank - The video is 100% high. This is the default value.</li><li>150 - The video is 150px high.</li></ul> |
| Autoplay (Boolean): Optional | If True, the video starts playing as soon as the page is rendered. If False, the video doesn't play until the Play video control is clicked. This is the default. |
| Loop (Boolean): Optional | If True, the video restarts playing as soon as it ends. If False, it does not replay. This is the default. |
| Muted (Boolean): Optional | If True, the audio of the video is disabled. If False, the audio is enabled. This is the default. |
| Controls (Boolean): Optional | If False, the video controls are disabled. If True, the video controls are enabled. This is the default.<br/>**Note** In the case of mobile apps, the controls are always enabled. |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |

## Notes

Autoplay parameter only works if Muted is set to True.

## Device Compatibility

In case of mobile, the controls will always be enabled.
