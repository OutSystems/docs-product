Fetch data using an optimized query. Aggregates can load data from the server of the local database, and they support combining several Entities and advanced filtering.

Use an Aggregate to get data from a database in OutSystems. Follow the steps: 

1. Right-click a Screen or a Block and select **Fetch data from Database**. An empty Aggregate opens, and Service Studio shows that you need to add an Entity.

   ![Crate new Aggregate](images/aggregate-create-ss.png?width=350)

1. With the Aggregate still open, navigate to **Data** > **Entities** > **Database**.

1. Drag one of the Entities to the Aggregate window. Service Studio populates the Aggregate with columns that correspond to the attributes of the Entity. Note also the name change; if your Entity is **MyEntity**, the Aggregate gets the name **GetMyEntity**.

    ![Columns from database in Aggregate](images/database-columns-aggregate-ss.png?width=800)

1. Go back to your Screen or Block and set an element to use the data. For example, if you have a **List** widget, set the **Source** of the List widget to **GetMyEntity.List**. You can always double-click an Aggregate to add more Entities, join data, or create filters.

## Notes on Max. Records and zero value

The **Max. Records** property in Aggregates controls the maximum number of records the Aggregate returns. **Max. Records** property works slightly different in **client actions** and **server actions** when you set the value to zero (**Max. Records = 0**).

* In the **server** actions, **Max. Records = 0** returns **all records** from database.
* On the **client** actions, **Max. Records = 0** returns **zero records** from database. Additionally, **Max. Records** is mandatory in Reactive Web and Mobile Apps in Screens/Blocks and client actions. This helps you control the amount of data the Aggregate returns and avoid performance issues.

Setting **Max. Records** to zero works like this in other elements that reuse Aggregates to get data, for example **Refresh Data**.