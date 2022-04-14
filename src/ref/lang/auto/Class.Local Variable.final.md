---
kinds: ServiceStudio.Model.Variables+LocalVariable+Kind
helpids: 1013
summary: A Local Variable exists only in the scope of its parent element.
locale: en-us
guid: d36d267e-97d6-4a18-ad83-08f8bd1e76a3
---

# Local Variable


A Local Variable exists only in the scope of its parent element, for example, a Screen or an Action. A Local Variable can only be assigned and used locally inside that scope. Local variables are destroyed when execution leaves the scope of the parent element. The image below shows how to add a Local Variable inside a Screen.  

![Adding a new Local Variable to a Screen](<images/add-local-variable-ss.png>)

## How to use

This example shows how to use a Local Variable to keep the value of a Search widget. The value of the Local Variable is then used to filter an Aggregate. 

1. Select the Input widget.

1. On the **Properties** tab, select the **Variable** dropdown and select **New Local Variable**.

    ![Adding a new Local Variable to an Input](<images/local-variable-ss.png>)

1. Enter a name for the variable, for example `SearchKeyword`. Make sure the **Data Type** is set to `Text`.

    ![Entering the name for the Local Variable](<images/variable-searchkeyword-ss.png>)

1. Double-click the aggregate on the Elements tree.

1. On the **Filter** tab, click **Add filter**.

1. Insert the filter condition. 

    ```
    Employee.FirstName like "%" + SearchKeyword + "%"
    ```


1. To save the filter, click **Close**. 

    ![Aggregate with a filter that uses the SearchKeyword Variable to filter the results](<images/filtered-aggregate-ss.png>) 

After you follow these steps and publish your module, you can test the functionality of the filter in your browser. The text inserted in the Input of the Search widget is stored in the defined Local Variable and is then used to filter the aggregate. When you change to another screen or close your browser, the Local Variable is destroyed and the filter no longer applies.   

Learn more in this [lesson about Variables](https://www.outsystems.com/training/lesson/2069/variables?LearningPathId=18).  

To practice, check these exercises where you can see examples of Local Variables usage:  

* In Reactive Web development: [Using Local Variables for pagination and sorting](https://www.outsystems.com/training/lesson/2045/pagination-and-sorting-exercise?LearningPathId=18)  
* In Traditional Web development: [Using Local Variables for data queries and widgets](https://www.outsystems.com/training/lesson/1766/data-queries-and-widgets-ii-exercise?LearningPathId=2)  

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

<script>
var meta = document.createElement('meta');
meta.name = "application_types";
meta.content = "traditional web apps, mobile apps, reactive web apps";
document.getElementsByTagName('head')[0].appendChild(meta);
</script>
