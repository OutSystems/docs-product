---
kinds: ServiceStudio.Model.Variables+AdvancedQueryParameter+Kind
helpids: 0
locale: en-us
guid: 5bbf3ba9-4d58-4cb3-9a6e-3634d2e01c31
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=1469:2187
summary: The article explains how to define and use query parameters in SQL queries within a Service Studio environment, using an Employee data model example
---
# Query Parameter

The SQL tool doesn't have direct access to variables or parameters defined outside its scope. To use input parameters or local variables in a SQL query, you need to define query parameters. Then, you need to map the input parameters or local variables to the query parameters. 

## How to use

In this example, there is a data model with an Entity named Employee. A screen fetches data using a SQL query that uses a search input as query parameter. Follow these steps:

1. From the toolbox, drag a **SQL** and drop it in the action flow between the **Start** and **End** nodes.

    ![Screenshot showing how to add a SQL element to the action flow in Service Studio](images/add-sql-ss.png "Adding SQL to Action Flow")

1. Double-click the newly created **SQL** to open the SQL Editor.

1. Right-click the **Parameters** folder, and select **Add Query Parameter**.

    ![Screenshot illustrating the addition of a query parameter in Service Studio](images/add-queryparameter-ss.png "Adding Query Parameter")

1. Set the **Name** of the Query Parameter to `QuerySearch`, and make sure its **Data Type** is set to `Text`.

    ![Screenshot depicting the process of naming a query parameter as 'QuerySearch' in Service Studio](images/name-queryparameter-ss.png "Naming Query Parameter")

1. In the **SQL** tab, enter the following query:

        SELECT
        {Employee}.[FirstName] + ' ' + {Employee}.[LastName],
        {Employee}.[Email],
        {Employee}.[Phone],
        {Employee}.[Salary]
        FROM
        {Employee}
        WHERE
        {Employee}.[FirstName] LIKE '%' + @QuerySearch + '%'
        OR
        {Employee}.[LastName] LIKE '%' + @QuerySearch + '%'

1. Double-click **Output Entities/Structures** to select the output structure of
the query. In this example, there is already a structure named EmployeeStructure with the attributes Name, Email, Phone and Salary. Select it, and click **Select**.

    ![Screenshot showing the selection of the output structure named EmployeeStructure in Service Studio](images/output-structure-ss.png "Selecting Output Structure")

1. Click **Test** to test the query.

1. In the **Test Inputs** tab, set a value for the QuerySearch parameter, then click **Test** again to make sure the filter is working.

1. Click **Close** to return to the flow. 

1. Select the **SQL** node in the action flow, and in the properties, set the **QuerySearch** to the search input variable. In this example, there is a local variable named SearchFilter, which keeps the value entered by the user in a Search widget.

    ![Screenshot demonstrating how to set the value of the 'QuerySearch' parameter to a local variable in Service Studio](images/set-parameter-value-ss.png "Setting Parameter Value")

1. Publish the Module using the 1-Click Publish button, then test it in the browser.

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
<td title="Description">Description</td>
<td>Text that documents the element.</td>
<td></td>
<td></td>
<td>Useful for documentation purpose.<br/>The maximum size of this property is 2000 characters.</td>
</tr>
<tr>
<td title="Data Type">Data Type</td>
<td>The parameter data type.</td>
<td>Yes</td>
<td>Text</td>
<td>The parameter data type must be a basic data type or an Entity Identifier.</td>
</tr>
<tr>
<td title="Expand Inline">Expand Inline</td>
<td>Set to Yes to use the query parameter to implement part or all of the SQL query at runtime.</td>
<td>Yes</td>
<td>No</td>
<td></td>
</tr>
</tbody>
</table>

