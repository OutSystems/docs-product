---
summary: A Local Variable exists only in the scope of its element.
--- 

A Local Variable exists only in the scope of its element. They can only be assigned and used locally inside that scope. Local variables are destroyed when execution leaves the scope of the parent element.  


## How to use

This example shows how to use a Local Variable to keep the value of a Search widget. The value of the variable is then used to filter an aggregate.

1. Select the Input widget, and on the **Properties** tab, create a local variable by selecting the **Variable** dropdown and selecting **New Local Variable**.

    ![Adding a new Local Variable to an Input](<images/local-variable-ss.png>)

1. Enter a name for the variable, for example `SearchKeyword`.

    ![](<images/variable-searchkeyword-ss.png>)

1. Use the Local Variable to [filter the aggregate](../../../develop/data/query/filter-results.md).

    ![](<images/filtered-aggregate-ss.png>)


Find more about [Local Variables](https://www.outsystems.com/training/lesson/2069/variables?LearningPathId=18).  
To practice, check these exercises where you can see examples of Local Variables usage:
* [Using Local Variables for pagination and sorting](https://www.outsystems.com/training/lesson/2045/pagination-and-sorting-exercise?LearningPathId=18)
* [Data Queries and Widgets II Exercise](https://www.outsystems.com/training/lesson/1766/data-queries-and-widgets-ii-exercise?LearningPathId=2)
