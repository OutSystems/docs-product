---
tags: Case Management; Case Management framework;
summary: Learn how to get a list of cases create by the requester logged in to your app.
guid: da294998-4af8-4fb5-acf8-939d4d2d5a06
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
---

# How to get list of cases for a requester

Learn how to get a list of cases created by a requester logged in to your app.
You can then use this list as the data source of a Table or List widget to enable requester to see a list and status of the cases they created.

## Get list of cases created by logged user { #basic-list}

Before following the steps, make sure you have created the UI module of your app, named **&lt;app-name&gt;_UI**.

To get a list of activities assigned to a case worker logged in to your app, follow these steps:

1. In **&lt;app-name&gt;_UI**, open **Manage Dependencies**, and add the following dependencies:

    * From  **CaseServices_API** producer, add the **Case_GetCases** action.
    * From the **CM_CaseServices_BL** producer, add the **RequesterScope** static entity.

1. In the screen where you want to display the list of activities, add a **Data Action**.

1. In the data action flow, add a **Case_GetCases** service action.

1. In the properties pane of the **Case_GetCases** action, select **Expand CaseScope**.

1. To get cases created by the logged in user, set **RequesterScopeId** as `Entities.RequesterScope.MyCases`.

1. To get activities assigned to the user, set **ActivityAssignmentStatus** as `Entities.ActivityAssignmentStatus.Assigned`.

1. Select the **Output Parameter**, and in the property pane set its **Data Type** to **CaseDetails list** by selecting **List...** > **CaseActivity\CaseDetails**.

1. In the flow, add an **Assign** after the **Case_GetCases** action.

1. In the **Assign**, add an assignment that sets the output parameter as `Case_GetCases.CaseResults`.

After these steps, use the output parameter as the data source of a **Table** or **List** to show the information to the requester.

## Add case business information to the list of cases

You may need to show extra business information about the case that's only available in the case business entity, for example the subject line of a support ticket.

To add case information that's stored in the case business entity, make sure you have created a [Data Action to get a list of cases](#basic-list), and then follow these steps:

1. In **&lt;app-name&gt;_UI**, open **Manage Dependencies**, and from the **&lt;business-entity&gt;_CS** producer, add the case business entity as a dependency.

1. In the flow of the data action used to fetch the list of cases, set the output parameter's **Data Type** as a **List** of **Records** composed by the **CaseDetails** structure and the **&lt;business-entity&gt;** entity by doing the following:

    1. In the **Data Type** dropwdown of the output parameter, select **List..**.
    1. Select **Record..**.
    1. Select **Add attribute to &lt;output-name&gt;**, and add the following attributes:
        * `CaseDetails` with **CaseActivity\CaseDetails** structure data type.
        * `<business-entity>` with **&lt;business-entity&gt;** entity data type.

1. If you followed the [procedure to get list of cases for a requester](#basic-list), delete the **Assign** from the flow.

1. In the flow, add a **For Each** after the **Case_GetCases** service action.

1. Set the **Record List** of the **For Each** as `Case_GetCases.CaseResults`.

1. In the flow, add an **Aggregate** to fetch the data of the case business entity by dragging the **&lt;business-entity&gt;** entity next to the **For Each**.

1. Connect the **For Each** to the **Get&lt;business-entity&gt;** aggregate created in the previous step.

1. In the **Get&lt;business-entity&gt;** aggregate, add a **Filter**, and set it as `<business-entity>.Id = Case_GetCases.CaseResults.Current.CaseId`, replacing &lt;business-entity&gt; by the name of your case business entity.

1. In the flow, add a **ListAppend** server action after the **Aggregate** created in step 6, and then connect the **Aggregate** to the **ListAppend**.

1. In the properties of **ListAppend**, set **List** as the output parameter.

1. Select **Expand Element** (represented by the **+** next to **Element**), set **CaseDetails** as `Case_GetCases.CaseResults.Current`, and set **&lt;business-entity&gt;** as `Get<business-entity>.List.Current`, replacing &lt;business-entity&gt; by the name of your case business entity.

1. Connect **ListAppend** to the **For Each**.

After these steps, use the output parameter as the data source of a **Table** or **List** to show the information to the requester.
