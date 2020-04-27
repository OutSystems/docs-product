---
tags: runtime-mobileandreactiveweb;  
summary: 
---

# Stacked Cards

You can use Stacked Cards UI Pattern to add swipeable cards that can be dragged in multiple directions triggering events, such as deny, approve, and archive. Ideal when you want to individually scan multiple cards.

   ![](images/stackedcards-preview.png)

## How to use the Stacked Cards Pattern

1. In Service Studio, in the Toolbox, search for  `Stacked Cards`. 

    The Stacked Cards widget is displayed.

    ![](images/stackedcards-icon.png)

1. From the Toolbox, drag the Swipe Events widget onto your application's screen.

    ![](images/Stacked_drag_pattern.png)

1. Add your content to the Content placeholder.

    ![](images/Stacked_interaction.png)

1. All available options have default parameters, but you can change them.

    ![](images/Stacked_default_parameters.png)

1. To use the overlays ( **UseOverlays** is _True_ by default), place content inside the respective placeholders ( **OverlayTop** , **OverlayRight** , **OverlayLeft**).

    ![](images/Stacked_overlay.png)

    a. If the option " **Use Overlays** " is set to _True_ and you don’t place content in the placeholders, they will not be displayed.  
    b. If the option “ **Use Overlays** ” is set _False_ and you add content to the placeholders, they will not be displayed.

After following these steps and publishing the module, you can test the pattern in your app.

### Adding styles to elements

This example shows you how to add styles to elements in the Pattern:

    
    
    .stackedcards-bottom, .stackedcards-top, .stackedcards-none {
         border-bottom: 1px solid #ebebeb; // Add a border-bottom to all elements
        background-color: #000; // Set a background-color to all elements
    }
    

### Setting the full height of elements

To set the full height of your elements in the Pattern, so that they fill the entire screen, use this CSS code:

    
    
    .stackedcards-container,
    .stackedcards {
        height: 100vh;
        -servicestudio-height: auto;
    }
    

### Defining specific heights for all Elements

The height of the first element defines the height of each element in the Pattern. To set a specific height, use the following CSS code:

    
    
    .stackedcards-container {
        height: 500px; // set your height
    }
    

### Applying different background colors to overlays

The overlays are enabled by default and have default colors in the Pattern. If you don’t want to use them, set “ **UseOverlays** ” to _False_ .

1. If the option " **UseOverlays** " is set to _True_ and you don’t place content in the placeholders, they will not be displayed.

1. If you change the option “ **UseOverlays** ” to _False_ and add content to the placeholders, they will not be displayed.

    ![](images/Stacked_background.png)

You can set other colors either by adding a container to **OverlayTop** , **OverlayRight** or **OverlayLeft** , and set your class. Or by using the following CSS code:

    
    
    .stackedcards-overlay.top {
         background-color: #2980b9; //set your background-color
    }
    .stackedcards-overlay.right {
        background-color: #27ae60; //set your background-color
    }
    .stackedcards-overlay.left {
        background-color: #c0392b; //set your background-color
    }
    

### Creating a button to execute swipes

Create each action and drag the [public actions](<public-actions.md>) (SwipeLeft, SwipeRight, or SwipeTop). In the Stacked Cards block, associate the handler to swipe events.  
![](images/Stacked_swipe.png)

### Creating a ListRemove button

Create an “OnListRemove” action and drag the ListRemoveNode and the UpdateStackedCards in the [public actions](<public-actions.md>) of the block.

## Properties

**Property** |  **Description** |  **Default Value**  
---|---|---  
![](images/input.png) StackedOptions  |  Change stacked cards view from bottom, top or none.  |  View from bottom  
![](images/input.png) Rotate  |  Activate the elements’ rotation for each move on stacked cards.  |  True 
![](images/input.png) Items  |  Number of visible elements when the stacked options are bottom or top.  |  5  
![](images/input.png) ElementsMargin  |  Define the distance of each element when the stacked options are bottom or top.  |  5  
![](images/input.png) UseOverlays  |  Enable or disable the overlays for swipe elements.  |  True
  
## Compatibility with other patterns

Avoid using the Stacked Cards Pattern inside patterns with swipe events / touch events, like [Tabs](<tabs.md>) or [Carousel](<carousel.md>).

## Samples

The following samples use the Stacked Cards pattern:

![](images/StackedCards-Sample-1.PNG)

![](images/StackedCards-Sample-2.PNG)

## See also

* OutSystems UI Pattern Page: [Stacked Cards](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/PatternDetail?PatternId=68)