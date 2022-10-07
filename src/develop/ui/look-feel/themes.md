---
summary: To edit or create a theme you need to know the basics about the theme structure. This document shows how themes integrate into the platform through predefined blocks and placeholders.
tags: support-application_development; support-Front_end_Development
locale: en-us
guid: fa7dc8c3-aea1-4ccb-a2d6-219772a1a7f2
app_type: traditional web apps, mobile apps, reactive web apps
---

# Themes

A Theme contains the details for visual presentation and changing a Theme changes how your app looks. A module has a default theme, and all UI Flows an Screens inherit it.

You can:

* [Set the default module Theme](#setting-the-default-module-theme), if you have several Themes in your module.

* [Create a blank Theme without any styles](#creating-a-theme-without-styles), so elements use only the CSS you create.

* [Create a new Theme based on the default Theme](#creating-a-theme-from-a-base-theme), if you want add styles to the existing Theme.

The default OutSystems Themes are part of the OutSystems UI framework. OutSystems optimized the built-in Themes for performance and to work well with scaffolding and Screen Templates.

## Setting the default module Theme

If you have more than one Theme in your module, you can change the default module Theme. Follow these steps in Service Studio:

1. Go to the **Interface** tab and select the module name at the top of the pane. The module properties show.

2. In the module properties locate the **Defaults** section.

3. In the **Default Theme** list select your Theme.

    ![Module properties and Theme](images/module-theme-ss.png?width=300)

## Creating a Theme without styles

It's possible to create a Theme without any styles. Follow these steps in Service Studio:

1. Go to the **Interface** tab.

2. Right-click the **Themes** folder, then select **Add Theme**. New Theme appears in the **Themes** folder.

3. In the **Base Theme** property list of the new Theme select **(None)**.
    
    ![A Theme with no base Theme](images/creating-blank-theme-ss.png?width=300)

4. Optionally, go to **Interface** > **UI Flows**, select a UI Flow and in the properties select you blank Theme **Theme** list. This makes all elements under the UI Flow to use the blank Theme. 

## Creating a Theme from a Base Theme

When you create a new app it already contains a copy of the CSS which you can edit. You can create new, additional, themes manually.

1. In the **Interface** tab right-click **Themes** and select **Add Theme**.
1. Enter the name of your new theme.
1. Optionally, change the **Base Theme**. If you do not see the Theme you want in the list, add a reference to it.
1. With your Theme selected in the properties, click on **Style Sheet**.
1. Enter your styles in the first tab of the CSS editor. You can't edit the original Theme, but you can create new styles with the same class names and override the original styles.

## The structure of a OutSystems UI Theme

The Themes in the OutSystems UI framework follow a structure based on the Screen requirements of an OutSystems app. Each Theme includes several Blocks and each Block consists of one or more Placeholders.

The following diagram shows how a new Theme inherits the layout from the base Theme, and how the platform uses the Blocks and Placeholders to generate a page. The main layout has Placeholders whose content are Blocks (the Header placeholder is replaced by the content generated in the Header block). The CSS is also inherited from the base Theme, but can be overridden by the application CSS.

![](images/themes-concept.png?width=500)

## Blocks

Different types of Screen require different Blocks. The following table specifies the required Blocks for the different type of Screens in web applications:

<table markdown="1">
<thead>
<tr>
<th rowspan="2">
Type of Screen
</th>
<th colspan="7">
Web Block
</th>
</tr>
<tr>
<th>
Layout
</th>
<th>
Info Balloon
</th>
<th>
Pop-up Editor
</th>
<th>
Email
</th>
<th>
Header
</th>
<th>
Menu
</th>
<th>
Footer
</th>
</tr>
</thead>
<tbody>
<tr>
<th>
Blank Screen
</th>
<td>
Required
</td>
<td></td>
<td></td>
<td></td>
<td>
Required
</td>
<td>
Required
</td>
<td>
Required
</td>
</tr>
<tr>
<th>
List Screen
</th>
<td>
Required
</td>
<td></td>
<td></td>
<td></td>
<td>
Required
</td>
<td>
Required
</td>
<td>
Required
</td>
</tr>
<tr>
<th>
Show Screen
</th>
<td>
Required
</td>
<td></td>
<td></td>
<td></td>
<td>
Required
</td>
<td>
Required
</td>
<td>
Required
</td>
</tr>
<tr>
<th>
Edit Screen
</th>
<td>
Required
</td>
<td></td>
<td></td>
<td></td>
<td>
Required
</td>
<td>
Required
</td>
<td>
Required
</td>
</tr>
<tr>
<th>
Info Balloon
</th>
<td></td>
<td>
Required
</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<th>
Pop-up Editor
</th>
<td></td>
<td></td>
<td>
Required
</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<th>
Email
</th>
<td></td>
<td></td>
<td></td>
<td>
Required
</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

The table can be interpreted like this:

* When creating or editing a blank screen in a web application, there should be web blocks for the layout, header, menu and footer, or
* When creating or editing an Email web application, there is only one block required.

The main content of the screens is placed in the block named **Layout**. Depending on the platform for which the Theme is developed, the layout can consist of different placeholders. For example, the layout in web application must have a placeholder that shows content (MainContent), but the breadcrumbs placeholder is optional.

This is the list of reserved names for the **Layout**  placeholders in the web Themes.

* Title
* MainContent
* Breadcrumbs
* Actions
* Header
* Menu
* Footer

A mobile Theme can have these placeholders in the layout block:

* HeaderLeft
* Title
* HeaderRight
* HeaderContent
* Content
* Bottom

The mobile Themes have the block-specific events and actions, which are later compiled into JavaScript/React event listeners and functions. Do not delete default events and actions relevant for the screen purpose. 

## Placeholders

What placeholders to use depends on the type of screen. Here is an overview for the web applications:

|Type of Screen/<br/> Placeholder|Title|MainContent	|Actions|Header|Menu|Footer|
|---|---|---|---|---|---|---|
|**Blank Screen**||Required||Optional|Optional|Optional|
|**List Screen**|Required|Required|Optional|Optional|Optional|Optional|
|**Edit Screen**|Required|Required|Optional|Optional|Optional|Optional|
|**Info Balloon**||Required|||||
|**Pop-up Editor**||Required|||||
|**Email**|Optional|Required|||||

Some examples:

* If, in the Theme properties, a web application has a web block assigned for Blank Screen, the only required placeholder for that web block is MainContent, or
* If, in the Theme properties, a web application has a web block assigned for Email, the only required placeholder for that web block is MainContent, while Title is optional.

Menu items in web can be created automatically by drag and drop. If you want to keep the same functionality in your Themes, create a menu web block with the required input parameters and the entities. Refer to the existing Themes for input parameters and entities.

Here is an example of blocks for a web Theme and their placeholders:

![](images/theme-layout.png?width=300)
