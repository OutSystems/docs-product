---
summary: Implement permission-based data access in OutSystems 11 (O11) using Access Control Lists (ACL) for dynamic and scalable data segregation.
tags: data segregation, security model, access control, role-based access control, data access control
guid: 3114f98f-16d0-4106-8628-5b0e80c6d21c
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/design/iBD5yo23NiW53L1zdPqGGM/Developing-an-Application?node-id=5721-6
audience:
  - backend developers
  - full stack developers
  - architects
outsystems-tools:
  - service studio
coverage-type:
  - evaluate
  - understand
topic:
  - acls
---

# Use Access Control List to set up permission-based access to data

## What is Access Control List?

An access control list (ACL) is a list of permissions attached to an object. The ACL stores what objects are granted to which users or group of users. Common uses of ACL are access to financial data to specific user profiles, data access based on user’s unit/branch or hierarchical accesses.

In OutSystems, the recommendation is to use [OutSystems user roles](https://success.outsystems.com/Documentation/11/Developing_an_Application/Secure_the_Application/User_Roles) to restrict or allow end users to access specific screens and operations of your application.
However, user roles shouldn’t be used if you want to set up a hierarchical permission control to your application data. To guarantee a scalable and dynamic data segregation per business requirement the recommendation is to build ACL.

For Core Services that require ACL, we propose a model where each Core Service module is responsible for setting the data access rules.

![Diagram illustrating the concept of an Access Control List in a data access scenario.](images/access-control-list.png "Access Control List Diagram")

The Core Services modules must isolate as much as possible the ACL logic in data retrieval methods (e.g., Web Service APIs), but for entities that are public and used outside the Core Service module, developers must know that the access to those tables need to be subject to ACL control.

For that reason, we advise that the objects (Entities) with an associated ACL should be tracked on an **ACL tracking list**, like the following:

|Core Service Module|Entity|ACL Entity|
|---|---|---|
|Customer_CS|Customer|CustomerACL|
|Employee_CS|Employee|EmployeeACL|
|...|...|...|

## ACL Patterns

### Creating new ACL Records

When creating data, if a good module isolation is being made, it should be handled by the proper Core Service who will be responsible by setting up the ACL, accordingly to the rules in place. For instance, when creating a Customer, read/write accesses can be given based on current Unit, Branch, etc.

![Flowchart showing the process of creating a new ACL record in the Customer_CS service.](images/creating-new-acl-record.png "Creating New ACL Record Process")

### Accessing new ACL Records

Accessing data should consider the access rules stored in the ACL, so when retrieving data from a given Entity, a join to the proper ACL entity should be made. This way, the result set will have only data compliant with the ACL rules.

![Flowchart demonstrating how to access new ACL records by joining with the ACL table.](images/accessing-new-acl-records.png "Accessing New ACL Records Process")

#### Example

Let’s see a possible approach on querying data controlled by an ACL.
With the below query, we are able to get a hierarchical view over the sales of the user’s team. While a Sales Account can only see its own sales, the Sales Director (parent in the hierarchy) is able to see the whole team sales.

![Screenshot of an SQL query example for accessing data controlled by an ACL.](images/acl-example.png "ACL Query Example")

* ACL provides, per user, the full list of users belonging to their hierarchy

* On every user profile update, recreate the ACL list

* Abstracts the original API(s), matching to internal structures and concepts (e.g. composing a customer concept with complementary information from different systems)

<div class="info" markdown="1">

This example provides a runtime accelerator to fetch hierarchical results.

</div>

## Performance

To improve performance of ACL rules, access control should be restricted to critical entities on top of a hierarchy, to avoid too much overhead on queries and code maintenance.

For example, if access control is set at Branch level, it is not necessary to do it on Unit or User level.

![Diagram showing the hierarchical control in ACL with Branch, Unit, and User levels.](images/acl-hierarchical-example.png "ACL Hierarchical Control Diagram")

## Best Practices

For Core Services where ACL is applicable, some conventions/best practices should be followed:

* ACL tables should have the same name than the Entity, followed by a suffix “ACL”.

    ![Screenshot showing the naming convention for ACL entities in the database.](images/acl-entity.png "ACL Entity Naming Convention")

* The ACL table should have the same “Public” property as the Entity. If possible, keep this property set to No, to have total control of ACL rules enforcement inside the Core Service.

    ![Screenshot depicting the privacy settings for an ACL entity, set to 'No' for public access.](images/acl-entity-private.png "ACL Entity Privacy Settings")

* When creating a new record on an Entity subject to ACL rules, the ACL record(s) should also be created. The logic to handle ACL rules creation should be placed in a separate server action to facilitate application management.

    ![Flowchart illustrating the process of creating ACL rules after a new record creation.](images/create-acl-logic.png "Create ACL Logic Flowchart")

<div class="info" markdown="1">

Changes on a record subject to ACL may require reprocessing the ACL rules for it.

</div>

* When retrieving data from an Entity with ACL rules, make a join between the Entity and the ACL entity to get the expected results list.

    ![Screenshot showing the data retrieval process from an Entity with ACL rules using a join operation.](images/retrieving-acl-data.png "Retrieving Data with ACL Rules")

* It may be necessary to create a reset action to remount the ACL rules. This action should implement the logic needed to recreate the full ACL table or only a subset of it.

    A good practice is to store all the actions related to ACL within a specific folder.

    ![Diagram illustrating the reset action for remounting ACL rules within the Customer_CS module.](images/acl-reset.png "ACL Reset Action Diagram")
