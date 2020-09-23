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

![Server-side aggregates](images/aggregate-server-side-ss.png?width=450)

## Notes on Max. Records and zero value

The **Max. Records** property in Aggregates controls the maximum number of records the Aggregate returns. **Max. Records** property works slightly different in **client actions** and **server actions** when you set the value to zero (**Max. Records = 0**).

* In the **server** actions, **Max. Records = 0** returns **all records** from database.
* In the **client** actions, **Max. Records = 0** returns **zero records** from database. Additionally, **Max. Records** is mandatory in Reactive Web and Mobile Apps in Screens/Blocks and client actions. This helps you control the amount of data the Aggregate returns and avoid performance issues.

Setting **Max. Records** to zero works like this in other elements that reuse Aggregates to get data, for example **Refresh Data**.

## Traditional Web Apps

In Traditional Web Apps, Aggregates run on the server, so you can only add [server-side Aggregates](#server-side-aggregates).

To load data when the screen loads in Traditional Web Apps, place an Aggregate in the **Preparation** action (right-click a screen add select **Add Preparation**.). **Preparation** exists in Traditional Web Apps only.

![Preparation in Traditional Web App](images/aggregate-preparation-ss.png?width=550)
