---
summary: Screen Templates contain sample data, which you can manage in a back-office. You can view, reset and add your own data.
---

# Sample data

Sample Data consists of example records from domains related to several industries. It is used in screens created from Screen Templates.

## Referencing sample data in apps

Sample data is useful when you need to create a prototype, proof of concept, or when you're following a tutorial that requires it. Reference the sample data by including the OutSystemsSampleDataDB module. Here is how you can do it:

1. Click the manage dependencies icon in the Service Studio toolbar, or press CTRL+Q. **Manage Dependencies** dialog opens.

    ![Manage dependencies icon](images/manage-dependencies.png?width=400)

2. Enter OutSystemsSampleDataDB to search the available producer modules. Select **OutSystemsSampleDataDB** in the results, and in the right pane select all **Entities** of the module.

    ![Manage dependencies adding module](images/manage-dependencies-sample-data-module.png?width=400)

3. Click **Apply** to confirm and close. The Entities are now available in the **Data** tab of Service Studio.

<div class="info" markdown="1">

If there are no results when you search for OutSystemsSampleDataDB, that could mean that [OutSystems Sample Data](https://www.outsystems.com/forge/component-overview/4145/outsystems-sample-data) component, usually installed with Platform Server, is not present in the environment. Try installing the component manually.

</div>


## Managing OutSystems Sample Data

Sample data is managed in the Sample Data Back-Office at `http://<yourserver>/OutSystemsSampleData/` where you can:

* View the sample data
* Import your sample data
* Reset the sample data

### View the Sample Data

To view the sample data, access the Sample Data Back-Office and click the **Backoffice** tab.

### Import your Sample Data

Follow these steps to import your own data for use in Screen Templates.

1. Access the Sample Data Back-Office.
2. In the **Data Management** section, click **Download Data**.
3. Populate the source files in the OriginalData.zip with your own data.
4. In the **Data Management** section, click **Choose File** and select your edited zip file.
5. Click **Upload**.

### Reset the Sample Data

To reset the sample data access the Sample Data Back-Office and in the **Data Management** section click **Reset Data**.

## Custom data model and records

You can create your own Entities as the source of data in your Screen Templates. This can be more suitable for your business requirements.
