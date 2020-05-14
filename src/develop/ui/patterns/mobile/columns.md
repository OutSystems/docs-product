---
tags: runtime-mobileandreactiveweb;  
summary: 
---

# Columns Pattern

You can use the Columns UI Pattern to split content into separate columns, improving the way information is displayed on-screen. <!--You can configure the behavior using the properties. They will define how columns will stack in different devices. This is ideal to improve the way information is displayed across  different devices. You can use this pattern to display a list of elements side by side, with a different number of items per row on different devices. -->

The following is a preview of the different ways content can be split into columns:

![](images/Column_columns.png)

## How to use the Columns UI Pattern




## Properties

**Property** |  **Description** |  
---|---
GutterSize (GutterSizeIdentifier): Optional  | Defines the space between columns.  
TabletBehavior (BreakColumns Identifier): Optional  |  Behavior of the columns in a Phone with Portrait orientation.  |  BreakNone  
PhoneBehavior (BreakColumns Identifier): Optional |  Behavior of the columns in a Phone with Landscape orientation.  |  BreakNone  
ExtendedClass  |  Behavior of the columns in a Tablet with Portrait orientation.  |  BreakNone  

**Entities.ColumnBreak.BreakNone (default)**

![](images/Column_break_none.png)  

**Entities.ColumnBreak.BreakMiddle**

![](images/Column_break_middle.png)

**Entities.ColumnBreak.BreakLast**

![](images/Column_break_last.png)

**Entities.ColumnBreak.BreakFirst**

![](images/Column_break_first.png)

## Samples

See how the [Account Dashboard sample](https://silkui.outsystems.com/Samples_Mobile.aspx#Mobile_Details-Samples_AccountDashboard) uses the Columns UI Pattern.

![](images/Sample_Account_Dashboard.png)
