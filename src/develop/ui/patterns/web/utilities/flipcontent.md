---
tags: runtime-traditionalweb; 
summary: FlipContent prioritizes information display, keeping the interface uncluttered.
---

# FlipContent

A container that builds a flippable widget with placeholders for front and back elements.

Use the FlipContent to prioritize information display, keeping the interface uncluttered. Show critical information first, revealing more details with a flip.

**How to use**

1. Drag the FlipContent pattern into the preview.

1. Set the content in the front and back placeholders.

1. Publish and test.

    ![](<images/flipcontent-image-1.gif?width=500>)

## Input Parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| Trigger  | Set the trigger event for the flip. It can be a mouse hover or a click event. | Trigger Identifier | False | Entities.Trigger.Hover |
| ExtendedClass  |  Add custom style classes to this Block. |  Text | False | none |

## Layout and Classes

![](<images/flipcontent-image-2.png?width=600>)

## CSS Selectors

| **Element** |  **CSS Class** |  **Description**  |
| --- | --- | --- |
| .flip-content | .flip-content.is--hover |  When Trigger parameter is Hover |
| .flip-content | .flip-content.is--click |  When Trigger parameter is Click |
| .flip-content | .flip-content.is--click.is--flipped |  When FlipContent is flipped |

## Advanced Use Case

### Use the Events on FlipContent pattern

It is possible to interact with other patterns or trigger actions with FlipContent events. To use the events, create a screen action to hold the event.

1. Create a local Boolean variable and name it "Flipped".

1. Drag the FlipContent pattern into the preview.

1. Set the content in the front and back placeholders.

    ![](<images/flipcontent-image-3.png>)

1. Drag a container into the preview and set the Name to AlertEvent.

1. Drag an If condition into the container and set the condition to "Flipped".

1. Set the content in the True and False branches (for instance, the Alert pattern).

    ![](<images/flipcontent-image-4.png>)

1. Select the FlipContent pattern and in the Events section, create a new screen action to hold the event.

    ![](<images/flipcontent-image-5.png>)

1. Drag the Assign tool in the screen action to assign the Flipped local variable to the isFlipped event variable.

1. Drag the Ajax Refresh node into the screen action and set AlertEvent as the parameter to update the container on the screen. Remove the animation effect.

    ![](<images/flipcontent-image-6.png>)

1. Publish and test.

    ![](<images/flipcontent-image-7.gif>)

### Use the Toggle server action on FlipContent pattern

It is possible to use a button or containers to interact with FlipContent by using a server action ToggleFlipContent.

1. Create a local Boolean variable and name it "Flipped".

1. Drag the FlipContent pattern into preview and set the Name property to FlipContentToggleAction.

1. In FlipContent, set the Trigger to Manual.

1. Set the content in the front and back placeholders.

    ![](<images/flipcontent-image-3.png>)

1. Drag a button into the preview.

1. Set the method to Ajax Submit and create a new screen action.

    ![](<images/flipcontent-image-8.png>)

1. In the screen action, go to Logic tab and drag the ToggleFlipContent server action into the screen action.

    ![](<images/flipcontent-image-5.png>)

1. Set the WidgetId in ToggleFlipContent.

    ![](<images/flipcontent-image-9.png>)

1. Publish and test.

    ![](<images/flipcontent-image-10.gif>)
