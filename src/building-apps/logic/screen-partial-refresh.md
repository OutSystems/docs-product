---
summary: It is possible to update certain parts of the screen without reloading the whole screen, thus improving the end user experience.
tags: support-Front_end_Development; support-webapps-featured; runtime-traditionalweb
locale: en-us
guid: cf447891-96c9-41a7-b624-455c180d4002
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing-an-Application?type=design&node-id=266%3A14&mode=design&t=GF97AOUqsRf9tsAh-1
---

# Use Ajax to Refresh Part of a Screen

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

<div class="info" markdown="1">

Are you developing a Reactive Web App? Keep in mind that Ajax Refresh does not exist in Reactive App, because the interface updates automatically when the data bound to it updates. Check the topic [Implement asynchronous data fetching using Aggregates](../data/operations/async-fetch-aggregates.md) to see how to update the interface with the Refresh Data node.

</div>

Refreshing only certain parts of a screen without having to re-render the whole screen improves the end user experience by creating dynamic interfaces and supporting faster user interactions.

For web applications, you can use Ajax to perform asynchronous requests to the web server that fetch only the necessary data to dynamically refresh the screen, without needing to refresh the whole page.

To refresh only part of a screen on a web app:

1. Add a button or link to the screen and set the property Method to 'Ajax Submit' so that the request to the server is performed asynchronously. 

2. Associate a new screen action with the button or link. 

3. In the new screen action, update the data displayed on the screen. For example, assign screen variables or refresh data from the database using the Refresh Data tool. 

4. Drag the Ajax Refresh from the toolbox to the action flow and select the widget that displays the updated data on the screen. The Ajax Refresh can only refresh widgets that have the property Name defined. 

![Flow diagram showing the process of refreshing part of a screen using Ajax in a Traditional Web App](images/screen-partial-refresh-flow.png "Ajax Screen Partial Refresh Flow")
