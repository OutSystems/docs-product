---
tags: 
summary: Learn how to enable and configure data editing in OutSystems 11 (O11) Data Grid by setting the AllowColumnEdit property to true and adding column widgets.
guid: 2f8a50d1-be34-401b-bd4a-c27ba72b37f7
locale: en-us
app_type: reactive web apps
platform-version: o11
figma: https://www.figma.com/file/ZqxffTIAhYyQg8Q2KbSFbb/Development?type=design&node-id=1168%3A0&mode=design&t=bneC7SMvNg6A2EZ4-1
---

# How to edit data in the OutSystems Data Grid

This example shows how to edit data in the Grid using columns.

**Prerequisites:** 

* Complete [How to use the OutSystems Data Grid component](how-to-view-data.md).

1. Select the **Grid** component, and on the **Properties** tab, expand **Optional Configs** and set the **AllowColumnEdit** property to **True**. 

    This allows the Grid values to be edited. 

   ![Screenshot showing the AllowColumnEdit property set to True in the Data Grid's properties panel.](images/grid-edit-true-ss.png "Enabling Column Edit in Data Grid")

1. In the Toolbox, search for Column.

    The Grid Column widgets are displayed.

   ![Screenshot displaying various Grid Column widgets such as Text Column, Number Column, and Checkbox Column.](images/grid-edit-columns-ss.png "Grid Column Widgets")

1. Drag the relevant Column type to the **GridColumnsPlaceholder**. 

    In this example, the **Text Column** is used.

   ![Screenshot of the Text Column properties tab with Header and Binding fields set to 'Name' and 'Sample_Product.Name' respectively.](images/grid-edit-textcolumn-ss.png "Configuring Text Column Properties")

1. On the Text Column **Properties** tab, enter the **Header** and **Binding** information.

    The **Header** property displays in the column’s header. In this example, **"Name"** is entered. 
 
    The **Binding** property displays the name of the entity and the attribute in the column. In this example, the entity is called Sample_Product and the Attribute is Name, so the Binding property is **"Sample_Product.Name"**.

    ![Screenshot of the Text Column properties tab with Header and Binding fields set to 'Name' and 'Sample_Product.Name' respectively.](images/grid-edit-textcolumn-ss.png "Configuring Text Column Properties")

1. Repeat steps 3 and 4 for the Column widgets you want to display on your Grid. 

    This examples uses the following:

    | **Widget** | **Property** |
    |---|---|
    |**Number Column** | Header: "Stock" <br/> Binding: "Sample_Product.Stock"|
    | **Currency Column**| Header: "Price"<br/> Binding: "Sample_Product.Price" | 
    |**Checkbox Column** | Header: "Is Favorite"<br/>Binding: "Sample_Product.IsFavourite" |  

    ![Screenshot showing the Data Grid with added columns for Name, Stock, Price, and Is Favorite with their respective bindings.](images/grid-edit-addcol-ss.png "Adding Columns to Data Grid")

After following these steps and publishing the module, you can test the component in your app. Double-click a cell to edit it's content.

**Result**

![Screenshot of the Data Grid with editable cells displaying product information such as Name, Stock, Price, and Is Favorite.](images/grid-edit-result-ss.png "Edited Data Grid Result")

**Note:** When you edit a cell, that cell and the corresponding line is marked with a black triangle to indicate a change in data. 
