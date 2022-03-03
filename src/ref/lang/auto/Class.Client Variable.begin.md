
In Mobile and Reactive Web apps, use Client Variables to store data client-side in a key-value format. For example, use these variables to store configurations and app context data.

Client Variables can only store [basic data types](<../../data/data-types/available-data-types.md>). The one exception is **Binary** data, which is a basic data type, but can't be stored in these variables.
The amount of data you have available for all Client Variables across an environment depends on the browser.

The value of a Client Variable is shared across different apps in the same environment, under these conditions:

* User Provider of the apps is the same.
* The apps are running in the same browser.

You can share the value of Client Variables through apps by using them in:

* Public Blocks
* Public Client Actions

Client Variables reset to their default values when the user signs out of the app or when the platform signs out the user automatically. However, don't use Client Variables to store sensitive or confidential information.

## Create a Client Variable 

You can add a Client Variable by clicking **Data** tab > **Client Variables** > **Add Client Variable**.

## How to use

This example shows how to use a Client Variable to keep the value of a Search widget. The value of the Client Variable is then used to filter an Aggregate. This value is kept if you change to another screen or close the browser.

1. In the **Data** tab, right-click **Client Variables** and select **Add Client Variable**.

1. Enter a name for the variable, for example `SearchKeyword`.

    ![New Client Variable created with the name SearchKeyword](<images/client-variable-new-ss.png>)

1. Select the Input widget.

1. On the **Properties** tab, on the **Variable** field, insert `Client.SearchKeyword`.

    ![Binding the Client Variable to the Input](<images/client-variable-input-ss.png>)

1. Double click the aggregate on the source tree to open it.

1. On the **Filter** tab, click **Add filter**.

1. Insert the filter condition. 

    ```
    Employee.FirstName like "%" + Client.SearchKeyword + "%"
    ```

1. Click **Close** to save the filter. 

    ![Aggregate with a filter that uses the SearchKeyword Variable to filter the results](<images/client-var-filtered-aggregate-ss.png>) 
