---
summary: Explore how to calculate values from grouped data using aggregate functions in OutSystems 11 (O11).
tags: support-application_development; support-Database; support-webapps
locale: en-us
guid: d2578f60-c7a2-40fe-8e74-382aecad9b2f
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=173:5
---

# Calculate Values from Grouped Data

Putting data into groups to calculate aggregated values allows you to extract more information from your data sets. In OutSystems, you can use aggregate functions to calculate values based on groups of identical data.

[Fetch the data](<fetch-display.md>) in an aggregate and do the following:

1. In the attribute with identical data, right-click, and select **Group by &lt;attribute name&gt;**.
1. In the attribute to calculate, right-click, and select an aggregate function such as **Count**.

Once you group or use aggregate functions on attributes, those attributes become the only output of the aggregate.

## Example

Consider that you already have an aggregate fetching all the data from the database. Open the aggregate and do the following:

In the Sorting Example application, we want to define how many employees are in each city. First, create a **Group by** city. Next, calculate the **count** of those employees by city. Assume that you already have an aggregate fetching all the employees from a sample database. 

Open the aggregate and do the following:

1. On the `City` attribute, right-click, and choose **Group By City**.
  
    ![Screenshot showing the selection of 'Group By City' option for the City attribute in an aggregate](images/group-attribute-ss.png "Group By City Attribute")

1. On the `Employee Id` attribute, right-click, and choose **count**.

    ![Screenshot demonstrating how to select the 'count' aggregate function for the Employee Id attribute](images/select-aggregate-function-ss.png "Select Aggregate Function")

1. Now you see how many employees are in each city.

    ![Example screenshot displaying the result of grouping employees by city and counting them in an aggregate](images/group-calculate-ex2-ss.png "Grouped Data Calculation Example")
