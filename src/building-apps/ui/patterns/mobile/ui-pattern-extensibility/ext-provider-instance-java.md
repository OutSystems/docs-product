---
tags: runtime-mobileandreactiveweb;
summary: Explore how to access and manipulate provider instances using the Initialized event in OutSystems 11 (O11).
locale: en-us
guid: CD21A754-068E-4DA7-9B74-A5122B1AEC7D
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing-an-Application?type=design&node-id=4647%3A10005&mode=design&t=ANpsYvOCthr9AWot-1
---
# Provider instance and JavaScript

## Initialized event

All provider dependent UI Patterns have an **Initialized** event. This can be used to retrieve the WidgetId and access the OutSystems API and  provider instance.

### How to access a provider instance through an initialized event

The following example demonstrates how to use the Date Picker Pattern to access an  instance and use the APIs available from that provider.

1. In Service Studio, in the Toolbox, search for the **Date Picker** Pattern.

    ![Screenshot showing the Date Picker pattern in the OutSystems Service Studio toolbox](images/datepicker-ss.png "Date Picker in Service Studio")

1. Drag the Pattern to the screen.

    ![Screenshot illustrating how to drag the Date Picker pattern onto the screen in OutSystems Service Studio](images/drag-datepicker-ss.png "Dragging Date Picker to the Screen")

1. On the **Properties** tab,  in the **Events** section, select **New Client Action** for the **Initialized** event.
    
    ![Screenshot depicting the process of creating a new client action for the Initialized event in OutSystems Service Studio](images/initialized-ss.png "Creating a New Client Action for Initialized Event")

1. Drag a JavaScript node to the **Initialized** event flow.

    ![Screenshot showing the addition of a JavaScript node to the Initialized event flow in OutSystems Service Studio](images/instance-js-ss.png "Adding JavaScript Node to Event Flow")

1. Inside the JavaScript node, create an input parameter, of type **Text** and set the **Name** to **WidgetId**.

    ![Screenshot demonstrating how to create an input parameter named WidgetId in a JavaScript node within OutSystems Service Studio](images/widgetid-para-ss.png "Creating an Input Parameter")

1. Assign the **WidgetId** to the Id returned by the **Initialized** event.

    ![Screenshot showing the assignment of the WidgetId to the Id returned by the Initialized event in OutSystems Service Studio](images/assignid-ss.png "Assigning WidgetId")

1. Use the OutSystems UI API (``OutSystems.OSUI.Patterns.DatePickerAPI.GetDatePickerItemById($parameters.WidgetId).provider``) to get the provider instance.

    ![Screenshot illustrating the use of OutSystems UI API to get the provider instance for the Date Picker pattern](images/api-ss.png "Using OutSystems UI API")

1. Add your JavaScript code using the provider instance.

1. Click **1-Click Publish**.

<div class="info" markdown="1">

This is a direct communication between the developer and the provider, so from this step on, OutSystems does not support any issues or features and the developer should be conscious of the code it produces.

</div>

## SetProviderConfigs Javascript API

If there’s some configuration  not represented in the ``Set[ProviderName]Configs`` client actions, or you just prefer to set the options using JavaScript, you can do so using the OutSystems API method. 

The API method receives the configuration and passes them to the provider which updates the Pattern in runtime. 

**Note:** This may result in a destroy/init cycle every time this API is called.

### How to set an extended option on the Date Picker using the OutSystems UI JavaScript API

1. Repeat the steps 1-5 from the [How to access a provider instance through an initialized event](#how-to-access-a-provider-instance-through-an-initialized-event).

1. Call the **SetProviderConfigsAPI** and pass the **WidgetId** and the ``OutSystems.OSUI.Patterns.DatePickerAPI.SetProviderConfigs($parameters.WidgetId, options = {inline: true})`` options object to the API.

1. Add your JavaScript code using the provider instance.

1. Click **1-Click Publish**.

<div class="info" markdown="1">

This is a direct communication between the developer and the provider, so from this step on, OutSystems does not support any issues or features and the developer should be conscious of the code it produces.

</div>

