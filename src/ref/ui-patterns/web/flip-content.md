---
tags: runtime-traditionalweb; 
summary: Advanced use cases for the Flip Content UI Pattern.
locale: en-us
guid: 478229ef-fead-4fea-be67-f0fdd66c7209
---

# Flip Content Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![](<images/flipcontent-6-diag.png?width=600>)

## CSS selectors

| **Element** |  **CSS Class** |  **Description**  |
| --- | --- | --- |
| .flip-content | .flip-content.is--hover |  When Trigger parameter is Hover |
| .flip-content | .flip-content.is--click |  When Trigger parameter is Click |
| .flip-content | .flip-content.is--click.is--flipped |  When FlipContent is flipped |

## Advanced use case

### Use the events on the Flip Content Pattern

It is possible to interact with other patterns or trigger actions with FlipContent events. To use the events, create a screen action to hold the event.

1. Create a local Boolean variable and name it "Flipped".

1. Drag the Flip Content pattern into the preview.

1. Set the content in the front and back placeholders.

    ![](<images/flipcontent-7-ss.png>)

1. Drag a container into the preview and set the Name to AlertEvent.

1. Drag an If condition into the container and set the condition to "Flipped".

1. Set the content in the True and False branches (for instance, the Alert pattern).

    ![](<images/flipcontent-8-ss.png>)

1. Select the FlipContent pattern and in the Events section, create a new screen action to hold the event.

    ![](<images/flipcontent-9-ss.png>)

1. Drag the Assign tool in the screen action to assign the Flipped local variable to the isFlipped event variable.

1. Drag the Ajax Refresh node into the screen action and set AlertEvent as the parameter to update the container on the screen. Remove the animation effect.

    ![](<images/flipcontent-10-ss.png>)

1. Publish and test.

    ![](<images/flipcontent-11.gif>)

### Use the Toggle server action on Flip Content Pattern

It is possible to use a button or containers to interact with FlipContent by using a server action ToggleFlipContent.

1. Create a local Boolean variable and name it "Flipped".

1. Drag the FlipContent pattern into preview and set the Name property to FlipContentToggleAction.

1. In FlipContent, set the Trigger to Manual.

1. Set the content in the front and back placeholders.

    ![](<images/flipcontent-7-ss.png>)

1. Drag a button into the preview.

1. Set the method to Ajax Submit and create a new screen action.

    ![](<images/flipcontent-12-ss.png>)

1. In the screen action, go to Logic tab and drag the ToggleFlipContent server action into the screen action.

    ![](<images/flipcontent-9-ss.png>)

1. Set the WidgetId in ToggleFlipContent.

    ![](<images/flipcontent-13-ss.png>)

1. Publish and test.

    ![](<images/flipcontent-image-10.gif>)
