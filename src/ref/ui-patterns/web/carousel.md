---
tags: runtime-traditionalweb;
summary: Advanced use cases for the Carousel UI Pattern.
locale: en-us
guid: d0b2bc8d-6a37-424d-8399-56e586304c93
---

# Carousel Reference

## Layout and classes

![](<images/carousel-3-diag.png?width=600>)

## Advanced

Here are some more advanced use-cases of the widget.

### Put arrows outside of Carousel

To place the arrows outside the carousel, change the input parameters Padding and Margin. To have this behavior both parameters must be of the same value. Padding creates a space around the carousel viewport and the margin pushes the elements apart, so they are hidden inside the carousel.

![](<images/carousel-4-ss.png>)  
![](<images/carousel-5-ss.png>)

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

![](<images/carousel-6-ss.png>)

#### Example 2

```css
.carousel .tns-nav > [aria-controls] {
    width: 12px;
    height: 6px;
    border-radius: 4px;
}
```

![](<images/carousel-7-ss.png>)

## Notes

Line Separator from ListRecords should be None.

![](<images/carousel-8-ss.png>)
