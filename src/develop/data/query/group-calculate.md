---
summary: Use aggregate functions to calculate values based on groups of identical data.
tags: support-application_development; support-Database; support-webapps
locale: en-us
guid: d2578f60-c7a2-40fe-8e74-382aecad9b2f
---

# Calculate Values from Grouped Data

Putting data into groups to calculate aggregated values allows you to extract more information from your data sets. In OutSystems, you can use aggregate functions to calculate values based on groups of identical data.

[Fetch the data](<fetch-display.md>) in an aggregate and do the following:

1. In the attribute with identical data, use the ![Aggregate Menu](images/aggregate-menu.png) menu and select **Group by &lt;attribute&gt;**.
1. In the attribute to calculate, use the ![Aggregate Menu](images/aggregate-menu.png) menu and select an aggregate function such as **Count**.

Once you group or use aggregate functions on attributes, those attributes become the only output of the aggregate.

## Example

In the GoOutWeb application to find, review, and rate places, you want to show the average rating of places to help to take a decision. Consider that you already have an Aggregate fetching all the reviews of a place from the database. Open the aggregate and do the following:

1. On the `Place.Id` attribute, open the ![Aggregate Menu](images/aggregate-menu.png) menu and choose **Group By Id**.

    ![](images/group-calculate.png)

1. On the `Review.Rate` attribute, open the ![Aggregate Menu](images/aggregate-menu.png) menu and choose **Average**.

1. Use the calculated values to display the average rating for each place on the screen.
