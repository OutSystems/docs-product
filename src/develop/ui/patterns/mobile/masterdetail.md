---
tags: runtime-mobileandreactiveweb;  
summary: Displays a master list and the details for the currently selected item.
---

# Master Detail

You can use the Master Detail Pattern to display a master list of items and their related details, for example, a list of employees and their corresponding details. 

![](images/masterdetail-preview.png)


## How to use the Master Detail UI Pattern

1. In Service Studio, in the Toolbox, search for `Master Detail`. 

    The Master Detail widget is displayed.
    
    ![](images/masterdetail-widget.png)

1. From the Toolbox, drag the Master Detail widget into the Main Content area of your application's screen.

     ![](images/masterdetail-image-1.png)

 1. Bind a List to the **ItemList** parameter and leverage the block events to change the content placeholder.

1. Create a local boolean variable and set it on **OpenedOnPhone**.

    ![](images/MasterDetail_list_open.png)

1. To open the detail of the clicked element, use a link for an action, set your local variable to True , and add logic to open the correct detail.

    ![](images/MasterDetail_assignments.png)

1. To close the detail, create an action and set your local variable to False , and use this action in the **DetailClose** event. Add the necessary logic.

    ![](images/MasterDetail_close_detail.png)

    ![](images/MasterDetail_list_open_false.png)

After following these steps and publishing the module, you can test the pattern in your app. 

## Properties

**Property** |  **Description** |   
|---|---|
|ItemList  |  These are the items for the list on the left side of the MasterDetail.  |  N/A  
  
 
  
## Compatibility with other patterns

This pattern should be used alone inside the screen content because it will adapt to the height of the parent. Additionally, you should avoid using the MasterDetail pattern inside patterns with swipe events, such as [Tabs](<tabs.md>).

## Samples

You can use the Master Detail pattern as a sample:

![](images/MasterDetail-Sample-1.PNG)
