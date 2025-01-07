---
summary: Explore how to create and manage custom screen templates in OutSystems 11 (O11) using the Service Studio environment.
tags: ide usage, reactive web apps, tutorials for beginners, screen template customization, outsystems development
locale: en-us
guid: 874543f6-0021-47c7-9b10-28853b48d6a3
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=186:47
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
  - forge
coverage-type:
  - apply
---

# Creating Screen Templates

Create new Screen Templates and make them available in your environment by adding them to a Custom Screen Templates Module.

## Creating a Custom Screen Templates Module

To add new Screen Templates to your environment, you first need to clone one of the Screen Template components: 

* [Custom Screen Templates Reactive](https://www.outsystems.com/forge/component-overview/7127/custom-screen-templates-reactive) for Reactive Web Apps
* [Custom Screen Templates Mobile](<https://www.outsystems.com/forge/component-overview/5060/custom-screen-templates-mobile>) for Mobile Apps
* [Custom Screen Templates Traditional Web](<https://www.outsystems.com/forge/component-overview/5089/custom-screen-templates-web>) for Traditional Web Apps

Follow these steps:

1. In Service Studio, go to the **Forge** tab and search for **Custom Screen Templates**. Find the Screen Template component for the type of app you need. 

    ![Screenshot of the Forge tab in Service Studio showing where to search for Custom Screen Templates](images/forge-1-ss.png "Forge Tab in Service Studio")
    
1. Click one of the components and then click **Open Module**. 
     
    ![Screenshot highlighting the Open Module option for a selected component in Service Studio](images/forge-2-ss.png "Open Module Option")

    A new tab opens in Service Studio displaying a warning message.
     
1. Click **Open a Clone**.

    ![Screenshot showing the Open a Clone option in Service Studio to clone a module](images/forge-3-ss.png "Open a Clone Option")

    Service Studio takes a few seconds to clone the module.

1. Click **Close**.

    ![Screenshot of the Close button in Service Studio after cloning a module](images/forge-4-ss.png "Close Button in Service Studio")

1. This is an optional, but a highly recommended step. 

    Go to the **Interface** tab, click the module title in the element tree, and edit the **Name** property to, for example, `MyCustomScreenTemplatesReactive` or `MyCustomScreenTemplatesMobile`. 
    
    ![Screenshot of the Interface tab in Service Studio where the module name is being edited](images/forge-5-ss.png "Editing Module Name")
    
    This makes the names of the cloned modules more meaningful.

1. Publish the module. 

    The module is now available on the **Development** tab, in **Independent Modules**.

    ![Screenshot showing the newly cloned module available in the Development tab under Independent Modules](images/forge-6-ss.png "Module in Development Tab")

    ![Screenshot of the Independent Modules section in Service Studio with the new module listed](images/forge-7-ss.png "Independent Modules Section")

1. From **Independent Modules**, move your Custom Screen Templates Module to the app you want to use it in. 

    To do this, click the Move module icon, select the app you want to move the template to, and click **Move**.
    
    ![Screenshot displaying the Move module icon in Service Studio for relocating a module](images/forge-8-ss.png "Move Module Icon")
        
    ![Screenshot of the process of selecting an app to move the Custom Screen Templates Module to](images/forge-9-ss.png "Selecting App for Module")

    The template module is now part of the app you selected.


## Creating new Screen Templates

1. Open the Custom Screen Templates Module where you want to add a new Screen Template. If you don't have such a module, follow the [instructions for creating it](<#creating-custom-screen-templates-module>) and then return to this step.

1. On the **Interface** tab, from the **UI Flows** folder, right-click your screen template UI flow and select **Add Screen**.

    ![Screenshot showing the option to add a new screen to a UI flow in the Custom Screen Templates Module](images/forge-10-ss.png "Adding New Screen")

1. In the **New Screen** window, select either a Screen Template with some content to bootstrap your template or choose **Empty** and click **Create Screen**. 

    In this example, we select **Empty**.

    ![Screenshot of the New Screen window in Service Studio with the Empty option selected](images/forge-11-ss.png "New Screen Window")

    The new screen opens: 

    ![Screenshot of a newly created empty screen in the Custom Screen Templates Module](images/forge-12-ss.png "Newly Created Screen")

1. Go to the **UI Flows** folder, expand the **Common** folder, and drag the **Layout** block onto the screen.

    ![Screenshot illustrating how to drag the Layout block onto a new screen in Service Studio](images/forge-13-ss.png "Dragging Layout Block")

    Note: This step only applies if you selected the **Empty** screen in the previous step.

1. [Set the preview image](<reference-metadata.md#preview-image>) and enter the [metadata](<reference-metadata.md>) for the Screen Template.

1. Publish the module.

    Your Screen Template is now available to all developers in the environment.

    ![Screenshot showing a published Screen Template now available to developers in the environment](images/forge-14-ss.png "Published Screen Template")

## Editing Screen Templates

You can edit your Screen Templates in your Custom Screen Templates Module. Republish the module to update the Screen Templates in the environment.

If you want to edit a Screen based on a template, edit the Screen. Editing a Screen Template won't change the Screens you created from the template. 

## Creating Screen Templates with a custom Theme

You can use a different Theme in each Custom Screen Template Module. The Custom Screen Templates Modules from Forge use the default Theme from the OutSystems UI. Screen Templates inherit the styles from the Theme. 

1. Follow the steps for [creating a Custom Screen Templates Module](<#creating-custom-screen-templates-module>).

1. Edit the module so it uses your Theme.

1. Follow the steps for [creating new Screen Templates](<#creating-new-screen-templates>).

OutSystems provides the following Forge components to assist you in creating your own style guide and Screen Templates:

* [OutSystems UI Style Guide Preview](https://www.outsystems.com/forge/component-overview/7527/outsystems-ui-style-guide-preview)
* [OutSystems UI Reactive Style Guide Template](https://www.outsystems.com/forge/component-overview/7526/outsystems-ui-reactive-style-guide-template)
* [OutSystems UI Style Guide Theme](https://www.outsystems.com/forge/component-overview/8240/outsystems-ui-style-guide-theme)