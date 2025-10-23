---
summary: Explore how to create and utilize UI elements in OutSystems 11 (O11) for both web and mobile applications.
locale: en-us
guid: a864addf-9175-49f9-905e-e90013c7d238
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=184:0
tags: ui design, screen templates, user interaction, widgets, ui flows
audience:
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - understand
  - apply
topic:
  - create-screen-scratch
  - screen-template
---

# Screens

A Screen is a user interface (UI) element that contains other UI elements for users to interact. An empty Screen contains a basic layout for you to add widgets. A Screen based on a Screen Template has predefined content that works as a demo.

How Screens show in an app to you users depends on the app type:

* In a Reactive Web App, Screens render as web pages in a browser.
* In Mobile Apps, Screens render as screens of a mobile app.

## Creating a Screen

To create a Screen, follow these steps in Service Studio:

1. Go to the **Interface** tab, and then expand the **UI Flows** folder.

    ![Screenshot showing the Interface tab with the UI Flows folder expanded in Service Studio](images/interface-tab-ui-flows-ss.png "Interface Tab and UI Flows in Service Studio")

1. From the **UI Flows**, right-click **MainFlow** and in the menu select **Add Screen**.

    ![Context menu in Service Studio with the option to Add Screen selected](images/add-screen-ss.png "Adding a New Screen")

1. Select one of the following:

    * **Empty**, to create an empty Screen
    * A Screen Template, to create a Screen based on a template

    ![Dialog in Service Studio for creating a new Screen with options for Empty or a Screen Template](images/create-blank-screen-ss.png "Creating a Blank Screen")

1. Optionally, enter a name in the **Screen name** field.

1. Click **Create Screen**.
