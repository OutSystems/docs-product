---
summary: Drag and drop patterns to use the most common UI components, like calendar, tool tip, carousel, and many more.
locale: en-us
guid: 8ba8f042-b63e-4dbf-b2b4-b05d61b7160c
app_type: traditional web apps, mobile apps, reactive web apps
---

# Patterns

<div class="info" markdown="1">

Check <a href="https://outsystemsui.outsystems.com/OutSystemsUIWebsite/PatternOverview" title="Demos and previews of the patterns">UI Patterns</a> on the OutSystems UI website for the list of patterns and their previews.

</div>

In OutSystems you can use the pre-built patterns, which implement common UI patterns and components. Patterns cover the most used UI patterns and interactions in mobile and web apps, to distance developers as much a possible from the need to program CSS.

## Customization 

You can customize the patterns by writing additional CSS that changes their look and feel. Additionally, you can change the structure to be able to display something else or remove unwanted elements. You can even change the code and the pattern behavior like adding swipe gestures or adding new events. Keep in mind that code customizations can make patterns behave unpredictably and are not officially supported.

By creating additional [CSS](../look-feel/css.md) on a new module, it is possible to override the look of most patterns, so this is the simplest way of customizing them.

Changing the structure of a pattern by, for instance, adding a couple of tabs, requires the pattern to be copied to a new module and then adding the correct placeholders. The same rule applies to code changes. A copied pattern will not be upgraded with OutSystems UI versions that have code fixes.

**Note:** From OutSystems 10 onward, it's not possible to directly change modules that are part of the UI framework. If you need to change a specific pattern, copy it and make the necessary changes in your cloned version.

## OutSystems UI version

Depending on what version of OutSystems UI you are using, some patterns may be deprecated. To find out what version of OutSystems UI you are using:

1. In Service Studio, click the **Dependencies** icon.

1. Click **In Use**.

1. Select **OutSystemsUI**.

![OutSystems UI version](<images/os-version-ss.png>)

For more information on how to migrate old versions, see the [Patterns and Versions Overview](https://outsystemsui.outsystems.com/OutsystemsUiWebsite/MigrationOverview).
