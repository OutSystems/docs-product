---
summary: Screens and Blocks follow a lifecycle composed by a set of stages. Learn what those stages are and you what can do at each one.
tags: runtime-mobileandreactiveweb; support-application_development; support-Application_Troubleshooting-featured; support-Mobile_Apps
locale: en-us
guid: 9205fe77-5e90-402b-ba73-45cdc745515a
app_type: mobile apps, reactive web apps
platform-version: o11
---

# Screen and Block Lifecycle Events

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

In OutSystems Mobile and Reactive Web Apps, the Screens and Blocks follow a lifecycle composed by a set of stages. Some of those stages are when you open the app and enter the default screen, navigate to another screen, or change the data of the screen or block.

The data of a screen or block are the following:

* Input parameters
* Variables
* Aggregates and Data Actions
* Validation messages

While implementing a Mobile or Reactive Web App, the developer can act upon those stages by using a set of event handler actions. These event handlers give the developer visibility over the screen and block lifecycle and the opportunity to implement logic when certain events occur. 

You can see and define the event handlers in the Events section of the properties editor of Screens and Blocks, or for the event handler triggered when data finished being fetched, in the properties editor of Aggregates or Data Actions.


## Lifecycle Stages

### On Opening the Application

![](images/lifecycle-open-application.png?width=831)

Opening an application is one of the situations when a screen is loaded (the other situation is when navigating from another screen). In this case, the app displays the configured splash screen and then navigates to the default screen.

<div class="info" markdown="1">

This article often mentions DOM, or Document Object Model. To learn more about DOM, check out [Introduction to the DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction) by MDN.

</div>

While displaying the splash screen, the application checks the user role against the roles with permission to access the screen (defined in the screen properties). After this verification, the Initialize event happens and the respective event handler action, the [On Initialize](<#on-initialize>) is triggered. Since the DOM of the default screen is not completely loaded when this event occurs, you can use this event handler to implement all the logic that doesn’t require the DOM, such as to initialize some default data.

When the On Initialize event handler ends, the Aggregates and Data Actions of the default screen concurrently start to fetch data (exemplified by the GetContacts and GetProfileImages of the image above), the DOM of the screen loads and the [Ready](<#on-ready>) and [Render](<#on-render>) event handlers run. The difference between these two events is that the Ready event only happens when opening the screen while the Render event also happens every time the data of the screen (such as input parameters, variables, aggregates and data actions, or validation messages) is modified. You can use both event handlers to act on the loaded DOM. Avoid accessing the data of the screen since this data may not be fetched yet.

Even before the data from the aggregates and the data actions is fetched, the screen appears to the user with the static resources. To prevent this situation, adopt an offline first implementation approach.

When the aggregates and data actions of the screen finish fetching the data, the widgets bound to these data sources automatically update with the fetched data. The [After Fetch](<#on-after-fetch>) event handler of each aggregate and data action runs, followed by the Render event (since the data of the screen was modified). For each After Fetch event, the application executes a Render event.

### On Navigating Between Screens

![](images/lifecycle-navigate-screens.png?width=834)

Navigating from a screen to another is a very common pattern of applications. This is usually triggered by a user interaction such as clicking a button or list item on the screen. Navigating between screens in OutSystems means that a new screen is loaded and then the previous screen is removed.

When the navigation starts, the DOM of the target screen immediately starts to load. This means that the DOM of the screen to be removed and the target screen are present at the same time. The DOM of the old screen is removed only after the Render event of the target screen, ensuring a fast and smooth transition between the screens and avoiding displaying the loading stages of the target screen to the user.

The first event handler to run is the [On Initialize](<#on-initialize>). The application continues to load the DOM of the target screen followed by its events, as documented in the section for when the application is opening. Since those events belong to the target screen, the active screen is the target screen and the `active-screen` class in the DOM is assigned to the elements of that screen.

After the [Render](<#on-render>) event of the target screen, the transition between the screens happens and the older screen is finally removed from the DOM. This means that the DOM of both screens are available between the Render event of the target screen and the Destroy event of the old screen.

### On Changing the Data of a Screen or Block

Every time you change the value of a data element of a Screen or Block, the application automatically reacts to it. Thus, the Render event is triggered and the UI elements that depend on the data automatically update. You don’t have to explicitly refresh the UI elements as you need to do for web apps.

For Screen or Block Aggregates and Data Actions, their new values are automatically updated in the UI elements, but you need to rerun the query explicitly. This can be done using the [Refresh Data](<../../ref/lang/auto/class-refresh-data.md>) flow element in the logic.

After data is fetched, the [After Fetch](<#on-after-fetch>) event occurs and, since the data returned from the Aggregate or Data Action belongs to the screen or block data and has changed, the Render event also occurs.

As an example, imagine a screen showing the details of a contact along with the list of calls to that contact. To get the calls, you use an Aggregate filtered by the value of the variable of the screen assigned with the current contact identifier. When the contact changes the screen will display the new contact details, so the screen variable is modified to contain the new contact identifier. To get the list of calls to this new contact, the Aggregate must run again. To do it, you only need to call the Refresh Data flow element in the logic and select the respective Aggregate or Data Action. When the query returns the new list of calls, the list in the screen is automatically updated.

### On Changing the Parameters of a Block

![](images/lifecycle-change-parameters.png?width=614)

To allow the notification and update of a block when one of its input parameters change, the application runs the [Parameters Changed](<#on-parameters-changed>) event handler of the block. A common use case for this event handler is to rerun some Aggregate or Data Action that depends on the input parameter, as exemplified in the image above where after a change in the calendar date, the query is executed again to obtain new values for the chart.

Since the input parameter is part of the data of the Block, the [Render](<#on-render>) event is also triggered, but only after the Parameters Changed event.

## Lifecycle Event Handlers

Event | Description
------|------------
[On Initialize](<#on-initialize>) | Occurs after checking the permission of the user to access the Screen, but before navigating to the Screen and fetching data. In Blocks, it occurs after the navigation. You can use it to initialize the Screen or Block by setting its default data.
[On Ready](<#on-ready>) | Occurs after the Screen or Block DOM is ready, before the transition starts.
[On Render](<#on-render>) | Occurs right after the Screen or Block On Ready event handler and every time the data of a Screen or Block changes. You can use it to update some third-party component.
[On After Fetch](<#on-after-fetch>) | Occurs after an Aggregate or Data Action has finished fetching data but before this data is rendered on the Screen or Block. You can use it to act upon the retrieved data.
[On Parameters Changed](<#on-parameters-changed>) | Occurs in a Block anytime the parent Screen or Block changes one of its input parameters. Changes to the input value inside the block do not trigger this event handler. You can use it to react to changes in the Block parameters, such as to update variables.
[On Destroy](<#on-destroy>) | Occurs before destroying a Screen or Block and removing it from the DOM. You can use it to implement logic when the component is disposed, such as to remove event listeners.

### On Initialize

The On Initialize event handler executes after checking the permission of the user to access the Screen, but before navigating to the Screen and starting to fetch data.

In Blocks, including any server action calls or local storage operations in this flow might cause the render of the Block to start before this action finishes. You will have issues if you set any variables in this flow that affect the render.

Notes:

* Keep this event handler action simple and avoid slow actions such as local storage operations, since it may delay the rendering of the Screen or Block.
* Avoid accessing the data of the Screen or Block since this action runs before the data is fetched. 

Use cases you can implement with this event handler:

* Assign a variable based on inputs. 
* Assign a variable based on some computation in JavaScript, such as a random number. 
* Redirect the application to another Screen if the user doesn’t have the authorization to see the Screen (only possible if the event handler belongs to a Screen). 
* Assign the parameters of a child Block based on the inputs of the Screen. 
* Access variables of the JavaScript window object. 

### On Ready

The On Ready event handler runs when the Screen or Block is ready, i.e. when the DOM is ready, after the first render. In Blocks, this event happens before the same event of the parent Screen or Block. To ensure a fast and smooth Screen or Block render, this event is triggered even before the transition to the Screen ends.

Notes:

* The DOM of the previous and current Screens are loaded when this event is triggered. To ensure that you are operating on the screen being created, execute logic only for the HTML `div` element with the class `active-screen`. 
* Keep this event handler action simple and avoid using Screen Aggregates or Data Actions, which run in parallel, to manipulate data that might not be available.
* Avoid accessing the data of the Screen or Block since this action runs before the data is fetched. If you need to develop some logic on these data, use the On After Fetch event handler of the respective Aggregate or Data Action. 

Use cases you can implement with this event handler:

* Initialize a third-party component that needs the DOM.
* Add listeners to a DOM element.
* Set the focus on an input widget.
* Add listeners to the JavaScript window object. 

### On Render

The On Render event handler runs after each time the Screen or Block is rendered, i.e. whenever the Screen or Block is opened (right after the On Ready event handler execution) and after any change of the data of the Screen. In Blocks, this event happens before the same event of the parent Screen or Block. You can use this event handler to update a third-party component such as a progress bar.

Notes:

* Avoid changing Screen or Block data since every time this data changes the On Render event is triggered again and the app might run in an infinite loop. 
* Keep this event handler action simple and avoid slow actions such as server requests, since it may delay the render of the Screen or Block. 
* On the first render of the Screen or Block avoid accessing the data of the Screen or Block since there is no guarantee that the data is already fetched. If you need to develop some logic on these data, use the On After Fetch event handler of the respective Aggregate or Data Action. 

Use cases you can implement with this event handler:

* Act upon a change in the data of the Screen or Block to update a third-party component.
* The same use cases as for the On Ready event handler. 

### On After Fetch

The On After Fetch event handler executes right after an Aggregate or Data Action finishes fetching data. Since each Aggregate or Data Action has its own On After Fetch event handler, you can implement logic to act upon the data retrieved from that data source.

Notes:

* When the On After Fetch event handler runs, the data has arrived and is available but it isn't bound to widgets. This means that the widgets haven't updated yet. 

Use cases you can implement with this event handler:

* Assign the first or last record returned by the query to a variable.
* In the master-detail pattern, to iterate a query to populate a list of lists.
* For queries dependent on other queries, you can use this event handler to trigger the dependent Aggregate.  

### On Parameters Changed

The On Parameters Changed is an event handler only for Blocks that runs after the parent Screen or Block changes an input of the Block. In case you have a Block inside another Block and a change of an input of the outside Block affects an input of the nested Block, the On Parameters Changed event handler of the outer Block runs before the same event of the nested Block. You can use this event handler to adapt the Block to the input parameter changes, such as to update variables or rerun Aggregates and Data Actions.

Use cases you can implement with this event handler:

* Refresh an Aggregate or Data Action that depends on that input parameter.
* Recalculate a variable that depends on the input parameter. 

### On Destroy

The On Destroy event handler executes when the Screen or Block is going to be destroyed. In Screens, this event happens when the transition to the new Screen ends. In Blocks, this event happens before the Block is removed from the DOM. This event is triggered following a top-down order: in case you have a Screen with nested Blocks, the event first happens in the Screen, then in the outer Block, and afterwards in the nested Blocks. You can use this event handler to implement logic to remove any footprint of the Screen or Block such as removing event listeners.

Notes:

* The DOM of the present and target screens is loaded when this event is triggered. To ensure that you are operating on the screen being destroyed, execute logic only for the HTML `div` element with the class `active-screen`. 
* Keep this event handler action simple and avoid slow actions such as server requests, since it may delay the removal of the Screen or Block and, in the case of exiting a screen, the loading of the next screen. 

Use cases you can implement with this event handler:

* Call the destroy action of third-party components.
* Clean the DOM to run a plugin again.
* Remove JavaScript listeners. 
