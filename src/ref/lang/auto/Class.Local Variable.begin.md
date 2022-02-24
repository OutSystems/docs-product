---
summary: A Local Variable exists only in the scope of its element.
--- 

A Local Variable exists only in the scope of its element. They can only be assigned and used locally inside that scope. Local variables are destroyed when execution leaves the scope of the parent element.  

In the following example, the Employees screen has four Local Variables (`SearchKeyword`, `TableSort`, `StartIndex` and `MaxRecords`):

**Place image here: Example of a screen with four Local Variables**

## How to use

In this example, we show how to use a Local Variable when using a widget that requires an input, like the Search widget. By default, the Search widget contains an Input placeholder and widget.

1. Select the Input widget, and on the **Properties** tab, create a local variable by selecting the **Variable** dropdown and selecting **New Local Variable**.

    ![](<images/local-variable-1-ss.png>)

1. Enter a name for the variable.

    In this example, we enter `SearchKeyword`.

    **Place image here: SearchKeyword**

    This variable holds the value entered by the user. This variable can only be used inside the screen where it is defined.

1. You can then define a filter in an aggregate using this local variable. In this example, we have the `GetEmployees` aggregate which has the attribute `FirstName`, among others. Double-click the aggregate from the Elements tree to open it.

    **Place image here: open the aggregate**

1. Select the **Filter** tab. Click **Add filter**.

    **Place image here: click Add filter**

1. Set the Filter Condition to:

    ```outsystems
    Employee.FirstName like "%" + SearchKeyword + "%"
    ```
    Click **Close** to save the filter.  
    The displayed data now changes according to the value of the Local Variable `SearchKeyword`.


Find more about Local Variables here: https://www.outsystems.com/training/lesson/2069/variables?LearningPathId=18 
