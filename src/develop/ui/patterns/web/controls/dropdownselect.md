---
tags: runtime-traditionalweb; 
summary: The Dropdown Select UI Pattern allows a search functionality or multiple selection in lists with enhanced UX experience.
---

# Dropdown Select 

You can use the Dropdown Select UI Pattern to implement a search functionality or multiple selection in lists. You can use the Dropdown Select UI Pattern when you need an enhanced combo box or list box in forms, as it offers a richer user experience than the list.

![](<images/dropdownselect-6-ss.png>)

**How to use the Dropdown Select UI Pattern**

1. In Service Studio, in the Toolbox, search for `Dropdown Select`.

    The Dropdown Select widget is displayed.

    ![](<images/dropdownselect-1-ss.png>)

1. From the Toolbox, drag the Dropdown Select widget into the Main Content area of your application's screen.

    ![](<images/dropdownselect-5-ss.png>)

1. Place Combo Box or List Box in the main editor. This is your main widget.

1. Make sure you enter a value in the Name property of the main widget. 

1. Drag DropdownSelect pattern into the preview next to your main widget.
  
1. Set the mandatory value `WidgetId` in the properties pane that corresponds to the main widget.

1. Adjust the widget width by adjusting the width of the outer container.


After following these steps and publishing the module, you can test the pattern in your app. 

How this pattern behaves depends on the way it is bound.

* If you bind it to a Combo Box widget, DropdownSelect works as a selectable Dropdown.
* If you bind it to a List Box, DropdownSelect works as a multi-select with removable tags.

## Properties

| **Property** |  **Description** | 
|---|---|
| WidgetId (Text): Mandatory |  Element name (Combo Box and List Box) that triggers the element. |  
| NoResultsText (Text): Optional |  Text to display when there are no results. The default value is _"No results found."_ |  
| SearchEnabled (Boolean): Optional  | If False, the search functionality is removed. This property does not work with the List Box. If True, the search functionality is enabled. This is the default value. | 
| SearchResultsLimit (Long Integer): Optional |  Limits the number of results shown. | 
| AdvancedFormat (Text): Optional   | Enables more options beyond what's provided through the inputs. For more options, go to [Choices library](https://github.com/jshjohnson/Choices). Default value is `{}`<p>Example</p> <li>`{ searchPlaceholderValue: 'Search' }`</li> |
| ExtendedClass (Text): Optional  |  Add custom style classes to the Dropdown Select UI Pattern. You define your [custom style classes](../../../../../../develop/ui/look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the Dropdown Select UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Dropdown Select UI styles being applied.</li></ul> |
  
