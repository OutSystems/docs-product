---
summary: A Local Variable exists only in the scope of its element.
--- 

A Local Variable exists only in the scope of its element. They can only be assigned and used locally inside that scope. Local variables are destroyed when execution leaves the scope of the parent element.  


## How to use

This example shows how to use a Local Variable to keep the value of a Search widget. The value of the variable is then used to filter an aggregate.

1. Select the Input widget, and on the **Properties** tab, create a local variable by selecting the **Variable** dropdown and selecting **New Local Variable**.

    ![Adding a new Local Variable to an Input](<images/local-variable-ss.png>)

1. Enter a name for the variable, for example `SearchKeyword`. Make sure the **Data Type** is set to `Text`.

    ![Entering the name for the Local Variable](<images/variable-searchkeyword-ss.png>)

1. Use the Local Variable to [filter the aggregate](../../../develop/data/query/filter-results.md).

    ![Aggregate with a filter that uses the SearchKeyword Variable to filter the results](<images/filtered-aggregate-ss.png>)


Find more about [Local Variables](https://www.outsystems.com/training/lesson/2069/variables?LearningPathId=18).  
To practice, check these exercises where you can see examples of Local Variables usage:
* In Reactive Web development: [Using Local Variables for pagination and sorting](https://www.outsystems.com/training/lesson/2045/pagination-and-sorting-exercise?LearningPathId=18)
* In Traditional Web development: [Using Local Variables for data queries and widgets](https://www.outsystems.com/training/lesson/1766/data-queries-and-widgets-ii-exercise?LearningPathId=2)
