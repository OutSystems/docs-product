---
kinds: ServiceStudio.Model.Nodes+DataSet+Kind, ServiceStudio.Model.NRNodes+WebScreenDataSet+Kind
helpids: 17203
---

# Aggregate

Fetch data using an optimized query. Aggregates can load data from the server of the local database, and they support combining several Entities and advanced filtering.

<div class="info" markdown="1">

We've been working on this article. Please let us know how useful this new version is by voting.

</div>

## Client-side Aggregates

Client-side Aggregates run in the client logic. Use them to get data for your widgets when a Screen or a Block loads. Follow the steps: 

1. Right-click a Screen or a Block and select **Fetch data from Database**. An empty Aggregate opens, and Service Studio shows that you need to add an Entity.

    ![Crate new Aggregate](images/aggregate-create-ss.png?width=350)

1. With the Aggregate still open, navigate to **Data** > **Entities** > **Database**.

1. Drag one of the Entities to the Aggregate window. Service Studio populates the Aggregate with columns that correspond to the attributes of the Entity. Note also the name change; if your Entity is **MyEntity**, the Aggregate gets the name **GetMyEntity**.

    ![Columns from database in Aggregate](images/database-columns-aggregate-ss.png?width=800)

1. Go back to your Screen or Block and set an element to use the data. For example, if you have a **List** widget, set the **Source** of the List widget to **GetMyEntity.List**. You can always double-click an Aggregate to add more Entities, join data, or create filters.

## Server-side Aggregates

Aggregates that run in the **server-side logic** are in the logic flows. To add an Aggregate in the server logic, drag an Aggregate from the toolbox to the flow of an action. 

![Server-side aggregates](images/aggregate-server-side-ss.png?width=350)

## Fetching all records in client-side logic

There are cases when you always need to fetch all records from the database, for example to populate drop-down box lists. There are two ways of doing it:

* Use a Screen Aggregate and set **Max. Records** higher than the maximum number of records you expect. Keep in mind that large amounts of data may slow down the user interface and degrade the responsiveness of the app.
* Use a Data Action instead of Screen Aggregate and leave **Max. Records** field empty. In Data Actions, the **Max. Records** value is optional, and if you provide no value the Data Action fetches all records from the database.   

## Traditional Web Apps

In Traditional Web Apps, Aggregates run on the server, so you can only add [server-side Aggregates](#server-side-aggregates).

To load data when the screen loads in Traditional Web Apps, place an Aggregate in the **Preparation** action (right-click a screen add select **Add Preparation**.). **Preparation** exists in Traditional Web Apps only.

![Preparation in Traditional Web App](images/aggregate-preparation-ss.png?width=550)

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
<td title="Timeout">Timeout</td>
<td>Maximum time in seconds to wait for the Aggregate to return data before triggering a Communication Exception. Overrides the default timeout defined on the module.</td>
<td></td>
<td></td>
<td>If there is no value specified in this property, the timeout corresponds to the "Default query timeout" parameter specified in the Platform Server Configuration Tool.<br/>Property not available in client actions.</td>
</tr>
<tr>
<td title="Cache in Minutes">Cache in Minutes</td>
<td>Maximum time content or results are stored in memory. When undefined, nothing is cached.</td>
<td></td>
<td></td>
<td>Property not available in client actions.</td>
</tr>
<tr>
<td title="Max. Records">Max. Records</td>
<td>Maximum number of records read from the database.</td>
<td></td>
<td></td>
<td>In Traditional Web App only. If undefined, the default value is:<br/>
        – In widgets: StartIndex + LineCount + 1;<br/>
        – Exporting to Excel: No limit.</td>
</tr>
<tr>
<td title="Start Index">Start Index</td>
<td>Index of the first List item to iterate. Can be an expression.</td>
<td></td>
<td></td>
<td>The expression used in this property (if present) is evaluated before the web screen preparation.</td>
</tr>
<tr>
<td title="Fetch">Fetch</td>
<td></td>
<td>Yes</td>
<td>At start</td>
<td></td>
</tr>
<tr class="separator">
<th colspan="5">Events</th>
</tr>
<tr>
<td title="On After Fetch">On After Fetch</td>
<td>Action executed after the aggregate fetches data from the data source.</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

## Runtime Properties

<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
<th>Read Only</th>
<th>Type</th>
<th>Observations</th>
</tr>
</thead>
<tbody>
<tr>
<td>List</td>
<td>Collection of records returned by the performed query.</td>
<td></td>
<td>Record List</td>
<td></td>
</tr>
<tr>
<td>Count</td>
<td>Number of records returned by the Count query.</td>
<td></td>
<td>Long Integer</td>
<td></td>
</tr>
<tr>
<td>IsDataFetched</td>
<td>True when data has been fetched from the database and is ready to be used.</td>
<td>Yes</td>
<td>Boolean</td>
<td></td>
</tr>
<tr>
<td>HasFetchError</td>
<td>True when there is an error during data fetch due to a server error or communication timeout.</td>
<td>Yes</td>
<td>Boolean</td>
<td></td>
</tr>
</tbody>
</table>

