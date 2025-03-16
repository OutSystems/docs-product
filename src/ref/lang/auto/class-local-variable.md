---
helpids: 1013
summary: Explore how to manage and utilize Local Variables within OutSystems 11 (O11) for scoped data handling in web development.
locale: en-us
guid: d36d267e-97d6-4a18-ad83-08f8bd1e76a3
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=1351:1635
tags: local variables, data handling, web development, application development, data filtering
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
topic:
  - local-variables
---

# Local Variable


A Local Variable exists only in the scope of its parent element, for example, a Screen, Action, Web Block, or Automatic Activity. A Local Variable can only be assigned and used locally inside that scope. Local variables are destroyed when execution leaves the scope of the parent element. The image below shows how to add a Local Variable inside a Screen.  

![Screenshot showing the process of adding a Local Variable inside a Screen in Service Studio](images/add-local-variable-inside-screen-ss.png "Adding a Local Variable in Service Studio")

## How to use

This example shows how to use a Local Variable to keep the value of a Search widget. The value of the Local Variable is then used to filter an Aggregate. 

1. Select the Input widget.

1. On the **Properties** tab, select the **Variable** dropdown and select **New Local Variable**.

    ![Screenshot of the Properties tab in Service Studio with the Variable dropdown expanded showing the New Local Variable option](images/local-variable-ss.png "New Local Variable Selection")

1. Enter a name for the variable, for example `SearchKeyword`. Make sure the **Data Type** is set to `Text`.

    ![Screenshot of a new Local Variable named SearchKeyword being created with the Data Type set to Text in Service Studio](images/variable-searchkeyword-ss.png "Defining a Local Variable as SearchKeyword")

1. Double-click the aggregate on the Elements tree.

1. On the **Filter** tab, click **Add filter**.

1. Insert the filter condition. 

    ```
    Employee.FirstName like "%" + SearchKeyword + "%"
    ```


1. To save the filter, click **Close**. 

    ![Screenshot of a filtered aggregate in Service Studio where the filter condition includes a Local Variable named SearchKeyword](images/filtered-aggregate-ss.png "Filtered Aggregate Using a Local Variable") 

After you follow these steps and publish your module, you can test the functionality of the filter in your browser. The text inserted in the Input of the Search widget is stored in the defined Local Variable and is then used to filter the aggregate. When you change to another screen or close your browser, the Local Variable is destroyed and the filter no longer applies.   

Learn more in this [lesson about Variables](https://learn.outsystems.com/training/journeys/web-developer-662/variables/o11/316).  

To practice, check these exercises where you can see examples of Local Variables usage:  

* In Reactive Web development: [Using Local Variables for pagination and sorting](https://learn.outsystems.com/training/journeys/web-developer-662/pagination-and-sorting-exercise/o11/559)  
* In Traditional Web development: [Using Local Variables for data queries and widgets](https://learn.outsystems.com/training/journeys/traditional-web-developer-655/data-queries-and-widgets-ii-exercise/o11/1126)  

## Properties

<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
<th>Mandatory</th>
<th>Default value</th>
<th>Observations</th>
</tr>
</thead>
<tbody>
<tr>
<td title="Name">Name</td>
<td>Identifies an element in the scope where it is defined, like a screen, action, or module.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Default Value">Default Value</td>
<td>Initial value of this element. If undefined, the default value of the data type is used.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Description">Description</td>
<td>Text that documents the element.</td>
<td></td>
<td></td>
<td>Useful for documentation purpose.<br/>The maximum size of this property is 2000 characters.</td>
</tr>
<tr>
<td title="Data Type">Data Type</td>
<td>The variable data type.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
