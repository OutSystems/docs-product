---
summary: Explore how to use structures and records for compound data types in OutSystems 11 (O11) for efficient app development.
tags: data structures, variables, app development best practices, compound data types, data modeling
locale: en-us
guid: eb3ff661-0b92-4f55-9bf3-cceb8dd2c0b9
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=174:18
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
topic:
  - compound-data
  - how-to-create-structures
---

# Use structures and records to create compound data types

During app development, consider using a variable to hold a collection of variables with various data types, grouped for logic efficiency. This approach is useful, for instance, when you assign values returned by an action without needing separate outputs for each value.

In OutSystems, you can create structured values using structures or records. A structure is a reusable custom data type within your module, while a record is specific to a single variable that you can't use elsewhere.

To declare and use a structure:

1. On the Data layer, right-click the folder Structures and select **Add Structure** to add a new structure.
1. To add an attribute, right-click the new structure, select **Add Structure Attribute**, and change the properties of the attribute such as the name and the data type.
1. Create a new variable.
1. Set the variable's data type to the structure you've created.

In the cross-platform Service Studio, to create a record for a variable, you need to:

1. Create a new variable in the element where the record is to be used.
1. Select the variable and change its **Data Type** to **Record...**. A Text attribute is added to the variable.
1. Optionally, change the **Data Type** and the **Name** of the attribute.
1. In the variable context menu you can add more attributes to the Record.

    <iframe src="https://player.vimeo.com/video/973090356" width="750" height="375" frameborder="0" allow="autoplay; fullscreen" allowfullscreen="">Video showing the process of creating a record for a variable in Service Studio.</iframe>

In the Windows-only Service Studio, to create a record for a variable, you need to:

1. Create a new variable in the element where the Record is to be used.
1. Select the variable and change its **Data Type** to **Record...**.
1. On the pop-up window, add attributes to the record and define the data types of the attributes.

## Example using a record

For an app focused on discovering and evaluating places of interest, used for mapping and navigating, you can utilize a REST API method to retrieve fundamental details about each place. This includes the place's Id, name, and average rating, which are stored in the Place and Review entities.

Since the data type that we will need to assign to the output parameter will only be used here, we will use a record:

1. Expose a REST API, name it Place and create the method GetPlace.
1. Add an input parameter to the GetPlace method named  `PlaceId`. Ensure the **Data Type** is **Place Identifier**.

    ![Screenshot of the Place REST API with an input parameter named PlaceId in Service Studio](images/structure-create-use-3-ss.png "Place REST API with Input Parameter")

1. To define the logic of the GetPlace method, in the element tree, double-click **GetPlace**.
1. Drag an aggregate from the toolbox into the action flow.
1. Add the Place and Review entities to the aggregate.
1. Filter the aggregate ensuring the Place.Id attribute matches the PlaceId parameter. Add a filter condition with `Place.Id = PlaceId`.

    ![Screenshot showing the logic of the GetPlace method with an aggregate filter condition in Service Studio](images/structure-create-use-4-ss.png "Logic of the GetPlace Method")

1. In the GetPlace method, add an output parameter called `PlaceInformation`.
1. Set the PlaceInformation **Data Type** to **Record...**. A Text attribute is added to the variable.
1. Change the **Data Type** of the Text attribute to the **Place** entity and its **Name** to `Place`.
1. Add a new attribute from the **PlaceInformation** context menu.
1. Change the **Data Type** of the attribute to the **Review** entity and its **Name** to `Review`.

    ![Screenshot of the output parameter configuration using a record in the GetPlace method in Service Studio](images/structure-create-use-5-ss.png "Output Parameter with a Record")

    <div class="info" markdown="1">

    You can also use the suggested Data Type **GetPlaceById Record Type** to set the PlaceInformation data type as a compound data as covered by steps 6 to 9.

    </div>

1. In the GetPlace method flow, assign the result of the aggregate to the output parameter.
    1. From the toolbox, drag an Assign after the aggregate.
    1. Add an assignment by setting the **Variable** to `PlaceInformation` and the **Value** to `GetPlaceById.List.Current`.

    ![Screenshot showing how to assign values to the output parameter PlaceInformation in the GetPlace method in Service Studio](images/structure-create-use-6-ss.png "Assign Values to the Output Parameter")

## Example using a structure

In an app for discovering and reviewing places of interest, you can create a REST API method to provide basic details about a registered end user. This includes their Id, name, and profile picture.

To reuse user information in another action, create a structure to hold this data, enabling data type reuse.

1. On the Data layer, right-click the folder Structures and add a new structure named `UserInfo`.

1. Add the following attributes to the new structure:

    * `Id` of type User Identifier
    * `Name` of type Text
    * `Photo` of type Binary Data

    ![Screenshot of creating and using structured data with a new structure named UserInfo in Service Studio](images/structure-create-use-1-ss.png "Creating and Using Structured Data")

1. Expose a REST API named User and create the method GetUser.

1. Add an input parameter with the User Id for which to return information.

1. In the action flow, add an aggregate with the User and Profile entities and filter using the User Id input parameter.

1. Add an output parameter called UserInformation and assign the UserInfo structure as its the data type.

1. To assign the values to the output variable, add an Assign element to the action and assign the first element returned from the aggregate.

1. Since the data type returned by the aggregate is different from the output variable, below the assignment in the properties of the Assign node, map the attributes from the aggregate output to the output parameter attributes.

![Screenshot showing the mapping of aggregate output to the attributes of the output parameter UserInformation in Service Studio](images/structure-create-use-2-ss.png "Mapping Aggregate Output to Output Parameter Attributes")
