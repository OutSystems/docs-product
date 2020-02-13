---
summary: How to create a new attribute to a data query and base its value on the other record's attributes.
tags: support-application_development; support-Database; support-webapps
---

# Create a Calculated Attribute in an Aggregate

There are situations when the data fetched from the database isn't enough and you need to add more information to each record, namely based on the values returned. OutSystems allows you to do it. You can add new attributes to the records returned by the aggregate based on the value of the other attributes:

1. In the aggregate, click on New Attribute to add a new attribute to the aggregate and name it.
1. Open the attribute menu and select Edit formula....
1. Define the expression to calculate the value.


## Example

In the GoOutWeb, a web application to check interesting places, we have a screen to list places. In this screen, we want to allow the end-user to filter the listed places by category selecting an available category from a Combo Box. Additionally, in each entry of the Combo Box we want to display the number of places that have that specific category along to the category name.

![Create a Calculated Attribute in an Aggregate](images/calculated-attribute-create-1.png)

To calculate this data and add it to each entry of the Combo Box:

1. Since this is a web application, add an aggregate to the screen's preparation.

1. Add the Place entity to it.

1. In the aggregate, do the following:

    1. Group by Category.Id.

    1. Count by Place.Id to have the number of places per each category.

    1. Group by Category.Label to get the label of each category.

    1. Open the last grouped column menu and add a new attribute. Name it "Combo Box Label".

    1. Assign the following expression to the created column:
    
        `If ( Label <> "", Label + " (" + Count + ")" , "Not categorized" + " (" + Count + ")" )` 
        
        Label and Count variables are two of the previously grouped columns.

    ![Create a Calculated Attribute in an Aggregate](images/calculated-attribute-create-2.png)

1. Go to the screen and add a Combo Box. Set its values to be the returning list of the new aggregate.
