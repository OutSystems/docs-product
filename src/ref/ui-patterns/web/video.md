---
tags: runtime-traditionalweb; 
summary: Explore advanced customization of video controls in Traditional Web Apps using OutSystems 11 (O11).
locale: en-us
guid: cd532674-6556-4684-bdd5-fcff4e6c422e
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=615:625
---

# Video Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and Classes

![Screenshot showing the layout and classes of the Video UI Pattern in a Traditional Web App](images/video-image-1.png "Video UI Pattern Layout")

## Advanced Use Case

### Use custom Play and Pause buttons

1. Set a name to the Video pattern.

    ![Image illustrating how to set a name to the Video pattern in the application](images/video-image-4.png "Setting Name to Video Pattern")

1. Create Play and Pause actions on the screen.

    ![Image depicting the creation of Play and Pause actions on the screen for the Video pattern](images/video-image-5.png "Creating Play and Pause Actions")

1. In the Logic tab, click on the OutSystems UI Web to go to the Video Folder.

    ![Image showing how to access the Video Folder in the Logic tab of OutSystems UI Web](images/video-image-6.png "Accessing Video Folder in Logic Tab")

1. Drag the PlayVideo and PauseVideo actions inside the Play and Pause actions you created.

    ![Image demonstrating how to drag the PlayVideo and PauseVideo actions into the created Play and Pause actions](images/video-image-7.png "Dragging Play and Pause Actions")

1. For each server action, set the WidgetId parameter to the name of the Video pattern.

    ![Image showing the process of setting the WidgetId parameter to the Video pattern's name for server actions](images/video-image-8.png "Setting WidgetId Parameter")

1. Create the elements you want to act as buttons. You can also wrap icons around containers and set the OnClick to the Play and Pause actions.

1. Publish and test.

    ![Animated GIF demonstrating the interaction with custom Play and Pause buttons in the Video UI Pattern](images/video-gif-1.gif "Video Pattern Interaction Demonstration")
