---
tags: runtime-traditionalweb; 
summary: UserInitials display user information in a circular badge.
---

# User Initials

You can use the User Initials UI Pattern to display a user’s initials or their image in a circular badge. 

![](<images/userinitials-image-4.png>)

**How to use the User Initials UI Pattern**

The User Initials UI Pattern usually displays dynamic information. In most cases, prior to using this pattern, you will need [to retrieve or update the Data](../../../../../develop/data/intro.md) that contains the information you want to display onscreen. You do this by using an [Action](../../../../../develop/logic/action-web.md). 

The following example demonstrates how you can display the initials of the registered users on your platform.

1. In Service Studio, in the Toolbox, search for `User Initials`. 

    The User Initials widget is displayed.

    ![](<images/userinitials-image-11.png>)

1. From the Toolbox, drag the User Initials widget into the Main Content area of your application's screen.

     ![](<images/userinitials-image-12.png>)

1. From the Element tree, create a Preparation action by right-clicking on your screen, and from the drop-down, select **Add Preparation**.
    
    This Preparation action executes logic that fetches the data before the screen is displayed.

     ![](<images/userinitials-image-13.png>)

1. Select the **Data** tab, and from the Entities tree, navigate to the **User** entity and drag it onto the Preparation action.

    ![](<images/userinitials-image-14.png>)

    This creates an [aggregate](https://success.outsystems.com/Documentation/11/Reference/OutSystems_Language/Data/Handling_Data/Queries/Aggregate) that retrieves all of the users on your platform.
       
1. To reopen your screen, select the **Interface** tab, and double-click on your screen.

1. Select the User Initials widget, and on the **Properties** tab, from the **Name** drop-down, select **Expression Editor**.

1. In the Expression Editor, enter the following expression and click **Done**.

    ``GetUsers.List.Current.User.Name``

    Note: You can also add the expression by navigating through the Expression Editor's **Scope** tree and double-clicking on the **Name** output parameter. 

    ![](<images/userinitials-image-15.png>)

   The **Name** property is now set to display the Name property of the Aggregate you added to the Preparation action, which gets the names of the registered users on your platform and displays them in the badge.

1. On the **Properties** tab, you can also customize the badge's look and feel by setting any of the optional properties, for example, the color, shape, and size. The following example displays a blue, medium-sized, circle badge.  

    ![](<images/userinitials-image-10.png>)  

After following these steps and publishing the module, you can test the pattern in your app.   
   

## Properties

| **Property** |  **Description** |
|---|---|
| Name (Text): Optional  |  The initials that appear inside the badge. Set this to a Data source that contains the value that the badge will display. Common use cases include displaying a value contained in a Variable or the result of an Aggregate (for instance, querying a 'Messages' table for the current user to return the count of new messages). <p>Examples <ul><li>_Blank_ - displays the initials JJ (default value)</li><li>_VariableName_ - displays the value that the variable "VariableName" holds at that time </li><li>_ExampleAggregate.Name_ - displays the names contained in the records returned by the "ExampleAggregate" aggregate execution</li></ul></p> | 
| Color (Color Identifier): Optional  | Set the badge color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available for the badge. <p>Examples <ul><li>_Blank_ - displays the badge in the color you chose when creating the app (default value)</li><li>_Entities.Color.Red_ - displays a red badge</li></ul></p></li></ul></p> | 
| Shape (Shape Identifier): Optional| Set the badge shape. Rounded, soft rounded, and sharp are the predefined shapes available for the badge. <p>Examples <ul><li>_Blank_ - displays a rounded badge (default value)</li><li>_Entities.Shape.Sharp_ - displays a square badge</li></ul></p>| 
| Size (Size Identifier): Optional  | Set the badge size. Small and medium are the predefined sizes available for the badge. <p>Examples <ul><li>_Blank_ - displays a medium sized badge (default value)</li><li>_Entities.Size.Small_ - displays a small sized badge</li></ul></p> | |
| IsLight (Boolean): Optional  | Specify the badge's background color. <p>Examples <ul><li>_Blank_ - A darker hue of the color is applied to the badge and a lighter color to the text (default value)</li><li>_True_ - A brighter hue of the color is applied to the badge and a darker color to the text.</li><li>_False_ - A darker hue of the color is applied to the badge and a lighter color to the text</li></ul></p> |
| ExtendedClass (Text): Optional |  Add custom style classes to the User Initials UI Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the User Initials UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the User Initials UI styles being applied.</li></ul></p> | 


<!---  Added to yml file
### See also
* OutSystems UI Live Style Guide: [User Initials](https://outsystemsui.outsystems.com/WebStyleGuidePreview/UserInitials.aspx)
* OutSystems UI Pattern Page: [User Avatar](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/PatternDetail?PatternId=80)