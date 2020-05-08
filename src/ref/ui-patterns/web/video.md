---
tags: runtime-traditionalweb; 
summary: Advanced use cases for the Video UI Pattern
---

# Video UI Pattern Reference

## Layout and Classes

![](<images/video-image-1.png>)

## Advanced Use Case

### Use custom Play and Pause buttons

1. Set a name to the Video pattern.

    ![](<images/video-image-4.png>)

1. Create Play and Pause actions on the screen.

    ![](<images/video-image-5.png>)

1. In the Logic tab, click on the OutSystems UI Web to go to the Video Folder.

    ![](<images/video-image-6.png>)

1. Drag the PlayVideo and PauseVideo actions inside the Play and Pause actions you created.

    ![](<images/video-image-7.png>)

1. For each server action, set the WidgetId parameter to the name of the Video pattern.

    ![](<images/video-image-8.png>)

1. Create the elements you want to act as buttons. You can also wrap icons around containers and set the OnClick to the Play and Pause actions.

1. Publish and test.

    ![](<images/video-gif-1.gif>)



