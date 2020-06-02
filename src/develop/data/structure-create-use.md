---
summary: Learn how to create and use complex data types in your applications.
tags: support-Mobile_Apps; support-webapps
---

# Use Structures and Records to Create Compound Data Types

While developing your application, you may find interesting to have a variable holding a collection of variables with different data types grouped together and use it in the logic or UI. For example, to assign the values returned by an action where you don't have to create one output for each value.

In OutSystems, you can create structured values by using a ![Structure.png](../../shared/icons-service-studio/structure.png) Structure or a Record. A Structure is a custom data type that you can use in your module. A Record is a custom data type data type defined for a single variable and cannot be reused in another variable.

To declare and use a Structure:

1. On the Data layer, right-click the folder Structures and select **Add Structure** to add a new Structure.
1. To add an attribute, right-click the new Structure, select **Add Structure Attribute**, and change the properties of the attribute such as the name and the data type.
1. Create a new variable.
1. Set the variable's data type to the Structure you've created.

To define a Record:

1. Create a new variable.
1. Change the data type of the variable to Record.
1. On the pop-up window, add attributes to the record and define the data types of the attributes.

## Example using a Record

In the application GoOutWeb, a Web app to find and review places of interest, we want to return basic information about a Place using a REST API method. The information to return about each place is the Id, the name, and the average rating.

Since the data type that we will need to assign to the output parameter will only be used here, we will use a Record:

1. Expose a REST API, name it Place and create the method GetPlace.
1. Add an input parameter with the Place Id for which to return information.
1. In the action flow, add an aggregate with the Place and Review entities and filter using the Place Id input parameter.
1. Add an output parameter called PlaceInformation.
1. Select the suggested data type `GetPlacesWithReviews Record Type` to set the data type of the output parameter to the records returned by the aggregate.
1. Back to the GetPlace action flow, to assign the values to the output variable, add an Assign flow element to the action and assign the first element returned from the aggregate to it. Since they are the of the same data type, there is no need to map the attributes between the two.
1. Publish and test.

## Example using a Structure

In the application GoOutWeb, a Web application to find and review places of interest, we are developing a REST API method to expose basic information about a registered end user of the application. The  information we are returning is the Id, the name, and the profile picture of an end user.

Since we are going to reuse the user information in another action of the application, we will create a Structure to hold this information thus allowing us to reuse the data type:

1. On the Data layer, right-click the folder Structures and add a new structure named `UserInfo`.

1. Add the following attributes to the new structure:

    * `Id` of type User Identifier
    * `Name` of type Text
    * `Photo` of type Binary Data

    ![Create and Use Structured Data](images/structure-create-use-1.png)

1. Expose a REST API named User and create the method GetUser.

1. Add an input parameter with the User Id for which to return information. 

1. In the action flow, add an aggregate with the User and Profile entities and filter using the User Id input parameter.

1. Add an output parameter called UserInformation and assign the UserInfo structure as its the data type.

1. To assign the values to the output variable, add an Assign element to the action and assign the first element returned from the aggregate.

1. Since the data type returned by the aggregate is different from the output variable, below the assignment in the properties of the Assign node, map the attributes from the aggregate output to the output parameter attributes.

1. Publish and test.

![Create and Use Structured Data](images/structure-create-use-2.png)
