---
summary: Use aggregate functions to calculate values based on groups of identical data.
tags: support-application_development; support-Database; support-webapps
locale: en-us
guid: d2578f60-c7a2-40fe-8e74-382aecad9b2f
app_type: traditional web apps, mobile apps, reactive web apps
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
  
    ![Group by city](images/group-calculate-ex-ss.png)

1. On the `Employee Id` attribute, right-click, and choose **count**.

    ![Count employees](images/group-calculate-ex1-ss.png)

1. Now you see how many employees are in each city.

    ![Employees per city](images/group-calculate-ex2-ss.png)
