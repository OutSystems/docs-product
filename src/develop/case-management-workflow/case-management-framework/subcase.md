---
tags: Case Management; Case Management framework.
summary: Learn about subcases and how to associate them with a parent case.
guid: 6f4a1519-2b35-46d4-979a-5578b33d4dc5
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Creating a case management app with subcases 

<div class="warning" markdown="1">

Parts of this article are out-of-date. We are aware of the problem and currently working on a revision.

</div>

A subcase is a case by itself that's linked to a parent case, so you need to create a case definition and also set the **ParentCaseId** input parameter while initializing the case with the **Case_Initialize** action.

The parameter **UserId** must also be used to define the user that created the subcase. This is required because the **GetUserId**() function doesn't work inside Business Process Technology (BPT). You can do this by creating an input parameter in the create action or by adding logic inside of it to fetch the desired **UserId** value.

## How to create subcases

To create subcases you start by creating the new core services module for your subcase, adapting the then [creating the subcase definition](#create-subcase), and then [adapting the parent case](#adapt-parent-case).

### Create subcase

A subcase is a case by itself that's linked to a parent case, so you need to create a case definition and also set the **ParentCaseId** input parameter while initializing the case with the **Case_Initialize** action.

<div class="info" markdown="1">

The parameter **UserId** should also be used to define the user that created the subcase. This is required because the GetUserId() function doesn't work inside BPTs. You can do this by also creating an input parameter in the create action or by adding logic inside of it to fetch the desired UserId value.

</div>

To create a subcase definition follow these steps:

1. In your case management app, create a new **Service** module and name it `<business-entity-name>_CS`. This is the core services modules that keeps the subcase business entity and business logic.

    <div class='info' markdown='1'>

    Replace &lt;business-entity-name&gt; with a name that represents the subcase buisness entity.

    </div>

1. Create the core services module for your subcase, by following [Step 1. of the create a case management app topic](bootstrap-app.md#step1) starting in **Step 1.3**.

1. Create the subcase definition by following [Step 2. of the create a case management app topic](bootstrap-app.md#step2).

1. Associate the subcase business entity with the subcase by following [Step 3. of the create a case management app topic](bootstrap-app.md#step3).

1. Create the initial subcase status by following [Step 4. of the create a case management app topic](bootstrap-app.md#step4).

1. Create the subcase bootstrapping action by following [Step 5. of the create a case management app topic](bootstrap-app.md#step5).

1. After completing **Step 5.**, in the **&lt;business-entity-name&gt;_Create** action, add an input parameter named `ParentCaseId` and with **Case Identifier** data type.

1. Select the **Case_Initialize** action, and set the **ParentCaseId** as `TextToIdentifier(ParentCaseId)`.

1. Publish the subcase core services module, &lt;business-entity-name&gt;, by selecting **1-Click Publish**.

1. In the **&lt;app-name&gt;_WF** module, create the process that is triggered on the creation of a subcase instance by following [Step 6. of the create a case management app topic](bootstrap-app.md#step6) staring in **Step 6.3**.

### Adapt parent case

The parent case process needs to be changed to trigger a subcase instance and also to check for the status of the subcase instance. To adapt the parent case follow these steps:

1. In the flow of the process for the parent case, add a new **Automatic Activity** where you want to trigger the subcase instance.

1. In the Automatic Activity flow, add the create action from the subcase business entity,**&lt;business-entity-name&gt;_Create**, and set the **ParentCaseId** action parameter as the input parameter of the process, `<parent-entity-name>Id`.

1. Add an **Output Parameter** to the automatic activity, name it `SubcaseId` and set the data type to **Case Identifier**.

1. Add an **Assign** after the **&lt;business-entity-name&gt;\_Create**, and set the `SubcaseId` (the automatic activity output parameter) as `<business-entity-name>_Create.CaseId` (the output of **&lt;business-entity-name&gt;\_Create** action).

    <div class="info" markdown="1">

    At runtime the execution of this Automatic Activity triggers a new instance of the subcase (as said previously everything works the same for a subcase, the create action will trigger its own BPT process) but it's the association to the parent case that triggers the process.

    </div>

1. Since the parent case and child case run in different instances you need to poll the child case from the parent case to know if it's completed for example. Add a **Wait** element to the parent’s process flow while setting a timeout value that makes sense for your use case and adding an **On Close** callback action to the Wait.

1. In the **On Close** action, drag the **Case** entity (from the **CM_Case_CS** module) to the flow to add an aggregate with the **Case** entity (from the **CM_Case_CS** module) as source.

1. Add a filter that filters the CaseId by the SubcaseId, by setting the filter condition as `Case.Id = <automatic-activity>.SubcaseId`, where &lt;automatic-activity&gt; is the name of the automatic activity created in step 1.

1. In the **On Close** action flow, set the **Condition** of the **If** to `GetCaseById.List.Current.Case.CompletedOn <> NullDate()` to check if the subcase has been closed.

1. Ensure the **True** connector is connected to an **End**, and the **False** connector is connected to a **Raise Exception**. This ensures that if the subcase is closed the Wait stops, and if the subcase isn't closed the Wait is reset and repeats the check once the timeout is reached again

1. Publish the module by selecting **1-Click Publish**.
