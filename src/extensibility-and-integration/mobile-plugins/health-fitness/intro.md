---
summary: The Health and Fitness plugin lets you use data from Apple HealthKit and Google Fit and create customized solutions for your users.
en_title: Health and Fitness Plugin 
tags: runtime-mobile;
---

# Health & Fitness Plugin

<div class="info" markdown="1">

OutSystems is preparing a Health & Fitness plugin for a general release. The team invites all developers and UX people to submit their feedback. How can the team make the plugin better? For what use cases you need documentation most? Let us know [at this forum topic](https://www.outsystems.com/forums/discussion/73732/health-fitness-plugin-under-development-feedback-wanted/)! 

</div>

The [Health & Fitness plugin](https://www.outsystems.com/forge/component-overview/11715/) enables you to access and use health and fitness data in a mobile app. The plugin provides access to the Apple HealthKit and Google Fit APIs by letting you use data relevant to your health and fitness use cases.

The plugin is unaware of the provider you use for data, but you always need to request permissions from users to access data. The plugin saves no health and fitness data to the device. In cases where your app writes data to the APIs, the package name is the identifier of the data source. 

As a good practice, verify the plugin is available in the app and prevent the app from crashing. Use the **Logic** > **Client Actions** > **HealthFitnessPlugin** > **CheckHealthFitnessPlugin** action for check for the plugin availability. If the plugin isn't available to the app, display an error to your users.

<div class="info" markdown="1">

To learn how to install and reference a plugin in your OutSystems apps, and how to install a sample app, see [Adding plugins](../intro.md#adding-plugins).

</div>

## Sample app

OutSystems provides a sample app that contains logic for common use cases. Install the [Health & Fitness sample app](https://www.outsystems.com/forge/component-overview/11715/) from Forge and then open it in Service Studio.

This sample app shows you how to do the following with the health and fitness data:

* Request permission to access
* Do simple queries that return the last logged value
* Do advanced queries for a specific period that return a list of values
* Use the data in user interface, such as cards, tables, and graphs

![Sample app home screen](images/sample-app.png) 

## Enabling your users to track their health and fitness data

The following steps show how to design a use case that includes health and fitness data.

1. Create logic to request permission to access health and fitness data
1. Create a user interface
1. Create logic to access and store health and fitness data
1. Optionally, create logic to write and store new health and fitness data

<div class="info" markdown="1">

Refer to the sample app for examples.

</div>

### Requesting access to health and fitness data

Before your app can access data, request permission from the users to access their health and fitness data. From Service Studio, select the **Logic** > **Client Actions** > **HealthFitnessPlugin** and use the **RequestPermission** action.

You can define the variables and the following permissions access types:

* Read
* Write
* Read and write

In the screen logic, request the permissions from the app users, in an action that's triggered by **On Initialize** event.

The plugin comes with groups of permissions. Use the groups of permissions as accelerators to check for access when you request data.

The plugin has groups of default variables in **Data** > **Entities** > **HealthFitnessPlugin** that define the permission type for:

* HealthVariables
* FitnessVariables
* ProfileVariables
* SummaryVariables

![Using permission variables to check for data availability](images/get-permissions-by-group-ss.png)

<div class="info" markdown="1">

Refer to the sample app for more examples.

</div>

### Creating a user interface

Start, for example, by defining a variable that corresponds to the type of output you want to show. Create a variable that holds the data so that you can access, store, and display the number of steps taken in a day (1).

![Sample interface to show steps](images/sample-interface-ss.png) 

To show the step count for the day, you can use an **Expression** and customize the look and feel of the parent widget (2).

### Create logic to access and use health and fitness data

The plugin reads and writes the data through the **AdvancedQuery** client action. In the **AdvancedQuery** action, set the values for the predefined variables.

The health or fitness query parameters might include:  

* period: start, end
* time unit: second, minute, hour, day, week, month, year
* operation type: sum, min, max, average 
  
![Getting data in AdvancedQuery from Google Fit and Apple HealthKit](images/get-fitness-data-ss.png) 

<div class="info" markdown="1">

Verify that access and storage of health or fitness data on the device works. Check the value of **AdvancedQuery**. If **Success** is True, handle the data in **AdvancedQuery.** by assigning it to a variable of the same data type. Refer to the sample app for an example.

</div>

### Create logic to write health and fitness data

To write health and fitness data you can use the **WriteData** action. Set the parameters for the type of health or fitness variable you want and the new value you want to store.

To check that writing the health or fitness data on the device is working, verify the value of **WriteData.Success** is **True**.

### Create logic to define a background job

To define a background job you can use the **SetBackgroundJob** action. Set the parameters for the type of health or fitness variable you want to keep evaluating, define the notification trigger condition and its frequency, and define the notification content. 

Parametrization for two different use cases of a background job is shown below:

#### Setting up a daily steps goal
In the case of a daily steps goal evaluator, you will probably want to issue a single notification per day if the daily steps goal is met. To achieve this you can use the following parametrization:

![Screenshot 2021-12-16 at 10 00 23](https://user-images.githubusercontent.com/81437871/146352239-727cc5f4-d8c1-4b35-bb8a-b232c37ff9a2.png)

#### Setting up a heart rate monitoring alarm
In the case of a heart rate monitoring alarm, try to strike a balance between job frequency and notification frequency. For example, you may want to check your heart rate every ten seconds. However, you would probably find it intrusive to receive notifications every time your heart rate goes above, or drops below, a certain value.

Consider the following parametrization for a background job that will notify you if your heart rate is above 190 bpm, with a maximum notification frequency of one notification per minute:

![Screenshot 2021-12-16 at 10 02 46](https://user-images.githubusercontent.com/81437871/146352389-950a22d7-ccca-40ae-9ead-7cda96434d56.png)

After you have created your background job you can update it or delete it using the **UpdateBackgroundJob** action or the **DeleteBackgroundJob** action, respectively.

To check that that the background job was successfully created, verify if the value of **SetBackgroundJob.Success** is **True**.

### Handling errors

The app with the plugin can run on many Android or iOS devices, with different hardware and configurations. To ensure a good user experience and prevent the app from crashing, handle the errors within the app.

Following is a list of actions you can use to make sure there are no errors:

| Variable        | Action                   | Description                                                    |
| --------------- | ------------------------ | -------------------------------------------------------------- |
| **IsAvailable** | CheckHealthFitnessPlugin | True if the plugin is available in the app.                    |
| **Success**     | AdvancedQuery            | True if there aren't errors while accessing and storing data.  |
| **Success**     | GetFitnessData (*)       | True if there aren't errors while accessing and storing  data. |
| **Success**     | WriteData                | True if there aren't errors while writing data.                |
| **Success**     | SetBackgroundJob         | True if there aren't errors while creating a background job.   |
(*) There are several actions in the Health & Fitness plugin that begin with **Get** and have a **Success** variable.
