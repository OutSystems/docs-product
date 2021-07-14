---
summary: Use aggregate functions to calculate values based on groups of identical data.
tags: support-application_development; support-Database; support-webapps
---

# Calculate Values from Grouped Data

Putting data into groups to calculate aggregated values allows you to extract more information from your data sets. In OutSystems, you can use aggregate functions to calculate values based on groups of identical data.

[Fetch the data](<fetch-display.md>) in an aggregate and do the following:

1. In the attribute with identical data, right-click, and select **Group by &lt;attribute name&gt;**.
1. In the attribute to calculate, right-click, and select an aggregate function such as **Count**.

Once you group or use aggregate functions on attributes, those attributes become the only output of the aggregate.

## Example

In the GoOutWeb application to find, review, and rate places, you want to show the average rating of places to help you make a decision. Consider that you already have an aggregate fetching all the reviews of a place from the database. Open the aggregate and do the following:
<!-- // I am here -->
In the Sorting Example application, we want to define how many employees are in each city. First, create a **Group by** city and then calculate the **count** of those employees by city. Assume that you already have an aggregate fetching all the employees from a sample database. Open the aggregate and do the following:


1. On the `City` attribute, right-click, and choose **Group By City**.

1. On the `Employee Id` attribute, right-click, and choose **count**.

1. Now you see how many employees are in each city.


![Group by city](images/group-calculate-ex-ss.png)

![Count employees](images/group-calculate-ex1-ss.png)

![Employees per city](images/group-calculate-ex2-ss.png)

