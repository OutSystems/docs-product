---
summary: Learn how to use the Table Records widget to display the records of an entity or a structure in a tabular layout. Reference.
tags: runtime-traditionalweb
---

You can use the Table Records widget to display the records of an entity or a structure in a tabular layout. You can define the table records as sortable making it easier for the user to read or find information faster. Record sorting can be fixed or dynamic, meaning that it can change during runtime. You can change the emphasis of a table row by changing its height and increase users' ability to read and interpret data in a table record by using zebra stripping. You can also use pagination to divide content and present it in a limited and digestible manner.

![Overview of Table Records widget in use](<images/tablerecords-1-ss.png>)

## How to use the Table Records widget

In this example, user data is fetched from the User entity and displayed on screen using the Table Records widget.

1. In Service Studio, in the Toolbox, search for `Table Records`.

    The Table Records widget is displayed.

    ![Table Records widget](<images/tablerecords-2-ss.png>)

1. From the Toolbox, drag the Table Records widget into the Main Content area of your application's screen.

    ![Drag Table Records widget onto screen](<images/tablerecords-3-ss.png>)

1. Add the relevant content to the Table Records widget. 

    In this example, from the **Data** tab, we drag the **User** entity into the Table Records widget. 

    ![Drag User database into widget](<images/tablerecords-4-ss.png>)

1. Return to your screen by selecting the **Interface** tab. Right-click the screen name and select **Add Preparation**.

    ![Add preparation](<images/tablerecords-5-ss.png>)

1. Add an Aggregate to the Preparation.

    ![Add an aggregate](<images/tablerecords-7-ss.png>)

1. Double-click the Aggregate, click the screen, and from the **Select Source** popup, select the database entity you want to retrieve data from. Click **OK**. In this example, we select the User entity.

    ![Select source entity](<images/tablerecords-6-ss.png>)

    The **GetUsers** aggregate is created.

    ![GetUsers aggregate is created](<images/tablerecords-8-ss.png>)

1. Return to your main screen, select the Table Records widget, and on the **Properties** tab, select the Source Record List (in this example, the GetUsers aggregate we just created).

    ![Select Source Record List](<images/tablerecords-9-ss.png>)

After following these steps and publishing the module, you can test the widget in your app.

### How to add a new column

1. Select and right-click the Table Records widget, and select **Table** > **Insert Column to the Left** or **Insert column to the Right**.


    ![Add new column](<images/tablerecords-10-ss.png>)

For more information about the Table Records widget properties, see [Table Records Widget](<../../../ref/lang/auto/Class.Table Records Widget.final.md>).