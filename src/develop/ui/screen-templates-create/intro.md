---
summary: Create your Screen Templates for all developers in the factory.
tags: support-Mobile_Apps-featured; support-webapps-featured
---

# Creating Screen Templates

Create new Screen Templates and make them available in your environment by adding them to a Custom Screen Templates Module.

## Creating Custom Screen Templates Module

To add new Screen Templates to your environment, you first need at least one clone of [Custom Screen Templates Web](<https://www.outsystems.com/forge/component-overview/5089/custom-screen-templates-web>) or [Custom Screen Templates Mobile](<https://www.outsystems.com/forge/component-overview/5060/custom-screen-templates-mobile>).

1. In Service Studio, go to the **outsystems** tab and search for **Custom Screen Templates**. There are three components in the results list; one for Mobile Apps, one for Reactive Apps, and one for Web Apps.

    ![Forge results for Custom Screen Templates](images/forge-1-ss.png)
    
1. Click one of the components and then click **Open Module**. 
     
    ![Forge component details page](images/forge-2-ss.png)

    A new tab opens in Service Studio displaying a warning message.
     
1. Click **Open a Clone**.

    ![Open clone confirmation dialog](images/forge-3-ss.png)

1. Once a clone of the module is created, click **Close**.

    ![Close clone dialog box](images/forge-4-ss.png)

1. This is an optional, but a highly recommended step. 

    Go to the **Interface** tab, click the module title in the element tree, and edit the **Name** property to, for example, ``MyCustomScreenTemplatesWeb`` or ``MyCustomScreenTemplatesMobile``. 
    
    ![Rename module name ](images/forge-5-ss.png)
    
    This makes the names of the cloned modules more meaningful.

1. Publish the module. 

    The module is now available on the **Development** tab, in **Independent Modules**.

    ![Rename module name ](images/forge-6-ss.png)

    ![Cloned module ](images/forge-7-ss.png)

1. Go to **Independent Modules** and move your Custom Screen Templates Module to another application. Move your mouse pointer over the module name to reveal the **Move to**
 command, and then click it.
    
   ![Independent modules](images/cloned-in-independent-modules.png)

## Creating new Screen Templates

Follow these steps to create new Screen Templates.

1. Open the Custom Screen Templates Module where you want to add new Screen Templates. If you don't have such module, follow the [instructions for creating it](<#creating-custom-screen-templates-module>) and then return to this section.
1. Go to the **Interface** tab and in the **UI Flows** folder right-click the **ScreenTemplates** flow. Select **Add Web Screen** (or **Add Mobile Screen**) from the context menu.
1. In the **New Screen** window select either a Screen Template with some content to bootstrap your template or choose **Empty**. Click **Create Screen**. A new Screen shows, with a message "You are editing a Screen Template" at the top.
1. If you selected **Empty** in the previous step, go to the **UI Flows** folder, expand the **Common** folder, drag the **Layout** block and drop it to the Screen.
1. [Set the preview image](<reference-metadata.md#preview-image>) and enter the [metadata](<reference-metadata.md>) for the Screen Template.
1. Publish the module. Your Screen Template is now available to all developers in the environment.

![Editing a Screen Template](images/creating-screen-template.png?width=500)

## Editing Screen Templates

Edit your Screen Templates in your Custom Screen Templates Module. Republish the module to update the Screen Templates in the environment. Keep in mind that editing an existing Screen Template does not affect Screens that are already created from it.

## Creating Screen Templates with custom Theme

You can use a different Theme in each Custom Screen Templates Module. Screen Templates inherit the styles from the Theme.

1. Follow the steps for [creating a Custom Screen Templates Module](<#creating-custom-screen-templates-module>).
1. Edit the module so it uses your Theme. The Custom Screen Templates Modules from Forge use BaseTheme, the default Theme from OutSystems UI.
1. Follow the steps for [creating new Screen Templates](<#creating-new-screen-templates>).

OutSystems provides the following Forge components to assist you in creating your own style guide and Screen Templates:

* [OutSystems UI Style Guide](<https://www.outsystems.com/forge/Component_Overview.aspx?ProjectId=5119>) - a Theme and starter Application Template based on OutSystems UI
* [OutSystems UI Style Guide Preview](<https://www.outsystems.com/forge/Component_Overview.aspx?ProjectId=5120>) - a preview of all OutSystems UI Styles, UI patterns, Widgets, and Screen Templates
