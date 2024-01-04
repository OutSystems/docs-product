---
summary: The Health and Fitness plugin lets you use data from Apple HealthKit and Google Fit and create customized solutions for your users.
locale: en-us
guid: 58915a48-1778-4182-b55f-77b91d6abb05
app_type: mobile apps
platform-version: o11
figma: https://www.figma.com/file/jSgZ0l0unYdVymLxKZasno/Extensibility-and-Integration?type=design&node-id=1265%3A86185&mode=design&t=187UAgmZTPxcY0ZG-1
---

# Health and Fitness Plugin

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

The [Health & Fitness plugin](https://www.outsystems.com/forge/component-overview/11715/) enables you to access and use health and fitness data in a mobile app. The plugin provides access to the Apple HealthKit and Google Fit APIs by letting you use data relevant to your health and fitness use cases.

The plugin is unaware of the provider you use for data, but you always need to request permissions from users to access data. The plugin saves no health and fitness data to the device. In cases where your app writes data to the APIs, the package name is the identifier of the data source.

As a good practice, verify the plugin is available in the app and prevent the app from crashing. Use the **Logic** > **Client Actions** > **HealthFitnessPlugin** > **CheckHealthFitnessPlugin** action to check for the plugin availability. If the plugin isn't available to the app, display an error to your users.

<div class="info" markdown="1">

To learn how to install and reference a plugin in your **OutSystems** apps, and how to install a sample app, see [Adding plugins](../intro.md#adding-plugins).

</div>

## Sample app

**OutSystems** provides a sample app that contains logic for common use cases. Install the [Health & Fitness sample app](https://www.outsystems.com/forge/component-overview/11715/) from Forge and then open it in Service Studio.

This sample app shows you how to do the following with the health and fitness data:

* Request permission to access
* Do simple queries that return the last logged value
* Do advanced queries for a specific period that return a list of values
* Retrieve raw data related to workouts, for a specific period. This is currently available on iOS only.
* Use the data in user interface components, such as cards, tables, and graphs

![Screenshot of the Health & Fitness sample app interface showing various health metrics.](images/sample-app.png "Health & Fitness Sample App")

## Enabling your users to track their health and fitness data

The following steps show how to design a use case that includes health and fitness data.

1. Create logic to request permission to access health and fitness data.
1. Create a user interface.
1. Create logic to access and store health and fitness data.
1. Create logic to access and use workout data (iOS only).
1. Optionally, create logic to write and store new health and fitness data.
1. Create logic to define a background job.

<div class="info" markdown="1">

Refer to the sample app for examples.

</div>

### Requesting access to health and fitness data

Before your app can access data, request permission from the users to access their health and fitness data. From Service Studio, select **Logic** > **Client Actions** > **HealthFitnessPlugin** and use the **RequestPermission** action.

You can define the variables and the following permissions access types:

* Read
* Write
* Read and write

In the screen logic, request the permissions from the app users, in an action that's triggered by the **On Initialize** event.

The plugin comes with groups of permissions. Use the groups of permissions as accelerators to check for access when you request data.

The plugin has groups of default variables in **Data** > **Entities** > **HealthFitnessPlugin** that define the permission type for:

* HealthVariables
* FitnessVariables
* ProfileVariables
* SummaryVariables
* WorkoutVariables

![Service Studio interface for requesting user permissions grouped by health and fitness data types.](images/get-permissions-by-group-ss.png "Requesting Permissions by Group")

<div class="info" markdown="1">

Refer to the sample app for more examples.

</div>

### Creating a user interface

Start, for example, by defining a variable that corresponds to the type of output you want to show. Create a variable that holds the data so that you can access, store, and display the number of steps taken in a day (1).

![Example of a user interface in Service Studio displaying daily step count.](images/sample-interface-ss.png "Sample User Interface for Health Data")

To show the step count for the day, you can use an **Expression** and customize the look and feel of the parent widget (2).

### Create logic to access and use health and fitness data

The plugin reads and writes the data through the **AdvancedQuery** client action. In the **AdvancedQuery** action, set the values for the predefined variables.

The health or fitness query parameters might include:

* period: start, end
* time unit: second, minute, hour, day, week, month, year
* operation type: sum, min, max, average

![Service Studio logic flow for accessing and querying health and fitness data.](images/get-fitness-data-ss.png "Accessing Health and Fitness Data")

<div class="info" markdown="1">

Verify that access and storage of health or fitness data on the device works. Check the value of **AdvancedQuery**. If **Success** is True, handle the data in **AdvancedQuery.** by assigning it to a variable of the same data type. Refer to the sample app for an example.

</div>

### Create logic to access and use workouts data (iOS only)

To enrich the data that the developer can already obtain from the **AdvancedQuery**, there's also a **GetWorkoutsData** client action that retrieves data related to workouts. To achieve that, it's required to set the values for the input parameters, including:

* period: start, end
* workout type and variable map: list of a structure that relates a Workout Type and a list of Variables to query on.

For the Workout Type and Variable map structure, the plugin already provides a couple of convenient default values to use:

* If no list is provided or it's empty, the plugin considers all workout types available and applies two variables to each: **Heart Rate** and **Active Energy Burned**.
* If the list contains an item that has a workout type set but with no variable list associated (or an empty one), the plugin considers two variables: **Heart Rate** and **Active Energy Burned**.

![Service Studio screen showing the GetWorkoutsData client action to retrieve workout-related data.](images/get-workouts-data-ss.png "Retrieving Workout Data")

<div class="info" markdown="1">

Verify that access and storage of health or fitness workout data on the device works. Check the value of **GetWorkoutsData**. If **Success** is True, handle the data in **GetWorkoutsData.** by assigning it to a variable of the same data type.

</div>

### Create logic to write health and fitness data

To write health and fitness data you can use the **WriteData** action. Set the parameters for the type of health or fitness variable you want and the new value you want to store.

To check that writing the health or fitness data on the device is working, verify that the value of **WriteData.Success** is **True**.

### Create logic to define a background job

To define a background job you can use the **SetBackgroundJob** action. Set the parameters for the type of health or fitness variable you want to monitor, define the notification trigger condition and its frequency, and define the notification content.

Parameterization for two different use cases of a background job is shown below:

#### Setting up a daily steps goal

In the case of a daily steps goal evaluator, you will probably want to issue a single notification per day if the daily steps goal is met. To achieve this you can use the following parameterization:

![Parameters setup in Service Studio for a background job to monitor daily steps goal.](images/set-background-job-ss.png "Setting Up a Background Job for Daily Steps Goal")

#### Setting up a heart rate monitoring alarm

In the case of a heart rate monitoring alarm, try to strike a balance between job frequency and notification frequency. For example, you may want to check your heart rate every ten seconds. However, you would probably find it intrusive to receive notifications every time your heart rate goes above, or drops below, a certain value.

Consider the following parameterization for a background job that notifies you if your heart rate is above 190 bpm, with a maximum notification frequency of one notification per minute:

![Configuration of a background job in Service Studio for heart rate monitoring with notification settings.](images/set-background-job2-ss.png "Setting Up a Heart Rate Monitoring Alarm")

After you have created your background job you can update or delete it using the **UpdateBackgroundJob** action and the **DeleteBackgroundJob** action, respectively.

To check that the background job was successfully created, verify that the value of **SetBackgroundJob.Success** is **True**.

### Create logic to disconnect your Android app from Google Fit

To disconnect your Android app from Google Fit, and consequently revoke all permissions, recording subscriptions, and sensor registrations, you can use the **DisconnectFromGoogleFit** action. To check that your app is no longer connected to Google Fit, verify that the value of **DisconnectFromGoogleFit.Success** is **True**.

After calling this action, you can also verify that the app no longer has access to any data by calling **AdvancedQuery**, **GetFitnessData**, **GetHealthData**, or **GetProfileData**.

<div class="info" markdown="1">

Your app should be implemented so that when a user chooses to disconnect it from Google Fit, it does not try to fetch any data or request any permissions until the user changes their decision.

</div>

### Handling errors

An app with the health and fitness plugin can run on many Android or iOS devices, with different hardware and software configurations. To ensure a good user experience and prevent the app from crashing, handle the errors within the app.

Following is a list of actions you can use to make sure there are no errors:

| Variable        | Action                   | Description                                                    |
| --------------- | ------------------------ | -------------------------------------------------------------- |
| **IsAvailable** | CheckHealthFitnessPlugin | True if the plugin is available in the app.                    |
| **Success**     | AdvancedQuery            | True if there aren't errors while accessing and storing data.  |
| **Success**     | GetWorkoutsData          | True if there aren't errors while accessing and storing data.  |
| **Success**     | GetFitnessData (*)       | True if there aren't errors while accessing and storing data.  |
| **Success**     | WriteData                | True if there aren't errors while writing data.                |
| **Success**     | SetBackgroundJob         | True if there aren't errors while creating a background job.   |
| **Success**     | DisconnectFromGoogleFit  | True if there aren't errors while disconnecting from Google Fit.|

(*) There are several actions in the Health & Fitness plugin that begin with **Get** and have a **Success** variable.
