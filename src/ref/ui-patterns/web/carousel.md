---
tags: ui component customization, css customization, web design, carousel customization, outsystems ui
summary: Explore advanced customization options for Carousel UI components in OutSystems 11 (O11), including external arrow placement and dot styling.
locale: en-us
guid: d0b2bc8d-6a37-424d-8399-56e586304c93
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?type=design&node-id=615%3A420&mode=design&t=Cx8ecjAITJrQMvRn-1
audience:
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Carousel Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![Diagram showing the layout and classes of a Carousel UI component](images/carousel-3-diag.png "Carousel Layout Diagram")

## Advanced

Here are some more advanced use-cases of the widget.

### Put arrows outside of Carousel

To place the arrows outside the carousel, change the input parameters Padding and Margin. To have this behavior both parameters must be of the same value. Padding creates a space around the carousel viewport and the margin pushes the elements apart, so they are hidden inside the carousel.

![Screenshot of a Carousel with arrows placed outside the viewport](images/carousel-4-ss.png "Carousel with External Arrows")  
![Screenshot of a Carousel with adjusted padding and margin to place arrows outside](images/carousel-5-ss.png "Carousel with Adjusted Padding and Margin")

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

![Screenshot showing custom style for Carousel dots with rectangular shape](images/carousel-6-ss.png "Custom Dots Style Example 1")

#### Example 2

```css
.carousel .tns-nav > [aria-controls] {
    width: 12px;
    height: 6px;
    border-radius: 4px;
}
```

![Screenshot displaying Carousel dots customized with a rounded rectangle shape](images/carousel-7-ss.png "Custom Dots Style Example 2")

## Notes

Line Separator from ListRecords should be None.

![Screenshot illustrating the line separator setting as None in a Carousel component](images/carousel-8-ss.png "Carousel Line Separator Setting")
