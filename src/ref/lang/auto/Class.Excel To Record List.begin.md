Use Excel To Record List to convert an Excel object to a Record List. Use this logic tool when you need to import Excel files at runtime.

<div class="info" markdown="1">

If you need to import data from an Excel file at design time, when developing your application, consider the following alternatives:

* If **you don't have OutSystems Entities for your Excel data** yet — in Service Studio, open the **Data** tab,  right-click on the **Database** node in the tree, and select **Import Entities from Excel...**. This creates a new Entity per Excel sheet and uses the data on the Excel file to bootstrap those entities with data. For more information, check [Create an Entity to Persist Data](../../../develop/data/modeling/entity-create.md).

* If you already have the entities and just want to **bootstrap data** — in Service Studio, open the **Data** tab, right-click on the Entity for which you want to import data, and select Advanced > **Create Action to Bootstrap Data from Excel...**. This creates an Action and an associated Timer to bootstrap entities with data from the Excel file. For more information check [Bootstrap an Entity Using an Excel File](../../../develop/data/excel-bootstrap.md).

</div>
