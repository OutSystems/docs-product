---
tags: runtime-traditionalweb; 
summary: Counter shows the total number of occurrences of several values regarding a single topic.
---

# Counter

<div class="info" markdown="1">

We’ve been working on this article. Please let us know how useful this new version is by voting.

</div>

You can use the Counter UI Pattern to display numerical information as a notification. For example, the Badge UI pattern is frequently used to notify users about the number of unread emails, unopened messages, or new tasks they may have.
 
 ![](<images/counter-image-14.png>)

**How to use the Counter UI Pattern**

The Counter UI Pattern usually displays dynamic information. In most cases, prior to using this pattern, you will need [to retrieve or update the Data](../../../../../develop/data/intro.md) that contains the information you want to display onscreen. You do this by using an [Action](../../../../../develop/logic/action-web.md). 

The following example demonstrates how you can display the number of registered users on your platform.

1. In Service Studio, in the Toolbox, search for `Counter`. 

    The Counter widget is displayed.

    ![](<images/counter-image-7.png>)

1. From the Toolbox, drag the Counter widget into the Main Content area of your application's screen.

    ![](<images/counter-image-9.png>)

1. From the Element tree, create a Preparation action by right-clicking on your screen, and from the drop-down, select **Add Preparation**.
    
    This Preparation action executes logic that fetches the data before the screen is displayed.

    ![](<images/counter-image-8.png>)
 

1. Select the **Data** tab, and from the Entities tree, navigate to the **User** entity and drag it onto the Preparation action.

    ![](<images/counter-image-10.png>)

    This creates an [aggregate](https://success.outsystems.com/Documentation/11/Reference/OutSystems_Language/Data/Handling_Data/Queries/Aggregate) that retrieves all of the users on your platform.
       
1. To reopen your screen, select the **Interface** tab, and double-click on your screen.

1. Within the Counter widget, right-click in the Text widget (containing the number 26), and select Convert to Expression.
    
      ![](<images/counter-image-11.png>)

1. In the Expression Editor, enter the following expression and click **Done**.

    ``GetUsers.Count``

    Note: You can also add the expression by navigating through the Expression Editor's **Scope** tree and double-clicking on the **Count** output parameter. 

   ![](<images/counter-image-12.png>)
    
   You have now created an expression that displays the Count property of the Aggregate you added to the Preparation action, which gets the number of users on your platform and displays them in your Counter.
    
1. From the **Properties** tab of each of the Counter's widgets, you can customize the Counter's display text and icon. For this example, the display text is changed to Registered Users.

      ![](<images/counter-image-13.png>)

1. Additionally, on the **Properties** tab, you can customize the Counter's look and feel by setting any of the optional properties, for example, the height and orientation.

      ![](<images/counter-image-3.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| **Property** |  **Description** |
|---|---|
| Orientation (Orientation Identifier): Optional  | Set the counter orientation. By default the counter is displayed horizontally. <p> Examples <ul><li>_Entities.Orientation.Horizontal_ - The counter displays horizontally </li><li>_Entities.Orientation.Vertical_ - The counter displays vertically</li></ul></p> |
| Height (Text): Optional  | Set the counter height. By default the counter height is 100 (pixel units). | 
| ExtendedClass (Text): Optional  |  Add custom style classes to the Counter UI Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the Counter UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Counter UI styles being applied.</li></ul></p> | 
