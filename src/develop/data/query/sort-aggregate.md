---
summary: Use fixed and dynamic sorting in Aggregates to display records on your application screens following a customized sorting the records they return.
tags: support-application_development; support-webapps
---

# Sort Results in an Aggregate

Most times, records display on screens following some order to facilitate reading or to help find information faster.

In OutSystems, aggregates let you choose how the records sort when they return. The sorting can be fixed or dynamic, meaning that it can change during runtime.

To display results in an aggregate with **fixed sorting**, follow these steps:

1. In the aggregate, select the column on which you want to sort and right-click the mouse.
1. Select **A-Z** to sort the results in ascending order or **Z-A** to sort the results in descending order.

To sort results in an aggregate with **dynamic sorting**, follow these steps:

1. In the aggregate,from the Sorting panel,  click **Add Dynamic Sort**. The expected input is an expression of type Text. This value can be the result of a condition or other logic implemented in the expression itself.
1. To refer to columns, select a variable of type Text previously defined from the Scope tree.

While defining expressions as values for your variable, you can specify:

* **Calculated or grouped attributes**, using the pattern `AttributeName` for ascending order or `AttributeName DESC` for descending order.
* **Entity attributes**, using the pattern `Entity.Attribute` or `Entity.Attribute DESC` for ascending or descending order.

## Example

In the Sorting Example, a reactive application displays  a list of employees, with details about each employee. We want to users to be able sort by the name of the employee in either ascending or descending order.

1. Open  Service Studio, create a new reactive application named Sorting Example.
1. Create a module with the default name.
1. Create an empty screen and name it.
1. Go to Manage Dependencies and search for sample_employees entity.
1. Fetch this entity to be used on the previous screen you created.
1. Drag and drop a list widget into the screen and define sample_employees as the source list of it.
1. Drag and drop the first name, last name and email attributes into the list.

1. Create a local variable named **SortAttribute** as text data type.
1. Double click on **aggregate GetEmployees**,
1. Go to the Sort tab and click **dynamic sort**, then define the local variable as the value for the dynamic sort.

1. From the toolbox, drag a **Button Group widget** to the top of the employees list and bind the **variable SortAttribute** with the Button Group.
1. Remove one of the Button Group Items and rename the remaining Button Group Items to **Sort ASC** and **Sort DESC**.

1. Select the **Sort ASC Button Group** Item and set the Value property to the expression "Sample_Employee.FirstName". This sorts the results of the aggregate by ascending order of the attribute FirstName.

1. Repeat the operation on **Sort DESC Button Group**, changing the expression to "Sample_Employee.FirstName DESC".

1. On the ButtonGroup, define an event **On Change** as a new client action.
1. Inside the new client action, drag refresh data and select the data source as **GetEmployees**.
1. Publish and test. Verify the list sorting changes after clicking the **Sort ASC** or **Sort DESC** buttons.  

