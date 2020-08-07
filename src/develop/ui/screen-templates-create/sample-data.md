---
summary: Screen Templates contain sample data, which you can manage in a back-office. You can view, reset and add your own data.
---

# Sample data

Sample Data consists of example records from domains related to several industries. Screen Templates use it to create instances of Screens.

## Referencing sample data in apps

Sample data is useful when you need to create a prototype, proof of concept, or when you're following a tutorial that requires it. Reference the sample data by including the OutSystemsSampleDataDB module. Here is how you can do it:

1. Click the manage dependencies icon in the Service Studio toolbar, or press CTRL+Q. **Manage Dependencies** dialog opens.

    ![Manage dependencies icon](images/manage-dependencies.png?width=400)

2. Enter OutSystemsSampleDataDB to search the available producer modules. Select **OutSystemsSampleDataDB** in the results, and in the right pane select all **Entities** of the module.

    ![Manage dependencies adding module](images/manage-dependencies-sample-data-module.png?width=400)

3. Click **Apply** to confirm and close. The Entities are now available in the **Data** tab of Service Studio.

<div class="info" markdown="1">

If there are no results when you search for OutSystemsSampleDataDB, that could mean that the [OutSystems Sample Data](https://www.outsystems.com/forge/component-overview/4145/outsystems-sample-data) component, usually installed with Platform Server, isn't present in the environment. Try installing the component manually.

</div>

## Managing OutSystems Sample Data

OutSystemsSampleDataDB provides a collection of public APIs that lets you:

* Export original data and Import your sample data
* Reset the sample data

### View the Sample Data

Sample Data entities are public, so you can create a custom back-office.

### Import your Sample Data

Follow these steps to import your own data for use in Screen Templates.

1. Reference **OutSystemsSampleDataDB**.
   
1. Use **DownloadOriginalData** from **Logic** > **Server Actions** > **OutSystemsSampleDataDB** > **Export** action to save the original source files in a zip archive.

1. Edit the source files in the zip archive with your own data.

1. Use the **Import** action to upload the updated file and replace the current data.

### Reset the Sample Data

To reset the sample data:

1. Access `http://<yourserver>/ServiceCenter/`

1. Go to the **Factory** > **Modules** tab.
1. Search for **OutSystemsSampleDataDB**.
1. Go to the **Timers** tab in the module details.
1. Select the **Reset_SampleData** timer and click **Run Now**.

If any app extends the provided entities, the Foreign Key constraint won't let the timer run successfully. To overcome this, delete such references (records) first.

## Custom data model and records

You can create your own Entities as the source of data in your Screen Templates. This can be more suitable for your business requirements.
