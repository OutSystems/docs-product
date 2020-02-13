
Use Client Variables to store [basic data types](<../../data/data-types/available-data-types.md>) client-side in a key-value format in Mobile and Reactive Web Apps. You can use them to cache, for example, configurations and app context data. The amount of data you have available for all Client Variables across an environment depends on the browser.

The value of a Client Variable is shared across different apps in the same environment, under these conditions:

* User Provider of the apps is the same
* The apps are running in the same browser

You can share the value of Client Variables through apps by using them in:

* Public Blocks
* Public Client Actions

Client Variables reset to their default values when the user signs out of the app or when the platform signs out the user automatically. However, do not use Client Variables to store sensitive or confidential information.

## Create a Client Variable 

You can add a Client Variable by clicking **Data** tab > **Client Variables** > **Add Client Variable**.

