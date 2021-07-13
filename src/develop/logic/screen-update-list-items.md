---
summary: Learn how to manipulate a list and update it right away on the screen without having to reload the screen on a traditional web app.
tags: support-application_development; support-Front_end_Development;
---

# Update List Items on a Screen

While editing items in lists it is more efficient to only refresh the affected items in the interface than the entire list. OutSystems provides system actions to manipulate lists. When the list you manipulate is being displayed on the screen, these actions can also refresh the affected elements displayed on the screen right away.

To update list items in Reactive Web and Mobile:

1. Display the list on a screen. 
1. Add a button or link that updates the list. 
1. In the action associated with the button or link, drag the *Run Client Action* from the toolbox to the action flow. 
1. Select one of the following system actions to manipulate elements in the list variable bound with the widget displayed on the screen: 
    * ListAppend
    * ListAppendAll
    * ListInsert
    * ListRemove
    * ListClear 
1. The widget automatically displays the updated list. 

To update list items in Traditional Web:

1. Display the list on a screen. 
1. Add a button or link that updates the list and set the Method property to Ajax Submit. 
1. In the action associated with the button or link, drag the Execute Action from the toolbox to the action flow. 
1. Select one of the following system actions to manipulate elements in the list variable of the widget displayed on the screen: 
    * ListAppend 
    * ListInsert 
    * ListRemove 
1. The widget automatically displays the updated list. 
