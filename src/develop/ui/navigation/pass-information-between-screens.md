---
summary: Learn how to create an input parameter to pass information to the destination screen.
tags: support-application_development; support-Mobile_Apps; support-webapps
locale: en-us
guid: abc236ca-9b9d-41ea-9694-7a0148c216b1
app_type: traditional web apps, mobile apps, reactive web apps
---

# Pass Data Between Screens With Input Parameters

Screens sometimes require input information. This is common in navigation, when users click on a link wanting to see more about an item. The destination Screen receives the information about the item, for example an identifier of a product. You pass information between screens with Input Parameters.

To pass information with Input Parameters:

1. In the destination Screen add an Input Parameter.
2. In the source Screen add a link to the destination Screen and set the Input Parameter value.

<div class="info" markdown="1">

To learn more about Screens, Widget, and Input Parameters see the [introductory video about the UI development](https://www.outsystems.com/learn/lesson/1923/ui-development) and [variables](https://www.outsystems.com/learn/lesson/2069/variables).

</div>

## Add a new Input Parameter in the destination Screen

To add an Input Parameter to a Screen in Service Studio:

1. Go to **Interface** > **UI Flows** > **MainFlow** and locate your Screen.

    ![Selected Screen in Service Studio](images/screen-selected-ss.png?width=400)

    <div class="info" markdown="1">

    You can use Input Parameters with Blocks as well. 

    </div>
    
   
2. Right-click the Screen and select **Add Input Parameter**. A new Input Parameter appears. 

    ![Help menu to Create Input Parameter](images/help-menu-input-parameter-ss.png?width=400)

3. Service Studio selects the name of the Input Parameter and sets the focus for you to enter the name. Enter the name of the Input Parameter and press the Enter key.

    ![Input Parameter with selected text name](images/new-input-parameter-ss.png?width=300)


<div class="info" markdown="1">

Use smart names with Input Parameters to set the data type automatically. For example, if you create an Input Parameter and name it **PurchaseDate**, Service Studio sets the data type to **Date**. See more in [Service Studio Tips and Tricks](../../../getting-started/tips-tricks/tips-tricks.md#Guess_my_Attribute.2FVariable_Data_Type).

</div>

## Send a value from the source Screen

In the Screen from which you're linking (source) to the Screen that receives the value (destination), add a widget and supply a value in the **On Click Event**. Here is an example with a Link widget, but the same works with a Button.

1. Search for the **Link** widget and drag it to the Screen. Then, enter your link text, for example "A link to another page".
   
    ![A Screen with a link](images/screen-with-link-ss.png?width=700)

    Right now you can't publish the app because the 1-Click Publish button is red and there's an error. That is expected, as you need to set a destination for your Link as well. 

2. Select the Link widget, go to **Properties** > **Events** > **On Click**, and in the list select your destination Screen. Notice how the Input Parameter shows below the Screen name in the properties.

    ![Link widget properties with the input parameter](images/link-properties-input-parameter-ss.png?width=400)
    
3. Still in the Link widget properties, under the Screen you selected, set the value for the Input Parameter.

    ![Link widget properties with the input parameter](images/link-properties-input-parameter-set-ss.png?width=400)

    In our example, we entered **100** directly in the Input Parameter field. Usually you set a dynamic value, for example, with a Local Variable.

4. Publish the app. When you click the link in the source Screen, the user navigates to the destination Screen. The destination Screen opens and receives **100** as the value of the Input Parameter.
