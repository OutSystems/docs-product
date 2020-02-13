---
tags: runtime-mobileandreactiveweb;  
summary: 
---

# Columns Pattern

The Columns pattern 
enables you to split content into multiple columns. You can configure the
behavior using the input parameters. They will define how columns will stack
in different devices. This is ideal to improve the way information is
displayed across different devices. You can use this pattern to display a list
of elements side by side, with a different number of items per row on
different devices.

Here's the preview , in Service Studio, of the different ways columns can be split into:

![](images/Column_Gutter.png)

![](images/Column_columns.png)

## How to Use the Columns Pattern

Configure the behavior using the input parameters to define how columns will
stack in different devices.

For an uneven number of columns, the following splits apply:

**Entities.ColumnBreak.BreakNone (default)**

![](images/Column_break_none.png)  

**Entities.ColumnBreak.BreakMiddle**

![](images/Column_break_middle.png)

**Entities.ColumnBreak.BreakLast**

![](images/Column_break_last.png)

**Entities.ColumnBreak.BreakFirst**

![](images/Column_break_first.png)

## Input Parameters

**Input Name** |  **Description** |  **Default Value**  
---|---|---  
![](images/input.png) UseGutter  |  Creates a space between columns.  | True  
![](images/input.png) PhonePortraitBreak  |  Behavior of the columns in a Phone with Portrait orientation.  |  BreakNone  
![](images/input.png) PhoneLandscapeBreak  |  Behavior of the columns in a Phone with Landscape orientation.  |  BreakNone  
![](images/input.png) TabletPortraitBreak  |  Behavior of the columns in a Tablet with Portrait orientation.  |  BreakNone  
![](images/input.png) TabletLandscapeBreak  |  Behavior of the columns in a Tablet with Landscape orientation.  |  BreakNone  
  
## Layout and Classes

![](images/Column_layout.png)

## Samples

See how the [Account Dashboard sample](https://silkui.outsystems.com/Samples_Mobile.aspx#Mobile_Details-Samples_AccountDashboard) uses the Columns pattern:

![](images/Sample_Account_Dashboard.png)
