---
tags: runtime-traditionalweb; 
summary: Carousel shows a subset of items in a cyclic view.
---

# Carousel

A dynamic widget that enables you to highlight pieces of content in a single space and a cyclic view.

The Carousel makes it possible to show more than one piece of content, while optimizing screen space by displaying only a subset of images on a cyclic view. The navigational controls on a carousel suggest additional content that is not visible, which encourages the user to continue exploring.


**How to use**

Elements inside the placeholder are split in different items. For dynamic content, use a List directly inside the placeholder and the list items will be Carousel Items by default.

1. Drag the Carousel pattern into your page.

1. Place your content into the Items placeholder. To use a Carousel with items from a database, drag a ListRecords into Items placeholder and create your custom content.
    
    ![](<images/carousel-image-1.png>)
    
    ![](<images/carousel-image-2.png>)

1. Publish and test.

## Input parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| Margin  |  Distance between each Carousel item. |  Integer | False | 16 |
| Padding  |  Distance between the screen edges and the visible items on the screen. |  Integer | False | 0 |
| Pagination  |  If true, sets the dots representing all items, which can be tapped to navigate directly to a given item. |  Boolean | False | True |
| Navigation  |  If true, shows arrows to navigate left and right. |  Boolean | False | True |
| Autoplay  |  If true, it enables the autoplay. |  Boolean | False | False |
| Rewind  |  Applies a Rewind effect when the Carousel reaches the end and Loop is enabled. The default behavior is to show the first item without rewinding through the remaining. |  Boolean | False | False |
| Loop  |  If true, it enables continuous slide of the Carousel even after it reaches the end. |  Boolean | False | False |
| InitialPosition  |  Sets the first element to show. |  Integer | False | 0 |
| ItemsDesktop  |  Number of items to be displayed at the same time while on desktop. |  DeviceConfig | False | 1 |
| ItemsTablet  |  Number of items to be displayed at the same time while on tablet. |  DeviceConfig | False | 1 |
| ItemsPhone  |  Number of items to be displayed at the same time while on phone. |  DeviceConfig | False | 1 |
| ExtendedClass  |  Adds custom style classes to this Block. |  Text | False | none |
| AdvancedFormat  |  Enables you to use more options than what is provided in the input parameters. For more information visit: https://github.com/ganlanyuan/tiny-slider. Example: `{ axis: 'vertical' }` |  Text | False | none |

## Layout and classes

![](<images/carousel-image-3.png?width=600>)

## Advanced

Here are some more advanced use-cases of the widget.

### Put arrows outside of Carousel

To place the arrows outside the carousel, change the input parameters Padding and Margin. To have this behavior both parameters must be of the same value. Padding creates a space around the carousel viewport and the margin pushes the elements apart, so they are hidden inside the carousel.

![](<images/carousel-image-4.png>)
![](<images/carousel-image-5.png>)

### Customizing the dots style

It is possible to change the style of the dots on a Carousel with the custom CSS. Here are two examples of how to do it. To use in your application, copy the CSS and put it in your theme.

#### Example 1

```css
.carousel .tns-nav > [aria-controls] {
    width: 16px;
    height: 2px;
    border-radius: 0;
}
```

![](<images/carousel-image-6.png>)

#### Example 2

```css
.carousel .tns-nav > [aria-controls] {
    width: 12px;
    height: 6px;
    border-radius: 4px;
}
```

![](<images/carousel-image-7.png>)

## Notes

Line Separator from ListRecords should be None.

![](<images/carousel-image-8.png>)
