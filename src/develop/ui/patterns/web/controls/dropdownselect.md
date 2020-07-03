---
tags: runtime-traditionalweb; 
summary: The Dropdown Select UI Pattern allows a search functionality or multiple selection in lists with enhanced UX experience.
---

# Dropdown Select

The Dropdown Select is a pattern that you can apply to other patterns to implement a search functionality or multiple selection in lists. You can use the Dropdown Select UI Pattern when you need an enhanced combo box or list box in forms, as it offers a richer user experience than the list.

![](<images/dropdownselect-6-ss.png>)

**How to use the Dropdown Select UI Pattern**

1. In Service Studio, in the Toolbox, search for `Dropdown Select`.

    The Dropdown Select widget is displayed.

    ![](<images/dropdownselect-1-ss.png>)

1. From the Toolbox, drag the Dropdown Select widget into the Main Content area of your application's screen.

    ![](<images/dropdownselect-5-ss.png>)

1. From the Toolbox, drag the Combo Box widget into the Main Content area of your application's screen, and on the Properties tab, enter a name for the widget. In this example, we enter `ListofEmployees`.

    ![](<images/dropdownselect-9-ss.png?width=800>)

1. Right-click your screen name, select **Add Local Variable**, and enter a name for the new variable. In this example, we enter `SelectedRecord`.

    ![](<images/dropdownselect-8-ss.png>)

1. Select the Combo Box widget, and on the **Properties** tab, enter the values for the **Variable** and **Source Entity** properties. In this example, we select **SelectedRecord** for the **Variable** property and drag the **Employees** entity into the Combo Box widget. This automatically becomes the **Source Entity** property value. 

    ![](<images/dropdownselect-11-ss.png?width=800>)

1. Select the Dropdown Select widget, and on the **Properties** tab, from the **WidgetId** drop-down, select the Combo Box widget Id. In this example, we select **ListofEmployees.Id**.

    ![](<images/dropdownselect-12-ss.png>)

1. You can change the Dropdown Select's look and feel by setting the (Optional) properties on the Properties tab.

    ![](<images/dropdownselect-13-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

How this pattern behaves depends on the way it is bound.

* If you bind it to a Combo Box widget, Dropdown Select works as a selectable dropdown.
* If you bind it to a List Box, Dropdown Select works as a multi-select dropdown with removable tags.

## Properties

| **Property** |  **Description** |
|---|---|
| WidgetId (Text): Mandatory |  Element name (Combo Box and List Box) that triggers the element. |  
| NoResultsText (Text): Optional |  Text to display when there are no results. The default value is _"No results found."_ |  
| SearchEnabled (Boolean): Optional  | If False, the search functionality is removed. This property does not work with the List Box. If True, the search functionality is enabled. This is the default value. | 
| SearchResultsLimit (Long Integer): Optional |  Limits the number of results shown. | 
| AdvancedFormat (Text): Optional   | Enables more options beyond what's provided through the inputs. For more options, go to [Choices library](https://github.com/jshjohnson/Choices). Default value is `{}`<p>Example</p> <li>`{ searchPlaceholderValue: 'Search' }`</li> |
| ExtendedClass (Text): Optional  |  Add custom style classes to the Dropdown Select UI Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the Dropdown Select UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Dropdown Select UI styles being applied.</li></ul> |
  
