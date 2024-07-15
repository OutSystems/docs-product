---
summary: OutSystems 11 (O11) accelerators enable faster creation of reactive web and mobile apps with customizable screen components.
tags: 
locale: en-us
guid: fc130f38-3ed2-46f5-a1d1-4319f3e37dfb
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing-an-Application?type=design&node-id=568%3A366&mode=design&t=VUTD7oZE9xvPWlG0-1
---

# Accelerators to compose a screen

OutSystems accelerators allow you to develop reactive web and mobile apps faster. They're smaller building blocks to compose a screen and are oriented to specific use cases such as a patient registration wizard, login with Google or a product gallery.

Each accelerator contains screen building blocks that you can add to your apps and modify.

To have the accelerators in Service Studio toolbox, you need to install [OutSystems Accelerators](https://www.outsystems.com/forge/component-overview/12197/outsystems-accelerators) from Forge.

All the accelerators are represented by the accelerator icon in the widget toolbox:

![Icon of the accelerator widget in the OutSystems Service Studio toolbox](images/acc-widget-ss.png "Accelerator Widget in Service Studio")

![Screenshot showing a list of available accelerators in OutSystems Service Studio](images/acc-acclist-ss.png "List of Accelerators in Service Studio")

## How to use accelerators

In Service Studio, open a Screen for editing and follow these steps:

1. In the Toolbox, browse or search for the accelerator you want to use in your app, for example, the Check Balance.

1. Drag the accelerator to your Screen.

1. Publish your app and preview the screen.

<iframe src="https://player.vimeo.com/video/973090137" width="750" height="395" frameborder="0" allow="autoplay; fullscreen" allowfullscreen="">Video displaying how to drag and drop an accelerator into a screen within OutSystems Service Studio.</iframe>

Once you've published your app, you can customize it by, for example, [replacing sample data with your own data](#replace-sample-data-with-real-data) and [adapting the UI and logic](#adapt-the-UI-and-logic) to match the user experience you want to achieve. You can also use the [Map](../patterns/mobile/interaction/map/map.md) accelerator in your app.

### Replace sample data with real data

Some accelerators are populated with sample data so that you can publish and preview the app in runtime without any required changes.

However, you can replace this sample data by dragging and dropping your entities onto the UI which automatically replaces the sample data with your data. Depending on the difference in data structures, there may be errors left to solve. For more information, see [Replace sample data](../screen-templates/replace-data.md).

### Adapt the UI and logic

You can change and adapt the UI and logic to suit your app. To help you with this, OutSystems provides you with plenty of different UI patterns in Service Studio. You can find an overview of all available patterns on the [OutSystems UI website](https://outsystemsui.outsystems.com/outsystemsUiWebsite/PatternsOverview).

### Screen templates

Most of the **List** accelerators have a matching **Details** screen template. These templates have the same look and feel and they're connected to the same sample data. There are multiple industry use cases available to choose from.

![Image displaying the accelerator list and details screen templates in OutSystems Service Studio](images/acc-list.png "Accelerator List and Details Screen Templates")
