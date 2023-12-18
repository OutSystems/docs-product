---
tags: runtime-mobileandreactiveweb;
summary: The article details how to use client actions to add events and configurations to UI Patterns in OutSystems
locale: en-us
guid: 6265028A-3331-417B-80BC-3E91A1E7B12C
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing-an-Application?type=design&node-id=4647%3A10996&mode=design&t=ANpsYvOCthr9AWot-1
---
# Provider client actions

The following extensibility client actions are available for UI Patterns:

* [Provider events](#provider-events)

* [Provider configuration](#provider-configuration)

### Provider events

To add further events beyond the ones the Patterns have by default, there’s a set of two client actions per provider that can be used to add or remove a new event and an associated callback.

The following table shows each provider based UI Pattern with its associated event client actions and parameters as well as the provider events.

|UI Pattern | Client action | Parameters | Provider events|
|---|---|---|---|
|Carousel |SetSplideEvent | <ul><li>WidgetId (string)</li><li>EventName (string)</li><li>Handler (object)</li><li>SplideEventId (string)</li><li>Success (boolean)</li><li>ErrorMessage (structure)</li></ul>| [Splide events](https://splidejs.com/guides/events/)|
|Carousel |UnsetSplideEvent | <ul><li>WidgetId (string)</li><li>SplideEventId (string)</li><li>Success (boolean)</li><li>ErrorMessage (structure)</li></ul>| [Splide events](https://splidejs.com/guides/events/)|
|<ul><li>Date Picker</li><li>Date Picker Range</li></ul>|SetFlatpickrEvent | <ul><li>WidgetId (string)</li><li>EventName (string)</li><li>Handler (object)</li><li>FlatpickrEventId (string)</li><li>Success (boolean)</li><li>ErrorMessage (structure)</li></ul>|[Flatpickr events](https://flatpickr.js.org/events/)|
|<ul><li>Date Picker</li><li>Date Picker Range </li></ul>|UnsetFlatpickrEvent | <ul><li>WidgetId (string)</li><li>FlatpickrEventId (string)</li><li>Success (boolean)</li><li>ErrorMessage (structure)</li></ul> | [Flatpickr events](https://flatpickr.js.org/events/)|
|<ul><li>Dropdown Search</li><li>Dropdown Tags</li></ul>|SetVirtualSelectEvent | <ul><li>WidgetId (string)</li><li>EventName (string)</li><li>Handler (object)</li><li>VirtualSelectEventId (string)</li>Success (boolean)<li>ErrorMessage (structure)</li></ul> | [VirtualSelect events](https://sa-si-dev.github.io/virtual-select/#/events)|
|<ul><li>Dropdown Search</li><li>Dropdown Tags</li></ul> |UnsetVirtualSelectEvent | <ul><li>WidgetId (string)</li><li>EventName (string)</li><li>VirtualSelectEventId (string)</li>Success (boolean)<li>ErrorMessage (structure)</li></ul> | [VirtualSelect events](https://sa-si-dev.github.io/virtual-select/#/events)|
|<ul><li>Range Slider</li><li>Range Slider Interval</li></ul>|SetNoUISliderEvent|<ul><li>WidgetId (string)</li><li>EventName (string)</li><li>Handler (object)</li><li>NoUiSliderEventId (string)</li><li>Success (boolean)</li><li>ErrorMessage (structure)</li></ul>|[noUiSlider events](https://refreshless.com/nouislider/events-callbacks/)|
|<ul><li>Range Slider</li><li>Range Slider Interval</li></ul>|UnsetNoUISliderEvent|<ul><li>WidgetId (string)</li><li>NoUiSliderEventId (string)</li><li>Success (boolean)</li><li>ErrorMessage (structure)</li></ul>|[noUiSlider events](https://refreshless.com/nouislider/events-callbacks/)|

## How to set a provider event
 
In the following example, the **noUiSlider** provider event is added to the Range Slider Pattern.

1. In Service Studio, in the Toolbox, search for the **Range Slider** Pattern.

    ![Screenshot of the Range Slider widget in OutSystems Service Studio](images/rangeslider-ss.png "Range Slider Widget in Service Studio")

1. Drag the Pattern to the screen and on the **Properties** tab, set the following mandatory properties:

    * **MinValue**: 0

    * **MaxValue:** 100

    * **StartingValue**: 50 

    ![Dragging the Range Slider widget to the screen and setting mandatory properties in Service Studio](images/rangeslider-drag-ss.png "Setting Properties for Range Slider")

1. Staying on the **Properties** tab, in the **Events** section, select **New Client Action** for both the **Initialized** and **OnValueChange** events.

    ![Creating a new client action for Initialized and OnValueChange events in Service Studio](images/initialized-ss.png "Creating New Client Action for Events")

1. Create a new **OnSlide** client action and add the relevant logic. 

    **Note**: The client action acts as a callback for the event.

    In this example, logic that triggers an ``"Is sliding"`` feedback message is added.

    ![Creating an OnSlide client action and adding logic in Service Studio](images/onslide-ss.png "Creating OnSlide Client Action")

1. To set the **OnSlide** client action to an **Object** variable:

    1. Drag a JavaScript node to the **Initialized** event flow.

        ![Dragging a JavaScript node to the Initialized event flow in Service Studio](images/javascript-ss.png "Adding JavaScript Node to Event")

    1. Create an output parameter of type **Object** (Callback) inside the JavaScript node and assign the output parameter to the **OnSlide** client action. (The platform may automatically add brackets () to the end of the assign, for example, ``$actions.OnSlide().`` If so, remove them.)

        ![Creating an output parameter and assigning it to the OnSlide client action in Service Studio](images/callback-ss.png "Assigning Client Action to Callback")

    **Note**: By default, the **SetNoUiSliderEvent** client action has a **Handler** input parameter of type **Object**. As you can’t directly pass client actions using parameters, you must change the **OnSlide** client action to an Object variable that can be passed to the **Handler** input parameter. 

1. On the **Logic** tab, go to **Client Actions** -> **OutSystemsUI**, expand the **Range Slider** folder and drag the **SetNoUiSliderEvent** client action to the action flow.

    ![Dragging SetNoUiSliderEvent client action to the action flow in Service Studio](images/setnouislider-ss.png "Setting NoUiSlider Event in Service Studio")

1. Set the following parameter values:

    * **WidgetId** to the **RangeSliderId** returned by the **Initialized** event.

    * **EventName** to the name of the event you want to add from the provider. In this example, the **Slide** event. (Note that this is case-sensitive).

    * **Handler** to the callback of type **Object** created in the JavaScript node.

        ![Setting the properties for the SetNoUiSliderEvent client action in Service Studio](images/clientaction-properties-ss.png "Configuring Client Action Properties")

1. Click **1-Click Publish**.

    ![Clicking 1-Click Publish to deploy changes in Service Studio](images/result-ss.png "Publishing Changes")

## Provider configuration

To add further configuration beyond the ones the Patterns have by default, there is  a specific client action per provider.

<div class="info" markdown="1">

Not all of the extended configuration options are available through the **ProviderConfigs** parameter structure. This is due to some incompatibility of the default input parameters or client actions already available for those patterns. For full access to the provider options, see  the [Provider instance and JavaScript](ext-provider-instance-java.md) section.

</div>

The following table shows each provider based UI Pattern with its associated configuration client actions and parameters.

|UI Pattern | Client action | Parameters | Provider events|
|---|---|---|---|
|Carousel |SetSplideConfigs | <ul><li> WidgetId (string)</li><li>ProviderConfigs </li>(structure)<li>Success (boolean)</li><li>ErrorMessage (structure)</li></ul> | [Splide options](https://splidejs.com/guides/options/) |
|<ul><li>Date Picker</li><li>Date Picker Range</li></ul> |SetFlatpickrConfigs| <ul><li>WidgetId (string)</li><li>ProviderConfigs (structure)</li><li>Success (boolean)</li><li>ErrorMessage (structure)</li></ul>|[Flatpickr options](https://flatpickr.js.org/options/)|
|<ul><li>Dropdown Search</li><li>Dropdown Tags</li></ul> |SetVirtualSelectConfigs | <ul><li>WidgetId (string)</li><li>ProviderConfigs (structure)</li><li>Success (boolean)</li><li>ErrorMessage (structure)</li></ul> | [VirtualSelect options](https://sa-si-dev.github.io/virtual-select/#/properties) |
|<ul><li>Range Slider</li><li>Range Slider Interval</li></ul> |SetNoUISliderConfigs|<ul><li>WidgetId (string)</li><li>ProviderConfigs (structure)</li><li>Success (boolean)</li><li>ErrorMessage (structure)</li></ul> | [noUiSlider options](https://refreshless.com/nouislider/slider-options/) |

### How to set a provider configuration

In the following example, the Date Picker Pattern is set to appear flat on the screen by using the **SetFlatpickrConfig** client action. 

1. In Service Studio, in the Toolbox, search for the **Date Picker** Pattern.

    ![Screenshot of the Date Picker widget in OutSystems Service Studio](images/datepicker-ss.png "Date Picker Widget in Service Studio")

1. Drag the Pattern to the screen.

    ![Dragging the Date Picker widget to the screen in Service Studio](images/drag-datepicker-ss.png "Dragging Date Picker to the Screen")

1. On the **Properties** tab,  in the **Events** section, select **New Client Action** for the **Initialized** event.
    
    ![Creating a new client action for Initialized and OnValueChange events in Service Studio](images/initialized-ss.png "Creating New Client Action for Events")

1. On the **Logic** tab, go to **Client Actions** -> **OutSystems UI**, expand the **Date Pickers** folder, and drag the **SetFlatpickerConfigs** client action inside the **Initialized** action flow.

    ![Dragging SetFlatpickrConfigs client action inside the Initialized action flow in Service Studio](images/setflatpickrconfig-ss.png "Configuring Flatpickr in Service Studio")

1. Set the **WidgetId** parameter to the **DatePickerWidgetId** parameter (returned by the Initialized action).

    ![Setting the WidgetId parameter for the Date Picker widget in Service Studio](images/datepicker-widgetid-ss.png "Setting Widget ID for Date Picker")

1. Expand the **ProviderConfigs** parameter and set the **Inline** option to **True**.

    ![Setting the Inline property to True for Flatpickr configuration in Service Studio](images/inline-ss.png "Setting Inline Property for Flatpickr")

1. Click **1-Click Publish**.

    ![Result of setting the Date Picker Pattern to appear flat on the screen](images/flat-datepicker-ss.png "Flat Date Picker Result")

<div class="info" markdown="1">

Everytime the **SetFlatpickerConfigs** client action is called, a destroy/init cycle of the provider is triggered, to update the Pattern in runtime. To mitigate a possible impact on performance, OutSystems recommend you only call this client action once.

</div>
