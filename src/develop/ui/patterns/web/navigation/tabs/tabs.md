---
tags: runtime-traditionalweb; 
summary: Tabs separate content into flat structure sections.
---

# Tabs

Use this pattern to display large sets of information which can be split into different areas, while always a click away. The headers can have other widgets, like counters, badges or icons.

![](images/tabs-gif1.gif?width=650)

Use the Tabs pattern when you need to separate content into sections with a flat structure. However, avoid using it in large forms.

**How to use**

Fill in the placeholders Header and Content with the Blocks TabsHeaderItem and TabsContentItem, respectively. Use any number of these as you need. In the parameters, specify the initial active tab, along with the Tabs orientation and justification. 

1. Drag Tabs pattern into the preview.

    ![](images/tabs-image1.png?width=750)

1. Set your content and publish.

## Demo

<iframe width="750" height="500" src="https://www.youtube.com/embed/97uPVx-Q1lQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Input parameters

### Tabs

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| ActiveTab  |  Set the Active Tab |  Text | False | none |
| Orientation  |  If Vertical, header is displayed side by side to the content; if Horizontal, header is displayed above content. |  Orientation Identifier | False | Entities.Orientation.Horizontal |
| IsJustified  |  The Tabs Header items are evenly distributed in the line, the first item is on the start and last item on the end. |  Boolean | False | 1 |
| IsRight  |  Aligns the Tabs Header items to right. Only active if the Orientation parameter is set to Vertical. |  Boolean | False | False |
| ExtendedClass  |  Adds custom style classes to the Tabs Block. |  Text | False | none |

### TabsHeaderItem

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| DataTab  |  Sets the name to connect to the TabsContentItem. Should be the same as the paired HeaderItem and unique |  Text | True | none |

### TabsContentItem

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| DataTab  |  Value that connects with the TabsHeaderItem. Should be the same as the paired ContentItem and unique. |  Text | True | none |

## Layout and classes

![](images/tabs-image2.png?width=750)

## CSS selectors

| **Element** |  **CSS Class** |  **Description**  |
| ---|---|---  
| Active Header |  .tabs-header-item.active |  It's active header (represented as the one with a colored underline)  |
| Active Tab  |  .tabs-content-item.active  |   It's active content  |
  

## Advanced

Here are some more advanced use-cases of the widget.

### Change the active header style

Write the following CSS in the CSS editor and change the `yourcolor` value:

`.tabs-header-item.active {
    border-bottom: var( --border-size-m) solid yourcolor;
}`

Or using CSS variables: `var(--color-yourcolor)`
example:

`.tabs-header-item.active {
background: border-bottom: var( --border-size-m) solid var(--color-red)
}`

### Add a background color to the tabs

1. Enclose the tabs with a container.
2. Add the classes `background-blue-lighter text-neutral-0`, this adds a light blue background and force the text to be white.
3. Publish the application.

![](images/tabs-image3.png?width=750)
