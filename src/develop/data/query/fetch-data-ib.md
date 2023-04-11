---
summary: Learn how to fetch data from an integration created using Integration Builder.
locale: en-us
guid: af0a23a7-38a2-4d2e-89da-a734af4e68a4
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Fetch and display data from an integration

After [adding an integration as a dependency to your module in Service Studio](../../../extensibility-and-integration/integration-builder/use.md#use), use the [actions from the integration](../../../extensibility-and-integration/integration-builder/structure.md) to fetch and manipulate the data from your external system of records. This article shows you how to fetch a single record or a list of records, that you can then show in a screen.

Fetch a single record, if, for example, to show data about a product in a product detail screen.
Fetch a list of records, if, for example, to show a table with a list of products in a product list screen.

Integrations created using Integration Builder include the following data fetching actions:

* `Get<Entity>` — Get the data of an entity record with the given identifier.
* `Search<Entity>s` — Get a list of entity records that fulfill the provided filter conditions. The list of results supports paging and custom ordering.
* `Count<Entity>s` — Count the number of entity records that fulfill the provided filter conditions. Note: SharePoint Online integrations don't include this action.

Start by [fetching data in your screen](#fetch-data), and then [show the data in your screen](#show-data).

## Prerequisites

Before you start, ensure you created an app with a module and [added the integration as a dependency to your module in Service Studio](../../../extensibility-and-integration/integration-builder/use.md#use).

## Fetch data from an integration { #fetch }

<div class="info" markdown="1">

If your module doesn't have a screen yet, add an empty screen. Go to **Interface** > **UI Flows**, right-click **MainFlow** and select **Add Screen**. In the **New Screen** window select **Empty**, enter **Home** as the Screen name, then click **CREATE SCREEN**.

</div>

### Fetch a list of records { #fetch-list }

To fetch a list of records of an entity, &lt;Entity&gt;, from an integration in a screen do the following:

1. In the **Interface tab** of your module, create a Data Action in the screen. Open the context menu for the Screen, and select **Fetch Data from Other Sources**.

1. In the element tree, select the **Out1** output parameter, and set its **Data Type** to **&lt;Entity&gt; List** by doing the following:
    
    1. In the **Data Type** property menu select **List...**.

    1. In the **List Element Type** dialog, go to the **Structures** section, select **&lt;Entity&gt;\\&lt;Entity&gt;**, and then click **OK**. &lt;Entity&gt; is the name of your entity, for example `Products`.

1. With the **Data Action** flow open, go to the **Logic** tab, find your integration, and drag the **Search&lt;Entity&gt;** to the action flow.

1. Add an **Assign** after the Search&lt;Entity&gt; action, and set the value of the output parameter as the output of the action. Add the following assignment:

    * `Out1` = `Search<Entity>.<Entity>`

After these steps, [show the list of records in the screen](#show-list).

### Fetch a single record { #fetch-record }

To fetch a single record of an entity, &lt;Entity&gt;, from an integration in a screen do the following:

1. In the **Interface tab** of your module, create a Data Action in the screen. Open the context menu for the Screen, and select **Fetch Data from Other Sources**.

1. In the element tree, set the **Data Type** of the **Out1** output parameter as the entity from your integration. In the **Data Type** dropdown, go to **Structures**, and select **&lt;Entity&gt;\\&lt;Entity&gt;**. &lt;Entity&gt; is the name of your entity, for example `Products`.

1. With the **Data Action** flow open, go to the **Logic** tab, find your integration, and drag the **Get&lt;Entity&gt;** to the action flow. &lt;Entity&gt; is the name of your entity, for example `Products`.

1. Add an **Assign** after the Get&lt;Entity&gt; action, and set the value of the output parameter as the output of the action. Add the following assignment:

    * `Out1` = `Get<Entity>.<Entity>`

After these steps, [show the record data in the screen](#show-record).

## Show data

Once you fetch data from the integration, use widgets or OutSystems UI patterns to show the data to end users.

### Show a list of records { #show-list }

To show a list of records from an integration, do the following:

1. Open the [screen where you fetched the data](#fetch-list), from the toolbox drag a **Table**, **List**, or **Gallery** to the screen.

1. From the element tree, expand the **Out1** output parameter from the data action, and drag each of the attributes you want to display to the **Table**, **List**, or **Gallery**.

1. Publish your module by selecting **1-Click Publish**.

### Show a single record { #show-record }

To show a single record from an integration in the [screen where you fetched the data](#fetch-record), use the **Out1** output parameter from the data action in one of the following widgets:

* If you want to show text or number values, use **Out1** in the **Expression Value** property of [**Expression** widgets](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-expression.md).

* If you want to show an image, use **Out1** in **URL** or **Image Content** properties of [**Image** widgets](../../../ref/lang/auto/servicestudio-plugin-nrwidgets-image.md).
